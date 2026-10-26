#!/usr/bin/env python3
"""Package self-contained KPSA ChatGPT plugin and Grok/Claude skills."""
import hashlib
import json
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist"
SOURCES = ("AI", "Scripts", "lux", "luxmath", "lux_headless", "luxmath_headless")
PLATFORMS = {"ChatGPT": "keyshot-python-scripting", "Grok": "keyshot-python-grok", "Claude": "keyshot-python-claude"}
VERSION = "1.1.0"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def source_files():
    found = {}
    for directory in SOURCES:
        folder = ROOT / directory
        if not folder.is_dir():
            raise RuntimeError("Missing " + directory)
        for path in sorted(folder.rglob("*")):
            if path.is_symlink():
                raise RuntimeError("Refusing symlink: " + str(path))
            if path.is_file() and "__pycache__" not in path.parts and path.suffix != ".pyc":
                found[path.relative_to(ROOT).as_posix()] = path.read_bytes()
    for path in ("README.md", "LICENSE", "2026_updates.md"):
        found[path] = (ROOT / path).read_bytes()
    must = ("AI/skill.md", "AI/constraints.md", "AI/best-practices.md", "AI/knowledge_base.md", "AI/index.md", "AI/integrations/keyshot-mcp.md", "AI/materials/Material Metal.txt", "lux/KeyShot_lux_API.md", "lux/KeyShot_luxmath_API.md")
    must += tuple("AI/skills/" + name + "/SKILL.md" for name in ("chatgpt", "grok", "claude"))
    for path in must:
        if path not in found:
            raise RuntimeError("Missing required source: " + path)
    return found

def entry(platform, name):
    return f'''---
name: {name}
description: "KeyShot 2026.3 beta Python scripting in {platform}, using full bundled lux and luxmath API dumps, material and shader guides, and optionally connected tools."
---

# KeyShot Python Scripting Assistant for {platform}

The platform-agnostic source controls all KeyShot scripting. This package is self-contained. BEFORE creating or reviewing scripts, read the following local files in sequence:

1. references/repo/AI/constraints.md and references/repo/AI/best-practices.md
2. references/repo/AI/skill.md (shared agnostic core)
3. references/repo/AI/knowledge_base.md (TOC), then references/repo/AI/index.md
4. references/repo/lux/KeyShot_lux_API.md and references/repo/lux/KeyShot_luxmath_API.md (2026.3 beta source of truth)
5. The relevant full material file, guide or example from references/repo/AI or references/repo/Scripts
6. references/repo/AI/skills/{platform.lower()}/SKILL.md (original platform adapter)

Validate every lux/luxmath symbol, owner and argument against the relevant 2026.3 beta dump. Do not prefer historical examples or 2026.1 public docs. Follow the full constraints, use no unapproved third-party libraries in embedded KeyShot Python, and provide a complete supported script or an exact API gap. Differentiate static verification from actual KeyShot GUI/headless/render/visual tests.

GitHub retrieval is optional: only read new files from donaldtuttle/Unofficial_KeyShot_Python when a real connected repository tool is available. Original KPSA archive at donaldtuttle/KeyShot-Python-AI-Knowledge is optional historical evidence if available. Otherwise work from these bundled references and say when remote retrieval was unavailable.

Live KeyShot MCP is optional: read references/repo/AI/integrations/keyshot-mcp.md. Verify actual local tool availability; check read-only status first. Do not infer local Windows KeyShot access from a cloud chat. Never enable arbitrary execute_python automatically. Do not modify scenes, render, save or overwrite outside the user's permission.

A Markdown skill and a GitHub URL do not themselves connect tools or install an MCP server.
'''.encode()

def add(z, name, data):
    info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    z.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

def run():
    docs = source_files()
    commit = subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "HEAD"], text=True).strip()
    inventory = json.dumps({"repository": "donaldtuttle/Unofficial_KeyShot_Python", "commit": commit,
                            "files": [{"path": p, "sha256": sha(d)} for p, d in sorted(docs.items())]}, indent=2).encode()
    OUT.mkdir(exist_ok=True)
    built = []
    for platform, name in PLATFORMS.items():
        filename = "KPSA_" + platform + ("_Plugin_" if platform == "ChatGPT" else "_Skill_") + VERSION + ".zip"
        prefix = "skills/" + name if platform == "ChatGPT" else name
        entries = {prefix + "/SKILL.md": entry(platform, name), prefix + "/SOURCE_MANIFEST.json": inventory}
        entries.update({prefix + "/references/repo/" + path: data for path, data in docs.items()})
        if platform == "Claude":
            checker = (ROOT / "tools" / "verify_symbols.py").read_bytes()
            index_path = ROOT / "references" / "api" / "2026.3-beta" / "symbols.json"
            if not index_path.is_file():
                subprocess.check_call([
                    "python3", str(ROOT / "tools" / "build_symbol_index.py"),
                    str(ROOT / "lux" / "KeyShot_lux_API.md"),
                    str(ROOT / "lux" / "KeyShot_luxmath_API.md"),
                    "--build", "2026.3-beta", "-o", str(index_path),
                ])
            entries[prefix + "/scripts/verify_symbols.py"] = checker
            entries[prefix + "/references/api/2026.3-beta/symbols.json"] = index_path.read_bytes()
        msg = ("Bundled complete Unofficial_KeyShot_Python AI/scripts/API snapshot. Connected GitHub and KeyShot MCP tools are optional, not included.\n"
               "LICENSE: GPLv3. README and LICENSE agree.\n")
        if platform == "ChatGPT":
            manifest = {"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
                        "name": "keyshot-python-scripting-assistant", "version": VERSION,
                        "description": "Verified KeyShot Studio 2026.3 beta Python scripting with complete bundled reference documents.",
                        "repository": "https://github.com/donaldtuttle/Unofficial_KeyShot_Python",
                        "extensions": {"com.openai": {"interface": {"displayName": "KeyShot Python Assistant",
                          "developerName": "Don Tuttle", "category": "Developer Tools", "capabilities": [],
                          "shortDescription": "Verified KeyShot scripting", "longDescription": "Verified KeyShot scripting with full 2026.3 API and materials.",
                          "defaultPrompt": ["Write a verified KeyShot 2026.3 Python script."]}}}}
            entries["plugin.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
            entries["README.md"] = (msg + "Install/update this portable plugin ZIP through ChatGPT. Packaging does not change an installed plugin.\n").encode()
        else:
            where = ".grok/skills or ~/.grok/skills" if platform == "Grok" else "Claude Customize > Skills (ZIP upload), or .claude/skills or ~/.claude/skills for Claude Code"
            entries[prefix + "/README.md"] = (msg + "Install to " + where + ".\n").encode()
        path = OUT / filename
        with zipfile.ZipFile(path, "w") as z:
            for arcname, data in sorted(entries.items()):
                add(z, arcname, data)
        with zipfile.ZipFile(path) as z:
            assert z.testzip() is None
            assert all(sha(z.read(prefix + "/references/repo/" + p)) == sha(d) for p, d in docs.items())
            assert z.read(prefix + "/SKILL.md").startswith(b"---\n")
            if platform == "Claude":
                assert z.read(prefix + "/scripts/verify_symbols.py").startswith(b"#!/usr/bin/env python3")
                assert b"schema_version" in z.read(prefix + "/references/api/2026.3-beta/symbols.json") or z.read(prefix + "/references/api/2026.3-beta/symbols.json").startswith(b"{")
            if platform == "ChatGPT":
                assert json.loads(z.read("plugin.json"))["name"] == "keyshot-python-scripting-assistant"
        print("PASS", filename, len(docs), "source files", path.stat().st_size, "bytes")
        built.append(path)
    (OUT / "SHA256SUMS.txt").write_text("".join(sha(p.read_bytes()) + "  " + p.name + "\n" for p in built))

if __name__ == "__main__":
    run()
