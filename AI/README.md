# KeyShot Python Agent (Agnostic)

Portable, model-agnostic agent setup for KeyShot Studio 2026.3 beta.

## API source of truth

[`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md) — `help(lux)` captured in the KeyShot 2026.3 beta scripting console. This is what exists in the runtime. Prefer it over the public 2026.1 website, which lags.


## Mandatory Knowledge (include all of this)

- `constraints.md` — hard rules (node IDs, dialogs, matrices, verification, API limits). Read first.
- `system_prompt.md` — drop-in system / developer message.
- `knowledge_base.md` — TOC. This is the TOC.
- `kpsa_knowledge/` — elevated KPSA guides (best practices, GUI, transforms, quick ref, thin API pointer).
- `materials/` — shader node types, parameters, and individual material files.
- `lux/KeyShot_lux_API.md` — 2026.3 beta API source of truth.
- `lux/KeyShot_luxmath_API.md` — 2026.3 beta math source of truth.

Treat every file under these as authoritative context. Do not invent API methods, parameter names, or node types. Verify against the 2026.3 beta dump.

## How to Use

1. Copy `system_prompt.md` into the system prompt.
2. Attach or include `constraints.md` + `knowledge_base.md` + the full contents of `kpsa_knowledge/` + `materials/` + `lux/KeyShot_lux_API.md` as knowledge/context.
3. The agent starts with constraints, uses the TOC, applies verification patterns, and verifies API against the 2026.3 beta dump.

Works with any LLM (Grok, Claude, GPT, local models, custom agents). No vendor lock-in.

## Maintenance

When KeyShot ships scripting changes, refresh `lux/KeyShot_lux_API.md` from a new `help(lux)` capture first, then update the relevant files in `kpsa_knowledge/` and `materials/`.
