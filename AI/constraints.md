# KeyShot Python Scripting Constraints and Hard Rules

**Target:** KeyShot 2026.1 (Python 3.13)  
**Agent scope:** Agnostic — works with any LLM. Use only `lux` / `luxmath` + Python standard library.

These rules are mandatory. Violate them and scripts will fail at runtime or produce incorrect results. Prefer live official docs over embedded dumps:

- Official scripting: https://media.keyshot.com/scripting/doc/2026.1/
- Headless: https://media.keyshot.com/scripting/headless_doc/2026.1/
- Repo reference (once established): point to the single clean location in Unofficial_KeyShot_Python.

## Python / API Environment

- Use **only** the KeyShot `lux` and `luxmath` API plus the Python standard library.
- No external UI libraries (Tkinter, PyQt, etc.) and no assumption of third-party packages.
- Prefer KeyShot-specific functions (`lux.getMaterialGraph()`, `lux.setCamera()`, `lux.getCamera()`, etc.) for scene and material work.
- Scripts run inside KeyShot’s isolated Python environment. Anything that touches `lux` must be valid inside KeyShot. External IDEs may write logic; mock `lux` when developing outside.
- Execution is synchronous / single-threaded. Use KeyShot’s internal queue for batch and render work (`lux.beginUndoSession()` / `lux.endUndoSession()` for batches).

Key 2026 notes (thin redundancy):
- `SceneNode.getMetadata()` available.
- `lux.renderAnimation()` supported in headless.
- Python 3.13.

## Data Handling

- Wrap a single string in a list when the function expects a list.
- Always check for `None` before calling methods on returned objects.
- Always check that API-returned lists are non-empty before indexing.
- Avoid mutable default arguments. Use `None` and initialize inside the function.
- Explicit type conversion when mixing strings, numbers, and lists.
- Safe dictionary access on option dicts. Use documented keys.
- Validate field types and ranges. Provide defaults for empty GUI fields.

## Material Graph and Node IDs (Highest Priority)

- Node IDs are dynamically generated and can change across sessions. **Do not treat them as stable identifiers.**
- Prefer node names. Assign unique names when needed.
- When connecting edges, use both material/node identifiers as required by the API.
- After linking or duplicating a material, **verify the result** (re-query the graph or check via an ID).
- `lux.createMultiMaterial()` creates a copy with unique node IDs. On complex graphs, still perform manual edge and parameter verification.
- Changes to a material graph affect the specific instance unless you explicitly update all instances / sub-materials.
- Use `lux.getMaterialGraph(name)` and the graph methods. Do not invent functions such as `lux.getMaterial()` or `lux.getMaterials()`.

### Shader Node Graphing and Material Graph Operations

- Node type matching is required when duplicating or creating nodes (`node.getType()`).
- Parameter type matching is required (`param.getType()`, `param.getValue()` / `setValue()`).
- Edge reconnection after duplication or copy must be verified. Do not assume edges are preserved.
- Clean unused nodes. Keep material graphs organized.
- Common errors: wrong node type, missing edges, parameter type mismatch, relying on dynamic IDs.

**Concrete pattern (hybrid modular + verification):**

```python
import lux

def duplicate_material(material_name):
    copied_material_name = f"{material_name}_Copy"
    return lux.createMultiMaterial(name=copied_material_name, mat=material_name)

def verify_node_parameters(source_node, target_node):
    for param in source_node.getParameters():
        new_param = target_node.getParameter(param.getName())
        if new_param and new_param.getValue() != param.getValue():
            new_param.setValue(param.getValue())

def verify_and_adjust_edges(source_graph, target_graph):
    node_mapping = {node.getName(): target_graph.getNodeByName(f"{node.getName()}_Copy")
                    for node in source_graph.getNodes()}
    for node in source_graph.getNodes():
        for edge in node.getOutputEdges():
            src = node_mapping.get(edge.getSourceNode().getName())
            tgt = node_mapping.get(edge.getTargetNode().getName())
            if src and tgt and not target_graph.hasEdge(src, tgt, edge.getID()):
                target_graph.newEdge(src, tgt, edge.getID())

def duplicate_and_verify_material(material_name):
    copied = duplicate_material(material_name)
    source_graph = lux.getMaterialGraph(name=material_name)
    copied_graph = lux.getMaterialGraph(name=copied)
    if not source_graph or not copied_graph:
        lux.logError("Graph missing after copy")
        return
    for source_node in source_graph.getNodes():
        target_node = copied_graph.getNodeByName(f"{source_node.getName()}_Copy")
        if target_node:
            verify_node_parameters(source_node, target_node)
    verify_and_adjust_edges(source_graph, copied_graph)
```

Always re-query after copy. Prefer names over IDs.

## GUI Input Dialog Constraints

- GUI dialogs use `lux.getInputDialog()` **only**. Not headless compatible.
- Field definitions are tuples. The tuple structure must be complete and correct for the dialog type.
- Common tuple patterns:
  - Text: `("key", lux.DIALOG_TEXT, "label:", "default")` — **non-empty default required**.
  - Integer: `("key", lux.DIALOG_INTEGER, "label:", default, (min, max))` — range is a tuple.
  - Double: similar with range.
  - Item/selection: `("key", lux.DIALOG_ITEM, "label:", default_index, [options])` — must include the options list.
  - File / Folder: appropriate `DIALOG_FILE` / `DIALOG_FOLDER` form.
- Empty fields, missing parameters, or incomplete tuples cause runtime errors ("Items of item tuple must be specified!"). Always provide defaults and validate the returned `opts` dict.
- Check `if opts:` before using results (user may cancel).

**Correct example:**

```python
values = [
    ("name", lux.DIALOG_TEXT, "Model Name:", "DefaultModelName"),  # non-empty default
    ("count", lux.DIALOG_INTEGER, "Count:", 1, (1, 100)),
    ("mode", lux.DIALOG_ITEM, "Mode:", 0, ["Fast", "Quality"])
]
opts = lux.getInputDialog(title="Settings", values=values)
if opts:
    # safe access
    name = opts.get("name", "DefaultModelName")
else:
    lux.logInfo("Dialog cancelled")
```

## Transforms and Matrices

- Start from identity: `luxmath.Matrix().makeIdentity()`.
- Order of operations matters. Absolute vs relative is meaningful (**absolute only on object nodes**).
- Pattern matrices (spiral, grid, circle, etc.) are built from identity + translate/rotate/scale.
- Bounding boxes differ by model / part / group / model set.
- Groups and models do not support absolute transforms; objects do.

**Example:**

```python
import luxmath
import math

matrix = luxmath.Matrix().makeIdentity().translate(luxmath.Vector(1.0, 0.0, 0.0))
# or for spiral:
angle_rad = index * angle_increment * (math.pi / 180.0)
offset = luxmath.Vector(math.cos(angle_rad), 0, math.sin(angle_rad)) * spacing
spiral = luxmath.Matrix().makeIdentity().translate(offset)
```

## Common API Misperceptions (Explicit Corrections)

- `lux.getSceneInfo()` does **not** return full scene data. Use specific getters (`getSceneMaterials`, `getCameras`, etc.).
- Studios reference current materials; they do not store independent material state.
- Node IDs are **not** stable across sessions.
- Material graph changes affect the specific instance unless updated everywhere.
- There is **no** `lux.getActiveCamera()`. Use `lux.getCamera()`.
- There is **no** `lux.getMaterial()` / `lux.getMaterials()`. Use `getMaterialGraph(name)` and `getSceneMaterials()`.

## Custom Functions

- Do **not** override KeyShot methods. Wrap them.
- Pattern: helper that calls `lux.getMaterialGraph`, finds a node, and calls the Lux method (`setColor`, `setValue`, etc.) rather than replacing the API.

## Scene Nodes vs Material Nodes

- Duplicating a scene tree node creates a new instance with its properties.
- Duplicating a material requires `lux.createMultiMaterial()` for independence and unique node IDs, plus post-copy edge/parameter verification.
- Absolute transforms only on object nodes. Groups/models aggregate children and do not support absolute.

## General Scripting

- Modular functions, consistent naming, docstrings.
- Check return values (import, render, etc.).
- Log or print for debugging (`lux.logError()`, `lux.logInfo()`).
- Check file paths exist before use.
- Structure for modularity. Test in small increments. Use descriptive names.
- Keep material graphs clean (delete unused nodes, logical connections).
- Automate routine tasks (library save, batch parameter updates, render output paths).
- Wrap critical API calls in try/except and check return values.
- Use `lux.beginUndoSession()` / `lux.endUndoSession()` for batches.

## Scripting Examples

New, fully comprehensive scripting examples live in the dedicated examples directory (not the old names). Reference those files only when pointing to concrete scripts:

- Materials: Complete conversion of KeyShot materials to OpenPBR.
- Camera: Gather all camera information, save to portable format (`.meta` / `.xml`), and re-apply later. Same pattern for other scene data.

Do not reference, list, or link any old example script names from previous knowledge files.

---

*These constraints are the single source of hard rules. Mirror them in system prompt, knowledge base, and relevant kpsa_knowledge / materials files. Update TOC only after content is solid.*
