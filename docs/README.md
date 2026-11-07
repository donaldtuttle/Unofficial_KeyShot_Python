# KeyShot Python Documentation

Technical guides for learning and using KeyShot Python, including API reference notes, GUI dialogs, material graphs, transformations, and scripting practices.

The complete reference documents used by the [AI knowledge collection](../AI/kpsa_knowledge/) are also available here in the main code documentation. The original filenames and full contents are preserved; these are not summaries or shortened versions.

## Scripting guides

| Guide | Contents |
| --- | --- |
| [Quick reference](KeyShotPython_Scripting_QuickReference_Documentation.txt) | KeyShot Python reference patterns. |
| [Best practices](KeyShotPythonScripting_API_BestPractices_Guide.txt) | Detailed scripting practices and examples. |
| [API reference notes](KeyShotPythonScripting_API_Documentation.txt) | A thin reference layer pointing to the captured API documentation. |
| [GUI dialog guide](KeyShotPythonScripting_API_GUI_GuideDocumentation.txt) | Native input dialogs and field tuple formats. |
| [Custom input dialog example](KS_CustomInputDialog_GUI.txt) | A compact GUI-only input-dialog example. |
| [Copy of a Copy](KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt) | Material-graph copying, nodes, parameters, and connections. |
| [Transformation matrix guide](KeyShotPythonScripting_TransformationMatrix_Documentation.txt) | Transformation matrices and related scripting examples. |

## API source references

The captured API documentation is the source of truth for the recorded KeyShot Studio 2026.3 beta build:

- [lux API](../lux/KeyShot_lux_API.md)
- [luxmath API](../lux/KeyShot_luxmath_API.md)

Use each module's own capture to verify calls. Guides and historical examples provide context and patterns; when working with another KeyShot build, check that build's exposed API.

## AI setup and packaging

- [AI agent setup](../AI/README.md)
- [AI knowledge table of contents](../AI/knowledge_base.md)
- [Platform-specific skill entry points](../AI/skills/README.md)
- [Skill packaging](PACKAGE_SKILLS.md)

## Shared documentation

The seven `.txt` guides in this folder are identical copies of the matching files in `AI/kpsa_knowledge/`. That location remains available to existing AI configurations and links. When updating a shared guide, keep both copies synchronized.
