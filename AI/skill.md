# KeyShot Python scripting skill

**Source:** private KeyShot-Python-AI-Knowledge `skills/keyshot-python/SKILL.md`

Use this knowledge base to solve the user's actual KeyShot scripting request.

## Entry point

**Use the 2026.2 dump first.** [`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md) is `help(lux)` from the KeyShot 2026.2 console. It is the API source of truth. If a symbol is not in that dump, do not use it.

Before every scripting task:

1. Verify the API against `lux/KeyShot_lux_API.md` (2026.2 `help(lux)` dump).
2. Read `AI/constraints.md` and `AI/best-practices.md`.
3. Open `AI/knowledge_base.md` — this is the TOC. Do not create or look for a separate TOC file.
4. Use `AI/index.md` only to narrow the topic after the TOC.
5. Pull the relevant guide, material file, or example.

The public 2026.1 website is secondary and lags. Do not prefer it over the dump.

**The AI MUST NOT use non-standard or external libraries.** Use built-in `lux`/`luxmath` and only task-necessary standard-library modules available in KeyShot's embedded runtime. No third-party packages, external GUI frameworks or installation workarounds. Do not add file I/O, file logging, threading or external processes unless the task expressly requires or authorizes the operation.

Identify the intended result, API area, KeyShot build, and GUI/headless mode. Infer ordinary choices from context; ask only when a missing choice materially changes the operation. Read the relevant knowledge topic and exact source evidence. Review historical examples as candidates against current corrections, not authorities.

Validate each exact API owner, argument name, accepted type, units, documented return and limitation. An ellipsis is not a usable Python signature. When evidence is incomplete, state the exact uncertainty and offer a documented alternative or a focused runtime probe. Do not fabricate a full solution to hide an unsupported operation.

For a supportable task, provide a complete executable-intended script with explicit imports, configuration, preconditions, meaningful comments, and mode-appropriate inputs. Use standard Python for computation and files; use documented KeyShot APIs for scene operations. Preserve original behavior or explain any deliberate change.

Explain how to run the script, how it works, and how to debug it. Cite exact source symbols from the 2026.2 dump. Report syntax, API declaration, static, mock, GUI, headless and visual/behavioral checks separately. Never promise runtime success from static checks.
