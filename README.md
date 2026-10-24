# Unofficial KeyShot Python

Unofficial KeyShot Python libraries, documentation, examples, and an agnostic AI agent setup.

**Current target: KeyShot Studio 2026.1** (Python 3.13 64-bit).

Official source of truth:
- GUI scripting: https://media.keyshot.com/scripting/doc/2026.1/
- Headless: https://media.keyshot.com/scripting/headless_doc/2026.1/
- Manual overview: https://manuals.keyshot.com/kss2026/en-us/manual/scripting.html

The large `lux/` and `luxmath/` markdown dumps in this repo are historical (primarily 2023–2024 era). They remain useful for reference but are not regenerated for every release. Prefer the official 2026.1 docs above for current signatures.

## Key 2026 Changes Relevant to Scripting

- Python 3.13.
- `lux.SceneNode.getMetadata()` — returns CAD metadata for the node as a dictionary. Enables scripts that act on engineer annotations (apply materials, move parts, render thumbnails, etc. based on metadata).
- `lux.renderAnimation()` available and preferred in headless. Starts the render engine once and processes the full animation (~3× faster than per-frame).
- Continued improvements to material graphs, multi-materials, CMF metadata, export (USD, 3MF, etc.), and render passes.

## Repository Layout

- `lux/`, `luxmath/`, `lux_headless/`, `luxmath_headless/` — historical API dumps.
- `Scripts/` — example scripts (still valid patterns).
- `AI/` — agnostic KeyShot Python agent (converted from prior KSPA knowledge). Drop the system prompt + knowledge base into any LLM (Grok, Claude, GPT, local, etc.).

## Using the AI Agent

See `AI/README.md`. The agent is intentionally model-agnostic: one system prompt + one knowledge base file. No vendor lock-in.

## Contributing

PRs welcome for new examples, 2026-specific patterns, or improvements to the AI knowledge base. Keep the unofficial nature clear.

## License

MIT — see LICENSE.
