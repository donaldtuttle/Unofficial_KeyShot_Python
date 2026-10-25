# Unofficial KeyShot Python

Unofficial KeyShot Python libraries, documentation, examples, and an agnostic AI agent setup.

The point of this repo is that the **public website lags**. What you get from KeyShot itself is more current.

## Source of truth — 2026.3 beta `help(lux)`

**[`lux/KeyShot_lux_API.md`](lux/KeyShot_lux_API.md)**

Captured from `help(lux)` in the KeyShot Studio **2026.3 beta** scripting console. This is the runtime API as KeyShot exposes it — not a website scrape, not a 2023–2024 dump.

- Prefer this over the public 2026.1 docs.
- If a symbol is not in this dump, do not invent it.
- OpenPBR and Planar Light parameters are not library constants. Reach them by inspecting the material graph (get nodes → get parameters).

That is the whole idea of an *unofficial* KeyShot Python repo: current API from KeyShot, not from a lagging website.

## Secondary (lags 2026.3 beta)

Public website docs are useful background only. They are not current for 2026.3 beta:

- GUI scripting: https://media.keyshot.com/scripting/doc/2026.1/
- Headless: https://media.keyshot.com/scripting/headless_doc/2026.1/
- Manual overview: https://manuals.keyshot.com/kss2026/en-us/manual/scripting.html

## Repository layout

- [`lux/KeyShot_lux_API.md`](lux/KeyShot_lux_API.md) — **2026.3 beta source of truth**
- [`lux/KeyShot_luxmath_API.md`](lux/KeyShot_luxmath_API.md) — 2026.3 beta math dump
- `luxmath/`, `lux_headless/`, `luxmath_headless/` — older dumps (historical; do not prefer over the 2026.3 beta lux dump)
- `Scripts/` — older example notes
- [`Scripts/examples/`](Scripts/examples/) — maintained example scripts (materials, information, transforms, rendering, GUI, animation)
- `AI/` — agnostic KeyShot Python agent. Drop the system prompt + knowledge base into any LLM (Grok, Claude, GPT, local, etc.). The agent is instructed to verify against the 2026.3 beta dump.

## Using the AI agent

See [`AI/README.md`](AI/README.md). One system prompt + one knowledge base. No vendor lock-in. The agent treats the 2026.3 beta dump as the API source of truth.

## Contributing

PRs welcome for new examples, 2026.2 patterns, or AI knowledge improvements. When KeyShot changes the scripting API, refresh `lux/KeyShot_lux_API.md` from a new `help(lux)` capture first.

## License

MIT — see LICENSE.
