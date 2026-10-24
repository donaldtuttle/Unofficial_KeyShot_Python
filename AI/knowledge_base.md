# KeyShot Python Knowledge Base

**This file is the TOC.** Do not create or look for a separate TOC.

**Version:** KeyShot Studio 2026.2  
**API source of truth:** [`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md) — `help(lux)` from the 2026.2 console. Prefer this over the public 2026.1 website.  
**Agent:** Agnostic LLM. Always start with `AI/constraints.md`.

## Table of Contents

### Constraints (mandatory — read first)
- [Hard Rules](constraints.md) — node IDs, dialog tuples, matrices, API limits, verification patterns
- [Best Practices](best-practices.md)

### System
- [System Prompt](system_prompt.md)
- [Skill](skill.md)
- [Topic Index](index.md) — detailed pointers after this TOC
- [2026 Mode Comparison](reference/mode-comparison.md) — secondary; 2026.1 website comparison only

### API source of truth
- [2026.2 help(lux) dump](../lux/KeyShot_lux_API.md) — primary for what exists in the runtime

### KPSA Knowledge (`AI/kpsa_knowledge/`)
- [Best Practices Guide](kpsa_knowledge/KeyShotPythonScripting_API_BestPractices_Guide.txt) — elevated constraints, material verification, GUI, transforms, scene node differences
- [GUI Input Dialog Guide](kpsa_knowledge/KeyShotPythonScripting_API_GUI_GuideDocumentation.txt)
- [Transformation Matrix Guide](kpsa_knowledge/KeyShotPythonScripting_TransformationMatrix_Documentation.txt)
- [Quick Reference](kpsa_knowledge/KeyShotPython_Scripting_QuickReference_Documentation.txt)
- [API Reference (thin)](kpsa_knowledge/KeyShotPythonScripting_API_Documentation.txt) — pointers only; dump is authoritative
- [Material Graph Copy Guide](kpsa_knowledge/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt)

### Materials (`AI/materials/`)
- [Shader Node Types & Parameters](materials/KeyShotPythonScripting_ShaderNodeTypes&Parameters_Documentation.txt)
- Individual `Material *.txt` parameter and usage files (Advanced, Metal, Plastic, etc.)
- [Material Graph Duplication](materials/Material_Graph_Duplication.txt)
- [OpenPBR Converter](materials/openpbr_material_converter.py)

### Examples (`AI/examples/`)
- [OpenPBR Converter](examples/openpbr_material_converter.py)
- [Information Inspector](examples/inspector/) — KeyShot Information Inspector v1.2.0

### Secondary (lags 2026.2)
- Public 2026.1 scripting: https://media.keyshot.com/scripting/doc/2026.1/
- Public 2026.1 headless: https://media.keyshot.com/scripting/headless_doc/2026.1/
- Do not prefer these over the 2026.2 dump.

## Agent Workflow

1. Read `constraints.md` and `best-practices.md` first.
2. Use this TOC to locate the topic.
3. Verify the exact API against `lux/KeyShot_lux_API.md`.
4. Use `index.md` only to narrow further.
5. Pull concrete patterns from the relevant knowledge file or example.
6. Generate code that satisfies all hard rules (dynamic node IDs + verification, complete dialog tuples, identity matrices, None/list checks, only lux/luxmath + stdlib).
