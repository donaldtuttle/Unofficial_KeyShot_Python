<!-- doc-id: kpsa-skills-keyshot-python-references-api-rules | target-api: 2026.3 | reviewed: 2026-10-23 -->

# KeyShot API pitfalls

- A scene node exposes `getMaterial`, `getKind`, `getName`, `getTransform` and `setMaterial`. Shader parameters belong to `ShaderNode`, not `SceneNode`. Do not turn instance methods into module functions.
- Use module camera accessors including `getCamera`, `getCameraPosition`, `getCameraLens`, `newCamera`, `setCamera` and `saveCamera`. The supplied reference does not establish a rich camera object returned by `getCamera`.
- A shader node's `getType` includes an internal type and a display name; do not feed the whole result into `newNode`. Use a verified shader constant or probe the representation in KeyShot.
- `getParameter` takes a parameter name. Check `isPure` before concrete value reads/writes; match parameter types. Shader-specific parameter tables in historical documents are candidates.
- `newEdge` needs source, target and a target parameter. An edge ID is not that parameter's name. Generic graph cloning remains unverified.
- `setMaterial(..., link=False)` documents a material duplicate; `duplicate(linkMats=False)` duplicates scene nodes/subtrees. `createMultiMaterial` creates a multi-material. Test isolation before depending on independent graph mutation.
- Absolute `applyTransform` requires an object node. Build matrices from identity; distinguish local/world and relative/absolute space. Keep transform order and intended pivot explicit.
- `setRGBA` uses 0–255; `setRGBAf` uses 0–1. Colorway entries refer to multi/sub colors already belonging together; accepted object/name representations remain partly underspecified.
- Dialog results can be `None`. `DIALOG_ITEM` returns a selection pair, not simply a string. Numeric controls require ranges. Use GUI calls only in GUI mode.
- `getRenderOptions` returns `RenderOptions`; `getImportOptions` returns a dictionary. Verify each option against its own API. No invented undo or transaction support.

For exact owner-qualified declarations, see the KeyShot Studio 2026.3 module captures in [retrieval guidance](retrieval.md).
