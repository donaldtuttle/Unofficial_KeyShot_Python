# Manifest — Files Ready for Unofficial_KeyShot_Python / AI/

**Generated:** 2026-10-24  
**Last material sync:** 2026-10-24 (full Metal, Generic PBR, General from private source)  
**Canonical source for future updates:** private repo `donaldtuttle/KeyShot-Python-AI-Knowledge`  
  - Sources under `sources/originals/SRC-*/`  
  - See `sources/README.md` for inventory and source IDs  
  - Audits, reviews, knowledge, and reference live there

**Target structure:**
- `AI/constraints.md` (new, dedicated hard rules)
- `AI/system_prompt.md`
- `AI/knowledge_base.md`
- `AI/kpsa_knowledge/` (updated former knowledge)
- `AI/materials/` (material shader/parameter files)

## Changes Summary

### New / Elevated
- **AI/constraints.md**: Extracted and elevated all hard constraints (Python/API limits, data handling, material graph + dynamic node IDs + verification, GUI dialog tuples, transforms, API misperceptions, custom functions, scene vs material nodes). Includes concrete code patterns (hybrid duplicate+verify, dialog examples, matrix identity). Points to live official 2026.1 docs.
- **AI/system_prompt.md**: Points agent to constraints.md first, live docs, TOC workflow, new examples only.
- **AI/knowledge_base.md**: TOC skeleton pointing into the knowledge folders; workflow preserved from UserInput guide style. Provisional anchors.

### KPSA Knowledge (`AI/kpsa_knowledge/`)
- BestPractices_Guide.txt: Header elevated with constraints pointer; key rules called out.
- API_GUI_GuideDocumentation.txt: Header elevated with dialog tuple rules.
- API_Documentation.txt: Bulk embedded API replaced with thin pointer to official docs + 2026 notes + common patterns.
- Other guides (QuickReference, TransformationMatrix, MaterialGraph_Copy) copied and available for further elevation.

### Materials (`AI/materials/`)
- ShaderNodeTypes&Parameters_Documentation.txt: Constraints note added (type matching, unstable IDs).
- MaterialGraph_CopyOfaCopy_Guide.txt: Header elevated with verification rules.
- Individual `Material *.txt` files: Metal, Generic PBR, and General now full verbatim from private source (SRC-612125cb6917, SRC-91f7c1cb3682, SRC-e5ee9a7c0cfe). Others as previously pushed.

### What was avoided
- No old scripting example names retained or linked.
- No invented API functions.
- No large stubs; full content written or copied with elevations.
- TOC not finalized with broken links.

## Next Steps (when ready)
1. Place new comprehensive scripting examples into the examples directory.
2. Finalize TOC anchors in knowledge_base.md and any internal file TOCs.
3. For future bulk updates, pull from private `KeyShot-Python-AI-Knowledge` sources/ and audits/ rather than older zips.
4. Optionally elevate remaining individual Material *.txt files with a one-line constraints pointer if desired.

Files are on disk under `/workspace/artifacts/AI/` and ready for review / zip.
