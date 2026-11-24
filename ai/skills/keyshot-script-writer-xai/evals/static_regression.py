#!/usr/bin/env python3
"""
Static regression checks for keyshot-script-writer skill content.
Parses and scans Markdown/Python files for known unsafe patterns.
Does not execute KeyShot or any lux code.
"""

import ast
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UNSAFE_PATTERNS = [
    (r"setGlobalIllumination\s*\(\s*lux\.RENDER_ENGINE_", "GI quality must not receive RENDER_ENGINE_*"),
    (r"Matrix\.translate\s*\(\s*\d", "luxmath.Matrix.translate requires a Vector"),
    (r"getNodesFromType\s*\(\s*[\"']", "getNodesFromType requires a SHADER_TYPE constant"),
    (r"lux\.XR_TURN_TABLE", "use XR_TYPE_TURNTABLE"),
    (r"lux\.VIEW_PERSPECTIVE", "VIEW_PERSPECTIVE is not in the dump"),
    (r"lux\.beginUndoSession\s*\(|lux\.endUndoSession\s*\(|lux\.getProgressBar\s*\(", "absent from 2026.3 dump"),
    (r"except\s+Exception:\s*\n\s*return\s+0\s*,\s*0", "inspection failure must not become zero edges"),
]

def scan_file(path):
    issues = []
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    for i, line in enumerate(lines, 1):
        if "not present" in line or "must not be used" in line or "Do not use" in line:
            continue
        for pat, msg in UNSAFE_PATTERNS:
            if re.search(pat, line):
                issues.append(f"{os.path.basename(path)}:{i}: {msg}")
    return issues

def check_save_material_helper_calls():
    """Parse one complete documented example and verify local function arity.
    This does not import KeyShot or execute scene code.
    """
    path = os.path.join(ROOT, "references", "KeyShot_Best_Practices_Examples.md")
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    match = re.search(r"### 4\. Save[^\n]*\n\s*```python\n(.*?)\n```", text, flags=re.S)
    if not match:
        return ["material library example missing"]
    try:
        tree = ast.parse(match.group(1))
    except SyntaxError as err:
        return [f"material library example syntax error: {err}"]
    helper_name = "save_sub_materials_to_library"
    helpers = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == helper_name]
    if len(helpers) != 1:
        return ["material library helper definition missing or duplicated"]
    helper = helpers[0]
    expected = len(helper.args.posonlyargs) + len(helper.args.args)
    issues = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name) or node.func.id != helper_name:
            continue
        received = len(node.args) + len(node.keywords)
        if received != expected:
            issues.append(f"material library helper receives {received} arguments; expected {expected}")
    return issues


def main():
    issues = check_save_material_helper_calls()
    for dirpath, _, filenames in os.walk(ROOT):
        for name in filenames:
            if name.endswith((".md", ".py")) and name != "CHANGELOG.md":

                issues.extend(scan_file(os.path.join(dirpath, name)))
    if issues:
        print("STATIC REGRESSION FAILURES:")
        for i in issues:
            print(" -", i)
        sys.exit(1)
    print("Static regression checks passed (no known unsafe patterns).")
    print("Note: this does not execute KeyShot or prove runtime behavior.")

if __name__ == "__main__":
    main()
