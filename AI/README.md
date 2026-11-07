# KeyShot Python Agent (Agnostic)

Portable, model-agnostic agent setup for KeyShot Studio 2026.3 beta.

## API source of truth

- [`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md): `help(lux)` captured in the KeyShot 2026.3 beta scripting console.
- [`lux/KeyShot_luxmath_API.md`](../lux/KeyShot_luxmath_API.md): `help(luxmath)` captured from the same build.

Use the capture for the relevant module. These are the declaration references for the recorded build; prefer them over the older public 2026.1 website for that build.

## Mandatory Knowledge (include all of this)

Paths below are relative to the repository root:

- `AI/constraints.md` — hard rules (node IDs, dialogs, matrices, verification, API limits). Read first.
- `AI/best-practices.md` — implementation and review practices.
- `AI/skill.md` — provider-neutral workflow and evidence rules.
- `AI/system_prompt.md` — drop-in system / developer message.
- `AI/knowledge_base.md` — TOC. This is the TOC.
- `AI/index.md` — topic index used to narrow retrieval.
- `AI/kpsa_knowledge/` — elevated KPSA guides (best practices, GUI, transforms, quick ref, thin API pointer).
- `AI/materials/` — shader node types, parameters, and individual material files.
- `lux/KeyShot_lux_API.md` — 2026.3 beta API declaration reference.
- `lux/KeyShot_luxmath_API.md` — 2026.3 beta math declaration reference.

Treat the collection as reference context, not as a set of equally authoritative API declarations. The 2026.3 beta `lux` and `luxmath` dumps take precedence over older guides for declarations about that build. Existing reference scripts may predate the current AI delivery contract and may remain useful or functional even when they do not follow every newer AI rule. Preserve author-reported successful KeyShot testing as distinct runtime evidence. For newly generated or revised scripts, follow the constraints and verify every API call against the appropriate capture and specific supplied observations; do not invent API methods, parameter names, or node types.

## How to Use

1. Copy `AI/system_prompt.md` into the host's supported system or instruction field.
2. Attach or make retrievable `AI/constraints.md`, `AI/best-practices.md`, `AI/skill.md`, `AI/knowledge_base.md`, `AI/index.md`, the full `AI/kpsa_knowledge/` and `AI/materials/` collections, and both `lux/KeyShot_lux_API.md` and `lux/KeyShot_luxmath_API.md`. Preserve relative directory structure where the host supports it.
3. The agent starts with constraints, uses the TOC, applies verification patterns, and checks each module against its own capture. Keep author-reported runtime tests separate from checks performed by the assistant.

The instructions are model-agnostic (Grok, Claude, GPT, local models, custom agents). Actual file access, context limits, and instruction placement depend on the host.

## Reusable skill and provider adapters

The **provider-agnostic core** is [`AI/skill.md`](skill.md). It defines the same KeyShot 2026.3 beta verification and safety contract regardless of host. The optional [MCP integration notes](integrations/keyshot-mcp.md) describe live scene access when a compatible local tool is actually connected.

Platform-specific skill entry points live in [`AI/skills/`](skills/): **ChatGPT**, **Grok**, and **Claude**. They add only host-specific setup and tool-discovery behavior; none replaces or weakens `AI/skill.md`. A source repository link or a Markdown instruction does **not** itself install a skill, configure a GitHub connector, or start the KeyShot bridge. When packaging a skill outside this checkout, include the core and its referenced documentation.

## Maintenance

When KeyShot ships scripting changes, refresh the relevant `help(lux)` and `help(luxmath)` captures first, then update the relevant files in `kpsa_knowledge/` and `materials/`. Record the build for each capture and keep source verification distinct from actual runtime results.
