# KeyShot Studio 2026.1 Python Knowledge Base

Baseline: KeyShot Studio 2026.1, Python 3.13 64-bit.

## Mandatory Knowledge Sources (use these)

**Full KPSA backup** is in `kpsa_knowledge/`:
- KeyShot_2026_Lux_API_Reference.txt — primary 2026 Lux API reference
- KS_MaterialScripts.txt — material graph scripts and patterns
- KS_ScriptDoc.txt, KS_QuickRef.txt, KS_Python_Guide.txt, KS_TOC.txt
- KSPA_BestPractices.txt, KSPA_PreloadKnowledge.txt, KSPA_UserInput.txt, KPSA_Quick_Guide.txt
- KS_CameraScripts.txt, KS_ColorColorway.txt, KS_CustomInputDialog_GUI.txt, KS_TransformMatrix.txt

**Material shader parameters** are in `materials/`:
- KeyShotPythonScripting_ShaderNodeTypes&Parameters_Documentation.txt
- All individual Material [Type].txt files
- KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.txt

Treat these as authoritative. Do not invent parameter names, node types, or API methods.

Official docs remain available at:
- https://media.keyshot.com/scripting/doc/2026.1/
- https://media.keyshot.com/scripting/headless_doc/2026.1/

## Important 2026 Features

- `node.getMetadata()` on `lux.SceneNode` → dictionary of CAD metadata.
- `lux.renderAnimation(...)` in headless (preferred path, ~3× faster).
- Python 3.13.

## Core Patterns

Scene traversal, transforms via luxmath.Matrix/Vector, material graph access via lux.getMaterialGraph(), RenderOptions, multi-materials, and headless automation are covered in the kpsa_knowledge/ files.

When generating or reviewing scripts, consult the relevant knowledge file first.
