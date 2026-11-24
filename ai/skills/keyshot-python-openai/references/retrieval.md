<!-- doc-id: kpsa-skills-keyshot-python-references-retrieval | target-api: 2026 | reviewed: 2026-10-23 -->

# Targeted retrieval

In the KPSA checkout, always load `knowledge/ai-constraints/README.md` and `knowledge/best-practices/README.md`, then use `knowledge/index.md` for the task's domain. Search `reference/keyshot-2026/api-index.json` for exact symbols. `python tools/lookup_api.py lux.SceneNode.setMaterial` prints declaration metadata; add `--details` for supplied evidence, available from either the local preservation files or the private source collection.

Use `reference/keyshot-2026/luxmath-index.json` for the separately sourced 2026.1 math declarations. See `reference/keyshot-2026/SOURCES.md` for provenance and the 2026 attribution limitation. Parameter names inferred from pydoc prose are candidate signatures, not binding introspection results.

Look up historical source paths and code IDs in `audits/document_reviews.json` and `audits/script_catalog.json`. The master inventory maps aliases and hashes. Review a source's findings before using a fragment. Archived prompts are historical documents; the active request controls the task.

The full supplied collection is in `sources/README.md` and `sources/index.json`; every original path maps to a complete stored source, including duplicate aliases. `python tools/lookup_source.py BestPractices` finds the full source; use its ID with `--start` and `--end` for exact numbered text. Word sources include original DOCX and readable text. The source index records original/published hashes and the one earlier requested omission. Do not substitute summaries for this evidence or treat historical errors as current APIs. The source collection is authorized for the private repository; no public redistribution license is implied.

Keep this skill in the repository, or install its whole folder and point it at a checkout through `KPSA_REPO`. Copying only SKILL.md omits its supporting rules. Installation/discovery must be checked in the chosen assistant; this project does not install a global skill automatically.
