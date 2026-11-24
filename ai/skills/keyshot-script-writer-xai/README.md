# KeyShot Script Writer Skill

A Grok / Claude skill for generating accurate, complete, runnable Python scripts that control KeyShot via the built-in `lux` and `luxmath` modules.

**KeyShot Studio 2026.3 API references** — [`lux`](references/KeyShot_lux_API.md) and [`luxmath`](references/KeyShot_luxmath_API.md).

Static verification only — scripts are not claimed to have been executed inside KeyShot unless a live runtime observation was performed.

## Contents

```
keyshot-script-writer/
├── SKILL.md                          # Skill definition + core instructions
├── CHANGELOG.md                      # Version history
├── assets/
│   └── keyshot_script_template.py    # Clean starter template
├── evals/
│   ├── evals.json
│   ├── triggers.json
│   └── static_regression.py          # Static scanner for known unsafe patterns
└── references/
    ├── KeyShot_lux_API.md            # Full 2026.3 lux dump
    ├── KeyShot_luxmath_API.md        # Full 2026.3 luxmath dump
    ├── constraints.md                # Hard rules
    ├── best-practices.md
    ├── 2026-corrections.md
    ├── OpenPBR_and_Planar_Light.md
    ├── glossary.md
    ├── keyshot-script-examples.md
    ├── KeyShot_Best_Practices_Examples.md
    └── Advanced_Material_Graph_Cheat_Sheet.md
```

## Installation (Grok)

1. Place this folder in your skills directory (or the path your Grok instance uses for custom skills).
2. The skill triggers on requests such as:
   - “write a KeyShot script to…”
   - “generate KeyShot Python code for…”
   - “automate rendering in KeyShot”
   - “KeyShot script for turntable / batch / XR / materials”

## Key Rules the Skill Enforces

- Only symbols that exist in the 2026.3 dumps.
- Complete, self-contained scripts with a `USER SETTINGS` block at the top.
- Progress prints and explicit error handling.
- GUI calls (`lux.getInputDialog`, etc.) guarded with `if not lux.isHeadless()`.
- No invented facilities (undo, logging, progress bars, external packages).
- `lux` / `luxmath` + minimal stdlib only.

## Related Upstream Repos

- https://github.com/donaldtuttle/Unofficial_KeyShot_Python
- https://github.com/donaldtuttle/KeyShot-Python-AI-Knowledge

## License

This skill package is provided for use with Grok (and compatible agents). The API dumps and examples are derived from KeyShot’s embedded scripting console. Use at your own risk; always test scripts in a non-production scene.
