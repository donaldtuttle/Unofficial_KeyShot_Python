#!/usr/bin/env python3
"""
verify_symbols.py  v1.0.0

Static check of KeyShot Python scripts against a symbol index produced by
build_symbol_index.py from help(lux) / help(luxmath) captures.

Usage
    python verify_symbols.py my_script.py --index references/api/2026.3-beta/symbols.json
    python verify_symbols.py my_script.py --build 2026.3-beta
        (searches ../references/**/symbols.json next to this file, then ./symbols.json)
    python verify_symbols.py a.py b.py --json        machine-readable output
    python verify_symbols.py a.py --strict           warnings and policy notes also fail

The script under test is parsed, never imported or executed, and lux is never
imported. Nothing here proves runtime behaviour: GUI, headless, render and
visual checks still require KeyShot.

What is checked
    * every lux.* / luxmath.* name, including "from lux import ..." and
      constant-string getattr(lux, "...");
    * members of values whose type the dump states (lux.getSceneTree() ->
      SceneNode, lux.getMaterialGraph() -> MaterialGraph, luxmath.Matrix()
      chains, ...). Types also flow into helper-function parameters from their
      call sites and from annotations such as  def f(node: lux.SceneNode);
    * for lux-derived values of unknown type, that the member exists on at
      least one declared lux/luxmath class (owner unverified);
    * call arguments: real signatures strictly, docstring-derived parameters
      as warnings;
    * deprecated API, save/export calls that throw in headless mode without
      a path, and skill-contract policy items (non-stdlib imports,
      subprocess/threading/network modules, open(), dialogs with no
      lux.isHeadless() check anywhere in the script).

Severity
    ERROR   not declared in the dump, wrong owner, or a call that breaks a
            real signature
    PROBE   only mentioned in dump docstrings, never declared - confirm in
            KeyShot before use (a console snippet is printed)
    WARN    docstring-based argument mismatch, deprecated API, headless
            hazard, unknown member on an untyped lux-derived value
    POLICY  skill-contract item that needs explicit task authorisation

Exit status: 0 clean, 1 errors, 2 probes (or warnings/policy with --strict),
3 usage or index error.

Standard library only. Runs in ordinary Python 3.9+, not inside KeyShot.
"""

from __future__ import annotations

import argparse
import re
import ast
import difflib
import hashlib
import json
import sys
import tokenize
from collections import Counter
from pathlib import Path

VERSION = "verify_symbols.py 1.0.0"
LUX_MODULES = ("lux", "luxmath")
SEVERITY_RANK = {"ERROR": 0, "PROBE": 1, "WARN": 2, "POLICY": 3}
SENSITIVE_STDLIB = {
    "subprocess", "threading", "multiprocessing", "socket", "socketserver", "asyncio",
    "concurrent", "ctypes", "http", "urllib", "ssl", "ftplib", "smtplib", "xmlrpc",
    "webbrowser",
}
STDLIB = getattr(sys, "stdlib_module_names", None)       # Python 3.10+
SEQUENCE_BUILTINS = {"sorted", "reversed", "list", "tuple", "set", "frozenset"}

# Attribute names that belong to plain Python values (str, list, dict, ...).
# A lux call that returns such a value may be followed by these freely.
BUILTIN_MEMBERS: set = set()
for _t in (str, bytes, bytearray, list, tuple, dict, set, frozenset, int, float,
           complex, bool, range, object):
    BUILTIN_MEMBERS.update(dir(_t))

# --------------------------------------------------------------------------
# Abstract values (plain tuples so they compare and hash cheaply)
#   ("module", mod)                 ("class", mod, cls)       ("inst", mod, cls)
#   ("func", mod, name)             ("method", mod, cls, name, bound)
#   ("undecl", mod, dotted_name)    ("list", element_value)
#   ("taint",)  lux-derived, type unknown
#   ("tmember", attr)  attribute of a tainted value
#   ("unknown",)  ("none",)
# --------------------------------------------------------------------------
UNKNOWN = ("unknown",)
TAINT = ("taint",)
NONE = ("none",)
LUXISH = {"module", "class", "inst", "func", "method", "undecl", "taint", "tmember"}


def is_luxish(v) -> bool:
    return v[0] in LUXISH or (v[0] == "list" and is_luxish(v[1]))


def combine(values) -> tuple:
    """Flow-insensitive merge of every value a name is bound to."""
    vals = [v for v in values if v != NONE]
    if not vals:
        return UNKNOWN
    if all(v == vals[0] for v in vals):
        return vals[0]
    return TAINT if any(is_luxish(v) for v in vals) else UNKNOWN


def element_of(v) -> tuple:
    if v[0] == "list":
        return v[1]
    if v[0] in ("inst", "taint", "tmember", "undecl"):
        return TAINT
    return UNKNOWN


# --------------------------------------------------------------------------
# Index
# --------------------------------------------------------------------------
class SymbolIndex:
    def __init__(self, data: dict, path: str = "<memory>", sha256: str | None = None):
        if data.get("schema") != 1 or "modules" not in data:
            raise ValueError(f"{path}: not a schema-1 symbols.json")
        self.path = path
        self.sha256 = sha256
        self.build = data.get("build") or "unknown-build"
        self.modules = data["modules"]
        self.owners: dict = {}                    # member name -> ["lux.SceneNode", ...]
        for mod, mdata in self.modules.items():
            for cname, cls in mdata["classes"].items():
                for mname in cls["members"]:
                    self.owners.setdefault(mname, []).append(f"{mod}.{cname}")
        self.doc_exact: dict = {}
        self.doc_prefix: dict = {}
        for mod, refs in data.get("doc_references", {}).items():
            for ref in refs:
                short = ref["symbol"].split(".", 1)[1]
                bucket = self.doc_prefix if ref.get("prefix") else self.doc_exact
                bucket.setdefault(mod, {})[short] = ref.get("mentioned_in", [])

    def has_module(self, mod: str) -> bool:
        return mod in self.modules

    def module_symbol(self, mod: str, name: str):
        mdata = self.modules.get(mod)
        if mdata is None:
            return None
        for kind, key in (("func", "functions"), ("class", "classes"), ("const", "constants")):
            if name in mdata[key]:
                return kind, mdata[key][name]
        return None

    def module_names(self, mod: str) -> list:
        mdata = self.modules.get(mod, {})
        return [*mdata.get("functions", {}), *mdata.get("classes", {}), *mdata.get("constants", {})]

    def member(self, mod: str, cls: str, name: str):
        try:
            return self.modules[mod]["classes"][cls]["members"].get(name)
        except KeyError:
            return None

    def class_members(self, mod: str, cls: str) -> list:
        try:
            return list(self.modules[mod]["classes"][cls]["members"])
        except KeyError:
            return []

    def doc_mention(self, mod: str, name: str):
        if name in self.doc_exact.get(mod, {}):
            return self.doc_exact[mod][name]
        for prefix, owners in self.doc_prefix.get(mod, {}).items():
            if name.startswith(prefix):
                return owners
        return None


def value_from_returns(spec) -> tuple:
    if not spec:
        return TAINT
    if spec.get("kind") == "list":
        return ("list", value_from_returns(spec.get("element")))
    mod, _, cls = spec.get("type", "").partition(".")
    if spec.get("kind") == "instance":
        return ("inst", mod, cls)
    if spec.get("kind") == "undeclared":
        return ("undecl", mod, cls)
    return TAINT


def _suggest(name: str, candidates) -> str:
    close = difflib.get_close_matches(name, list(candidates), n=3, cutoff=0.7)
    return f" Closest declared: {', '.join(close)}." if close else ""


# --------------------------------------------------------------------------
# Analyzer
# --------------------------------------------------------------------------
class Analyzer:
    def __init__(self, index: SymbolIndex, tree: ast.Module, policy: bool = True, source: str = ""):
        self.index = index
        self.tree = tree
        self.policy = policy
        self.source = source
        self.findings: list = []
        self._seen: set = set()
        self.stats: Counter = Counter()
        self.scope_of: dict = {}
        self.parent_scope: dict = {}
        self.bindings: dict = {}           # (scope, name) -> [(mode, payload, eval_scope)]
        self.annotations: dict = {}        # (scope, name) -> (annotation, eval_scope)
        self.funcdefs: dict = {}           # (scope, name) -> FunctionDef
        self.global_names: dict = {}       # scope -> {names declared global}
        self.values: dict = {}
        self.star_imports: list = []
        self.probes: set = set()           # (mod, root name) for the console snippet
        self.gui_calls: list = []
        self.file_io: list = []
        self.headless_checked = False
        self.allows: dict = {}          # code -> reason
        self.allowances: list = []

    # ---- findings --------------------------------------------------------
    def add(self, severity, node, code, symbol, message):
        line = getattr(node, "lineno", 0)
        col = getattr(node, "col_offset", -1) + 1
        key = (line, col, code, message)
        if key in self._seen:
            return
        self._seen.add(key)
        if severity == "POLICY" and code in self.allows:
            self.allowances.append({
                "severity": "ALLOW", "line": line, "col": col, "code": code,
                "symbol": symbol, "message": message,
                "reason": self.allows[code],
            })
            return
        self.findings.append({"severity": severity, "line": line, "col": col,
                              "code": code, "symbol": symbol, "message": message})

    # ---- scopes ----------------------------------------------------------
    def _assign_scopes(self, node, scope):
        for child in ast.iter_child_nodes(node):
            self.scope_of[child] = scope
            if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda, ast.ClassDef)):
                self.parent_scope[child] = scope
                self._assign_scopes(child, child)
            else:
                self._assign_scopes(child, scope)

    def lookup_scope(self, scope, name):
        if name in self.global_names.get(scope, ()):
            return self.tree
        s, first = scope, True
        while s is not None:
            # Class bodies are not visible from the functions nested in them.
            if (first or not isinstance(s, ast.ClassDef)) and (
                    (s, name) in self.bindings or (s, name) in self.annotations):
                return s
            first = False
            s = self.parent_scope.get(s)
        return None

    def _key(self, scope, name):
        return (self.tree if name in self.global_names.get(scope, ()) else scope, name)

    def _bind(self, scope, name, mode, payload, eval_scope):
        self.bindings.setdefault(self._key(scope, name), []).append((mode, payload, eval_scope))

    def _bind_target(self, target, mode, expr, scope):
        if isinstance(target, ast.Name):
            self._bind(scope, target.id, mode, expr, scope)
        elif isinstance(target, ast.Starred):
            self._bind_target(target.value, mode, expr, scope)
        elif isinstance(target, (ast.Tuple, ast.List)):
            elts = target.elts
            if (mode == "value" and isinstance(expr, (ast.Tuple, ast.List))
                    and len(expr.elts) == len(elts)
                    and not any(isinstance(e, ast.Starred) for e in elts + expr.elts)):
                for t, e in zip(elts, expr.elts):
                    self._bind_target(t, "value", e, scope)
                return
            if (mode == "element" and len(elts) == 2 and isinstance(expr, ast.Call)
                    and isinstance(expr.func, ast.Name) and expr.func.id == "enumerate"
                    and expr.args):
                self._bind_target(elts[0], "const", UNKNOWN, scope)
                self._bind_target(elts[1], "element", expr.args[0], scope)
                return
            sub = "part" if mode == "value" else "element_part"
            for t in elts:
                self._bind_target(t, sub, expr, scope)

    # ---- collection pass -------------------------------------------------
    def _collect(self):
        for node in ast.walk(self.tree):
            if isinstance(node, ast.Global):
                self.global_names.setdefault(self.scope_of.get(node, self.tree), set()).update(node.names)
        for node in ast.walk(self.tree):
            s = self.scope_of.get(node, self.tree)
            if isinstance(node, ast.Import):
                self._bind_import(node, s)
            elif isinstance(node, ast.ImportFrom):
                self._bind_import_from(node, s)
            elif isinstance(node, ast.Assign):
                for t in node.targets:
                    self._bind_target(t, "value", node.value, s)
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                self.annotations[self._key(s, node.target.id)] = (node.annotation, s)
                if node.value is not None:
                    self._bind_target(node.target, "value", node.value, s)
            elif isinstance(node, (ast.For, ast.AsyncFor, ast.comprehension)):
                self._bind_target(node.target, "element", node.iter, s)
            elif isinstance(node, (ast.With, ast.AsyncWith)):
                for item in node.items:
                    if item.optional_vars is not None:
                        self._bind_target(item.optional_vars, "value", item.context_expr, s)
            elif isinstance(node, ast.NamedExpr):
                self._bind_target(node.target, "value", node.value, s)
            elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.Lambda)):
                if not isinstance(node, ast.Lambda):
                    self.funcdefs[self._key(s, node.name)] = node
                    self._bind(s, node.name, "const", UNKNOWN, s)
                a = node.args
                for arg in [*a.posonlyargs, *a.args, *a.kwonlyargs, a.vararg, a.kwarg]:
                    if arg is None:
                        continue
                    self.bindings.setdefault((node, arg.arg), [])      # parameter is local
                    if getattr(arg, "annotation", None) is not None:
                        self.annotations[(node, arg.arg)] = (arg.annotation, s)
            elif isinstance(node, ast.ClassDef):
                self._bind(s, node.name, "const", UNKNOWN, s)
            elif isinstance(node, ast.ExceptHandler) and node.name:
                self._bind(s, node.name, "const", UNKNOWN, s)

        # Call sites give helper-function parameters their types.
        for node in ast.walk(self.tree):
            if not (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)):
                continue
            s = self.scope_of.get(node, self.tree)
            ds = self.lookup_scope(s, node.func.id)
            fd = self.funcdefs.get((ds, node.func.id)) if ds is not None else None
            if fd is None:
                continue
            positional = [a.arg for a in [*fd.args.posonlyargs, *fd.args.args]]
            named = set(positional) | {a.arg for a in fd.args.kwonlyargs}
            for i, arg in enumerate(node.args):
                if isinstance(arg, ast.Starred) or i >= len(positional):
                    break
                self.bindings[(fd, positional[i])].append(("value", arg, s))
            for kw in node.keywords:
                if kw.arg in named:
                    self.bindings[(fd, kw.arg)].append(("value", kw.value, s))

    def _bind_import(self, node, s):
        for alias in node.names:
            top = alias.name.split(".")[0]
            bound = alias.asname or top
            if top not in LUX_MODULES:
                self._bind(s, bound, "const", UNKNOWN, s)
                self._policy_import(node, alias.name)
                continue
            if alias.name != top:
                self.add("ERROR", node, "E-IMPORT", alias.name,
                         f"'{alias.name}': {top} is a built-in module with no submodules.")
            if not self.index.has_module(top):
                self.add("WARN", node, "W-NO-DUMP", top,
                         f"The index has no {top} capture; {top}.* usage is not checked.")
                self._bind(s, bound, "const", UNKNOWN, s)
            else:
                self._bind(s, bound, "const", ("module", top), s)

    def _bind_import_from(self, node, s):
        mod = node.module or ""
        top = mod.split(".")[0]
        if node.level or top not in LUX_MODULES:
            for alias in node.names:
                if alias.name != "*":
                    self._bind(s, alias.asname or alias.name, "const", UNKNOWN, s)
            if not node.level:
                self._policy_import(node, mod)
            return
        if mod != top:
            self.add("ERROR", node, "E-IMPORT", mod, f"'{mod}': {top} has no submodules.")
        if not self.index.has_module(top):
            self.add("WARN", node, "W-NO-DUMP", top,
                     f"The index has no {top} capture; names imported from it are not checked.")
            for alias in node.names:
                if alias.name != "*":
                    self._bind(s, alias.asname or alias.name, "const", UNKNOWN, s)
            return
        for alias in node.names:
            if alias.name == "*":
                self.add("WARN", node, "W-STAR-IMPORT", top,
                         f"'from {top} import *' hides which API names the script relies on.")
                self.star_imports.append(top)
                continue
            self.check_module_symbol(top, alias.name, node)
            self._bind(s, alias.asname or alias.name, "const",
                       self.module_member_value(top, alias.name), s)

    def _policy_import(self, node, modname):
        if not self.policy or not modname:
            return
        top = modname.split(".")[0]
        if top in SENSITIVE_STDLIB:
            self.add("POLICY", node, "S-SENSITIVE", top,
                     f"imports '{top}': subprocess, threading and network use need explicit "
                     f"task authorisation.")
        elif STDLIB is not None and top not in STDLIB and top != "__future__":
            self.add("POLICY", node, "S-IMPORT", top,
                     f"'{top}' is not in the standard library; third-party packages are "
                     f"usually unavailable in KeyShot's embedded Python.")

    # ---- value inference -------------------------------------------------
    def module_member_value(self, mod, name):
        if not self.index.has_module(mod):
            return UNKNOWN
        sym = self.index.module_symbol(mod, name)
        if sym:
            if sym[0] == "func":
                return ("func", mod, name)
            if sym[0] == "class":
                return ("class", mod, name)
            return UNKNOWN                      # constants are plain values
        if self.index.doc_mention(mod, name) is not None:
            return ("undecl", mod, name)
        return UNKNOWN

    def member_value(self, base, attr):
        k = base[0]
        if attr.startswith("__") and attr.endswith("__"):
            return UNKNOWN
        if k == "module":
            return self.module_member_value(base[1], attr)
        if k in ("class", "inst"):
            entry = self.index.member(base[1], base[2], attr)
            if entry is None:
                return UNKNOWN
            if entry["kind"] == "attribute":
                return TAINT
            bound = k == "inst" or entry["kind"] != "instance"
            return ("method", base[1], base[2], attr, bound)
        if k == "undecl":
            return ("undecl", base[1], f"{base[2]}.{attr}")
        if k in ("taint", "tmember"):
            return ("tmember", attr)
        return UNKNOWN

    def _builtin_name(self, node, scope, names):
        return (isinstance(node, ast.Name) and node.id in names
                and self.lookup_scope(scope, node.id) is None)

    def call_value(self, call, scope):
        f = call.func
        if self._builtin_name(f, scope, SEQUENCE_BUILTINS) and call.args:
            return ("list", element_of(self.infer(call.args[0], scope)))
        if self._builtin_name(f, scope, {"getattr"}) and len(call.args) >= 2 \
                and isinstance(call.args[1], ast.Constant) and isinstance(call.args[1].value, str):
            return self.member_value(self.infer(call.args[0], scope), call.args[1].value)
        callee = self.infer(f, scope)
        k = callee[0]
        if k == "func":
            entry = self.index.modules[callee[1]]["functions"][callee[2]]
            return value_from_returns(entry.get("returns"))
        if k == "method":
            entry = self.index.member(callee[1], callee[2], callee[3]) or {}
            return value_from_returns(entry.get("returns"))
        if k == "class":
            return ("inst", callee[1], callee[2])
        if k == "tmember":
            return UNKNOWN if callee[1] in BUILTIN_MEMBERS else TAINT
        if k == "undecl":
            return ("undecl", callee[1], callee[2] + "()")
        return UNKNOWN

    def infer(self, e, scope):
        if isinstance(e, ast.Name):
            s = self.lookup_scope(scope, e.id)
            if s is None:
                for mod in self.star_imports:
                    if self.index.module_symbol(mod, e.id):
                        return self.module_member_value(mod, e.id)
                return UNKNOWN
            return self.values.get((s, e.id), UNKNOWN)
        if isinstance(e, ast.Constant):
            return NONE if e.value is None else UNKNOWN
        if isinstance(e, ast.Attribute):
            return self.member_value(self.infer(e.value, scope), e.attr)
        if isinstance(e, ast.Call):
            return self.call_value(e, scope)
        if isinstance(e, ast.Subscript):
            return element_of(self.infer(e.value, scope))
        if isinstance(e, ast.IfExp):
            return combine([self.infer(e.body, scope), self.infer(e.orelse, scope)])
        if isinstance(e, ast.BoolOp):
            return combine([self.infer(v, scope) for v in e.values])
        if isinstance(e, (ast.NamedExpr, ast.Await)):
            return self.infer(e.value, scope)
        if isinstance(e, (ast.List, ast.Tuple, ast.Set)) and e.elts:
            return ("list", combine([self.infer(x, scope) for x in e.elts]))
        if isinstance(e, (ast.ListComp, ast.SetComp, ast.GeneratorExp)):
            return ("list", self.infer(e.elt, scope))
        return UNKNOWN

    def annotation_value(self, ann, scope):
        if isinstance(ann, ast.Constant) and isinstance(ann.value, str):
            try:
                ann = ast.parse(ann.value, mode="eval").body
            except SyntaxError:
                return None
        if isinstance(ann, ast.BinOp) and isinstance(ann.op, ast.BitOr):        # X | None
            for side in (ann.left, ann.right):
                if not (isinstance(side, ast.Constant) and side.value is None):
                    return self.annotation_value(side, scope)
            return None
        if isinstance(ann, ast.Subscript):                                      # Optional[X], List[X]
            head = ann.value.attr if isinstance(ann.value, ast.Attribute) else getattr(ann.value, "id", "")
            inner = ann.slice
            if head == "Optional":
                return self.annotation_value(inner, scope)
            if head in ("list", "List", "Sequence", "Iterable", "set", "Set"):
                v = self.annotation_value(inner, scope)
                return ("list", v) if v else None
            return None
        v = self.infer(ann, scope)
        if v[0] == "class":
            return ("inst", v[1], v[2])
        if v[0] == "undecl":
            return v
        return None

    def _evaluate(self, key):
        ann = self.annotations.get(key)
        if ann is not None:
            v = self.annotation_value(*ann)
            if v is not None:
                return v
        vals = []
        for mode, payload, es in self.bindings.get(key, []):
            if mode == "const":
                vals.append(payload)
            elif mode == "value":
                vals.append(self.infer(payload, es))
            elif mode in ("element", "part"):
                vals.append(element_of(self.infer(payload, es)))
            elif mode == "element_part":
                vals.append(element_of(element_of(self.infer(payload, es))))
        return combine(vals)

    def _solve(self):
        keys = set(self.bindings) | set(self.annotations)
        for _ in range(12):
            changed = False
            for key in keys:
                new = self._evaluate(key)
                if self.values.get(key, UNKNOWN) != new:
                    self.values[key] = new
                    changed = True
            if not changed:
                break

    # ---- check pass ------------------------------------------------------
    def check_module_symbol(self, mod, name, node):
        if not self.index.has_module(mod):
            return
        if mod == "lux" and name == "isHeadless":
            self.headless_checked = True
        sym = self.index.module_symbol(mod, name)
        if sym:
            self.stats["module_verified"] += 1
            kind, entry = sym
            if kind == "func" and entry.get("deprecated"):
                self.add("WARN", node, "W-DEPRECATED", f"{mod}.{name}",
                         f"{mod}.{name} is marked deprecated in the dump: \"{entry.get('summary', '')}\"")
            return
        mention = self.index.doc_mention(mod, name)
        if mention is not None:
            where = ", ".join(mention[:3]) + (" ..." if len(mention) > 3 else "")
            self.add("PROBE", node, "P-DOC-ONLY", f"{mod}.{name}",
                     f"{mod}.{name} is not declared in the {self.index.build} dump, though the "
                     f"docs of {where} mention it. Confirm it exists in KeyShot before use.")
            self.probes.add((mod, name))
            self.stats["probe"] += 1
            return
        self.add("ERROR", node, "E-UNDECLARED", f"{mod}.{name}",
                 f"{mod}.{name} is not declared in the {self.index.build} dump."
                 + _suggest(name, self.index.module_names(mod)))
        self.stats["not_found"] += 1

    def _check_attribute(self, node, scope):
        attr = node.attr
        if attr.startswith("__") and attr.endswith("__"):
            return
        base = self.infer(node.value, scope)
        k = base[0]
        if k == "module":
            self.check_module_symbol(base[1], attr, node)
        elif k in ("class", "inst"):
            mod, cls = base[1], base[2]
            entry = self.index.member(mod, cls, attr)
            if entry is not None:
                self.stats["owner_verified"] += 1
                if entry.get("deprecated"):
                    self.add("WARN", node, "W-DEPRECATED", f"{mod}.{cls}.{attr}",
                             f"{mod}.{cls}.{attr} is marked deprecated in the dump.")
                return
            others = [o for o in self.index.owners.get(attr, []) if o != f"{mod}.{cls}"]
            hint = (f" It exists on {', '.join(others)} - wrong owner?" if others
                    else _suggest(attr, self.index.class_members(mod, cls)))
            self.add("ERROR", node, "E-NO-MEMBER", f"{mod}.{cls}.{attr}",
                     f"{mod}.{cls} has no member '{attr}' in the {self.index.build} dump.{hint}")
            self.stats["not_found"] += 1
        elif k == "undecl":
            self.add("PROBE", node, "P-UNDECLARED-TYPE", f"{base[1]}.{base[2]}.{attr}",
                     f"'.{attr}' is used on {base[1]}.{base[2]}, which the dump mentions but never "
                     f"declares, so its members cannot be verified.")
            self.probes.add((base[1], base[2].split(".")[0].rstrip("()")))
            self.stats["probe"] += 1
        elif k in ("taint", "tmember"):
            if attr in BUILTIN_MEMBERS:
                return
            if attr in self.index.owners:
                self.stats["owner_unverified"] += 1
                return
            self.add("WARN", node, "W-UNKNOWN-MEMBER", attr,
                     f"'.{attr}' is not a member of any class in the {self.index.build} dump "
                     f"(the receiver comes from lux but its type is not stated)."
                     + _suggest(attr, self.index.owners))
            self.stats["not_found"] += 1

    def _check_args(self, call, entry, label, implicit_self=False, inferred_owner=False):
        if not entry or entry.get("kind") == "attribute":
            return
        src = entry.get("params_source", "none")
        if src == "none":
            return
        if any(isinstance(a, ast.Starred) for a in call.args) or any(k.arg is None for k in call.keywords):
            return
        if entry.get("accepts_varargs") and entry.get("accepts_varkw"):
            return
        self.stats["calls_checked"] += 1
        self.stats[f"calls_{src}"] += 1
        params = entry.get("params", [])
        strict = src == "signature" and not inferred_owner
        basis = "its signature" if src == "signature" else "its documented parameters (documented order assumed)"
        if inferred_owner:
            basis += f"; owner inferred because only {label.rsplit('.', 1)[0]} defines this name"
        npos = max(0, len(call.args) - (1 if implicit_self else 0))
        keywords = [k.arg for k in call.keywords]
        positional = [p for p in params if not p.get("keyword_only")]
        names = {p["name"]: p for p in params}
        problems = []
        if npos > len(positional) and not entry.get("accepts_varargs"):
            problems.append(f"takes {len(positional)} positional argument(s), {npos} given")
        for kw in keywords:
            p = names.get(kw)
            if p is None:
                if not entry.get("accepts_varkw"):
                    known = f" (documented: {', '.join(names)})" if names else " (no parameters)"
                    problems.append(f"unknown keyword '{kw}'{known}")
            elif p.get("positional_only"):
                problems.append(f"'{kw}' is positional-only")
        filled = {p["name"] for p in positional[:npos]}
        for kw in keywords:
            if kw in filled:
                problems.append(f"'{kw}' given both positionally and by keyword")
        filled |= set(keywords)
        missing = [p["name"] for p in params if p.get("required") and p["name"] not in filled]
        if missing:
            problems.append("missing required " + ", ".join(f"'{m}'" for m in missing))
        if problems:
            self.add("ERROR" if strict else "WARN", call, "E-ARGS" if strict else "W-ARGS", label,
                     f"{label}(): " + "; ".join(problems) + f" - per {basis}.")

    def _check_hazards(self, call, entry, label):
        if entry.get("gui_only"):
            self.gui_calls.append((call, label))
        note = entry.get("headless_note")
        if note:
            params = entry.get("params", [])
            first = params[0]["name"] if params else None
            given = bool(call.args) or any(k.arg == first for k in call.keywords)
            if not given:
                self.add("WARN", call, "W-HEADLESS", label,
                         f"{label}() is called without '{first}'. The dump says: \"{note}\"")

    def _check_call(self, call, scope):
        f = call.func
        if self._builtin_name(f, scope, {"getattr"}):
            if len(call.args) >= 2 and isinstance(call.args[1], ast.Constant) \
                    and isinstance(call.args[1].value, str):
                base = self.infer(call.args[0], scope)
                if base[0] == "module" and len(call.args) == 2:
                    self.check_module_symbol(base[1], call.args[1].value, call)
            return
        if self._builtin_name(f, scope, {"open"}):
            self.file_io.append(call)
            return
        callee = self.infer(f, scope)
        k = callee[0]
        if k == "func":
            entry = self.index.modules[callee[1]]["functions"][callee[2]]
            label = f"{callee[1]}.{callee[2]}"
            self._check_args(call, entry, label)
            self._check_hazards(call, entry, label)
        elif k == "method":
            mod, cls, name, bound = callee[1:]
            entry = self.index.member(mod, cls, name)
            label = f"{mod}.{cls}.{name}"
            self._check_args(call, entry, label, implicit_self=not bound)
            if entry:
                self._check_hazards(call, entry, label)
        elif k == "tmember":
            owners = self.index.owners.get(callee[1], [])
            if len(owners) == 1:
                mod, _, cls = owners[0].partition(".")
                entry = self.index.member(mod, cls, callee[1])
                self._check_args(call, entry, f"{owners[0]}.{callee[1]}", inferred_owner=True)

    def _collect_allows(self):
        """# kpsa: allow CODE -- reason. Reason is required."""
        pattern = re.compile(r"^\s*#\s*kpsa:\s*allow\s+([A-Z0-9-]+)\s*(?:--\s*(.+))?\s*$")
        for i, line in enumerate(self.source.splitlines(), 1):
            m = pattern.match(line)
            if not m:
                continue
            code, reason = m.group(1), (m.group(2) or "").strip()
            if not code.startswith("S-"):
                self.findings.append({
                    "severity": "WARN", "line": i, "col": 1, "code": "W-ALLOW",
                    "symbol": code,
                    "message": "kpsa allow applies to POLICY codes only. ERROR and PROBE cannot be silenced.",
                })
                continue
            if not reason:
                self.findings.append({
                    "severity": "WARN", "line": i, "col": 1, "code": "W-ALLOW",
                    "symbol": code, "message": "kpsa allow comment needs a reason after --",
                })
                continue
            self.allows[code] = reason

    def _policy_checks(self):
        if not self.policy:
            return
        if self.gui_calls and not self.headless_checked:
            for call, label in self.gui_calls:
                self.add("POLICY", call, "S-HEADLESS-GUARD", label,
                         f"{label}() opens a dialog, and the script never calls lux.isHeadless(). "
                         f"Guard it if the script may run headless.")
        for call in self.file_io:
            self.add("POLICY", call, "S-FILE-IO", "open",
                     "open(): file I/O - confirm the task authorises it.")

    def run(self):
        self._collect_allows()
        self._assign_scopes(self.tree, self.tree)
        self._collect()
        self._solve()
        for node in ast.walk(self.tree):
            s = self.scope_of.get(node, self.tree)
            if isinstance(node, ast.Attribute) and isinstance(node.ctx, ast.Load):
                self._check_attribute(node, s)
            elif isinstance(node, ast.Call):
                self._check_call(node, s)
        self._policy_checks()
        self.findings.sort(key=lambda f: (f["line"], f["col"], SEVERITY_RANK[f["severity"]]))
        return self.findings


# --------------------------------------------------------------------------
# Results, reports, exit codes
# --------------------------------------------------------------------------
def probe_snippet(probes) -> str:
    if not probes:
        return ""
    lines = ["# Paste into the KeyShot scripting console:"]
    for mod in sorted({m for m, _ in probes}):
        names = sorted({n for m, n in probes if m == mod})
        lines.append(f"import {mod}")
        lines.append(f"for _name in {tuple(names)!r}:")
        lines.append(f"    print('{mod}.' + _name, hasattr({mod}, _name))")
    lines.append("# For each True: capture help(<module>.<name>) and rebuild the index.")
    return "\n".join(lines)


def exit_code_for(findings, strict: bool) -> int:
    severities = {f["severity"] for f in findings}
    if "ERROR" in severities:
        return 1
    if "PROBE" in severities or (strict and severities & {"WARN", "POLICY"}):
        return 2
    return 0


def analyze_source(source: str, index: SymbolIndex, filename: str = "<script>",
                   policy: bool = True, strict: bool = False) -> dict:
    result = {"file": filename, "syntax": "pass", "findings": [], "stats": {},
              "probe_snippet": "", "exit_code": 0}
    try:
        tree = ast.parse(source, filename=filename)
    except SyntaxError as exc:
        result["syntax"] = "fail"
        result["findings"] = [{"severity": "ERROR", "line": exc.lineno or 0, "col": exc.offset or 0,
                               "code": "E-SYNTAX", "symbol": "",
                               "message": f"Syntax error: {exc.msg}"}]
        result["exit_code"] = 1
        return result
    analyzer = Analyzer(index, tree, policy=policy, source=source)
    result["findings"] = analyzer.run()
    result["allowances"] = analyzer.allowances
    result["stats"] = dict(analyzer.stats)
    result["probe_snippet"] = probe_snippet(analyzer.probes)
    result["exit_code"] = exit_code_for(result["findings"], strict)
    return result


def render_text(result: dict, index: SymbolIndex) -> str:
    out = [result["file"]]
    for f in result["findings"]:
        loc = f"{f['line']}:{f['col']}"
        out.append(f"  {loc:<8} {f['severity']:<6} {f['code']:<18} {f['message']}")
    for a in result.get("allowances") or []:
        out.append(f"  {a['line']}:{a['col']:<4} ALLOW  {a['code']:<18} {a['message']} -- {a['reason']}")
    if not result["findings"] and not result.get("allowances"):
        out.append("  no findings")
    s = Counter(result.get("stats", {}))
    sev = Counter(f["severity"] for f in result["findings"])
    refs = s["module_verified"] + s["owner_verified"] + s["owner_unverified"] + s["probe"] + s["not_found"]
    digest = (index.sha256 or "")[:12]
    py = f"{sys.version_info.major}.{sys.version_info.minor}"
    out += [
        "",
        f"  Verification - {VERSION}, index build {index.build}" + (f" (sha256 {digest}...)" if digest else ""),
        f"    Syntax          {result['syntax']} - parsed by Python {py}, not KeyShot's interpreter",
    ]
    if result["syntax"] == "pass":
        out += [
            f"    API references  {refs}: {s['module_verified']} module-level verified, "
            f"{s['owner_verified']} owner-verified members, {s['owner_unverified']} owner-unverified, "
            f"{s['probe']} probe, {s['not_found']} not found",
            f"    Call arguments  {s['calls_checked']} checked "
            f"({s['calls_signature']} by signature, {s['calls_docstring']} by docstring)",
        ]
    out += [
        f"    Findings        {sev['ERROR']} error, {sev['PROBE']} probe, {sev['WARN']} warning, "
        f"{sev['POLICY']} policy",
        "    Not run         GUI runtime, headless runtime, render, visual (require KeyShot)",
    ]
    if result.get("probe_snippet"):
        out += ["", "  Runtime probe:"] + ["    " + l for l in result["probe_snippet"].splitlines()]
    return "\n".join(out)


def find_index(build: str | None) -> Path:
    here = Path(__file__).resolve().parent
    candidates = []
    for root in (here.parent / "references", here / "references"):
        if root.is_dir():
            candidates += sorted(root.rglob("symbols.json"))
    for extra in (here / "symbols.json", Path.cwd() / "symbols.json"):
        if extra.is_file():
            candidates.append(extra)
    matches = []
    for path in dict.fromkeys(candidates):
        try:
            data_build = json.loads(path.read_text(encoding="utf-8")).get("build")
        except (OSError, ValueError):
            continue
        if build is None or data_build == build:
            matches.append((path, data_build))
    if not matches:
        raise ValueError(f"no symbols.json found{' for build ' + build if build else ''}; pass --index")
    if len(matches) > 1 and build is None:
        listed = ", ".join(f"{b} ({p})" for p, b in matches)
        raise ValueError(f"several indexes found - choose one with --build: {listed}")
    return matches[0][0]


def load_index(path: Path) -> SymbolIndex:
    raw = path.read_bytes()
    return SymbolIndex(json.loads(raw.decode("utf-8")), str(path), hashlib.sha256(raw).hexdigest())


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check KeyShot scripts against a lux/luxmath symbol index.")
    ap.add_argument("scripts", nargs="+", help="Python files to check")
    group = ap.add_mutually_exclusive_group()
    group.add_argument("--index", help="path to symbols.json")
    group.add_argument("--build", help="find symbols.json for this build label, e.g. 2026.3-beta")
    ap.add_argument("--json", action="store_true", help="print JSON instead of text")
    ap.add_argument("--strict", action="store_true", help="warnings and policy notes also fail (exit 2)")
    ap.add_argument("--no-policy", action="store_true", help="skip skill-contract policy checks")
    args = ap.parse_args(argv)

    try:
        index = load_index(Path(args.index) if args.index else find_index(args.build))
    except (OSError, ValueError) as exc:
        print(f"verify_symbols: {exc}", file=sys.stderr)
        return 3

    results = []
    for name in args.scripts:
        try:
            with tokenize.open(name) as fh:
                source = fh.read()
        except (OSError, SyntaxError) as exc:
            print(f"verify_symbols: cannot read {name}: {exc}", file=sys.stderr)
            return 3
        results.append(analyze_source(source, index, name, policy=not args.no_policy,
                                      strict=args.strict))

    code = max(r["exit_code"] for r in results)
    if args.json:
        print(json.dumps({"tool": VERSION, "index": {"path": index.path, "build": index.build,
                                                    "sha256": index.sha256},
                          "results": results, "exit_code": code}, indent=1))
    else:
        print("\n\n".join(render_text(r, index) for r in results))
    return code


if __name__ == "__main__":
    sys.exit(main())
