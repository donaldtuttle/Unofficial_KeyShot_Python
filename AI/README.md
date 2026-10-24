# KeyShot Python Agent (Agnostic)

Portable, model-agnostic agent setup derived from the KeyShot Python Scripting Assistant (KSPA/KPSA) knowledge, updated for KeyShot Studio 2026.1.

## Mandatory Knowledge (include all of this)

- `system_prompt.md` — drop-in system / developer message.
- `knowledge_base.md` — high-level structured reference.
- `materials/` — full material shader types, geometry/texture nodes, and every parameter with type.
- `kpsa_knowledge/` — **complete KPSA knowledge backup**:
  - `KeyShot_2026_Lux_API_Reference.txt` — 2026 Lux API reference
  - `KS_MaterialScripts.txt`, `KS_ScriptDoc.txt`, `KS_QuickRef.txt`, `KS_Python_Guide.txt`
  - `KSPA_BestPractices.txt`, `KSPA_PreloadKnowledge.txt`, `KSPA_UserInput.txt`, `KPSA_Quick_Guide.txt`
  - `KS_CameraScripts.txt`, `KS_ColorColorway.txt`, `KS_CustomInputDialog_GUI.txt`, `KS_TransformMatrix.txt`, `KS_TOC.txt`
  - `MANIFEST.md` / `MANIFEST.json` / `README.md` for inventory

Treat every file under `kpsa_knowledge/` and `materials/` as authoritative context. Do not invent API methods, parameter names, or node types.

## How to Use

1. Copy `system_prompt.md` into the system prompt.
2. Attach or include `knowledge_base.md` + the full contents of `materials/` + the full contents of `kpsa_knowledge/` as knowledge/context.
3. The agent is instructed to use these files as the source of truth for scripts, material graphs, parameters, best practices, and 2026 API surface.

Works with any LLM (Grok, Claude, GPT, local models, custom agents). No vendor lock-in.

## Maintenance

When KeyShot ships scripting changes, update the relevant files in `kpsa_knowledge/` and `materials/` first.
