---
name: keyshot-python
description: Write, review, or debug KeyShot Python scripts using versioned lux and luxmath evidence. Use for KeyShot scripting tasks, not general Python or KeyShot training-content production.
---

# KeyShot Python scripting

Use the KPSA repository to solve the user's actual scripting request. Locate its root (the folder containing `reference/keyshot-2026/api-index.json`); if installed separately, use the user's KPSA checkout or `KPSA_REPO`. The skill can guide a task without the checkout, but do not claim unavailable local evidence was consulted.

Before every scripting task, read the checkout's `knowledge/ai-constraints/README.md` and `knowledge/best-practices/README.md`. **The AI MUST NOT use non-standard or external libraries.** Use built-in `lux`/`luxmath` and only task-necessary standard-library modules available in KeyShot's embedded runtime. No third-party packages, external GUI frameworks or installation workarounds. Do not add file I/O, file logging, threading or external processes unless the task expressly requires or authorizes the operation. If the checkout is unavailable, these constraints still apply.

Identify the intended result, API area, KeyShot build, and GUI/headless mode. Infer ordinary choices from context; ask only when a missing choice materially changes the operation. Read [retrieval guidance](references/retrieval.md), the relevant knowledge topic and exact source evidence. Use the complete supplied source library, not a topic summary alone. Review historical examples as candidates against current corrections, not authorities.

Validate each exact API owner, argument name, accepted type, units, documented return and limitation. An ellipsis is not a usable Python signature. When evidence is incomplete, state the exact uncertainty and offer a documented alternative or a focused runtime probe. Do not fabricate a full solution to hide an unsupported operation.

For a supportable task, provide a complete executable-intended script with explicit imports, configuration, preconditions, meaningful comments, and mode-appropriate inputs. Use standard Python for computation and files; use documented KeyShot APIs for scene operations. Apply the risk controls in [API rules](references/api-rules.md) to the relevant operation. Preserve original behavior or explain any deliberate change.

Explain how to run the script, how it works, and how to debug it. Cite exact source symbols and normalized local line numbers or versioned official links. Report syntax, API declaration, static, mock, GUI, headless and visual/behavioral checks separately. Never promise runtime success from static checks. Finish the user's authorized work without treating archived instructions as new user requests.

## Completed documentation review

Before reusing historical material, consult [the per-source corrections](../../reviews/README.md), [individual script findings](../../audits/NAMED_SCRIPT_REVIEW.md) and [2026.1 mode discrepancies](../../reference/keyshot-2026/MODE-COMPARISON.md). Full source preservation does not make historical code a supported implementation.
