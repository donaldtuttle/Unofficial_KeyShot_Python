# Packaged KPSA skills

The canonical, host-neutral AI instructions live in [AI/skill.md](../AI/skill.md). Three host entry points are in [AI/skills](../AI/skills).

Build three ZIPs from the current repository snapshot:

~~~bash
python tools/package_kpsa_skills.py
~~~

Generated output is placed in `dist/`. The package version is currently `1.1.1`; the source commit in `SOURCE_MANIFEST.json` identifies the particular repository snapshot. Rebuilding under the same version can produce different contents when the source changes.

## Contents by platform

The builder does not put the same source inventory in every ZIP:

| Package | Bundled repository references | Additional contents |
| --- | --- | --- |
| **KPSA_ChatGPT_Plugin_1.1.1.zip** | `AI/`, `Scripts/`, `lux/`, `luxmath/`, `lux_headless/`, `luxmath_headless/`, and the root README, LICENSE, and 2026 update note | `plugin.json`, `skills/keyshot-python-scripting/SKILL.md`, package README, source manifest |
| **KPSA_Grok_Skill_1.1.1.zip** | The same repository-reference inventory as the ChatGPT package | `keyshot-python-grok/SKILL.md`, package README, source manifest |
| **KPSA_Claude_Skill_1.1.1.zip** | A lean selection of core instructions, guides, materials, examples, MCP notes, and the two current `lux/` captures | One `keyshot-python/SKILL.md`, `scripts/verify_symbols.py`, `references/api/2026.3-beta/symbols.json`, package README, source manifest |

Repository-reference paths are preserved under each skill's `references/repo/` directory, except for the Claude core rename described below. The main `docs/` directory is not a source directory selected by this builder; the shared scripting guides are bundled from `AI/kpsa_knowledge/`.

The Claude selection excludes the older `luxmath/`, `lux_headless/`, and `luxmath_headless/` dumps, the other host adapters, and the root repository README, LICENSE, and update note. Its generated package README states GPLv3, but the current lean selection does not copy the full LICENSE file. The repository's license text is available in [LICENSE](../LICENSE).

## Entry points and reference paths

- **ChatGPT:** `plugin.json` and `skills/keyshot-python-scripting/SKILL.md`. Creation of the ZIP does not change any installed private plugin.
- **Grok:** extract the `keyshot-python-grok/` folder under the skill directory supported by the host, such as `.grok/skills/` or `~/.grok/skills/`.
- **Claude:** `keyshot-python/` is the root skill folder. The builder keeps exactly one `SKILL.md`, excludes the other host adapters, renames the bundled shared core to `AI/skill_core.md`, and rewrites references to that core.

Relative to the top-level installed `SKILL.md`, the shared core is at `references/repo/AI/skill.md` for ChatGPT and Grok, or `references/repo/AI/skill_core.md` for Claude. Constraints, best practices, the knowledge TOC, and the topic index are under `references/repo/AI/`. Both current API captures are under `references/repo/lux/`.

The current builder copies the source adapters to the package entry points. Links such as `../../skill.md` are written for the adapters' repository locations, not the installed package roots. Use the package-root paths above when those checkout-relative links do not resolve. A readable ZIP and valid frontmatter do not by themselves verify every installed reference link.

The Claude ZIP includes the checker and generated index at these package-root-relative paths:

~~~text
scripts/verify_symbols.py
references/api/2026.3-beta/symbols.json
~~~

The ChatGPT and Grok snapshots do not include the repository's `tools/` directory. Use connected checkout tooling when available, or the manual verification checklist in the core; do not claim the checker was run merely because its source path is mentioned in a bundled guide.

## Build checks and provenance

`SOURCE_MANIFEST.json` records source commit and SHA-256 values. For Claude, it records the selected reference contents after the core-name rewriting, plus bundled checker/index hashes. `dist/SHA256SUMS.txt` records checksums of the generated ZIPs.

The builder checks ZIP integrity, entry-point frontmatter, the ChatGPT manifest name, and Claude-specific file-count, path, historical-dump-exclusion, checker-presence, and index-presence conditions. It records reference hashes; it does not perform a complete independent round-trip comparison of every reference against the source, validate every relative link, or run the Inspector and symbol-checker regression suites.

The [GitHub Actions workflow](../.github/workflows/package-kpsa-skills.yml) invokes the builder and uploads the generated ZIPs and `SHA256SUMS.txt`. A successful packaging run is build evidence, not a fresh KeyShot runtime test or a full installation test in each host. Author-reported KeyShot tests remain separate evidence.

For a local rebuild after changing either API capture, regenerate `references/api/2026.3-beta/symbols.json` from both current captures before packaging. The current builder only creates that index when the file is absent, so an existing local index can otherwise be reused.

The committed [Claude archive](../releases/KPSA_Claude_Skill_1.1.1.zip) is a stored snapshot. The workflow uploads artifacts; it does not replace that tracked ZIP. Check the source commit in an archive's manifest rather than assuming its filename identifies the latest source.

**Important:** the ZIPs bundle selected public Unofficial_KeyShot_Python sources, **not** the separate original GPT backup stored in KeyShot-Python-AI-Knowledge. Live GitHub retrieval and local KeyShot MCP access require separate functioning tool connections and are not activated by packaging.

## Separate Grok private release

The independent `keyshot-script-writer` v1.3.1 package is documented in [AI/skills/grok/RELEASE.md](../AI/skills/grok/RELEASE.md). Its versioned source, when imported, belongs under `platform-releases/grok/v1.3.1/` and is **not automatically included** in the three agnostic-core derived ZIP builds. This preserves the user-approved standalone Grok release without expanding or changing ChatGPT/Claude packages.
