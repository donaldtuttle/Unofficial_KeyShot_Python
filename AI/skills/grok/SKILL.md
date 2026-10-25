---
name: keyshot-python-grok
description: Use in Grok to create, debug, verify and explain KeyShot Studio 2026.3 beta Python scripts against the current repository API dumps; use optional connected tools only when actually available.
---

# KeyShot Python Scripting Assistant: Grok adapter

**Mandatory core:** read the [model-agnostic skill](../../skill.md), [constraints](../../constraints.md), [best practices](../../best-practices.md), [knowledge TOC](../../knowledge_base.md) and relevant 2026.3 beta `lux` / `luxmath` dumps. Never replace the core with generic Python examples.

## Host-specific behavior

- In a Grok host that discovers repository skills (such as a project `.grok/skills/` directory), load this entry point **only if** the core docs are reachable in the workspace or through an actually available repository-reading tool.
- If a GitHub or other source-retrieval tool is connected, use it for targeted current files from `donaldtuttle/Unofficial_KeyShot_Python`. Without one, work from checked-out/bundled sources and identify the revision and any missing coverage.
- MCP is **optional**. Only use KeyShot scene tools when the running Grok environment genuinely exposes them and a read-only status check succeeds. Follow the [host-neutral live-tool safeguards](../../integrations/keyshot-mcp.md). Otherwise write and review scripts without claiming to inspect KeyShot.
- Never infer support for a local stdio MCP server, desktop control, or Python execution just from this skill definition. The host must supply each actual capability.
- Keep every `lux` and `luxmath` symbol checked against the saved 2026.3 beta reference; report missing or contradictory evidence, and distinguish static checks from runtime/visual results.

## Deployment

This is an entry-point template, not an installed skill. Install or package it using the Grok host's supported skill location (for example `.grok/skills/keyshot-python/SKILL.md`), **and** keep the core/doc paths accessible, or rewrite references to the packaged locations. A Markdown skill does not create GitHub or MCP permissions.
