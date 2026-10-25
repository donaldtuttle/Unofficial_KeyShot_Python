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

## Dump wins

The repo is the only API source. Guides in it can contradict the 2026.2 dump. Before showing a script, check every `lux` and `luxmath` symbol against `lux/KeyShot_lux_API.md`. If a guide and the dump disagree, the dump is correct. Do not show a script that uses a symbol absent from the dump.

## Verification checklist (required before delivery)

Source: `lux/KeyShot_lux_API.md` (2026.2 `help(lux)` dump). Nothing else counts.

Before returning a script, check every `lux` and `luxmath` symbol:

- [ ] Symbol exists in the dump (function, method, or constant)
- [ ] Called on the correct owner (module vs node, graph, edge, parameter)
- [ ] Arguments match the dump (names, types, required vs optional)
- [ ] Ellipsis signatures are not treated as complete
- [ ] GUI-only calls guarded with `if not lux.isHeadless()` when the task may run headless
- [ ] No invented facilities (logging, undo, progress, or any symbol absent from the dump)
- [ ] Node IDs re-queried after any graph copy or link
- [ ] None and empty-list returns checked before use
- [ ] Only `lux` / `luxmath` + stdlib; no external libraries unless the user explicitly asks
- [ ] File I/O, threading, and subprocesses only if the task authorizes them
- [ ] Headless: no GUI calls; explicit paths; `lux.isHeadless()` checked

If a box cannot be checked, do not ship that call. Name the missing symbol and offer a documented alternative or say it is unsupported.

Do not verify against the 2026.1 website, the historical archive, or model memory.

## Headless error handling

Check `lux.isHeadless()` before any dialog. In headless, require explicit config and raise if it is missing. In GUI, check cancellation. Never omit a path on save, export, or render in headless — that throws. Do not use third-party GUI toolkits.

**The AI MUST NOT use non-standard or external libraries, unless the user gives explicit instructions to do so.** Use built-in `lux`/`luxmath` and only task-necessary standard-library modules available in KeyShot's embedded runtime. No third-party packages, external GUI frameworks or installation workarounds. Do not add file I/O, file logging, threading or external processes unless the task expressly requires or authorizes the operation. External libraries usually fail in KeyShot; warn if the user asks for one.

Identify the intended result, API area, KeyShot build, and GUI/headless mode. Infer ordinary choices from context; ask only when a missing choice materially changes the operation. Read the relevant knowledge topic and exact source evidence. Review historical examples as candidates against current corrections, not authorities.

Validate each exact API owner, argument name, accepted type, units, documented return and limitation. An ellipsis is not a usable Python signature. When evidence is incomplete, state the exact uncertainty and offer a documented alternative or a focused runtime probe. Do not fabricate a full solution to hide an unsupported operation.

For a supportable task, provide a complete executable-intended script with explicit imports, configuration, preconditions, meaningful comments, and mode-appropriate inputs. Use standard Python for computation and files; use documented KeyShot APIs for scene operations. Preserve original behavior or explain any deliberate change.

Explain how to run the script, how it works, and how to debug it. Cite exact source symbols from the 2026.2 dump. Report syntax, API declaration, static, mock, GUI, headless and visual/behavioral checks separately. Never promise runtime success from static checks.
