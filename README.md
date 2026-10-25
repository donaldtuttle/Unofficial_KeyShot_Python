# Unofficial KeyShot Python Knowledge Base

Unofficial KeyShot Python API references, scripting documentation, material and shader information, examples, training resources, and platform-agnostic AI agent configurations.

This repository originally started as a collection of technical documentation, scripts, and reference materials I developed for my KeyShot Python training courses. Over time, it grew into a much larger knowledge base covering the lux and luxmath APIs, material and shader parameters, scripting workflows, practical examples, and information I’ve collected through years of working with KeyShot.

One advantage of maintaining these resources is that the official KeyShot Python documentation available online doesn’t always reflect the latest releases. API information retrieved directly from KeyShot can provide more current references. However, this repository goes well beyond API documentation. It includes additional technical knowledge, examples, and training materials that aren’t necessarily available in the official documentation. A particularly important part of the collection is the **internal material and shader parameter reference**, which records scripting details that are usually discovered by inspecting actual material graphs in KeyShot.

I also used this knowledge base to develop my custom KeyShot Python Scripting GPT. With OpenAI transitioning from Custom GPTs to plugins, I wanted to preserve the complete collection rather than limit it to what a plugin can accommodate. Moving everything into GitHub allows me to maintain the original resources, continue expanding them, and make them publicly available.

Moving forward, the goal is to maintain this as an evolving, AI-agnostic KeyShot Python resource. Alongside updated API references, documentation, and scripting examples, I’ll be developing and adding AI skills and agent configurations that can be used across different AI platforms.

The idea is simple: preserve the knowledge, keep it current, and make it accessible to both people learning KeyShot Python and AI assistants helping them write scripts.

## API source of truth — KeyShot Studio 2026.3 beta

The primary references were captured directly from KeyShot's embedded Python scripting console, rather than copied from the public website:

- **[`lux/KeyShot_lux_API.md`](lux/KeyShot_lux_API.md)** — the `help(lux)` dump documenting exposed scene, material graph, camera, environment, import/export, rendering, and other KeyShot Python APIs.
- **[`lux/KeyShot_luxmath_API.md`](lux/KeyShot_luxmath_API.md)** — the `help(luxmath)` dump documenting the vector and matrix API used for transformations.

These captures are the **API source of truth for the recorded 2026.3 beta build**. Prefer them over the older public 2026.1 scripting pages and historical examples. An AI assistant must not invent a missing function, method, constant, or argument. When working with a different KeyShot build, check what that build actually exposes.

## Why the material and shader parameters are here

Knowing a `lux` function exists is only half the challenge of scripting materials. The public KeyShot Python documentation explains how to access material graphs, but does not provide a comprehensive per-shader inventory of the **exact internal parameter names, types, and observed values**. The names shown in KeyShot's Material Graph interface do not always match the identifiers a Python script must use.

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
            print("  ", parameter.getName(), parameter.getType())
```

**Preserving that hard-to-find information is one of the reasons this knowledge base exists.** Rather than requiring everyone to rediscover shader identifiers and parameter types in the scripting console, the repository brings together:

- **[Individual material references](AI/materials/)** with material-specific parameters and usage notes.
- **[Shader node types and parameters](AI/materials/KeyShotPythonScripting_ShaderNodeTypes&Parameters_Documentation.txt)** covering shader, texture, procedural, and geometry-node details.
- **[OpenPBR and Planar Light runtime parameters](AI/materials/OpenPBR_and_Planar_Light.md)** captured from material graphs in KeyShot 2026.3 beta.

This makes the collection useful both to people learning KeyShot Python and to **AI assistants that need concrete material and shader information instead of guessed parameter names**. The saved parameter lists are reference observations, not a guarantee that every material or KeyShot version exposes identical settings. For an actual script, verify the relevant graph and parameter types in the target scene.

## Secondary (lags 2026.3 beta)

Public website docs are useful background only. They are not current for 2026.3 beta:

- GUI scripting: https://media.keyshot.com/scripting/doc/2026.1/
- Headless: https://media.keyshot.com/scripting/headless_doc/2026.1/
- Manual overview: https://manuals.keyshot.com/kss2026/en-us/manual/scripting.html

## Repository layout

- [`lux/KeyShot_lux_API.md`](lux/KeyShot_lux_API.md) — **2026.3 beta source of truth**
- [`lux/KeyShot_luxmath_API.md`](lux/KeyShot_luxmath_API.md) — 2026.3 beta math dump
- `luxmath/`, `lux_headless/`, `luxmath_headless/` — older dumps (historical; do not prefer over the 2026.3 beta lux dump)
- `Scripts/` — older example notes
- [`Scripts/examples/`](Scripts/examples/) — collected reference scripts (materials, information, transforms, rendering, GUI, animation)
- `AI/` — agnostic KeyShot Python agent. Drop the system prompt + knowledge base into any LLM (Grok, Claude, GPT, local, etc.). The agent is instructed to verify against the 2026.3 beta dump.

## Scripts and reference status

This repository preserves KeyShot Python scripts collected for training, practical use, and reference across different KeyShot releases. These scripts are **examples and source material**, not a single uniformly current or AI-contract-compliant script collection. Some older scripts have continued to function in their original workflows even when they do not follow every rule in the newer `AI/constraints.md`.

The AI constraints govern **new scripts written or revised by an AI assistant**. They are not, by themselves, proof that an older example is broken. When reusing a reference script, check its intended KeyShot version, runtime assumptions, side effects, and each `lux`/`luxmath` call against the appropriate current API dump. A working history is valuable evidence but does not replace a fresh runtime test on the target build.

Newer versions will gradually replace outdated examples. Preserve useful historical versions and their provenance rather than rewriting, deleting, or labeling working examples defective solely for differences in style or contract.

## Using the AI agent

See [`AI/README.md`](AI/README.md). One system prompt + one knowledge base. No vendor lock-in. The agent treats the 2026.3 beta dump as the API source of truth.

## Selected script examples

The repository also includes scripts I've shared with the KeyShot community. These are examples of what can be built with the API, not the primary purpose of this knowledge base:

- **[KeyShot Information Inspector v1.2.0](AI/examples/inspector/KeyShot_Inspector_1_2.py):** A GUI diagnostic utility with 74 selectable report operations across 12 categories, tested in KeyShot by the author. See the [quick start and safety notes](AI/examples/inspector/README_KeyShot_Inspector_v1_2_0.txt) and [complete user guide](AI/examples/inspector/KeyShot_Information_Inspector_v1_2_0_User_Guide.txt).
- **[Material-to-OpenPBR Converter](AI/examples/openpbr_material_converter.py):** A material conversion example using shader parameters and material graph connections.

The Inspector can write report/trace files, and its optional all-saved-item inspections temporarily change active camera, environment, or image-style selections. The converter modifies materials. Review each script's scope and test scene-changing operations on a saved copy. Other [reference scripts](Scripts/examples/) remain available throughout the repository.

## Contributing

PRs welcome for new examples, 2026.3 beta patterns, or AI knowledge improvements. When KeyShot changes the scripting API, refresh `lux/KeyShot_lux_API.md` from a new `help(lux)` capture first.

## License

GPLv3 — see LICENSE.
