# KeyShot Python Knowledge Base

**This file is the TOC.** Do not create or look for a separate TOC. Use this index for the bundled guides.

**Version:** KeyShot Studio 2026.3

**API source:** [KeyShot Studio 2026.3 runtime captures](#api-source-of-truth).

**Agent:** Agnostic LLM. Always start with `AI/constraints.md`.

## Knowledge overview

The assistant is backed by these documents. Query by topic, then verify against the 2026.3 dump.

| Topic | File |
| --- | --- |
| Hard rules | [constraints.md](constraints.md) |
| Best practices | [best-practices.md](best-practices.md) |
| Topic index | [index.md](index.md) |
| API source of truth | [2026.3 help(lux) dump](../lux/KeyShot_lux_API.md) |
| Quick reference | [kpsa_knowledge/KeyShotPython_Scripting_QuickReference_Documentation.txt](kpsa_knowledge/KeyShotPython_Scripting_QuickReference_Documentation.txt) |
| GUI / headless | [kpsa_knowledge/KeyShotPythonScripting_API_GUI_GuideDocumentation.txt](kpsa_knowledge/KeyShotPythonScripting_API_GUI_GuideDocumentation.txt) |
| Material graph copy | [kpsa_knowledge/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt](kpsa_knowledge/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt) |
| Transforms | [kpsa_knowledge/KeyShotPythonScripting_TransformationMatrix_Documentation.txt](kpsa_knowledge/KeyShotPythonScripting_TransformationMatrix_Documentation.txt) |
| Shader types | [materials/KeyShotPythonScripting_ShaderNodeTypes_and_Parameters_Documentation.txt](materials/KeyShotPythonScripting_ShaderNodeTypes_and_Parameters_Documentation.txt) |

File naming in `kpsa_knowledge/` follows `KeyShotPythonScripting_<Topic>_<Type>.txt`. Materials are individual `Material_*.txt` files, not a nested zip.

## Table of Contents

### Constraints (mandatory — read first)
- [Hard Rules](constraints.md) — node IDs, dialog tuples, matrices, API limits, verification patterns
- [Best Practices](best-practices.md)

### System
- [Skill](skill_core.md) — provider-agnostic core workflow
- [Optional KeyShot MCP](integrations/keyshot-mcp.md) — connected live tools, not automatically installed
- [Topic Index](index.md) — detailed pointers after this TOC

### API source of truth

- Scripting Console: [`lux`](../lux/KeyShot_lux_API.md) and [`luxmath`](../lux/KeyShot_luxmath_API.md)
- Headless runtime: [`lux`](../lux_headless/KeyShot_headless_lux_API.md) and [`luxmath`](../luxmath_headless/KeyShot_headless_luxmath_API.md)

### KPSA Knowledge (`AI/kpsa_knowledge/`)
- [Best Practices Guide](kpsa_knowledge/KeyShotPythonScripting_API_BestPractices_Guide.txt)
- [GUI Input Dialog Guide](kpsa_knowledge/KeyShotPythonScripting_API_GUI_GuideDocumentation.txt)
- [Transformation Matrix Guide](kpsa_knowledge/KeyShotPythonScripting_TransformationMatrix_Documentation.txt)
- [Quick Reference](kpsa_knowledge/KeyShotPython_Scripting_QuickReference_Documentation.txt)
- [API Reference (thin)](kpsa_knowledge/KeyShotPythonScripting_API_Documentation.txt) — pointers only; dump is authoritative
- [Material Graph Copy Guide](kpsa_knowledge/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt)

### Materials (`AI/materials/`)
- [OpenPBR and Planar Light runtime parameters](materials/OpenPBR_and_Planar_Light.md) — observed parameter values
- [Shader Node Types & Parameters](materials/KeyShotPythonScripting_ShaderNodeTypes_and_Parameters_Documentation.txt)
- Individual `Material_*.txt` parameter and usage files
- [Material Graph Duplication](materials/Material_Graph_Duplication.txt)
- [OpenPBR Converter](materials/openpbr_material_converter.py)

### Examples
- [OpenPBR Converter](examples/openpbr_material_converter.py)
- [Information Inspector](examples/inspector/)

### KeyShot scripting manual
- GUI: https://manuals.keyshot.com/kss2026/en-us/manual/scripting-console.html
- Headless: https://manuals.keyshot.com/kss2026/en-us/manual/exposed-headless-scripting-functionality.html

## Agent Workflow

1. Read `constraints.md` and `best-practices.md` first.
2. Use this TOC to locate the topic.
3. Use `index.md` only to narrow further.
4. Pull concrete patterns from the relevant knowledge file or example.
5. **Verification step:** check each `lux` or `luxmath` symbol against its module and mode capture (exists, correct owner, matching arguments, GUI guard if needed).
6. Generate code that satisfies all hard rules. If a symbol is absent from the dump, do not use it.

## Dump wins

The repo is the only API source. Guides in it can contradict the 2026.3 dump. Before showing a script, check each `lux` or `luxmath` symbol against its module and mode capture. If a guide and the dump disagree, the dump is correct. Do not show a script that uses a symbol absent from the dump.

## Verification checklist

Use the 2026.3 capture for the module and runtime mode.

Before delivery, check every `lux` and `luxmath` symbol:

- [ ] Symbol exists in the dump (function, method, or constant)
- [ ] Called on the correct owner (module vs node, graph, edge, parameter)
- [ ] Arguments match the dump (names, types, required vs optional)
- [ ] Ellipsis signatures are not treated as complete
- [ ] GUI-only calls guarded with `if not lux.isHeadless()` when the task may run headless
- [ ] No invented facilities (logging, undo, progress, or any symbol absent from the dump)
- [ ] Node IDs re-queried after any graph copy or link
- [ ] None and empty-list returns checked before use
- [ ] Only `lux` / `luxmath` + stdlib; no external libraries unless the user explicitly asks
- [ ] File I/O, threading, and subprocesses only if the task authorizes them
- [ ] Headless: no GUI calls; explicit paths; `lux.isHeadless()` checked

If a box cannot be checked, do not ship that call. Name the missing symbol and offer a documented alternative or say it is unsupported.

Verify calls against the current runtime captures.
