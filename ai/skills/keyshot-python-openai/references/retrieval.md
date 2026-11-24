# Targeted retrieval

Use the [Unofficial KeyShot Python repository](https://github.com/donaldtuttle/Unofficial_KeyShot_Python) for KeyShot Studio 2026.3. Use the paths below in a local checkout, or retrieve the same files from a single GitHub revision.

| Reference | Path |
| --- | --- |
| `lux` API capture | [`lux/KeyShot_lux_API.md`](https://github.com/donaldtuttle/Unofficial_KeyShot_Python/blob/main/lux/KeyShot_lux_API.md) |
| `luxmath` API capture | [`luxmath/KeyShot_luxmath_API.md`](https://github.com/donaldtuttle/Unofficial_KeyShot_Python/blob/main/luxmath/KeyShot_luxmath_API.md) |
| Headless `lux` API capture | [`lux_headless/KeyShot_headless_lux_API.md`](https://github.com/donaldtuttle/Unofficial_KeyShot_Python/blob/main/lux_headless/KeyShot_headless_lux_API.md) |
| Headless `luxmath` API capture | [`luxmath_headless/KeyShot_headless_luxmath_API.md`](https://github.com/donaldtuttle/Unofficial_KeyShot_Python/blob/main/luxmath_headless/KeyShot_headless_luxmath_API.md) |
| Scripting constraints | [`ai/skills/keyshot-script-writer-xai/references/constraints.md`](https://github.com/donaldtuttle/Unofficial_KeyShot_Python/blob/main/ai/skills/keyshot-script-writer-xai/references/constraints.md) |
| Best practices | [`ai/skills/keyshot-script-writer-xai/references/best-practices.md`](https://github.com/donaldtuttle/Unofficial_KeyShot_Python/blob/main/ai/skills/keyshot-script-writer-xai/references/best-practices.md) |

Find the exact owner-qualified declaration in the relevant module capture. Verify the arguments, types, and execution mode against the source. An ellipsis in a declaration calls for checking the accompanying argument descriptions.

See the KeyShot Studio 2026 manual for the [Scripting Console](https://manuals.keyshot.com/kss2026/en-us/manual/scripting-console.html) and [Headless Scripting](https://manuals.keyshot.com/kss2026/en-us/manual/exposed-headless-scripting-functionality.html). Check headless support in the target runtime before relying on a scene operation there.

Keep this skill’s reference files with `SKILL.md`. A separately installed skill can use a checkout specified by `KPSA_REPO`. When a required capture is unavailable, identify the missing declaration before prescribing the operation.
