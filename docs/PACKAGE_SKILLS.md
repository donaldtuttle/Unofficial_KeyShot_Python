# Packaged KPSA skills

The canonical, host-neutral AI instructions live in [AI/skill.md](../AI/skill.md). Three host entry points are in [AI/skills](../AI/skills).

Build three self-contained ZIPs from the current repository snapshot:

~~~bash
python tools/package_kpsa_skills.py
~~~

Output is placed in ignored `dist/` (see output filenames below). Every ZIP includes **all AI, Scripts, lux, luxmath, lux_headless and luxmath_headless files**, plus the root README, LICENSE and 2026 update note. The original directory tree is preserved under `references/repo/`, and SHA-256 checksums and source commit are recorded in each `SOURCE_MANIFEST.json`. The build validates all reference bytes against their originals.

- **KPSA_ChatGPT_Plugin_1.1.0.zip**: portable `plugin.json`, a `skills/keyshot-python-scripting/SKILL.md` entry point and complete local references. Use ChatGPT's plugin installation/update workflow. Creation of this ZIP does **not** change any installed private plugin.
- **KPSA_Grok_Skill_1.1.0.zip**: `keyshot-python-grok/` root skill folder, ready to extract under `.grok/skills/` or `~/.grok/skills/` for a supported Grok agent.
- **KPSA_Claude_Skill_1.1.0.zip**: `keyshot-python-claude/` root skill folder, ready for Claude's ZIP skill uploader or extraction to `.claude/skills/` / `~/.claude/skills/`.

A [GitHub Actions workflow](../.github/workflows/package-kpsa-skills.yml) builds the same files and uploads an artifact containing the ZIPs and SHA256SUMS.txt.

**Important:** the ZIPs bundle the current public Unofficial_KeyShot_Python source tree, **not** the separate original GPT backup stored in KeyShot-Python-AI-Knowledge. Live GitHub retrieval and local KeyShot MCP access require separate functioning tool connections and are not activated by packaging.

**License:** GPLv3. README and LICENSE agree. Packages preserve the original LICENSE.
