#!/usr/bin/env python3
"""Import the frozen Grok v1.3.1 skill ZIP without altering the agnostic core."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import stat
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "platform-releases" / "grok" / "v1.3.1"
EXPECTED_ZIP_SHA256 = "da15e2b8b1fbd08eb853b147392e6830aa157b24747c4f8860e0a4c39e301d42"
EXPECTED_PREFIX = "keyshot-script-writer/"
EXPECTED_NAMES = {
    "SKILL.md", "CHANGELOG.md", "assets/keyshot_script_template.py",
    "evals/triggers.json", "evals/evals.json", "evals/static_regression.py",
    "references/keyshot-script-examples.md", "references/KeyShot_luxmath_API.md",
    "references/KeyShot_Best_Practices_Examples.md", "references/OpenPBR_and_Planar_Light.md",
    "references/Advanced_Material_Graph_Cheat_Sheet.md", "references/glossary.md",
    "references/2026-corrections.md", "references/best-practices.md",
    "references/KeyShot_lux_API.md", "references/constraints.md",
}
API_PAIRS = (
    ("references/KeyShot_lux_API.md", "lux/KeyShot_lux_API.md"),
    ("references/KeyShot_luxmath_API.md", "lux/KeyShot_luxmath_API.md"),
)

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_file", type=Path, help="Original v1.3.1 release ZIP")
    args = parser.parse_args()
    source = args.zip_file.resolve()
    archive = source.read_bytes()
    if sha256(archive) != EXPECTED_ZIP_SHA256:
        parser.error("Refusing unrecognized release ZIP (SHA-256 mismatch)")
    if DEST.exists():
        parser.error(f"Destination already exists: {DEST}. No overwrite is permitted.")
    with zipfile.ZipFile(source) as z:
        if z.testzip() is not None:
            parser.error("ZIP integrity check failed")
        names = z.namelist()
        if len(names) != len(set(names)) or any(not n.startswith(EXPECTED_PREFIX) for n in names):
            parser.error("Unexpected, duplicate, or unsafe archive paths")
        subpaths = set()
        for entry in z.infolist():
            rel = entry.filename[len(EXPECTED_PREFIX):]
            path = Path(rel)
            if (not rel or path.is_absolute() or ".." in path.parts or
                    "\\\\" in rel or ":" in rel or entry.is_dir() or
                    stat.S_ISLNK(entry.external_attr >> 16)):
                parser.error(f"Unsafe ZIP entry: {entry.filename}")
            subpaths.add(path.as_posix())
        if subpaths != EXPECTED_NAMES:
            parser.error("Package file inventory differs from the frozen v1.3.1 release")
        for member, repo_path in API_PAIRS:
            if z.read(EXPECTED_PREFIX + member) != (ROOT / repo_path).read_bytes():
                parser.error(f"API dump differs from repository: {member}")
        DEST.mkdir(parents=True)
        for name in sorted(names):
            target = DEST / name[len(EXPECTED_PREFIX):]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(z.read(name))
    check = subprocess.run(
        [sys.executable, str(DEST / "evals" / "static_regression.py")],
        text=True, capture_output=True, check=False,
    )
    if check.returncode:
        print(check.stdout, check.stderr, file=sys.stderr)
        shutil.rmtree(DEST)
        raise SystemExit("Static regression check failed; imported directory discarded")
    manifest = {
        "name": "Grok KeyShot Script Writer", "version": "1.3.1",
        "source_zip_name": source.name, "zip_sha256": EXPECTED_ZIP_SHA256,
        "runtime_tested": False,
        "files": [{"path": p, "sha256": sha256((DEST / p).read_bytes())} for p in sorted(EXPECTED_NAMES)],
    }
    (DEST / "SOURCE_MANIFEST.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print("PASS: v1.3.1 imported and static checks passed.")
    print(f"Added under {DEST.relative_to(ROOT)} (not installed in Grok).")
    print("Commit platform-releases/grok/v1.3.1 separately; do not overwrite AI/skill.md.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
