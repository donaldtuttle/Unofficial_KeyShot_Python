---
name: keyshot-python-claude
description: Use in Claude to generate, review and debug KeyShot Studio 2026.3 beta Python scripts with strict lux/luxmath verification, optional repository retrieval and explicitly connected local KeyShot MCP tools.
---

# KeyShot Python Scripting Assistant: Claude adapter

**Mandatory core:** read [`AI/skill.md`](../../skill.md). It is the contract. This file adds Claude setup only. It does not replace or relax the core.

Also read [`AI/constraints.md`](../../constraints.md), [`AI/best-practices.md`](../../best-practices.md), [`AI/knowledge_base.md`](../../knowledge_base.md) and the 2026.3 beta dumps named in the core.

## Host-specific behavior

- If running Claude Code with this repository checked out, use local file-reading tools for specific source documents and keep their revision visible. Otherwise use connected GitHub/repository tools only if configured, or rely on explicitly bundled user documents.
- Checker, when this repository is checked out: `python tools/verify_symbols.py script.py --index path/to/symbols.json`. Build the index with `tools/build_symbol_index.py` if it is not already present.
- The independent [lfoletti/keyshot-mcp](https://github.com/lfoletti/keyshot-mcp) prototype documents a Claude Code local stdio MCP client and a Windows KeyShot bridge. It is optional, not a dependency of this skill. It has reported tests on KeyShot 2026.2 Pro; do not presume 2026.3 beta compatibility.
- Only when the local MCP server and bridge actually appear in Claude's tool list, first call a read-only status/inspection tool and follow [`AI/integrations/keyshot-mcp.md`](../../integrations/keyshot-mcp.md). Do not infer a connection from `.mcp.json` in somebody else's repository.
- Ask before destructive or ambiguous scene changes. Do not enable the upstream `execute_python` feature without explicit authorization. A third-party package for an external MCP server does not authorize imports into generated KeyShot scripts.
- When the bridge is absent, provide fully sourced scripts or a precise unsupported gap, not a claim of live scene access. Record which checks were static, mock or actual GUI/headless/render/visual observations.

## Deployment

This is a source adapter. A compatible Claude Code host can load a project skill from a location such as `.claude/skills/keyshot-python/SKILL.md`. Keep this repository and the linked core files in scope, or package them together with corrected relative links. Committing this file does not install the bridge or enable MCP.
