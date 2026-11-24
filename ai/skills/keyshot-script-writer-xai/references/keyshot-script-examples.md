# KeyShot Script Examples & Advanced Patterns

This reference supplements the main SKILL.md. Some snippets are complete and executable; others are illustrative and may contain placeholders or incomplete signatures. Non-executable fragments are labeled as such. All lux/luxmath symbols must still be verified against the 2026.3 beta dumps before use.

## Table of Contents
- Advanced Still Render with Passes and Post Effects
- Material Graph Editing Example (Color + Roughness)
- Using luxmath for Precise Transforms
- Headless / CLI Scripting Notes
- Queue Management & Batch Processing
- Common Constants Reference
- Troubleshooting & Debugging Tips

## Advanced Still Render with Passes and Post Effects
```python
import lux
import os

output_dir = r"C:\Renders\Hero"
os.makedirs(output_dir, exist_ok=True)

# Setup
env = lux.getActiveEnvironment()
env.setLightingEnvironment(r"C:\HDRI\neutral_studio.exr")
env.setBrightness(0.9)
env.setGroundReflections(True)

cam = lux.getCamera()
lux.setCameraPosition((120, -180, 95))
lux.setCameraLookAt((0, 0, 40))
lux.setCameraFieldOfView(32)

# Render options + passes
opts = lux.getRenderOptions()
opts.setMaxSamplesRendering(96)
lux.setRenderEngine(lux.RENDER_ENGINE_PRODUCT)
opts.setGlobalIllumination(3)
opts.setOutputAlphaChannel(True)
opts.setOutputDepthPass(True)
opts.setOutputNormalsPass(True)
opts.setOutputDiffusePass(True)
opts.setOutputShadowPass(True)
opts.setOutputReflectionPass(True)
opts.setDofQuality(2)  # if using depth of field

# Image style (post)
style = lux.getActiveImageStyle()
style.setBloom(True)
style.setVignette(True)
style.setDenoise(True)

# Render
lux.renderImage(os.path.join(output_dir, "hero_beauty.jpg"), 2560, 1440, opts, lux.RENDER_OUTPUT_JPEG)
print("Beauty + passes rendered. Check output folder for AOVs.")
```

## Material Graph Editing Example
Editing node graphs requires care — always backup first (`lux.saveFile()`).

```python
import lux

mat_name = "Product Shell"
graph = lux.getMaterialGraph(mat_name)
if not graph:
    print(f"Material '{mat_name}' not found")
else:
    # Find diffuse nodes (use SHADER_TYPE constant, not string)
    diffuse_nodes = graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE)
    if diffuse_nodes:
        node = diffuse_nodes[0]
        color_param = node.getParameter("Color") or node.getParameter("Base Color")
        if color_param:
            color_param.setValue((0.8, 0.2, 0.1))  # Reddish
            print(f"Updated color on {mat_name}")
    
    # Roughness example
    rough_param = node.getParameter("Roughness") if 'node' in locals() else None
    if rough_param:
        rough_param.setValue(0.35)
    
    graph.executeGeometryNodes()  # If any displacement/geometry nodes present
```

## Using luxmath for Precise Transforms & Calculations
```python
import lux
import luxmath

root = lux.getSceneTree()
matches = root.find("Logo Plate")

if matches and len(matches) == 1:
    obj = matches[0]
    # Get current transform
    current = obj.getTransform(world=True)
    
    # Correct luxmath: translate takes a Vector
    trans = luxmath.Matrix().makeIdentity().translate(luxmath.Vector((0, 0, 25)))
    # rotateY is not a documented Matrix method in the 2026.3 luxmath dump.
    # Use documented rotate / rotateAxis methods only after verifying the signature.
    new_transform = trans
    obj.applyTransform(new_transform)
    print("Object transformed")
elif matches:
    print(f"Ambiguous: {len(matches)} matches for 'Logo Plate'")
else:
    print("Node not found")
```

## Headless / CLI Scripting Notes
KeyShot supports headless execution (no GUI). Typical invocation (exact flags depend on platform/version):

```
keyshot.exe --headless --script "C:\Scripts\my_automation.py" --scene "C:\Scenes\product.ksp" --output "C:\Renders"
```

Inside script you can still use most lux calls. Some UI-dependent features (dialogs, certain previews) are unavailable. Use `print()` for logging; output is captured in console or log file.

Check KeyShot documentation or `--help` for your specific build. Combine with task schedulers or render farm wrappers for overnight batches.

## Queue Management & Batch Processing
```python
import lux

opts = lux.getRenderOptions()
opts.setAddToQueue(True)  # or set via RenderOptions

# Queue multiple renders
lux.renderImage("preview.jpg", 800, 600, opts, lux.RENDER_OUTPUT_JPEG)
# Correct argument order for renderAnimation
lux.renderAnimation("anim_frames", "f_%d.exr", True, 1920, 1080, 24, None, opts, lux.RENDER_OUTPUT_EXR)

# Later or in separate script
lux.processQueue()  # Starts processing the render queue
```

Useful for submitting many jobs without blocking the main thread.

## Common Constants Reference (selected)

**Render Output Formats**
- `lux.RENDER_OUTPUT_JPEG`
- `lux.RENDER_OUTPUT_PNG`
- `lux.RENDER_OUTPUT_EXR`
- `lux.RENDER_OUTPUT_TIFF8`, `TIFF32`
- `lux.RENDER_OUTPUT_PSD8`, `PSD16`, `PSD32`

**Render Engines / Modes**
- `lux.RENDER_ENGINE_PRODUCT`, `RENDER_ENGINE_INTERIOR`
- `lux.RENDER_ENGINE_PRODUCT_GPU`, `RENDER_ENGINE_INTERIOR_GPU`
- `lux.RENDER_MODE_ADVANCED`, `RENDER_MODE_TIME`, `RENDER_MODE_SAMPLES`

**Standard Views**
- `lux.VIEW_FRONT`, `VIEW_BACK`, `VIEW_LEFT`, `VIEW_RIGHT`, `VIEW_TOP`, `VIEW_BOTTOM`, `VIEW_ISOMETRIC`

**Units**
- `lux.UNIT_MM`, `UNIT_CM`, `UNIT_M`, `UNIT_IN`, `UNIT_FT`

**Export Formats** (for `lux.exportFile`)
- `lux.EXPORT_OBJ`, `EXPORT_FBX`, `EXPORT_GLTF`, `EXPORT_STL`, `EXPORT_3MF`, `EXPORT_USD`

**XR Types** (for renderXR)
- `lux.XR_TYPE_TURNTABLE`, `XR_TYPE_SPHERICAL`, `XR_TYPE_CYLINDRICAL`, `XR_TYPE_CUSTOM`

Full list available in the version-specific pydoc at media.keyshot.com/scripting/doc/

## Troubleshooting & Debugging Tips

1. **"lux module not found"**: You are running the .py outside KeyShot. Open the file from inside KeyShot's Scripting Console or use the Run button in Scripts tab. Never execute KeyShot scripts with system Python directly.

2. **Object not found by name**: Names are case-sensitive and must match exactly (including spaces). Use `root.find("Name", depth=10)` or iterate children. Print ` [c.getName() for c in root.getChildren()] ` to inspect.

3. **Material changes not visible**: After editing graphs, call `graph.executeGeometryNodes()` if geometry nodes exist. Some changes require a render refresh or `lux.saveFile()` + reload.

4. **Render looks different from interactive**: Ensure the same camera, environment, image style, and RenderOptions are applied in script. Interactive viewport may use lower quality preview settings.

5. **Performance / Long runtimes**: Reduce samples for testing. Use GPU engines when available. Disable undo. Close other applications. For very large scenes, consider splitting into model sets.

6. **Paths with backslashes**: Use raw strings `r"C:\path"` or forward slashes `/`. Python on Windows handles both in most KeyShot contexts.

7. **No output or black images**: Check camera is not inside geometry, lighting environment is valid path, samples > 0, and region is not set to a tiny area in RenderOptions.

8. **Script errors in console**: KeyShot's Python interpreter prints tracebacks. Common: wrong constant names (use `lux.` prefix), passing wrong types to setValue (check parameter type with `param.getType()`).

9. **IDE Autocompletion**: Use the community stubs repo (github.com/larsniem/keyshot-scripting-stubs). Place in your editor's python path or use as type hints.

10. **Version-specific features**: Newer KeyShot versions add more AOV passes, better GPU denoising, and additional RenderOptions keys. If a method is missing, check the pydoc for your exact KeyShot build or fall back to older equivalent.

## Next Steps for Complex Workflows

- Combine with external tools: generate CSV of variations → script reads it and sets model sets + materials in loop.
- Use `lux.getMetaData()` or custom properties for scene intelligence.
- For web-ready output, explore `renderConfiguration(..., web=True)` which can produce HTML/JSON viewers.
- Persistent settings: store user prefs in a small JSON sidecar and load at script start.

Test every script on a copy of your production scene first. When in doubt, start with a minimal working example from the main SKILL.md and iteratively add features while printing state at each step.
