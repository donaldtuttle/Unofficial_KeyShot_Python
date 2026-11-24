# KeyShot Python Scripting Reviewer

This repository is a source-preserving export of **KeyShot Python Scripting Reviewer (KPSR)**, package `gpt-e2ffc2e54121dcc9cafc60768b8dc90e`, version `0.184.3`.

KPSR is a skills-only Agent Plugin for reviewing and generating Python scripts used with KeyShot. Its original package metadata describes it as a reviewer that identifies potential issues, inefficiencies, and areas for improvement.

## Contents

- `plugin.json` — portable Agent Plugins 1.0 manifest.
- `.codex-plugin/plugin.json` — original Codex compatibility manifest.
- `assets/gpt-icon.png` — original plugin icon.
- `skills/instructions/SKILL.md` — original KPSR instructions.
- `skills/instructions/agents/openai.yaml` — original agent-facing metadata.
- `skills/instructions/lookup/knowledge-index.json` — original knowledge-file index.
- `skills/instructions/references/` — 16 original knowledge and example files.
- `INVENTORY.md` — human-readable export inventory and accessibility notes.
- `EXPORT-MANIFEST.json` — machine-readable export provenance and original-file inventory.
- `SHA256SUMS.txt` — SHA-256 checksums for every original plugin file.

## Source preservation

All 22 files from the accessible plugin bundle were copied byte-for-byte. Their hashes were checked after copying. The four repository documentation files listed above were added for this export; no original configuration, instruction, knowledge, image, or example file was edited.

## Put this on GitHub

1. Extract the ZIP.
2. Create an empty GitHub repository.
3. Add the extracted directory contents at the repository root.
4. Review `INVENTORY.md`, especially the missing-source and licensing notes, before making the repository public.

The archive is intended as a GitHub-ready source snapshot. It has not been rewritten as a public plugin-directory submission, and it does not include publisher attestations or other portal-only materials.

## Important notes

- The plugin instructions refer to `KeyShot 2024.3_Headless_Scripting_Documentation.txt`, but that file was not present in the accessible bundle or its knowledge index.
- `Scripting_Materials_Documentation.txt` appears in an example request in the instructions, but no file with that name was present in the accessible bundle.
- No standalone `.py` or other executable script files were exposed. Script examples are embedded in the original text knowledge assets, principally `KeyShot_Python_Script_Examples_with_ToC.txt`.
- No license file or license field was exposed. This export does not infer or grant redistribution rights; add an appropriate license only if the owner has the authority to do so.
- The original `agents/openai.yaml` and manifest presentation fields are preserved exactly, including any truncation or current-format validation issues.

See `INVENTORY.md` for the complete file list and `SHA256SUMS.txt` for integrity verification.
