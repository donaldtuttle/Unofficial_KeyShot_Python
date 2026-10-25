# Script catalog

Maintained examples for KeyShot Studio 2026.3 beta.

**API source of truth:** [`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md) — `help(lux)` from the 2026.3 beta console. Prefer this over the public website.

KeyShot operations require the real runtime. “Syntax verified” does not mean runtime verified.

## From the maintained example set

| Script | Purpose |
| --- | --- |
| [information/camera_info.py](information/camera_info.py) | Report current camera using documented accessors. |
| [information/scene_report.py](information/scene_report.py) | Report node kind and metadata. No scene changes. |
| [materials/report_parameters.py](materials/report_parameters.py) | Inspect graph parameters; skip pure parameters. |
| [materials/copy_concrete_parameters.py](materials/copy_concrete_parameters.py) | Copy selected plain scalars. Dry-run default. Does not clone graphs. |
| [materials/configure_ies.py](materials/configure_ies.py) | Set color and IES file on an identified shader. |
| [transformations/translate_object.py](transformations/translate_object.py) | Absolute transform on one object ID. Dry-run default. |
| [transformations/pattern_positions.py](transformations/pattern_positions.py) | Ordinary Python grid/circle/pyramid/spiral planning. No KeyShot calls. |
| [rendering/render_image_safe.py](rendering/render_image_safe.py) | Render a new PNG. Dry-run default. |
| [import-export/import_model_additive.py](import-export/import_model_additive.py) | Additive import with explicit options. Dry-run default. |
| [gui/dialog_example.py](gui/dialog_example.py) | GUI dialog with cancellation check. No scene mutation. |
| [animation/frame_sequence.py](animation/frame_sequence.py) | Held-frame render and separate encode. |
| [models/activate_model_sets.py](models/activate_model_sets.py) | Activate requested model sets after preflight. |

## Earlier reference scripts (cleaned)

| Script | Purpose |
| --- | --- |
| [materials/delete_unused_nodes.py](materials/delete_unused_nodes.py) | Remove unconnected graph nodes. Skips roots and constant colors. |
| [materials/color_gradient_connect.py](materials/color_gradient_connect.py) | Connect a Color Gradient node to a diffuse parameter. |
| [materials/save_submaterials_to_library.py](materials/save_submaterials_to_library.py) | Save multi-material sub-materials to the library. |

Also see `AI/materials/` for the OpenPBR converter and material-graph duplication note, and `AI/examples/inspector/` for the Information Inspector.

## Historical archive (not authoritative)

[`Scripts/archive/HISTORICAL_SCRIPTS.md`](../archive/HISTORICAL_SCRIPTS.md) holds older script notes. Recover a pattern from it, then verify every call against the 2026.3 beta dump before reuse. Do not treat it as current API.
