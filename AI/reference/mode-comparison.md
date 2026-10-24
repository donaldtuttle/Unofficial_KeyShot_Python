# 2026 declaration and mode comparison

**Target:** KeyShot Studio 2026.2 (prefer over 2026.1 when available)

**Source note:** private KeyShot-Python-AI-Knowledge `reference/keyshot-2026/MODE-COMPARISON.md` (corrected 2026-10-24)

The full declaration comparison contains **688 GUI** and **644 headless** lux declarations from the 2026.1 pages. All headless declarations also occur in the GUI page. The 44 GUI-page-only declarations are listed below. Presence is documentation evidence, not a runtime test; absence does not establish impossibility.

Primary sources (2026.1; 2026.2 public lux pages not yet available at the standard path):
- GUI lux: https://media.keyshot.com/scripting/doc/2026.1/lux.html
- Headless lux: https://media.keyshot.com/scripting/headless_doc/2026.1/lux.html
- luxmath: https://media.keyshot.com/scripting/doc/2026.1/luxmath.html

## Supplied-only discrepancies (not promoted)

These entries appear in supplied/historical indexes but are not corroborated as library-level constants or functions in the available 2026 reference. Do not treat them as usable API.

- `lux.CAMERA_MODE_ORBIT`
- `lux.CAMERA_MODE_PATH`
- `lux.getAnimations`
- `lux.getNodeAnimations`

**Removed from discrepancy list (user correction):**
- `SHADER_TYPE_OPENPBR` and `SHADER_TYPE_PLANAR_LIGHT` are **not** library constants. OpenPBR and Planar Light parameters are only reachable by inspecting the material graph (get nodes → get parameters). They do not exist as `SHADER_TYPE_*` values in the library.

## GUI-page-only declarations

- `lux.DIALOG_CHECK`
- `lux.DIALOG_DOUBLE`
- `lux.DIALOG_FILE`
- `lux.DIALOG_FOLDER`
- `lux.DIALOG_INTEGER`
- `lux.DIALOG_ITEM`
- `lux.DIALOG_LABEL`
- `lux.DIALOG_TEXT`
- `lux.MESSAGE_BOX_CRITICAL`
- `lux.MESSAGE_BOX_INFO`
- `lux.MESSAGE_BOX_WARNING`
- `lux.UNIT_CM`
- `lux.UNIT_FT`
- `lux.UNIT_IN`
- `lux.UNIT_M`
- `lux.UNIT_MM`
- `lux.XR_CENTER_CAMERA`
- `lux.XR_CENTER_CAMERA_PIVOT`
- `lux.XR_CENTER_ENVIRONMENT`
- `lux.XR_CENTER_OBJECT`
- `lux.XR_TYPE_CUSTOM`
- `lux.XR_TYPE_HEMISPHERICAL`
- `lux.XR_TYPE_SPHERICAL`
- `lux.XR_TYPE_TUMBLE`
- `lux.XR_TYPE_TURNTABLE`
- `lux.dumpTree`
- `lux.getActiveConfiguration`
- `lux.getBrowserDialog`
- `lux.getInputDialog`
- `lux.getInputDouble`
- `lux.getInputFile`
- `lux.getInputFolder`
- `lux.getInputInt`
- `lux.getInputItem`
- `lux.getInputText`
- `lux.getMessageBox`
- `lux.isUndoEnabled`
- `lux.renderConfiguration`
- `lux.renderFrames`
- `lux.renderMultiMaterial`
- `lux.renderXR`
- `lux.screenshot`
- `lux.setSceneUnit`
- `lux.setUndoEnabled`

## Notes

- 2026.2 release notes mention additional animation scripting (create/edit/delete object and camera keyframe animations) and script performance improvements. Specific new function names are not listed in the public notes.
- Prefer official 2026.2 lux reference when it becomes available.
