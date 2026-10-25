# 2026 declaration and mode comparison

**Target:** KeyShot Studio 2026.3 beta

**API source of truth:** [`lux/KeyShot_lux_API.md`](../../lux/KeyShot_lux_API.md) — `help(lux)` from the 2026.3 beta console. Prefer this over the public 2026.1 website.

This file is a secondary comparison of the public 2026.1 website pages. It is not current for 2026.3 beta. The website lags and can omit or invent symbols.

The 2026.1 website comparison contains **688 GUI** and **644 headless** lux declarations. All headless declarations also occur in the GUI page. The 44 GUI-page-only declarations are listed below. Presence on the website is documentation evidence, not a runtime test. Absence from this list does not establish impossibility in 2026.3 beta — check the dump.

## Secondary sources (2026.1 website, lags)

- GUI lux: https://media.keyshot.com/scripting/doc/2026.1/lux.html
- Headless lux: https://media.keyshot.com/scripting/headless_doc/2026.1/lux.html
- luxmath: https://media.keyshot.com/scripting/doc/2026.1/luxmath.html

Do not prefer these over the 2026.3 beta dump.

## Agent knowledge base

Read these before generating scripts. They override this file for hard rules and patterns.

- [Constraints](../constraints.md) — mandatory hard rules (node IDs, dialogs, matrices, verification, API limits)
- [Best practices](../best-practices.md)
- [Knowledge base](../knowledge_base.md) — TOC and workflow
- [Index](../index.md) — topic pointers
- [System prompt](../system_prompt.md)
- [Skill](../skill.md)
- [2026.3 beta API dump](../../lux/KeyShot_lux_API.md) — source of truth

## GUI-page-only declarations (2026.1 website)

These appear only on the 2026.1 GUI lux page (not in the 2026.1 headless page). Confirm against the 2026.3 beta dump before use:

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

- 2026.2 release notes (superseded by the 2026.3 beta dump) mention additional animation scripting (create/edit/delete object and camera keyframe animations) and script performance improvements. Specific new function names are not listed in the public notes. Check the 2026.3 beta dump.
- OpenPBR and Planar Light parameters are reachable only by inspecting the material graph (get nodes → get parameters). They are not library constants.
