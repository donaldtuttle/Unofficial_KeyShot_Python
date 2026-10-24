# Glossary — KeyShot Python scripting

Terms used in this knowledge base. Prefer the 2026.2 dump for exact symbols.

## Scripting

- **lux** — KeyShot's built-in Python module. Scene, materials, cameras, rendering.
- **luxmath** — Companion module for vectors, matrices, and related math.
- **Headless** — KeyShot without a GUI. Avoid dialog and other GUI-only calls.
- **Scene tree** — Hierarchy of scene nodes (groups, models, objects, cameras).
- **Material graph** — Node graph of shaders, textures, and utilities for a material.
- **Node** — A scene node or a shader node. Do not mix the two.
- **Studio** — Saved combination of camera, environment, model sets, and image style.
- **Image style** — Postprocessing preset (basic or photographic).

## API rules

- **Source of truth** — `lux/KeyShot_lux_API.md`, from `help(lux)` in KeyShot 2026.2. Not the public website.
- **Node IDs** — Session-specific and unstable. Prefer names. Re-query after copy or link.
- **Pure parameter** — A parameter driven by a connection. Do not call `getValue()` on it.
- **GUI-safe** — Calls that require the GUI. Guard with `if not lux.isHeadless()`.

## Constants (examples)

- `NODE_TYPE_*` — Scene node kinds.
- `SHADER_TYPE_*` — Shader node types for `newNode` / `getNodesFromType`.
- `PARAMETER_TYPE_*` — Shader parameter kinds.
- `DIALOG_*` — Input dialog field types. GUI only.

OpenPBR and Planar Light are not library constants. Reach them by inspecting the material graph.

## Math

- **luxmath.Matrix** — 4×4 transform. Start from identity.
- **luxmath.Vector** — 3D point or direction.
- Absolute transforms only on object nodes.

## Knowledge layout

- **TOC** — `AI/knowledge_base.md`. There is no separate ToC file.
- **Index** — `AI/index.md`. Topic pointers after the TOC.
- **Examples** — `Scripts/examples/` (maintained) and `AI/examples/` (OpenPBR, Inspector).
- **Historical archive** — `Scripts/archive/HISTORICAL_SCRIPTS.md`. Not current API.
