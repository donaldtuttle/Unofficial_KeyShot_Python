# Platform-specific KPSA skill entry points

**One shared contract:** [`../skill.md`](../skill.md) is vendor-neutral. Read it alongside [`../constraints.md`](../constraints.md), [`../best-practices.md`](../best-practices.md), and the [knowledge TOC](../knowledge_base.md).

These are **three small host adapters**, not three competing KeyShot knowledge bases:

| Host | Entry point | Deployment notes |
| --- | --- | --- |
| ChatGPT | [`chatgpt/SKILL.md`](chatgpt/SKILL.md) | Package with the core/docs in a ChatGPT plugin. A connected GitHub tool or local MCP is a separately configured capability. |
| Grok | [`grok/SKILL.md`](grok/SKILL.md) | Copy/package for a compatible Grok skill host (for example `.grok/skills/<skill-name>/SKILL.md`), keeping the full core accessible. |
| Claude | [`claude/SKILL.md`](claude/SKILL.md) | Copy/package for a compatible Claude skill host (for example `.claude/skills/<skill-name>/SKILL.md` in Claude Code), keeping the full core accessible. |

## Installation versus repository storage

These files are **source templates**. Merely committing them under `AI/skills/` does not install or activate them in any chat app. A usable skill package must include the core instructions and source references or grant a genuine tool connection that can read the repository. Do not promise cloud access to a localhost KeyShot bridge.

Recommended behavior everywhere: retrieve minimal relevant documents; validate every `lux`/`luxmath` call against the **2026.3 beta dumps**; use MCP tools only if present and connected; default to no scene mutation; distinguish verified evidence from untested assumptions. [Integration details](../integrations/keyshot-mcp.md).

## Grok independent frozen release

[Grok v1.3.1 release record and importer](grok/RELEASE.md) preserve its separate, statically verified skill without overriding this project's agnostic core or its three platform adapters. The original ZIP must be imported before its release source is present under `platform-releases/`.
