# Knowledge index

**Source:** private KeyShot-Python-AI-Knowledge `knowledge/index.md` (reviewed 2026-10-23)

For every scripting task, first read `AI/constraints.md` and `AI/best-practices.md`. Then retrieve the relevant topic, exact API entries, and applicable findings. **The AI MUST NOT use non-standard or external libraries, unless the user gives explicit instructions to do so.**

## API source of truth

- Scripting Console: [`lux`](../lux/KeyShot_lux_API.md) and [`luxmath`](../lux/KeyShot_luxmath_API.md)
- Headless runtime: [`lux`](../lux_headless/KeyShot_headless_lux_API.md) and [`luxmath`](../luxmath_headless/KeyShot_headless_luxmath_API.md)

## Core agent files (flat)

- [Constraints](constraints.md) — mandatory hard rules
- [Best practices](best-practices.md)
- [Skill](skill_core.md) — agent skill definition
- [Knowledge base (TOC)](knowledge_base.md)
- [Materials](materials/) — per-shader parameter docs + material examples
- [KPSA knowledge](kpsa_knowledge/) — QuickReference, matrix, GUI, material graph guides
- [Examples](examples/) — runnable scripts (OpenPBR converter, Information Inspector)

## KeyShot scripting manual

- GUI: https://manuals.keyshot.com/kss2026/en-us/manual/scripting-console.html
- Headless: https://manuals.keyshot.com/kss2026/en-us/manual/exposed-headless-scripting-functionality.html
- Manual: https://manuals.keyshot.com/kss2026/en-us/manual/scripting.html

## Topics (pointers to existing kpsa_knowledge / materials)

- API ownership and evidence → constraints + best-practices + 2026.3 dump
- Cameras → QuickReference + 2026.3 dump
- Scene nodes → QuickReference + 2026.3 dump
- Materials and duplication → materials/ + [Material_Graph_Duplication.txt](materials/Material_Graph_Duplication.txt)
- Material graphs, parameters and edges → materials/ + ShaderNodeTypes doc + 2026.3 dump
- OpenPBR conversion → [materials/openpbr_material_converter.py](materials/openpbr_material_converter.py)
- Scene inspection / diagnostics → [examples/inspector/](examples/inspector/) (KeyShot Information Inspector v1.2.0)
- Transformations → TransformationMatrix doc
- GUI dialogs → API_GUI_Guide + constraints + 2026.3 dump
- Rendering / Import-export / Headless / Animation → QuickReference + 2026.3 dump

Full source collection and audits remain in the private repo `donaldtuttle/KeyShot-Python-AI-Knowledge`.
