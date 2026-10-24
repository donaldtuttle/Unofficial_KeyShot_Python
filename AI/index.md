# Knowledge index

**Source:** private KeyShot-Python-AI-Knowledge `knowledge/index.md` (reviewed 2026-10-23)

For every scripting task, first read `AI/constraints.md` and `AI/best-practices.md`. Then retrieve the relevant topic, exact API entries, and applicable findings. **The AI MUST NOT use non-standard or external libraries.**

## API source of truth

- [2026.2 help(lux) dump](../lux/KeyShot_lux_API.md) — primary for what exists in the 2026.2 runtime. Prefer this over the public 2026.1 website.

## Core agent files (flat)

- [Constraints](constraints.md) — mandatory hard rules
- [Best practices](best-practices.md)
- [Skill](skill.md) — agent skill definition
- [Knowledge base (TOC)](knowledge_base.md)
- [2026 mode comparison](reference/mode-comparison.md) — secondary; 2026.1 website comparison only
- [Materials](materials/) — per-shader parameter docs + material examples
- [KPSA knowledge](kpsa_knowledge/) — QuickReference, matrix, GUI, material graph guides
- [Examples](examples/) — runnable scripts (OpenPBR converter, Information Inspector)

## Secondary (lags 2026.2)

- GUI: https://media.keyshot.com/scripting/doc/2026.1/
- Headless: https://media.keyshot.com/scripting/headless_doc/2026.1/
- Manual: https://manuals.keyshot.com/kss2026/en-us/manual/scripting.html
- Do not prefer these over the 2026.2 dump.

## Topics (pointers to existing kpsa_knowledge / materials)

- API ownership and evidence → constraints + best-practices + 2026.2 dump
- Cameras → QuickReference + 2026.2 dump
- Scene nodes → QuickReference + 2026.2 dump
- Materials and duplication → materials/ + [Material_Graph_Duplication.txt](materials/Material_Graph_Duplication.txt)
- Material graphs, parameters and edges → materials/ + ShaderNodeTypes doc + 2026.2 dump
- OpenPBR conversion → [materials/openpbr_material_converter.py](materials/openpbr_material_converter.py)
- Scene inspection / diagnostics → [examples/inspector/](examples/inspector/) (KeyShot Information Inspector v1.2.0)
- Transformations → TransformationMatrix doc
- GUI dialogs → API_GUI_Guide + constraints + 2026.2 dump
- Rendering / Import-export / Headless / Animation → QuickReference + 2026.2 dump

Full source collection and audits remain in the private repo `donaldtuttle/KeyShot-Python-AI-Knowledge`.
