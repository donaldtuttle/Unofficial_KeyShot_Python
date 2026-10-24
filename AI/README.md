# KeyShot Python Agent (Agnostic)

Portable, model-agnostic agent setup for KeyShot Studio 2026.x (prefer 2026.2 when available; Python 3.13).

## Mandatory Knowledge (include all of this)

- `constraints.md` — hard rules (node IDs, dialogs, matrices, verification, API limits). Read first.
- `system_prompt.md` — drop-in system / developer message.
- `knowledge_base.md` — TOC-driven structured reference.
- `kpsa_knowledge/` — elevated KPSA guides (best practices, GUI, transforms, quick ref, thin API pointer).
- `materials/` — shader node types, parameters, and individual material files.

Treat every file under these as authoritative context. Do not invent API methods, parameter names, or node types. Prefer live official 2026 docs for full signatures.

## How to Use

1. Copy `system_prompt.md` into the system prompt.
2. Attach or include `constraints.md` + `knowledge_base.md` + the full contents of `kpsa_knowledge/` + `materials/` as knowledge/context.
3. The agent is instructed to start with constraints, use the TOC, apply verification patterns, and prefer official docs.

Works with any LLM (Grok, Claude, GPT, local models, custom agents). No vendor lock-in.

## Maintenance

When KeyShot ships scripting changes, update the relevant files in `kpsa_knowledge/` and `materials/` first, then elevate constraints if needed.
