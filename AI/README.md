# KeyShot Python Agent (Agnostic)

Portable, model-agnostic agent setup derived from the earlier KeyShot Python Scripting Assistant (KSPA) knowledge documents, updated for KeyShot Studio 2026.1.

## Contents

- `system_prompt.md` — drop-in system / developer message.
- `knowledge_base.md` — structured reference the model should treat as authoritative context (API surface, 2026 changes, common patterns, examples, constraints).

## How to Use

1. Copy `system_prompt.md` content into the system prompt of your preferred LLM or agent framework.
2. Attach or paste `knowledge_base.md` as context / knowledge / file (or concatenate if the context window is large enough).
3. Optionally include any of the example scripts from `../Scripts/` or the historical API dumps for deeper reference.
4. Ask for scripts, reviews, or explanations. The agent is instructed to prefer official 2026.1 docs when signatures are uncertain and to call out 2026-specific features (`getMetadata`, headless `renderAnimation`).

Works with Grok, Claude, GPT, local models, or custom agent runtimes. No proprietary GPT store dependency.

## Maintenance

When KeyShot ships a new scripting surface, update `knowledge_base.md` first (especially the 2026 / current-version section), then adjust the system prompt only if the overall behavior needs to change.
