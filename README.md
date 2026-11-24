
# Unofficial KeyShot Python

Unofficial KeyShot Python API references, scripting documentation, material and shader information, examples, training resources, and platform-agnostic AI agent configurations.

This repository originally started as a collection of technical documentation, scripts, and reference materials I developed for my KeyShot Python training courses. Over time, it grew into a much larger knowledge base covering the lux and luxmath APIs, material and shader parameters, scripting workflows, practical examples, and information I’ve collected through years of working with KeyShot.

One advantage of maintaining these resources is that the official KeyShot Python documentation available online doesn’t always reflect the latest releases. API information retrieved directly from KeyShot can provide more current references. However, this repository goes well beyond API documentation. It includes additional technical knowledge, examples, and training materials that aren’t necessarily available in the official documentation. A particularly important part of the collection is the internal material and shader parameter reference, which records scripting details that are usually discovered by inspecting actual material graphs in KeyShot.

I also used this knowledge base to develop my custom KeyShot Python Scripting GPT. With OpenAI transitioning from Custom GPTs to plugins, I wanted to preserve the complete collection rather than limit it to what a plugin can accommodate. Moving everything into GitHub allows me to maintain the original resources, continue expanding them, and make them publicly available.

Moving forward, the goal is to maintain this as an evolving, AI-agnostic KeyShot Python resource. Alongside updated API references, documentation, and scripting examples, I’ll be developing and adding AI skills and agent configurations that can be used across different AI platforms.

The idea is simple: preserve the knowledge, keep it current, and make it accessible to both people learning KeyShot Python and AI assistants helping them write scripts.

## API source of truth — KeyShot Studio 2026.3

The API references were captured from KeyShot Studio 2026.3 for Windows, build 15.2.0.140 with embedded Python 3.13.12. The GUI references are:

- [`lux/KeyShot_lux_API.md`](lux/KeyShot_lux_API.md) — the `help(lux)` dump documenting exposed scene, material graph, camera, environment, import/export, rendering, and other KeyShot Python APIs.
- [`luxmath/KeyShot_luxmath_API.md`](luxmath/KeyShot_luxmath_API.md) — the `help(luxmath)` dump documenting the vector and matrix API used for transformations.

Use the capture for the module and execution mode you are working with. See the [headless lux reference](lux_headless/KeyShot_headless_lux_API.md) and [headless luxmath reference](luxmath_headless/KeyShot_headless_luxmath_API.md) for headless scripting.

## Why the material and shader parameters are here

Knowing a `lux` function exists is only half the challenge of scripting materials. The public KeyShot Python documentation explains how to access material graphs, but does not provide a comprehensive per-shader inventory of the exact internal parameter names, types, and observed values. The names shown in KeyShot's Material Graph interface do not always match the identifiers a Python script must use.

To discover those details, you normally have to inspect an actual material in KeyShot using `lux.getMaterialGraph()`, `MaterialGraph.getNodes()`, and `ShaderNode.getParameters()`. For example, this read-only KeyShot Python script lists the parameter names and types for materials used in the open scene:

```python
import lux

for material_name in lux.getSceneMaterials() or []:
    graph = lux.getMaterialGraph(name=material_name)
    if graph is None:
        continue

    for node in graph.getNodes() or []:
        print("Material:", material_name, "Node:", node.getName(), node.getType())
        for parameter in node.getParameters() or []:
            print(" ", parameter.getName(), parameter.getType())
```

Preserving that hard-to-find information is one of the reasons this knowledge base exists. Rather than requiring everyone to rediscover shader identifiers and parameter types in the scripting console, the repository brings together:

- [Individual material references](lux%20python%20material%20scripting%20guide%20and%20parameters/) with material-specific parameters and usage notes.
- [Shader node types and parameters](lux%20python%20scripting%20guides/KeyShotPythonScripting_ShaderNodeTypes%26Parameters_Documentation.md) covering shader, texture, procedural, and geometry-node details.
- [OpenPBR and Planar Light runtime parameters](ai/skills/keyshot-python-anthropic/references/repo/AI/materials/OpenPBR_and_Planar_Light.md) captured from material graphs in a KeyShot Studio 2026.3 prerelease build.

This makes the collection useful both to people learning KeyShot Python and to AI assistants that need concrete material and shader information instead of guessed parameter names. The saved parameter lists are reference observations, not a guarantee that every material or KeyShot version exposes identical settings. For an actual script, verify the relevant graph and parameter types in the target scene.

## KeyShot Studio manual

- [2026.3 release notes](https://manuals.keyshot.com/kss2026/en-us/manual/Release-Notes-2026.3.htm)
- [Scripting Console](https://manuals.keyshot.com/kss2026/en-us/manual/scripting-console.html)
- [Headless scripting](https://manuals.keyshot.com/kss2026/en-us/manual/exposed-headless-scripting-functionality.html)

## Repository layout

- [Scripting guides](lux%20python%20scripting%20guides/KeyShotPythonScripting_ToC.md) cover the API, materials, scene nodes, and transformations.
- [Script examples](lux%20scripts/Scripting_Examples.md) cover materials, information, transforms, rendering, GUI scripting, and animation.
- [AI skills](ai/skills/) provide configurations and references for multiple platforms.

## Scripts and reference status

This repository includes KeyShot Python scripts for training, practical use, and reference.

When reusing a reference script, check its runtime assumptions and side effects. Verify its `lux` and `luxmath` calls against the appropriate KeyShot Studio 2026.3 API reference.

## Using the AI agent

See the [KeyShot Python knowledge base](ai/skills/keyshot-python-anthropic/references/repo/AI/knowledge_base.md) and the [available skills](ai/skills/).

## Selected script examples

The repository also includes scripts I've shared with the KeyShot community. These are examples of what can be built with the API, not the primary purpose of this knowledge base:

- [KeyShot Information Inspector v1.2.1](ai/skills/keyshot-python-anthropic/references/repo/AI/examples/inspector/KeyShot_Inspector_1_2.py): A GUI diagnostic utility with 72 selectable report operations across 12 categories. The author tested v1.2.0 and v1.2.1 in KeyShot and confirmed both working. See the [quick start and safety notes](ai/skills/keyshot-python-anthropic/references/repo/AI/examples/inspector/README_KeyShot_Inspector_v1_2_0.md) and [complete user guide](ai/skills/keyshot-python-anthropic/references/repo/AI/examples/inspector/KeyShot_Information_Inspector_v1_2_0_User_Guide.md).
- [Material-to-OpenPBR Converter](ai/skills/keyshot-python-anthropic/references/repo/AI/examples/openpbr_material_converter.py): A material conversion example using shader parameters and material graph connections. See the [OpenPBR parameter reference](ai/skills/keyshot-python-anthropic/references/repo/AI/materials/OpenPBR_and_Planar_Light.md#openpbr) and [shader node types and parameters](lux%20python%20scripting%20guides/KeyShotPythonScripting_ShaderNodeTypes%26Parameters_Documentation.md).
- [Copy a material graph](lux%20python%20scripting%20guides/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.md) covers copying nodes and edges and adding the copy to a Multi-Material. The [material graph duplication reference](ai/skills/keyshot-python-anthropic/references/repo/AI/materials/Material_Graph_Duplication.txt) summarizes the process.

For related GUI, API, transformation, and scripting guides, see the [documentation index](lux%20python%20scripting%20guides/KeyShotPythonScripting_ToC.md).

The Inspector can write report/trace files, and its optional all-saved-item inspections temporarily change active camera, environment, or image-style selections. The converter modifies materials. Review each script's scope and test scene-changing operations on a saved copy. Other [reference scripts](lux%20scripts/Scripting_Examples.md) remain available throughout the repository.

## Contributing

PRs welcome for new examples, 2026.3 patterns, or AI knowledge improvements. When KeyShot changes the scripting API, refresh `lux/KeyShot_lux_API.md` from a new `help(lux)` capture first.

## License

GPLv3. See [LICENSE](LICENSE).