# 2026 declaration and mode comparison

**Target:** KeyShot Studio 2026.2 (prefer over 2026.1 when available)

**Source note:** private KeyShot-Python-AI-Knowledge `reference/keyshot-2026/MODE-COMPARISON.md` (cleaned 2026-10-24)

The full declaration comparison contains **688 GUI** and **644 headless** lux declarations from the 2026.1 pages. All headless declarations also occur in the GUI page. The 44 GUI-page-only declarations are listed below. Presence is documentation evidence, not a runtime test; absence does not establish impossibility.

## Official sources

Primary sources (2026.1; 2026.2 public lux pages not yet available at the standard path):
- GUI lux: https://media.keyshot.com/scripting/doc/2026.1/lux.html
- Headless lux: https://media.keyshot.com/scripting/headless_doc/2026.1/lux.html
- luxmath: https://media.keyshot.com/scripting/doc/2026.1/luxmath.html

Prefer 2026.2 docs when available.

## Agent knowledge base

Read these before generating scripts. They override this file for hard rules and patterns.

- [Constraints](../constraints.md) — mandatory hard rules (node IDs, dialogs, matrices, verification, API limits)
- [Best practices](../best-practices.md)
- [Knowledge base](../knowledge_base.md) — TOC and workflow
- [Index](../index.md) — topic pointers
- [System prompt](../system_prompt.md)
- [Skill](../skill.md)

## GUI-page-only declarations

These appear only on the GUI lux page (not in the headless page):

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
- OpenPBR and Planar Light parameters are reachable only by inspecting the material graph (get nodes → get parameters). They are not library constants.
