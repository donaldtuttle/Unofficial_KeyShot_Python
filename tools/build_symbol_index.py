#!/usr/bin/env python3
"""
build_symbol_index.py  v1.0.0

Convert KeyShot scripting-console captures of help(lux) and help(luxmath)
into a machine-readable symbol index (symbols.json) used by verify_symbols.py.

Usage
    python build_symbol_index.py lux/KeyShot_lux_API.md lux/KeyShot_luxmath_API.md \
        --build 2026.3-beta -o references/api/2026.3-beta/symbols.json

    Each input may hold one or several help() captures. Markdown code fences,
    console prompts (>>>) and timing lines are ignored.

What is extracted, per module
    * functions, classes, class members (instance / class / static methods and
      attributes) and DATA constants;
    * parameters - from the real signature when pydoc shows one, e.g.
      "(self, /)" or "(object, /)", otherwise from KeyShot's docstring
      convention "name = description *" (a trailing * marks a required
      argument). Each callable records params_source = "signature",
      "docstring" or "none", so the checker can treat docstring-derived
      parameters as evidence rather than proof;
    * return types, only where the dump text states them (the provenance
      sentence is recorded with each one);
    * symbols that docstrings mention but the dump never declares, such as a
      constant family named in prose but absent from DATA.

Self-check
    The class names in each CLASSES hierarchy must match the class blocks that
    were parsed. A mismatch means the capture is truncated or the parser
    misread it; the build then exits with status 1 unless
    --allow-inconsistent is given.

Standard library only. Runs in ordinary Python 3.9+, not inside KeyShot.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import sys
from pathlib import Path

GENERATOR = "build_symbol_index.py 1.0.0"
SCHEMA_VERSION = 1

# --------------------------------------------------------------------------
# pydoc layout patterns
# --------------------------------------------------------------------------
TOP_HEADERS = {
    "NAME", "DESCRIPTION", "PACKAGE CONTENTS", "SUBMODULES", "CLASSES",
    "FUNCTIONS", "DATA", "VERSION", "AUTHOR", "CREDITS", "FILE",
}
HELP_START = re.compile(r"^(\s*)Help on (?:built-in )?module ([A-Za-z_][\w.]*):\s*$")
CLASS_HDR = re.compile(r"^    class ([A-Za-z_]\w*)(?:\((.*)\))?:?\s*$")
FUNC_HDR = re.compile(r"^    ([A-Za-z_]\w*)(\(.*\))\s*$")
DATA_LINE = re.compile(r"^    ([A-Za-z_]\w*) = (.*)$")
BODY_LINE = re.compile(r"^\s*\|(.*)$")
MEMBER_HDR = re.compile(r"^  ([A-Za-z_]\w*)(\(.*\))?(?: = (.*))?\s*$")
IDENT = re.compile(r"[A-Za-z_]\w*")
SEPARATOR = re.compile(r"-{3,}")

# KeyShot docstring parameter convention: "name = description. *"
PARAM_LINE = re.compile(r"^([A-Za-z_]\w*)\s*=\s+(.*)$")
DEFAULT_RE = re.compile(r"\(default\s*=\s*([^)]*)\)", re.IGNORECASE)

# Mentions of lux / luxmath symbols inside any docstring.
# "lux.SHADER_TYPE_.." and "lux.ANIMATION_TYPE_*" are prefix (family) references.
REF_RE = re.compile(r"\b(lux|luxmath)\.([A-Za-z_][A-Za-z0-9_]*)(\.{2,}|\*)?")

# Return-type statements, applied only to text the dump actually contains.
OWN_DOC_RETURNS = re.compile(
    r"^(?:Get|Gets|Return|Returns|Retrieve|Retrieves)\b[^.]*?"
    r"\b(lux|luxmath)\.([A-Za-z_]\w*)\s+(?:object|instance)\b")
OWN_DOC_LIST = re.compile(r"\blist of (?:all )?(lux|luxmath)\.([A-Za-z_]\w*) objects\b")
CLASS_DOC_FACTORY = re.compile(r"\b(?:using|calling:?|via)\s+(lux|luxmath)\.([A-Za-z_]\w*)\s*\(")
HEADLESS_NOTE = re.compile(
    r"[^.]*\bheadless\b[^.]*\b(?:exception|throw)[^.]*\.?"
    r"|[^.]*\b(?:exception|throw)[^.]*\bheadless\b[^.]*\.?", re.IGNORECASE)

SECTIONS = [
    (re.compile(r"^Methods defined here:$"), "instance"),
    (re.compile(r"^Class methods defined here:$"), "class"),
    (re.compile(r"^Static methods defined here:$"), "static"),
    (re.compile(r"^(?:Data descriptors|Readonly properties) defined here:$"), "attribute"),
    (re.compile(r"^Data and other attributes defined here:$"), "attribute"),
    (re.compile(r"^.+ inherited from (.+):$"), "inherited"),
]


# --------------------------------------------------------------------------
# Small text helpers
# --------------------------------------------------------------------------
def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _clean_lines(text: str) -> list[str]:
    """Normalise newlines and tabs; drop Markdown code fences."""
    text = text.lstrip("\ufeff").replace("\r\n", "\n").replace("\r", "\n")
    lines = []
    for raw in text.split("\n"):
        if raw.strip().startswith("```"):
            continue
        lines.append(raw.expandtabs(8).rstrip())
    return lines


def _dedent(lines: list[str], n: int) -> list[str]:
    if n <= 0:
        return list(lines)
    return [line[min(_indent(line), n):] for line in lines]


def _join(lines: list[str]) -> str:
    return " ".join(line.strip() for line in lines if line.strip())


def _summary(lines: list[str]) -> str:
    for line in lines:
        if line.strip():
            return line.strip()
    return ""


def _split_top_level(text: str) -> list[str]:
    """Split a signature on commas that are not inside brackets."""
    parts, depth, cur = [], 0, []
    for ch in text:
        if ch in "([{":
            depth += 1
        elif ch in ")]}":
            depth -= 1
        if ch == "," and depth == 0:
            parts.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    parts.append("".join(cur))
    return [p.strip() for p in parts if p.strip()]


# --------------------------------------------------------------------------
# Signatures and docstring parameters
# --------------------------------------------------------------------------
def parse_signature(sig: str, is_method: bool):
    """Return (params, accepts_varargs, accepts_varkw) for a real signature,
    or None when pydoc shows the opaque "(...)" form."""
    inner = sig.strip()[1:-1].strip()
    if inner == "...":
        return None
    parts = _split_top_level(inner)
    slash = parts.index("/") if "/" in parts else -1
    params, varargs, varkw, kwonly = [], False, False, False
    for i, part in enumerate(parts):
        if part == "/":
            continue
        if part == "*":
            kwonly = True
            continue
        if part.startswith("**"):
            varkw = True
            continue
        if part.startswith("*"):
            varargs = kwonly = True
            continue
        name, eq, default = part.partition("=")
        name = name.split(":")[0].strip()
        if (i == 0 and is_method and name in ("self", "cls")) or name.startswith("$"):
            continue
        params.append({
            "name": name,
            "required": not eq,
            "default": default.strip() or None,
            "positional_only": i < slash,
            "keyword_only": kwonly,
        })
    return params, varargs, varkw


def parse_doc_params(doc_lines: list[str]) -> list[dict]:
    """Read "name = description *" lines at the docstring's base indent.
    Deeper-indented lines (code examples, dictionary layouts) are skipped."""
    nonblank = [line for line in doc_lines if line.strip()]
    if not nonblank:
        return []
    base = min(_indent(line) for line in nonblank)
    params, seen = [], set()
    for line in nonblank:
        if _indent(line) != base:
            continue
        m = PARAM_LINE.match(line.strip())
        if not m or m.group(1) in seen:
            continue
        name, desc = m.group(1), m.group(2).strip()
        seen.add(name)
        default = DEFAULT_RE.search(desc)
        params.append({
            "name": name,
            "required": desc.endswith("*"),
            "default": default.group(1).strip() if default else None,
            "positional_only": False,
            "keyword_only": False,
            "doc": desc.rstrip("* ").strip(),
        })
    return params


def make_callable(sig: str | None, doc_lines: list[str], is_method: bool) -> dict:
    text = _join(doc_lines)
    nonblank = [line.strip() for line in doc_lines if line.strip()]
    entry = {"signature": sig, "summary": nonblank[0] if nonblank else ""}
    parsed = parse_signature(sig, is_method) if sig else None
    if parsed is not None:
        params, varargs, varkw = parsed
        entry.update(params=params, params_source="signature",
                     accepts_varargs=varargs, accepts_varkw=varkw)
    else:
        params = parse_doc_params(doc_lines)
        entry.update(params=params, params_source="docstring" if params else "none",
                     accepts_varargs=False, accepts_varkw=False)
    if re.search(r"\bdeprecated\b", text, re.IGNORECASE):
        entry["deprecated"] = True
    first_real = next((l for l in nonblank if not l.lower().startswith("deprecated")), "")
    if first_real.startswith("Show "):
        entry["gui_only"] = True          # dialogs: "Show dialog ...", "Show message box."
    note = HEADLESS_NOTE.search(text)
    if note:
        entry["headless_note"] = note.group(0).strip()
    gui_params = [p["name"] for p in params
                  if re.search(r"only in GUI mode", p.get("doc", ""), re.IGNORECASE)]
    if gui_params:
        entry["gui_only_params"] = gui_params
    return entry


# --------------------------------------------------------------------------
# Section parsers
# --------------------------------------------------------------------------
def _section_kind(text: str):
    for rx, kind in SECTIONS:
        m = rx.match(text)
        if m:
            return kind, (m.group(1) if kind == "inherited" else "")
    return None


def _parse_class_body(cname: str, body: list[str], module: str, docs: list) -> dict:
    doc, raw_members = [], []
    kind, source, current, skip = None, "", None, False
    for content in body:
        stripped = content.strip()
        if SEPARATOR.fullmatch(stripped):
            current = None
            continue
        if stripped and _indent(content) <= 2:
            sec = _section_kind(stripped)
            if sec:
                kind, source = sec
                skip = kind == "inherited" and source.startswith("builtins.")
                current = None
                continue
        if kind is None:                       # class docstring precedes all sections
            doc.append(content)
            continue
        if skip:
            continue
        if stripped and _indent(content) == 2:
            m = MEMBER_HDR.match(content)
            if m:
                current = {"name": m.group(1), "sig": m.group(2), "value": m.group(3),
                           "kind": kind, "source": source, "doc": []}
                raw_members.append(current)
                continue
        if current is not None:
            current["doc"].append(content)

    members = {}
    for mem in raw_members:
        if mem["name"] in members:
            continue
        if mem["kind"] == "attribute" or mem["sig"] is None:
            entry = {"kind": "attribute", "summary": _summary(mem["doc"])}
            if mem["value"] is not None:
                entry["value"] = mem["value"]
        else:
            mkind = "instance" if mem["kind"] == "inherited" else mem["kind"]
            entry = {"kind": mkind, **make_callable(mem["sig"], mem["doc"], mkind == "instance")}
        if mem["kind"] == "inherited":
            entry["inherited_from"] = mem["source"]
        members[mem["name"]] = entry
        docs.append((f"{module}.{cname}.{mem['name']}", "\n".join(mem["doc"])))

    class_doc = _join(doc)
    docs.append((f"{module}.{cname}", class_doc))
    return {"summary": _summary(doc), "members": members, "_doc": class_doc}


def _parse_classes(lines: list[str], module: str, docs: list):
    classes, tree = {}, set()
    i, n = 0, len(lines)
    while i < n and not CLASS_HDR.match(lines[i]):       # inheritance tree
        for tok in re.split(r"[\s,()]+", lines[i].strip()):
            if tok and IDENT.fullmatch(tok):
                tree.add(tok)
        i += 1
    while i < n:
        m = CLASS_HDR.match(lines[i])
        if not m:
            i += 1
            continue
        cname, body = m.group(1), []
        i += 1
        while i < n:
            line = lines[i]
            bm = BODY_LINE.match(line)
            if bm:
                body.append(bm.group(1))
            elif line.strip():
                break
            else:
                body.append("")
            i += 1
        classes[cname] = _parse_class_body(cname, body, module, docs)
    return classes, tree


def _parse_functions(lines: list[str], module: str, docs: list) -> dict:
    raw, current = [], None
    for line in lines:
        m = FUNC_HDR.match(line)
        if m:
            current = (m.group(1), m.group(2), [])
            raw.append(current)
        elif current is not None:
            current[2].append(line)
    funcs = {}
    for name, sig, doc in raw:
        if name not in funcs:
            funcs[name] = make_callable(sig, doc, is_method=False)
            docs.append((f"{module}.{name}", "\n".join(doc)))
    return funcs


def _parse_data(lines: list[str]) -> dict:
    consts = {}
    for line in lines:
        m = DATA_LINE.match(line)
        if not m:
            continue
        raw = m.group(2).strip()
        try:
            vtype = type(ast.literal_eval(raw)).__name__
        except (ValueError, SyntaxError):
            vtype = None
        consts[m.group(1)] = {"value": raw, "type": vtype}
    return consts


def _split_sections(lines: list[str]) -> dict:
    sections, current = {}, None
    for line in lines:
        if line in TOP_HEADERS:
            current = line
            sections.setdefault(current, [])
        elif current is not None:
            sections[current].append(line)
    return sections


def split_modules(text: str):
    """Yield (module-name-or-None, dedented lines) for each help() capture."""
    lines = _clean_lines(text)
    starts = [i for i, line in enumerate(lines) if HELP_START.match(line)]
    blocks = []
    if starts:
        for k, i in enumerate(starts):
            m = HELP_START.match(lines[i])
            end = starts[k + 1] if k + 1 < len(starts) else len(lines)
            blocks.append((m.group(2), _dedent(lines[i:end], len(m.group(1)))))
    else:
        for i, line in enumerate(lines):
            if line.strip() == "NAME":
                blocks.append((None, _dedent(lines[i:], _indent(line))))
                break
    return blocks


def parse_module(name_hint, lines: list[str], problems: list):
    sections = _split_sections(lines)
    declared, _, mdoc = _summary(sections.get("NAME", [])).partition(" - ")
    declared = declared.strip()
    module = name_hint or declared
    if not module:
        problems.append("A capture block has no module name (no 'Help on ...' or NAME line).")
        return None
    if name_hint and declared and declared != name_hint:
        problems.append(f"Header says module '{name_hint}' but NAME says '{declared}'.")
    docs = [(module, mdoc)]
    classes, tree = _parse_classes(sections.get("CLASSES", []), module, docs)
    functions = _parse_functions(sections.get("FUNCTIONS", []), module, docs)
    constants = _parse_data(sections.get("DATA", []))

    if tree != set(classes):
        problems.append(
            f"{module}: CLASSES hierarchy lists {len(tree)} classes but {len(classes)} class "
            f"blocks were parsed (listed only: {sorted(tree - set(classes))}; "
            f"parsed only: {sorted(set(classes) - tree)}). Capture truncated or misread?")
    if any(l.strip() for l in sections.get("FUNCTIONS", [])) and not functions:
        problems.append(f"{module}: FUNCTIONS section present but no function headers parsed.")
    if not (classes or functions or constants):
        problems.append(f"{module}: nothing parsed.")
    data = {"summary": mdoc.strip(), "classes": classes, "functions": functions,
            "constants": constants}
    return module, data, docs


# --------------------------------------------------------------------------
# Cross-module passes: return types and undeclared doc references
# --------------------------------------------------------------------------
def _returns_for(modules: dict, mod: str, cls: str, source: str) -> dict:
    declared = mod in modules and cls in modules[mod]["classes"]
    return {"kind": "instance" if declared else "undeclared",
            "type": f"{mod}.{cls}", "source": source}


def infer_returns(modules: dict) -> None:
    for mod, data in modules.items():
        callables = [(f"{mod}.{name}", entry) for name, entry in data["functions"].items()]
        for cname, cls in data["classes"].items():
            callables += [(f"{mod}.{cname}.{mname}", m) for mname, m in cls["members"].items()
                          if m["kind"] != "attribute"]
        # 1. The callable's own first docstring line names the returned type.
        for qual, entry in callables:
            summary = entry.get("summary", "")
            m = OWN_DOC_LIST.search(summary)
            if m:
                elem = _returns_for(modules, m.group(1), m.group(2), f"docstring of {qual}")
                entry["returns"] = {"kind": "list", "element": elem, "source": elem["source"]}
                continue
            m = OWN_DOC_RETURNS.search(summary)
            if m:
                entry["returns"] = _returns_for(modules, m.group(1), m.group(2),
                                                f"docstring of {qual}")
        # 2. A class docstring names the function that produces it.
        for cname, cls in data["classes"].items():
            for fmod, fname in CLASS_DOC_FACTORY.findall(cls.get("_doc", "")):
                target = modules.get(fmod, {}).get("functions", {}).get(fname)
                if fmod == mod and target is not None and "returns" not in target:
                    target["returns"] = _returns_for(modules, mod, cname,
                                                     f"class docstring of {mod}.{cname}")
        # 3. "... a copy of this Matrix and return the result" / "Creates an identity matrix"
        for cname, cls in data["classes"].items():
            copy_rx = re.compile(rf"\bcopy of (?:this|the) {re.escape(cname)}\b", re.IGNORECASE)
            make_rx = re.compile(rf"^Creates? an? .*\b{re.escape(cname.lower())}\b", re.IGNORECASE)
            for mname, m in cls["members"].items():
                if m["kind"] == "attribute" or "returns" in m:
                    continue
                summary = m.get("summary", "")
                if copy_rx.search(summary) and re.search(r"\breturn", summary, re.IGNORECASE):
                    m["returns"] = _returns_for(modules, mod, cname, f"docstring of {mod}.{cname}.{mname}")
                elif m["kind"] == "class" and make_rx.search(summary):
                    m["returns"] = _returns_for(modules, mod, cname, f"docstring of {mod}.{cname}.{mname}")


def _declared_names(data: dict) -> set:
    return set(data["functions"]) | set(data["classes"]) | set(data["constants"])


def undeclared_doc_references(modules: dict, docs: list) -> dict:
    found = {}
    for owner, text in docs:
        for mod, name, tail in REF_RE.findall(text or ""):
            if mod not in modules:
                continue
            prefix = bool(tail) and name.endswith("_")
            names = _declared_names(modules[mod])
            ok = any(s.startswith(name) for s in names) if prefix else name in names
            if ok:
                continue
            key = (mod, name, prefix)
            rec = found.setdefault(key, {"symbol": f"{mod}.{name}", "prefix": prefix,
                                         "mentioned_in": []})
            if owner not in rec["mentioned_in"]:
                rec["mentioned_in"].append(owner)
    out = {}
    for (mod, _, _), rec in sorted(found.items()):
        rec["mentioned_in"].sort()
        out.setdefault(mod, []).append(rec)
    return out


# --------------------------------------------------------------------------
# Public API
# --------------------------------------------------------------------------
def build_index(sources, build: str, source_commit: str | None = None):
    """sources: iterable of (label, text[, sha256-of-file-bytes]).
    Returns (index_dict, problems)."""
    modules, docs, problems, source_records = {}, [], [], []
    for item in sources:
        label, text = item[0], item[1]
        digest = item[2] if len(item) > 2 else hashlib.sha256(text.encode("utf-8")).hexdigest()
        found = []
        for hint, lines in split_modules(text):
            parsed = parse_module(hint, lines, problems)
            if parsed is None:
                continue
            module, data, mdocs = parsed
            if module in modules:
                problems.append(f"Module '{module}' appears in more than one capture; "
                                f"kept the first, ignored the one in {label}.")
                continue
            modules[module] = data
            docs.extend(mdocs)
            found.append(module)
        if not found:
            problems.append(f"{label}: no help() capture recognised.")
        source_records.append({"file": label, "modules": found, "sha256": digest})

    infer_returns(modules)
    refs = undeclared_doc_references(modules, docs)
    for data in modules.values():
        for cls in data["classes"].values():
            cls.pop("_doc", None)

    index = {
        "schema": SCHEMA_VERSION,
        "generator": GENERATOR,
        "build": build,
        "source_commit": source_commit,
        "sources": source_records,
        "modules": modules,
        "doc_references": refs,
        "notes": [
            "params_source 'signature' comes from a real pydoc signature; 'docstring' from "
            "KeyShot's 'name = description *' lines (documented order assumed for positional "
            "use); 'none' means the dump gives no usable parameter information.",
            "returns entries exist only where the dump text states the type; see each 'source'.",
            "doc_references lists symbols that docstrings mention but this capture never "
            "declares. They require a runtime check (hasattr/dir in KeyShot) before use.",
        ],
    }
    return index, problems


def summarise(index: dict) -> list[str]:
    lines = []
    for mod, data in index["modules"].items():
        typed = sum(1 for e in data["functions"].values() if "returns" in e)
        typed += sum(1 for c in data["classes"].values()
                     for m in c["members"].values() if "returns" in m)
        members = sum(len(c["members"]) for c in data["classes"].values())
        lines.append(
            f"{mod}: {len(data['classes'])} classes ({members} members), "
            f"{len(data['functions'])} functions, {len(data['constants'])} constants, "
            f"{typed} stated return types, "
            f"{len(index['doc_references'].get(mod, []))} undeclared doc references")
    return lines


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Build symbols.json from KeyShot help() captures.")
    ap.add_argument("dumps", nargs="+", help="help(lux) / help(luxmath) capture files (.md/.txt)")
    ap.add_argument("--build", required=True, help="KeyShot build label, e.g. 2026.3-beta")
    ap.add_argument("-o", "--output", default="symbols.json", help="output path (default: symbols.json)")
    ap.add_argument("--source-commit", default=None, help="repository commit SHA to record")
    ap.add_argument("--allow-inconsistent", action="store_true",
                    help="write the index even if self-checks fail")
    args = ap.parse_args(argv)

    sources = []
    for name in args.dumps:
        path = Path(name)
        try:
            raw = path.read_bytes()
        except OSError as exc:
            print(f"build_symbol_index: cannot read {name}: {exc}", file=sys.stderr)
            return 2
        sources.append((path.as_posix(), raw.decode("utf-8", errors="replace"),
                        hashlib.sha256(raw).hexdigest()))

    index, problems = build_index(sources, args.build, args.source_commit)
    for line in summarise(index):
        print(line, file=sys.stderr)
    for mod, refs in index["doc_references"].items():
        for ref in refs:
            kind = "prefix" if ref["prefix"] else "symbol"
            print(f"  undeclared {kind} {ref['symbol']}"
                  f"{'*' if ref['prefix'] else ''} - mentioned in "
                  f"{', '.join(ref['mentioned_in'][:3])}"
                  f"{' ...' if len(ref['mentioned_in']) > 3 else ''}", file=sys.stderr)
    for p in problems:
        print(f"PROBLEM: {p}", file=sys.stderr)
    if problems and not args.allow_inconsistent:
        print("build_symbol_index: self-check failed; index not written "
              "(use --allow-inconsistent to override).", file=sys.stderr)
        return 1

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(index, indent=1, sort_keys=True, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"wrote {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
