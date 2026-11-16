---
name: keyshot-python-chatgpt
description: Use in ChatGPT to write, review, debug and explain KeyShot Studio 2026.3 beta Python scripts from verified lux/luxmath source evidence, optionally using connected repository or KeyShot tools.
---

# KeyShot Python Scripting Assistant: ChatGPT adapter

**Mandatory core:** read [the provider-agnostic skill](../../skill.md) and its linked [constraints](../../constraints.md), [best practices](../../best-practices.md), [knowledge TOC](../../knowledge_base.md) and 2026.3 beta `lux` / `luxmath` dumps before generating KeyShot code. This file **does not override** the core.

## Host-specific behavior

- If the ChatGPT session/plugin **actually exposes a connected GitHub tool**, fetch the minimum relevant files from `donaldtuttle/Unofficial_KeyShot_Python`. Use the original KPSA archive only for needed historical context and when accessible. A `repository` field or linked GitHub URL in a plugin manifest is not itself access to the repo.
- Otherwise, use the documentation **bundled in the installed plugin** or expressly provided by the user. Note if the bundle lacks an individual material file, current example or updated API dump. Never claim you checked GitHub when you did not.
- If the current ChatGPT runtime exposes an **actual local KeyShot MCP connection**, follow the [integration contract](../../integrations/keyshot-mcp.md), start with `keyshot_status`, and use read-only inspection before any authorized write. This is **not** implied by a skill, MCP repository, or private plugin. Web/mobile sessions must not be assumed to have access to the user's local Windows application.
- Do not enable `execute_python` or bypass a missing tool by suggesting unrequested networking or unsupported libraries in KeyShot.
- For every answer, state whether evidence came from live GitHub, bundled documentation, or live KeyShot; separate static verification from any runtime test. Follow the complete-script / explicit-gap response contract in the core.

## Deployment

This is a **source adapter**. To use it in a ChatGPT plugin, package this `SKILL.md` together with the **full agnostic core and referenced docs** at paths that the installed skill can actually read; or configure an explicit supported retrieval tool. Merely adding this file to GitHub does **not** update or install the user's existing private plugin.
