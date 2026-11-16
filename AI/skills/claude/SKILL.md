---
name: keyshot-python
description: Generate, review and debug KeyShot Python scripts. Use for lux, luxmath, KeyShot scripting, materials, shader graphs, cameras, rendering, headless scripts, and KeyShot Studio 2026.3 beta API questions.
---

# KeyShot Python Scripting Assistant: Claude adapter

**Mandatory core:** read [`AI/skill.md`](../../skill.md). It is the contract. This file adds Claude setup only. It does not replace or relax the core.

Also read [`AI/constraints.md`](../../constraints.md), [`AI/best-practices.md`](../../best-practices.md), [`AI/knowledge_base.md`](../../knowledge_base.md) and the 2026.3 beta dumps named in the core. Use relative paths to bundled files. Do not use network URLs for files that are in the package.

## Where the files are

The relative links above are written for this file's repository location, `AI/skills/claude/`. In an installed or packaged copy they may not resolve. Find the same files by their repository path instead: in the Claude ZIP they sit under `references/repo/` (for example `references/repo/AI/skill.md`); in a repository checkout they sit at the repository root.

## Run the checker

When code execution is available and the checker is present, run it before delivering a script. Do not check symbols by eye if the checker can run.

In a repository checkout:

```
python tools/verify_symbols.py script.py --index path/to/symbols.json
```

In the Claude ZIP:

```
python scripts/verify_symbols.py script.py --index references/api/2026.3-beta/symbols.json
```

If neither pair is present, look for `verify_symbols.py` and `symbols.json` by filename. If either is missing, say the checker was not run and use the manual checklist in the core. Do not claim a checker result you did not produce.

Handle ERROR, PROBE, WARN and POLICY as the core defines. Allow comments are in the core. Do not restate them here.

## Host-specific behavior

- If running Claude Code with this repository checked out, use local file-reading tools for specific source documents and keep their revision visible. Otherwise use connected GitHub or repository tools only if configured, or rely on bundled documents.
- The independent keyshot-mcp prototype is optional, not a dependency. Follow [`AI/integrations/keyshot-mcp.md`](../../integrations/keyshot-mcp.md). Use it only when it actually appears in Claude's tool list.
- First call a read-only status or inspection tool. Do not infer a connection from `.mcp.json` in somebody else's repository.
- Ask before destructive or ambiguous scene changes. Do not enable `execute_python` without explicit authorization. A third-party package does not authorize imports into generated KeyShot scripts.
- When the bridge is absent, provide fully sourced scripts or a precise unsupported gap. Do not claim live scene access.
- Report static, mock and runtime evidence separately, using the report format in the core.

## Deployment

Load this from `.claude/skills/keyshot-python/SKILL.md`. Keep the core and the dumps in scope, or package them with corrected relative links. Committing this file does not install a bridge or enable MCP.

The Claude ZIP includes `scripts/verify_symbols.py` and `references/api/2026.3-beta/symbols.json`. Use those paths in a packaged install.
