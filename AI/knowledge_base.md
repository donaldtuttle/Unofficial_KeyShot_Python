# KeyShot Studio 2026.1 Python Knowledge Base

Baseline: KeyShot Studio 2026.1, Python 3.13 64-bit.

**Material Graph / Shader Node Authority:**
The complete list of material shader types, geometry nodes, texture nodes, and every parameter (with types) is in the `materials/` folder:
- KeyShotPythonScripting_ShaderNodeTypes&Parameters_Documentation.txt
- KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt
- Individual Material [Type].txt files (Advanced, Anisotropic, Area Light, Cutaway, Dielectric, Diffuse, Emissive, Flat, Gem, General, Generic, Generic PBR, Glass, Glass Solid, Ground, IES Light, Liquid, Measured, Metal, Metallic Paint, Multi-Layer Optics, Paint, Plastic, Plastic Cloudy, Plastic Transparent, Point Light, RealCloth, Scattering Medium, Spotlight, Thin Film, Toon, Translucent, Translucent Medium, Velvet, Wireframe, Xray, etc.)

Always consult those files for exact parameter names and types when creating or modifying material graphs. Do not guess parameter names.

Official API docs: https://media.keyshot.com/scripting/doc/2026.1/ and headless counterpart.

## Core Modules

- `lux` — scene, materials, cameras, rendering, environments, studios, metadata.
- `luxmath` — Vector and Matrix (4×4) for transforms.

## Important 2026 Features

- `node.getMetadata()` on `lux.SceneNode` → dictionary of CAD metadata.
- `lux.renderAnimation(...)` in headless (preferred, ~3× faster).
- Python 3.13.

## Scene Nodes

```python
root = lux.getSceneTree()
for node in root.find(name="Something"):
    meta = node.getMetadata()
    node.hide()
    node.setMaterial("Matte White", link=False)
    M = luxmath.Matrix().makeIdentity().translate(luxmath.Vector((1,0,0)))
    node.applyTransform(M)
```

## Rendering

```python
opts = lux.getRenderOptions()
opts.setAdvancedRendering(samples=256)
lux.renderImage("/out/frame.png", width=1920, height=1080, opts=opts)
lux.renderAnimation("/out/frames", frameFiles="frame.%04d.png", width=1920, height=1080, fps=30, opts=opts)
```

## Materials & Graphs

Use the materials/ docs for parameter names.

```python
graph = lux.getMaterialGraph("MyMat")
root_node = graph.getRoot()
param = root_node.getParameter("color")  # confirm exact name in materials/ docs
param.setValue((1, 0, 0))
```

## When Uncertain

Point to official 2026.1 docs or the materials/ parameter lists. Suggest `help(lux.SomeClass)` inside the console.
