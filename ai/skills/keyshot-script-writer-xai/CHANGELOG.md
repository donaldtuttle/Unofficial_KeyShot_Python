# Changelog

## 2026-10-24 — v1.3.1 release hotfix

- Corrected the material-library example's mismatched function call (it passed three positional arguments to a two-argument helper). Removed now-unused library-path calculation and corrected the save-result wording.
- Explicitly marked four teaching/reference code fences as non-standalone or schematic; no API behavior was changed.
- Added an executable AST regression check for the previously broken material-library helper call.
- Kept the 2026.3 beta API references unchanged. No KeyShot GUI/headless or visual runtime tests were performed.

## 2026-10-24 — API compliance pass (v1.3)

Static verification against the 2026.3 beta dumps only. No KeyShot runtime execution or rendering was performed.

### Corrections
- Both orphan-cleanup helpers are now inspection-only by default. Deletion requires explicit authorization. Inspection failure is never treated as zero edges. Unknown animation nodes are protected.
- Environment creation no longer assumes `newEnvironment` returns an object. Pattern is create + activate, then re-query with `lux.getActiveEnvironment()` and verify the name before configuration.
- Sub-material saving validates the name against `lux.getSceneMaterials()` before calling `saveMaterial`. Shader-node names that are not registered scene materials are skipped and reported.
- Model-set restoration moved into a `finally` block. `setModelSets` result is checked. Variation flags are documented as all False, so the example does not claim distinct images beyond the active-set selection.
- Non-executable or incomplete snippets remain labeled as such.
- Added `evals/static_regression.py` — an executable static scanner for known unsafe patterns. It does not run KeyShot.

### Preserved
- Platform-agnostic KPSA rules.
- GitHub and MCP remain optional and are not represented as connected.
- Unsupported examples retained as explicitly marked historical/unverified rather than deleted.

## 2026-10-24 — API compliance pass (v1.2)

Static verification against the 2026.3 beta dumps only. No KeyShot runtime execution or rendering was performed.

### Corrections
- Orphan cleanup: inspection failure no longer treated as zero connections. Nodes whose edge counts cannot be read are skipped, not deleted.
- Turntable example retitled and clarified: it renders whatever animation already exists in the scene. It does not create a turntable or use an unused `frames` variable.
- `saveMaterial` example corrected: `folder` is a relative path inside the KeyShot material library, not an absolute filesystem path. Shader node names are not automatically registered scene materials.
- Batch model-set example no longer claims “all” sets. It operates on active sets, restores the previous selection, and only mentions queue mode if `setAddToQueue` is enabled.
- Direct indexing of `getNodesFromType(...)[0]` replaced with empty-result check and pure-parameter guard.
- `newEnvironment` / `setLightingEnvironment` no longer assume undocumented return contracts.
- Auto-save recommendation removed. Destructive operations remind the user; they do not save unless requested.
- Incorrect constants removed: `VIEW_PERSPECTIVE` and `XR_TURN_TABLE` (replaced with documented `XR_TYPE_*` forms).
- `DIALOG_TEXT` nonempty-default claim aligned with `2026-corrections.md`.
- Illustrative snippets labeled as non-executable where they contain placeholders.

### Preserved
- Platform-agnostic KPSA rules.
- GitHub and MCP remain optional and are not represented as connected.
- Unsupported examples retained as explicitly marked historical/unverified rather than deleted.

## 2026-10-24 — API compliance pass (v1.1)

Full static audit against the 2026.3 beta dumps. No KeyShot runtime execution or rendering was performed.

### Corrections
- Fixed `setGlobalIllumination` misuse. It takes a quality integer 0–5 (0 disables). Render engine is set separately via `lux.setRenderEngine()`.
- Fixed `renderAnimation` positional argument order (third argument is `keepFrames`, not width).
- Added `references/KeyShot_luxmath_API.md` (2026.3 beta dump). Corrected `luxmath.Matrix` usage to documented form (`Matrix().makeIdentity().translate(luxmath.Vector(...))`).
- Fixed `root.find()` examples to treat the return as a collection (check length before use).
- Fixed `getNodesFromType` to use `lux.SHADER_TYPE_*` constants, not strings.
- Clarified that `lux.getModelSets()` returns only active sets.
- Fixed `renderConfiguration` name argument to include required extension and `%d` for image mode.
- Marked `lux.beginUndoSession()`, `lux.endUndoSession()`, and `lux.getProgressBar()` as absent from the 2026.3 beta dump. Retained as explicit historical/unverified notes outside executable guidance.
- Updated template header to target 2026.3 beta and removed older-version compatibility claim.
- Added regression cases covering the confirmed errors.

### Preserved
- Platform-agnostic KPSA rules (dump wins, no invented facilities, no external libraries unless explicitly confirmed, headless guards).
- GitHub and MCP remain optional and are not represented as connected.

## 2026-10-24
- Updated from https://github.com/donaldtuttle/Unofficial_KeyShot_Python and the [private knowledge archive](https://github.com/donaldtuttle/KeyShot-Python-AI-Knowledge)
- Added 2026.3 beta `help(lux)` dump as API source of truth (`references/KeyShot_lux_API.md`)
- Added mandatory constraints, best practices, 2026 corrections, OpenPBR/Planar Light notes, and glossary
- Incorporated verification checklist, headless patterns, and "dump wins" rule into SKILL.md
- Clarified that external libraries must not be assumed, and that guides can conflict with the dump
