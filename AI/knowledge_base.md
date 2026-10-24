# KeyShot Studio 2026.1 Python Knowledge Base

Baseline: KeyShot Studio 2026.1, Python 3.13 64-bit.
Official docs: https://media.keyshot.com/scripting/doc/2026.1/ and headless counterpart.

## Core Modules

- `lux` — scene, materials, cameras, rendering, environments, studios, metadata.
- `luxmath` — Vector and Matrix (4×4) for transforms.

## Important 2026 Features

- `node.getMetadata()` on `lux.SceneNode` → dictionary of CAD metadata attached to the node. Use this to drive logic (material assignment, visibility, camera framing, thumbnail renders) from engineer annotations.
- `lux.renderAnimation(...)` in headless: preferred path. Engine starts once; full animation is rendered (~3× faster than looping per-frame renderImage). Supports frame patterns, video output, RenderOptions.
- Python 3.13.
- Continued strong material graph, multi-material, CMF/MaterialMetadata, and export support (USD, 3MF, etc.).

## Scene Nodes

```python
root = lux.getSceneTree()
for node in root.find(name="Something"):
    meta = node.getMetadata()          # 2026
    node.hide()
    node.setMaterial("Matte White", link=False)
    M = luxmath.Matrix().makeIdentity().translate(luxmath.Vector((1,0,0)))
    node.applyTransform(M)             # relative
    # node.applyTransform(M, absolute=True)  # absolute (objects only)
```

Key methods: getName, setName, getMaterial, setMaterial, getTransform, applyTransform, getParent, getChildren, find, hide/show, getBoundingBox, snapToGround, getMetadata, isObject/isGroup/isCamera/etc.

## Rendering

```python
opts = lux.getRenderOptions()
opts.setAdvancedRendering(samples=256)
# or setMaxTimeRendering / setMaxSamplesRendering
lux.renderImage("/out/frame.png", width=1920, height=1080, opts=opts)

# Headless animation (2026 preferred)
lux.renderAnimation("/out/frames", frameFiles="frame.%04d.png", width=1920, height=1080, fps=30, opts=opts)
```

RenderOptions controls samples, time, passes (AO, shadow, caustics, layers, …), queue, background, network.

## Materials & Graphs

```python
graph = lux.getMaterialGraph("MyMat")
root_node = graph.getRoot()
param = root_node.getParameter("color")
param.setValue((1, 0, 0))
# or graph.newNode(...), newEdge, setMultiMaterial, etc.
```

MultiMaterial, MaterialMetadata (CMF text/image fields + ThumbnailRenderOptions), Colorway, ColorParameter all remain available.

## Cameras & Environment

`lux.getCamera()`, `setCamera`, `newCamera`, `setCameraPosition`, `setCameraLookAt`, `setCameraFieldOfView`.
`lux.getActiveEnvironment()` → Env (brightness, rotation, size, ground, backplate, lighting image).

## Import / Export / File

`lux.importFile`, `openFile`, `saveFile`, `exportFile` (OBJ, glTF, USD, 3MF, …). Headless defaults to non-interactive.

## Common Patterns & Constraints

- Always start transforms from `luxmath.Matrix().makeIdentity()`.
- Absolute transforms only on object nodes.
- Check return values of long operations (import, render) for cancellation/failure.
- Resource folders via `lux.getResourceFolder(...)` or constants.
- Local Python modules can be used if "Use local Python paths" is enabled (Preferences → General → Scripting), but stick to pure Python or known-compatible packages for reliability.
- Headless: no GUI dialogs; use dontAsk where available; prefer queue + processQueue for batch work.

## Example Snippets

Hide by name:
```python
root = lux.getSceneTree()
for n in root.find(name="Cord"):
    n.hide()
```

Metadata-driven material (2026):
```python
root = lux.getSceneTree()
for node in root.find(""):
    meta = node.getMetadata()
    if meta and meta.get("material") == "rubber":
        node.setMaterial("Rubber Black")
```

Headless animation render:
```python
opts = lux.getRenderOptions()
opts.setMaxTimeRendering(30)
lux.renderAnimation("/renders", frameFiles="anim.%04d.exr", width=1920, height=1080, fps=24, opts=opts)
```

## When Uncertain

Point the user at the official 2026.1 pydoc pages or suggest `help(lux.SomeClass)` / `help(lux.someFunction)` inside the KeyShot console.
