# KeyShot Python scripting skill

**Source:** private KeyShot-Python-AI-Knowledge `skills/keyshot-python/SKILL.md`

Use this knowledge base to solve the user's actual KeyShot scripting request.

## Entry point

Before every scripting task:

1. Read `AI/constraints.md` and `AI/best-practices.md`.
2. Open `AI/knowledge_base.md` — this is the TOC. Do not create or look for a separate TOC file.
3. Use `AI/index.md` only to narrow the topic after the TOC.
4. Pull the relevant guide, material file, or example.

**The AI MUST NOT use non-standard or external libraries.** Use built-in `lux`/`luxmath` and only task-necessary standard-library modules available in KeyShot's embedded runtime. No third-party packages, external GUI frameworks or installation workarounds. Do not add file I/O, file logging, threading or external processes unless the task expressly requires or authorizes the operation.

Identify the intended result, API area, KeyShot build, and GUI/headless mode. Infer ordinary choices from context; ask only when a missing choice materially changes the operation. Read the relevant knowledge topic and exact source evidence. Review historical examples as candidates against current corrections, not authorities.

Validate each exact API owner, argument name, accepted type, units, documented return and limitation. An ellipsis is not a usable Python signature. When evidence is incomplete, state the exact uncertainty and offer a documented alternative or a focused runtime probe. Do not fabricate a full solution to hide an unsupported operation.

For a supportable task, provide a complete executable-intended script with explicit imports, configuration, preconditions, meaningful comments, and mode-appropriate inputs. Use standard Python for computation and files; use documented KeyShot APIs for scene operations. Preserve original behavior or explain any deliberate change.

Explain how to run the script, how it works, and how to debug it. Cite exact source symbols or versioned official links. Report syntax, API declaration, static, mock, GUI, headless and visual/behavioral checks separately. Never promise runtime success from static checks.

Official docs (prefer 2026.2 when available):
- https://media.keyshot.com/scripting/doc/2026.1/
- https://media.keyshot.com/scripting/headless_doc/2026.1/
