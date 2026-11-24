---
name: keyshot-script-writer
description: Write accurate, complete Python scripts for KeyShot using the lux module. Covers scene, materials, cameras, rendering, animations, batch, XR. Verify every call against the 2026.3 help(lux) dump. Use for any KeyShot scripting request.
---

# Keyshot Script Writer

## Overview

This skill generates accurate, complete, runnable Python scripts that control KeyShot via its built-in `lux` module. It covers scene manipulation, camera/lighting control, material graphs, rendering pipelines (still, animation, configuration, XR), and export workflows.

**API source of truth:** [`help(lux)`](references/KeyShot_lux_API.md) and [`help(luxmath)`](references/KeyShot_luxmath_API.md) from KeyShot Studio 2026.3. Check both the API signature and the documented execution mode before using a symbol.

Before generating any script:
1. Read `references/constraints.md` (mandatory hard rules) and `references/best-practices.md`.
2. Verify every `lux` / `luxmath` symbol, owner, and arguments against the 2026.3 dumps.
3. Guard GUI-only calls with `if not lux.isHeadless()` when the script may run headless.
4. Deliver complete, self-contained scripts with user settings at the top, progress prints, and explicit error handling. No placeholders or invented facilities.

## When to Use This Skill

Activate on triggers such as: "write a KeyShot script to...", "generate KeyShot Python code for...", "automate rendering in KeyShot with script", "KeyShot script for turntable", "batch render configurations KeyShot", or any debugging of lux API calls.

## Core Principles

- **Strict environment rule**: KeyShot embeds a specialized Python binding (C-backed) to the `lux` module. **Only use documented `lux.*` and `luxmath.*` functions + minimal safe stdlib (os, platform, sys, datetime)**. Never assume standard Python libraries or external packages (numpy, etc.) are available unless the user explicitly confirms they have enabled a matching local Python install in Preferences. External libraries usually fail inside KeyShot.
- The `lux` module is pre-loaded in the Scripting Console and when running .py files from the Scripts folder. Always start with `import lux` (and `import luxmath` only when using Vector/Matrix transforms).
- **All generated scripts must be COMPLETE, self-contained, and immediately runnable** in KeyShot with no placeholders, outlines, hypotheticals, or missing pieces. Every script must include: clear header, user-editable SETTINGS section at the very top, full logic, progress prints, and error handling where appropriate. The user will paste and test directly.
- Scripts execute in the context of the currently open scene. Always validate early with `lux.hasContents()` and `lux.getSceneInfo()`.
- KeyShot operations are stateful. Many methods (set*, apply*, render*) modify the live scene immediately. Do not invent undo, progress, or logging facilities that are not in the dump.
- **Exact API usage only** (from the 2026.3 dump): Use `lux.getCamera()`, `lux.getSceneTree()`, `lux.getMaterialGraph(name)`, `lux.getSceneMaterials()`, `lux.getActiveEnvironment()`, `lux.getRenderOptions()`, `lux.getInputDialog(...)`, etc. Never invent function names. Dump wins over any guide.
- For GUI interaction (Scripting Console or button scripts): Use `lux.getInputDialog(...)`. Guard with `if not lux.isHeadless()`. Handle cancellation (None). Prefer one complete dialog. See `references/constraints.md` for the headless pattern.
- Rendering: `lux.renderImage(path, width, height, opts, format)`, `lux.renderAnimation(...)`, `lux.renderConfiguration(...)`, `lux.renderXR(...)` — pass a `RenderOptions` object. Many parameters have sensible defaults. Always pass an explicit path in headless.
- Material work: Prefer `SceneNode.setMaterial(name)` or `lux.setObjectMaterial(...)` for simple cases. Use `lux.getMaterialGraph(name)` + node/parameter methods only for advanced graph editing. Re-query node IDs after any copy or link. Pure parameters forbid getValue/setValue.
- Paths: Use raw strings `r"C:\..."` or forward slashes. Handle OS differences with `platform.system()` when needed (e.g., material library paths).

## Verification Checklist (required before delivery)

Source: `references/KeyShot_lux_API.md` and `references/KeyShot_luxmath_API.md` (2026.3 dumps). Nothing else counts.

Before returning a script, check every `lux` and `luxmath` symbol:
- Symbol exists in the dump (function, method, or constant)
- Called on the correct owner (module vs node, graph, edge, parameter)
- Arguments match the dump (names, types, required vs optional)
- Ellipsis signatures are not treated as complete
- GUI-only calls guarded with `if not lux.isHeadless()` when the task may run headless
- No invented facilities (logging, undo, progress, or any symbol absent from the dump)
- Node IDs re-queried after any graph copy or link
- None and empty-list returns checked before use
- Only `lux` / `luxmath` + stdlib; no external libraries unless the user explicitly asks
- File I/O, threading, and subprocesses only if the task authorizes them
- Headless: no GUI calls; explicit paths; `lux.isHeadless()` checked

If a box cannot be checked, do not ship that call. Name the missing symbol and offer a documented alternative or say it is unsupported.

## Strict Rules for All Generated Scripts

1. **Complete & Working Only**: Every script must be a full, self-contained, copy-paste-and-run program. No comments like "# TODO", no example snippets, no "you can add...", no outlines. The entire concept must work end-to-end when pasted into KeyShot.
2. **User Settings at Top**: All configurable values (paths, names, numbers, booleans) must be in a clearly marked `### USER SETTINGS ###` block at the very top, using simple variables. User changes only this section.
3. **Progress & Debug Prints**: Include `print()` statements at every major step so the user sees exactly what is happening in the Scripting Console.
4. **Exact lux API**: Use only functions and constants that exist in the 2026.3 dump. Examples of correct calls: `lux.getCamera()`, `lux.getMaterialGraph(name)`, `lux.renderImage(...)`, `lux.getInputDialog(...)`.
5. **GUI Dialogs**: When user input is needed in GUI mode, use `lux.getInputDialog()` with properly formed tuples. Provide a unique `id=` for persistence across runs. Guard for headless.
6. **Headless Compatible**: Where possible, design so the script can also run via command line (`keyshot --script ...`). Avoid GUI-only calls unless wrapped in mode detection.
7. **Error Resilience**: Wrap risky operations in try/except with informative prints. Check return values and object existence before using them.
8. **Backup First**: For destructive or heavy operations (material changes, large duplicates, etc.), remind the user. Do not auto-save the scene unless the user explicitly requested a save.

## Key API Entry Points and Patterns (verify against dump)

**Scene Access**
```python
import lux
print(lux.getSceneInfo())
if not lux.hasContents():
    print("ERROR: Scene is empty")
    # handle or exit
root = lux.getSceneTree()
```

**Cameras**
```python
cam = lux.getCamera()
lux.setCameraPosition((x, y, z))
lux.setCameraLookAt((tx, ty, tz))
lux.setCameraFieldOfView(35.0)
lux.newCamera("My Turntable Cam")
lux.setStandardView(lux.VIEW_ISOMETRIC)
```

**Environment & Lighting**
```python
env = lux.getActiveEnvironment()
env.setBrightness(1.2)
env.setLightingEnvironment("/path/to/hdri.hdr")  # or .exr
env.setRotation(45)
env.setGroundShadows(True)
```

**Objects & Transforms (SceneNode)**
```python
root = lux.getSceneTree()
obj = root.find("Part Name", depth=5)  # Returns a collection
if obj and len(obj) == 1:
    node = obj[0]
    node.setMaterial("Gold")
    # Correct luxmath usage (see KeyShot_luxmath_API.md)
    m = luxmath.Matrix().makeIdentity().translate(luxmath.Vector((0, 0, 10)))
    node.applyTransform(m)
    node.hide()
    bbox = node.getBoundingBox(world=True)
elif obj:
    print(f"Ambiguous match: {len(obj)} nodes")
else:
    print("Node not found")
```

**Materials**
- For simple assignment: `node.setMaterial("Material Name")`
- For graph editing (advanced):
```python
graph = lux.getMaterialGraph("My Material")
nodes = graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE)
if nodes:
    node = nodes[0]
    param = node.getParameter("Color")
    if param and not param.isPure():
        param.setValue((1.0, 0.8, 0.2))  # RGB tuple or appropriate type
else:
    print("No diffuse nodes found")
```

**Render Options (common settings)**
```python
opts = lux.getRenderOptions()
opts.setMaxSamplesRendering(128)
lux.setRenderEngine(lux.RENDER_ENGINE_PRODUCT)  # or INTERIOR / *_GPU
opts.setGlobalIllumination(3)                   # quality 0–5 (0 disables)
opts.setOutputAlphaChannel(True)
opts.setThreads(0)  # 0 = auto
opts.setOutputDepthPass(True)
# Many more: setOutput*Pass, setCausticsQuality, setDofQuality, setAddToQueue, etc.
```

**Rendering Calls (signature sketches for reference; not executable Python)**
```python
lux.renderImage(path, width=None, height=None, opts=None, format=None)
lux.renderAnimation(folder, frameFiles="frame.%d.jpg", keepFrames=True, width=None, height=None, fps=12, videoName=None, opts=None, format=None)
lux.renderConfiguration(name, folder, web=False, modelVariations=False, materialVariations=False, studioVariations=False, opts=None)
# name must contain an image extension (jpg/jpeg/png). For images mode it must also contain '%d'.
lux.renderXR(folder, name, type=lux.XR_TYPE_TURNTABLE, center=lux.XR_CENTER_OBJECT, ...)
```

**GUI Custom Input Dialogs — lux.getInputDialog (GUI mode only)**
Professional way to collect multiple inputs. Use for scripts run from console or buttons.

```python
values = [
    ("out_folder", lux.DIALOG_FOLDER, "Output folder:", r"C:\Renders\Project"),
    ("base_name", lux.DIALOG_TEXT, "Base filename:", "render_01"),
    ("samples", lux.DIALOG_INTEGER, "Max samples:", 64, (8, 512)),
    ("use_gpu", lux.DIALOG_CHECK, "Use GPU render engine?", True),
]

dialog_result = lux.getInputDialog(
    title="Render Job Settings",
    desc="Configure and run the automated render.",
    values=values,
    id="project_render_v2"   # Unique ID → KeyShot remembers previous choices
)

if dialog_result is None:
    print("User cancelled the dialog.")
else:
    print("User choices:", dialog_result)
    # Access as dialog_result["out_folder"], dialog_result["samples"], etc.
```

**Critical Notes on Dialogs**:
- Guard with `if not lux.isHeadless()` before any dialog call. In headless, require explicit config and raise if missing.
- Prefer one complete input dialog for related inputs.
- `DIALOG_ITEM` needs choices and returns an index/display pair; cancellation is None.
- A text field does not universally require a nonempty default (check the dump and `references/2026-corrections.md`).
- Use a unique `id` string so KeyShot persists the last used values for that script.
- The returned value is a dict (or None if cancelled).
- Always pass an explicit path to save, export, or render in headless.

**Other Useful Exact Calls**
- `lux.getSceneMaterials()`, `lux.getMaterialGraph(name)`, `lux.getCameras()`, `lux.getEnvironments()`
- `lux.newModelSet(name)`, `lux.setModelSets(names_list)`, `lux.getModelSets()` (returns **active** sets only)
- `lux.setActiveStudio(name)`, `lux.setActiveEnvironment(name)`
- `lux.saveFile(path=None)`, `lux.openFile(path)`, `lux.importFile(path)`
- `lux.processQueue()` after setting `opts.setAddToQueue(True)`
- Full constant list in the 2026.3 dump (`references/KeyShot_lux_API.md`)

## Common Errors & How to Avoid Them

- **Wrong camera function**: Use `lux.getCamera()` (not `getActiveCamera`). Do not assume a rich camera object with `.name` / `.position` / `.fov`.
- **Material access**: Use `lux.getMaterialGraph("Exact Material Name")` or `lux.getSceneMaterials()`. Never `lux.getMaterial()` or `lux.getMaterials()`.
- **Dialog errors**: Guard for headless. Check cancellation. Item tuples for `DIALOG_ITEM` must be complete.
- **Type / argument errors**: Pass correct types (tuples for vectors/positions, proper constants). Verify against the dump.
- **Object not found**: Names are case-sensitive. Use `root.find("Name", depth=10)` and always check `if obj:` before using. `find()` yields a collection — check empty and ambiguous matches.
- **Material graph changes not visible**: Call `graph.executeGeometryNodes()` after edits. Re-query node IDs after copy or link. Save/reload scene if needed.
- **Headless vs GUI**: Dialogs and some UI calls fail in headless. Use the pattern in `references/constraints.md`.
- **Pure parameters**: Do not call `getValue` / `setValue` on pure (connected) parameters.
- **Render looks wrong**: Ensure camera, environment, image style, and RenderOptions are explicitly set in the script (interactive viewport may differ).

Always test in the real KeyShot Scripting Console. The user will report exact errors for refinement.

## Example Scripts

### Example 1: Quick Still Render with Custom Camera & HDRI
```python
import lux
import os

# === USER SETTINGS ===
output_dir = r"C:\Renders\MyProject"
os.makedirs(output_dir, exist_ok=True)
hdri_path = r"C:\HDRI\studio_light.exr"
camera_pos = (150, -200, 120)
look_at = (0, 0, 50)
fov = 28.0
width, height = 1920, 1080
samples = 64

# === SCRIPT ===
print("Setting up scene...")
env = lux.getActiveEnvironment()
env.setLightingEnvironment(hdri_path)
env.setBrightness(1.0)
env.setRotation(30)

cam = lux.getCamera()
lux.setCameraPosition(camera_pos)
lux.setCameraLookAt(look_at)
lux.setCameraFieldOfView(fov)

opts = lux.getRenderOptions()
opts.setMaxSamplesRendering(samples)
lux.setRenderEngine(lux.RENDER_ENGINE_PRODUCT)
opts.setGlobalIllumination(3)
opts.setSharperTextureFiltering(True)

output_path = os.path.join(output_dir, "hero_render.jpg")
print(f"Rendering to {output_path}...")
lux.renderImage(output_path, width, height, opts, lux.RENDER_OUTPUT_JPEG)
print("Done!")
```

### Example 2: Render Existing Scene Animation
```python
import lux
import os

output_dir = r"C:\Renders\Animation"
os.makedirs(output_dir, exist_ok=True)
fps = 30
width, height = 1280, 720

print("Rendering existing scene animation...")
print("Note: this does not create a turntable or any new animation.")
print("It renders whatever animation is already present in the scene.")

opts = lux.getRenderOptions()
opts.setMaxSamplesRendering(32)
lux.setRenderEngine(lux.RENDER_ENGINE_PRODUCT_GPU)
opts.setGlobalIllumination(2)

lux.setCameraLookAt((0, 0, 0))  # Adjust to model center

lux.renderAnimation(
    output_dir,
    "frame_%d.png",
    True,          # keepFrames
    width, height, fps,
    "animation.mp4",
    opts,
    lux.RENDER_OUTPUT_PNG
)
print("Animation render job submitted.")
```

### Example 3: Batch Render Active Model Sets
```python
import lux
import os

output_base = r"C:\Renders\Batch"
# getModelSets() returns only currently active sets.
# To inventory inactive sets, walk root children and use isModelSet().
previous_active = list(lux.getModelSets() or [])
sets = previous_active
print(f"Active model sets: {sets}")
if not sets:
    print("No active model sets. Nothing to render.")
else:
    opts = lux.getRenderOptions()
    opts.setMaxSamplesRendering(48)
    # opts.setAddToQueue(True)  # uncomment only if queue mode is intended
    # All variation flags are False: this does not establish a distinct image per set
    # beyond the active model-set selection itself.

    try:
        for model_set in sets:
            result = lux.setModelSets([model_set])
            if result is False:
                print(f"Warning: setModelSets returned False for {model_set}")
            out_dir = os.path.join(output_base, model_set)
            os.makedirs(out_dir, exist_ok=True)
            print(f"Rendering set: {model_set}")
            lux.renderConfiguration(
                f"variation_%d.jpg", out_dir,
                web=False,
                modelVariations=False,
                materialVariations=False,
                studioVariations=False,
                opts=opts
            )
    finally:
        # Always attempt to restore previous selection, even on error
        if previous_active:
            restore = lux.setModelSets(previous_active)
            print(f"Restored previous selection: {restore}")
    print("Batch finished.")
```

## Best Practices & Edge Cases

See `references/best-practices.md` and `references/2026-corrections.md` for the full set. Key points:

- **Performance**: Cache stable lookups. Do not invent undo sessions or parallel workers. Avoid transforming both a parent and its children.
- **Units**: Check/set with `lux.setSceneUnit(unit, keep=True)`. Note the parameter is `keep`, not `rescale`.
- **Headless / CLI**: KeyShot supports `keyshot.exe --script "C:\path\to\script.py" --scene "scene.ksp"`. Check `lux.isHeadless()`. Always pass explicit paths.
- **Error Handling**: Wrap key calls in try/except. Many lux methods return None on failure. Use `print(lux.getSceneInfo())` and `scene.find(...)` checks liberally.
- **Material Graphs**: Editing node graphs is powerful but fragile — always backup scene first. Use `graph.executeGeometryNodes()` after geometry node changes. Re-query IDs after copy/link. OpenPBR and Planar Light parameters are read from the graph at runtime (`references/OpenPBR_and_Planar_Light.md`).
- **Large Scenes**: Limit depth in `find()` calls. Use model sets or configurations for variations instead of duplicating geometry.
- **Output Formats**: Match extension to `RENDER_OUTPUT_*` constant. EXR/TIFF for 32-bit passes; JPEG for quick previews.
- **Testing**: Develop in the Scripting Console (Window > Scripting Console). Use the Scripts tab to save/load reusable .py files. Add `print()` everywhere during development. Separate static checks from runtime tests.
- **Target build** — Use the KeyShot Studio 2026.3 API references and test on that build in the intended execution mode.
- **External Python**: Do not use external libraries unless the user explicitly asks and confirms availability in the embedded runtime.

## Additional Resources

- **API source of truth**: `references/KeyShot_lux_API.md` and `references/KeyShot_luxmath_API.md` (2026.3 dumps)
- Headless 2026.3 API captures: [`lux`](https://github.com/donaldtuttle/Unofficial_KeyShot_Python/blob/main/lux_headless/KeyShot_headless_lux_API.md) and [`luxmath`](https://github.com/donaldtuttle/Unofficial_KeyShot_Python/blob/main/luxmath_headless/KeyShot_headless_luxmath_API.md).
- Mandatory constraints: `references/constraints.md`
- Best practices: `references/best-practices.md`
- 2026 corrections and pitfalls: `references/2026-corrections.md`
- OpenPBR / Planar Light runtime parameters: `references/OpenPBR_and_Planar_Light.md`
- Glossary: `references/glossary.md`
- KeyShot Studio 2026 manual for the [Scripting Console](https://manuals.keyshot.com/kss2026/en-us/manual/scripting-console.html) and [Headless Scripting](https://manuals.keyshot.com/kss2026/en-us/manual/exposed-headless-scripting-functionality.html).
- Scripting examples in KeyShot UI: Scripts tab > Examples
- For production-ready best practices + complete examples: `references/KeyShot_Best_Practices_Examples.md`
- Quick-reference cheat sheet for advanced material graph patterns: `references/Advanced_Material_Graph_Cheat_Sheet.md`
- Additional curated examples: `references/keyshot-script-examples.md`
- Clean starter template: `assets/keyshot_script_template.py` (always put user settings in the top block)
- Upstream knowledge bases: https://github.com/donaldtuttle/Unofficial_KeyShot_Python and https://github.com/donaldtuttle/KeyShot-Python-AI-Knowledge

## Limitations & When to Decline

This skill focuses on the official `lux` Python API verified against the 2026.3 dump. It does not cover:
- Creating custom KeyShot plugins (C++ / Luxion SDK)
- Third-party render farm integration beyond queue export
- Reverse-engineering undocumented internal calls
- Inventing facilities that are not in the dump

If a request falls outside KeyShot Python scripting (e.g., "write a Blender script"), respond normally or suggest the appropriate tool.

Always produce scripts that are safe, commented, and respect the user's scene state. Ask clarifying questions about KeyShot version, desired output resolution/format, specific objects/materials, or whether the script should be interactive vs. fully automatic. If evidence is incomplete, state the uncertainty and offer a documented alternative or a focused runtime probe.

**Static verification only.** This skill verifies symbols against the 2026.3 dumps. It does not claim that any script has been executed or rendered inside KeyShot unless a live runtime observation was performed.
