# Knowledge index

**Source:** private KeyShot-Python-AI-Knowledge `knowledge/index.md` (reviewed 2026-10-23)

For every scripting task, first read `AI/constraints.md` and `AI/best-practices.md`. Then retrieve the relevant topic, exact API entries, and applicable findings. **The AI MUST NOT use non-standard or external libraries.**

## Core agent files (flat)

- [Constraints](constraints.md) — mandatory hard rules
- [Best practices](best-practices.md)
- [Skill](skill.md) — agent skill definition
- [2026 mode comparison](reference/mode-comparison.md)
- [Materials](materials/) — per-shader parameter docs
- [KPSA knowledge](kpsa_knowledge/) — QuickReference, matrix, GUI, material graph guides
- [Examples](examples/) — runnable scripts (OpenPBR converter)

## Official live docs (prefer for signatures)

- GUI: https://media.keyshot.com/scripting/doc/2026.1/
- Headless: https://media.keyshot.com/scripting/headless_doc/2026.1/
- Manual: https://manuals.keyshot.com/kss2026/en-us/manual/scripting.html
- Prefer 2026.2 docs when available.

## Topics (pointers to existing kpsa_knowledge / materials)

- API ownership and evidence → constraints + best-practices + official docs
- Cameras → QuickReference + official docs
- Scene nodes → QuickReference
- Materials and duplication → materials/ + MaterialGraph guides
- Material graphs, parameters and edges → materials/ + ShaderNodeTypes doc
- OpenPBR conversion → [examples/openpbr_material_converter.py](examples/openpbr_material_converter.py)
- Transformations → TransformationMatrix doc
- GUI dialogs → API_GUI_Guide + constraints
- Rendering / Import-export / Headless / Animation → QuickReference + official docs

Full source collection and audits remain in the private repo `donaldtuttle/KeyShot-Python-AI-Knowledge`.
