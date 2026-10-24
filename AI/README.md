# KeyShot Python Agent (Agnostic)

Portable, model-agnostic agent setup derived from the earlier KeyShot Python Scripting Assistant (KSPA) knowledge documents, updated for KeyShot Studio 2026.1.

## Contents

- `system_prompt.md` — drop-in system / developer message.
- `knowledge_base.md` — structured reference (API surface, 2026 changes, common patterns).
- `materials/` — **mandatory full knowledge**: every material shader type, geometry nodes, texture nodes, and their parameters. These are the original KSPA knowledge files covering all shader slots and parameters. Include this entire folder as context for the agent.

## How to Use

1. Copy `system_prompt.md` into the system prompt.
2. Attach or include `knowledge_base.md` **and the full contents of `materials/`** (or the two main documentation files plus all Material *.txt files) as knowledge/context.
3. The agent is instructed to use the material parameter docs as authoritative for node types, parameter names, and types when building or editing material graphs.

Works with any LLM. No vendor lock-in.

## Maintenance

Material parameter lists live in `materials/`. Update them if KeyShot adds or changes shader nodes.
