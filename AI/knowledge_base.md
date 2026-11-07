# KeyShot Python Knowledge Base

**This file is the TOC.** Do not create or look for a separate TOC. There is no `KeyShotPythonScripting_ToC.txt`.

**Version:** KeyShot Studio 2026.3 beta  
**API declaration references:** [`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md) and [`lux/KeyShot_luxmath_API.md`](../lux/KeyShot_luxmath_API.md), captured from the 2026.3 beta console. Check each module against its own capture. Prefer these over the public 2026.1 website for this build.  
**Agent:** Agnostic LLM. Always start with `AI/constraints.md`.

## Knowledge overview

The assistant is backed by these documents. Query by topic, then verify against the applicable 2026.3 beta dump.

| Topic | File |
| --- | --- |
| Hard rules | [constraints.md](constraints.md) |
| Best practices | [best-practices.md](best-practices.md) |
| Glossary | [glossary.md](glossary.md) |
| System prompt | [system_prompt.md](system_prompt.md) |
| Topic index | [index.md](index.md) |
| lux declarations | [2026.3 beta help(lux) dump](../lux/KeyShot_lux_API.md) |
| luxmath declarations | [2026.3 beta help(luxmath) dump](../lux/KeyShot_luxmath_API.md) |
| Quick reference | [kpsa_knowledge/KeyShotPython_Scripting_QuickReference_Documentation.txt](kpsa_knowledge/KeyShotPython_Scripting_QuickReference_Documentation.txt) |
| GUI / headless | [kpsa_knowledge/KeyShotPythonScripting_API_GUI_GuideDocumentation.txt](kpsa_knowledge/KeyShotPythonScripting_API_GUI_GuideDocumentation.txt) |
| Material graph copy | [kpsa_knowledge/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt](kpsa_knowledge/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt) |
| Transforms | [kpsa_knowledge/KeyShotPythonScripting_TransformationMatrix_Documentation.txt](kpsa_knowledge/KeyShotPythonScripting_TransformationMatrix_Documentation.txt) |
| Shader types | [materials/KeyShotPythonScripting_ShaderNodeTypes_and_Parameters_Documentation.txt](materials/KeyShotPythonScripting_ShaderNodeTypes_and_Parameters_Documentation.txt) |
| Collected script references | [Scripts/examples/](../Scripts/examples/) |

File naming in `kpsa_knowledge/` follows `KeyShotPythonScripting_<Topic>_<Type>.txt`. Materials are individual `Material_*.txt` files, not a nested zip.

## Table of Contents

### Constraints (mandatory — read first)
- [Hard Rules](constraints.md) — node IDs, dialog tuples, matrices, API limits, verification patterns
- [Best Practices](best-practices.md)
- [Glossary](glossary.md)

### System
- [System Prompt](system_prompt.md)
- [Skill](skill.md) — provider-agnostic core workflow
- [Platform adapters](skills/README.md) — ChatGPT, Grok, Claude
- [Optional KeyShot MCP](integrations/keyshot-mcp.md) — connected live tools, not automatically installed
- [Topic Index](index.md) — detailed pointers after this TOC
- [2026 Mode Comparison](reference/mode-comparison.md) — secondary; 2026.1 website comparison only

### API source of truth

- [2026.3 beta help(luxmath) dump](../lux/KeyShot_luxmath_API.md)
- [2026.3 beta help(lux) dump](../lux/KeyShot_lux_API.md) — primary for what exists in the runtime

### KPSA Knowledge (`AI/kpsa_knowledge/`)
- [Best Practices Guide](kpsa_knowledge/KeyShotPythonScripting_API_BestPractices_Guide.txt)
- [GUI Input Dialog Guide](kpsa_knowledge/KeyShotPythonScripting_API_GUI_GuideDocumentation.txt)
- [Transformation Matrix Guide](kpsa_knowledge/KeyShotPythonScripting_TransformationMatrix_Documentation.txt)
- [Quick Reference](kpsa_knowledge/KeyShotPython_Scripting_QuickReference_Documentation.txt)
- [API Reference (thin)](kpsa_knowledge/KeyShotPythonScripting_API_Documentation.txt) — pointers only; dump is authoritative
- [Material Graph Copy Guide](kpsa_knowledge/KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt)

### Materials (`AI/materials/`)
- [OpenPBR and Planar Light runtime parameters](materials/OpenPBR_and_Planar_Light.md) — 2026.3 beta capture
- [Shader Node Types & Parameters](materials/KeyShotPythonScripting_ShaderNodeTypes_and_Parameters_Documentation.txt)
- Individual `Material_*.txt` parameter and usage files
- [Material Graph Duplication](materials/Material_Graph_Duplication.txt)
- [OpenPBR Converter](materials/openpbr_material_converter.py)

### Examples
- [OpenPBR Converter](examples/openpbr_material_converter.py)
- [Information Inspector](examples/inspector/)
- [Script references](../Scripts/examples/) — examples of mixed provenance; verify API calls and runtime assumptions before reuse
- [Historical archive](../Scripts/archive/HISTORICAL_SCRIPTS.md) — not current API

### Secondary (lags 2026.3 beta)
- Public 2026.1 scripting: https://media.keyshot.com/scripting/doc/2026.1/
- Public 2026.1 headless: https://media.keyshot.com/scripting/headless_doc/2026.1/
- Do not prefer these over the 2026.3 beta dump.

## Agent Workflow

1. Read `constraints.md` and `best-practices.md` first.
2. Use this TOC to locate the topic.
3. Use `index.md` only to narrow further.
4. Pull concrete patterns from the relevant knowledge file or example.
5. **Verification step:** check `lux` symbols against `lux/KeyShot_lux_API.md` and `luxmath` symbols against `lux/KeyShot_luxmath_API.md` (declaration, owner, arguments, and mode).
6. Follow the hard rules for newly generated or revised scripts. Do not invent a missing API. Preserve existing tested code unless a change is requested and justified.

## Declaration and runtime evidence

The captures are the primary references for the recorded build's API declarations. Guides and examples can disagree with them; state the exact discrepancy rather than silently choosing an explanation or inventing an overload.

Runtime observations are a separate kind of evidence. An author's explicit confirmation that a script was tested successfully in KeyShot counts as author-reported runtime testing. Preserve that record and its stated scope. Do not replace it with "untested" merely because the reviewing assistant has not executed KeyShot. Do not infer unreported builds, scene coverage, or individual call outcomes from a successful workflow.

A static declaration mismatch is not, by itself, a reproduced runtime failure. For an existing tested script, report the mismatch separately and leave the code unchanged unless authorized to repair a demonstrated problem. For a new call, establish the required declaration or supplied runtime evidence before presenting it as supported. Model memory is not API evidence.

## Verification checklist

Declaration sources: `lux/KeyShot_lux_API.md` and `lux/KeyShot_luxmath_API.md` for their respective modules. Record author-reported tests, direct runtime observations, static checks, and mocks separately.

Before delivery, check every `lux` and `luxmath` symbol:

- [ ] Symbol exists in its module's capture (function, method, or constant), or a specific supplied runtime observation establishes it
- [ ] Called on the correct owner (module vs node, graph, edge, parameter)
- [ ] Arguments match the available evidence (names, types, required vs optional)
- [ ] Ellipsis signatures are not treated as complete
- [ ] GUI-only calls guarded with `if not lux.isHeadless()` when the task may run headless
- [ ] No invented facilities (logging, undo, progress, or symbols without evidence)
- [ ] Node IDs re-queried after any graph copy or link
- [ ] None and empty-list returns checked before use
- [ ] Only `lux` / `luxmath` + stdlib; no external libraries unless the user explicitly asks
- [ ] File I/O, threading, and subprocesses only if the task authorizes them
- [ ] Headless: no GUI calls; explicit paths; `lux.isHeadless()` checked
- [ ] Existing author-reported runtime results retained without overstating their scope

If evidence for a new call is missing, identify the exact gap and use a documented alternative or request a focused observation when needed. Do not label an unchanged, author-tested script defective solely because a checklist item is unresolved.

Do not substitute the 2026.1 website, the historical archive, or model memory for evidence about the target build.
