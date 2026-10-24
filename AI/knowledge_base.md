# KeyShot Python Knowledge Base

**Version:** 2026.1 (Python 3.13)  
**Agent:** Agnostic LLM. Always start with `AI/constraints.md`.

## Table of Contents

### Constraints (mandatory — read first)
- [Hard Rules and Best Practices](constraints.md) — node IDs, dialog tuples, matrices, API limits, verification patterns

### System
- [System Prompt](system_prompt.md)

### KPSA Knowledge (`AI/kpsa_knowledge/`)
- [Best Practices Guide](kpsa_knowledge/KeyShotPythonScripting_API_BestPractices_Guide.txt) — elevated constraints, material verification, GUI, transforms, scene node differences
- [GUI Input Dialog Guide](kpsa_knowledge/KeyShotPythonScripting_API_GUI_GuideDocumentation.txt)
- [Transformation Matrix Guide](kpsa_knowledge/KeyShotPythonScripting_TransformationMatrix_Documentation.txt)
- [Quick Reference](kpsa_knowledge/KeyShotPython_Scripting_QuickReference_Documentation.txt)
- [API Reference (thin)](kpsa_knowledge/KeyShotPythonScripting_API_Documentation.txt) — pointers to official 2026.1 docs

### Materials (`AI/materials/`)
- [Shader Node Types & Parameters](materials/KeyShotPythonScripting_ShaderNodeTypes&Parameters_Documentation.txt)
- [Material Graph Copy Guide](materials/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt)
- Individual `Material *.txt` parameter and usage files (Advanced, Metal, Plastic, etc.)

### Official Live Docs (preferred over any embedded dump)
- Scripting: https://media.keyshot.com/scripting/doc/2026.1/
- Headless: https://media.keyshot.com/scripting/headless_doc/2026.1/

## Agent Workflow

1. Read `constraints.md` first (hard rules).
2. Use this TOC to locate the topic.
3. Pull concrete patterns from the relevant knowledge file.
4. Generate code that satisfies all hard rules (dynamic node IDs + verification, complete dialog tuples, identity matrices, None/list checks, only lux/luxmath + stdlib).
5. Prefer live official docs for full API details. Keep only thin 2026 notes.

## Scripting Examples

Reference the new examples directory only (OpenPBR material conversion, camera metadata .meta/.xml round-trip, etc.). Do not use or list old example names.

---

*TOC anchors and links are provisional. Finalize after all files are confirmed solid. Do not link broken references.*
