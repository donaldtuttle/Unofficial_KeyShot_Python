# KeyShot Studio 2026 Scripting Updates (Unofficial Notes)

Target: 2026.x (prefer 2026.3 beta when available; Python 3.13).

## New / Notable

- **CAD metadata in scripting**  
  `lux.SceneNode.getMetadata()` returns a dictionary of metadata imported from CAD (SolidWorks, Creo, etc.).  
  Previously visible only in the UI metadata viewer; now fully scriptable.  
  Typical uses: conditional material assignment, part visibility, automated thumbnail or camera framing based on engineer properties.

- **Headless animation rendering**  
  `lux.renderAnimation(...)` is the preferred path.  
  KeyShot starts the render engine once and processes the entire animation (average ~3× faster than looping `renderImage` per frame).

- Python version: 3.13 64-bit.

- **2026.2** (superseded by 2026.3 beta) added additional animation scripting (create/edit/delete object and camera keyframe animations) and script performance improvements. Specific new function names are not yet listed in public notes.

## Still Core

SceneNode traversal and transforms (luxmath), MaterialGraph manipulation, MultiMaterial, MaterialMetadata / CMF, RenderOptions + passes, Env / ImageStyle / Studio, import/export, headless queue and network options.

## Official References

- https://media.keyshot.com/scripting/doc/2026.1/
- https://media.keyshot.com/scripting/headless_doc/2026.1/
- https://manuals.keyshot.com/kss2026/en-us/manual/scripting.html
- Prefer the 2026.3 beta dump when available.

The historical API markdown dumps in this repository pre-date 2026. Use the official pages for exact current signatures.
