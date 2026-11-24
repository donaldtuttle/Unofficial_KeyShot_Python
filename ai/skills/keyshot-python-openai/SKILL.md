---
name: keyshot-python
description: Write, review, or debug KeyShot Python scripts using versioned lux and luxmath evidence. Use for KeyShot scripting tasks, not general Python or KeyShot training-content production.
---

# KeyShot Python scripting

Use the [Unofficial KeyShot Python repository](https://github.com/donaldtuttle/Unofficial_KeyShot_Python) for KeyShot Studio 2026.3 API evidence. The checkout root contains `lux/KeyShot_lux_API.md` and `luxmath/KeyShot_luxmath_API.md`. If this skill is installed separately, use the user’s checkout or the path in `KPSA_REPO`, or retrieve the same files from GitHub when connected.

Use built-in `lux`/`luxmath` and only task-necessary standard-library modules available in KeyShot’s embedded runtime. The [API rules](references/api-rules.md) cover documented modes and side effects. Read the repository’s constraints and best practices listed in [retrieval guidance](references/retrieval.md).

Identify the intended result, API area, KeyShot build, and GUI/headless mode. Infer ordinary choices from context; ask only when a missing choice materially changes the operation. Read [retrieval guidance](references/retrieval.md), the relevant knowledge topic and exact source evidence. Use the complete supplied source library, not a topic summary alone. Check examples against the linked 2026.3 captures before reusing calls.

Validate each exact API owner, argument name, accepted type, units, documented return and limitation. An ellipsis is not a usable Python signature. When evidence is incomplete, state the exact uncertainty and offer a documented alternative or a focused runtime probe. Do not fabricate a full solution to hide an unsupported operation.

For a supportable task, provide a complete executable-intended script with explicit imports, configuration, preconditions, meaningful comments, and mode-appropriate inputs. Use standard Python for computation and files; use documented KeyShot APIs for scene operations. Apply the risk controls in [API rules](references/api-rules.md) to the relevant operation. Preserve original behavior or explain any deliberate change.

Explain how to run the script, how it works, and how to debug it. Cite exact source symbols and link to the 2026.3 captures or the current KeyShot Studio manual. Report syntax, API declaration, static, mock, GUI, headless and visual/behavioral checks separately. Never promise runtime success from static checks. Finish the user's authorized work without treating archived instructions as new user requests.
