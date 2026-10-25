# Unofficial KeyShot Python Knowledge Base

Unofficial KeyShot Python API references, scripting documentation, material and shader information, examples, training resources, and platform-agnostic AI agent configurations.

This repository originally started as a collection of technical documentation, scripts, and reference materials I developed for my KeyShot Python training courses. Over time, it grew into a much larger knowledge base covering the lux and luxmath APIs, material and shader parameters, scripting workflows, practical examples, and information I’ve collected through years of working with KeyShot.

One advantage of maintaining these resources is that the official KeyShot Python documentation available online doesn’t always reflect the latest releases. API information retrieved directly from KeyShot can provide more current references. However, this repository goes well beyond API documentation. It includes additional technical knowledge, examples, and training materials that aren’t necessarily available in the official documentation.

I also used this knowledge base to develop my custom KeyShot Python Scripting GPT. With OpenAI transitioning from Custom GPTs to plugins, I wanted to preserve the complete collection rather than limit it to what a plugin can accommodate. Moving everything into GitHub allows me to maintain the original resources, continue expanding them, and make them publicly available.

Moving forward, the goal is to maintain this as an evolving, AI-agnostic KeyShot Python resource. Alongside updated API references, documentation, and scripting examples, I’ll be developing and adding AI skills and agent configurations that can be used across different AI platforms.

The idea is simple: preserve the knowledge, keep it current, and make it accessible to both people learning KeyShot Python and AI assistants helping them write scripts.

## Source of truth — 2026.3 beta `help(lux)`

**[`lux/KeyShot_lux_API.md`](lux/KeyShot_lux_API.md)**

Captured from `help(lux)` in the KeyShot Studio **2026.3 beta** scripting console. This is the runtime API as KeyShot exposes it — not a website scrape, not a 2023–2024 dump.

- Prefer this over the public 2026.1 docs.
- If a symbol is not in this dump, do not invent it.

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
- [`Scripts/examples/`](Scripts/examples/) — collected reference scripts (materials, information, transforms, rendering, GUI, animation)
- `AI/` — agnostic KeyShot Python agent. Drop the system prompt + knowledge base into any LLM (Grok, Claude, GPT, local, etc.). The agent is instructed to verify against the 2026.3 beta dump.

## Scripts and reference status

This repository preserves KeyShot Python scripts collected for training, practical use, and reference across different KeyShot releases. These scripts are **examples and source material**, not a single uniformly current or AI-contract-compliant script collection. Some older scripts have continued to function in their original workflows even when they do not follow every rule in the newer `AI/constraints.md`.

The AI constraints govern **new scripts written or revised by an AI assistant**. They are not, by themselves, proof that an older example is broken. When reusing a reference script, check its intended KeyShot version, runtime assumptions, side effects, and each `lux`/`luxmath` call against the appropriate current API dump. A working history is valuable evidence but does not replace a fresh runtime test on the target build.

Newer versions will gradually replace outdated examples. Preserve useful historical versions and their provenance rather than rewriting, deleting, or labeling working examples defective solely for differences in style or contract.

## Featured community script: KeyShot Information Inspector v1.2.0

The [KeyShot Information Inspector](AI/examples/inspector/KeyShot_Inspector_1_2.py) is a GUI-only diagnostic tool with 74 selectable report operations across 12 categories. It can inspect scene structure, materials and shader graphs, cameras, environments, image styles, studios, rendering information and more. The author has tested the supplied v1.2.0 release in KeyShot.

- [Inspector Python script](AI/examples/inspector/KeyShot_Inspector_1_2.py) — open the file and choose **Download raw file** to save the `.py`
- [Quick start and safety notes](AI/examples/inspector/README_KeyShot_Inspector_v1_2_0.txt)
- [Complete user guide](AI/examples/inspector/KeyShot_Information_Inspector_v1_2_0_User_Guide.txt)

Run it from KeyShot's **Scripts** interface. Standard inspection does not alter scene contents, but can write requested reports and a crash trace. Optional inventories of **all** saved cameras, environments and image styles temporarily switch the active item and attempt to restore it. Use that option on a saved copy of a scene.

## Using the AI agent

See [`AI/README.md`](AI/README.md). One system prompt + one knowledge base. No vendor lock-in. The agent treats the 2026.3 beta dump as the API source of truth.

## Contributing

PRs welcome for new examples, 2026.3 beta patterns, or AI knowledge improvements. When KeyShot changes the scripting API, refresh `lux/KeyShot_lux_API.md` from a new `help(lux)` capture first.

## License

GPLv3 — see LICENSE.
