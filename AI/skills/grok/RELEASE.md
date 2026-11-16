# Grok private skill: frozen v1.3.1 release

The independent **keyshot-script-writer v1.3.1** ZIP is a validated Grok-specific release of KeyShot Python scripting guidance. It supplements, and **does not replace**, the canonical [provider-agnostic core](../../skill.md) or this platform's [Grok adapter](SKILL.md).

**Release source:** `keyshot-script-writer-v1.3.1-release.zip` (the supplied corrected release archive).

**ZIP SHA-256:** `da15e2b8b1fbd08eb853b147392e6830aa157b24747c4f8860e0a4c39e301d42`.

The release has 16 files, including both KeyShot Studio 2026.3 beta API dumps, the script template, best-practice references, evaluation JSON and an executable **static** regression checker. The archive's static checker passes. No live GUI, headless, scene, or render result is certified.

## Import into this repository

Run from the repository root, with an actual local copy of the approved ZIP:

```bash
python tools/import_grok_release.py path/to/keyshot-script-writer-v1.3.1-release.zip
python platform-releases/grok/v1.3.1/evals/static_regression.py
git add platform-releases/grok/v1.3.1
git commit -m "Archive frozen Grok KeyShot script writer v1.3.1"
git push
```

The importer verifies the **exact ZIP SHA**, all 16 expected member paths, the ZIP's integrity, both API references against current repository files, and the static regression script. It refuses overwrite and writes a per-file provenance manifest.

The source is stored under `platform-releases/` (outside `AI/`) so that the shared ChatGPT, Grok and Claude package builder doesn't accidentally absorb a second set of Grok-only instructions into every platform ZIP.

**Important:** This README and importer are repository preparation. The original release ZIP itself is **not** committed or installed merely by adding these files. Do not claim otherwise.
