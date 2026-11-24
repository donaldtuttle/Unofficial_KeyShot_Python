# Corrected 2026 contracts

Read `references/constraints.md` first. **The AI MUST NOT use non-standard or external libraries.** This page brings together the behavior errors found during documentation review; each named symbol should be verified against `references/KeyShot_lux_API.md`.

## Scene hierarchy, model sets and resources

`lux.getSceneTree` returns a SceneNode root. Traverse `getChildren()` on the actual nodes to inspect a hierarchy; `find()` yields a collection, so check empty and ambiguous matches before mutation. Node kinds come from `getKind()`. Scene nodes, shader nodes, material graphs and environment objects are distinct receivers.

`lux.getModelSets` lists **active** model sets. To inventory inactive sets too, inspect root children with `isModelSet()`. `lux.setModelSets(names)` activates the requested sets and deactivates the others; False can follow partial activation. Activation is separate from geometry hiding. Use documented node `hide()`/`show()` for visibility; no recursive keyword is specified. `SceneNode.delete()` is documented but destructive. Protect exact targets and do not infer that an unconnected shader root is unused.

Use `lux.getKeyShotFolder(type=...)` with the relevant FOLDER constant for configured resources. Hardcoded KeyShot 12 paths and “all non-Windows systems are macOS” are historical assumptions. A timestamp alone is not a uniqueness guarantee for an output.

## Importing, exporting and saving

`lux.getImportOptions` mixes dictionary-field descriptions with argument prose. Read the source before choosing a keyword. The selected-model-set prose contains `model_set_import`/`model_set_import_to` and `GetId()` inconsistencies; do not repair undocumented option names by guesswork.

For the returned import dictionary, `import_type=0` adds, `1` updates active geometry, and `2` clears/imports a new scene. `geometry_units` is conversion from meters, not the GUI display unit. `merge_objects` refers to identically named objects. `model_set_import_to` describes all=0, active=1, selected=2 and new=3. Do not create one temporary set and assume a separately imported new set is the same object. Identify actual imported IDs before renaming or transforming; a whole-scene search can affect preexisting geometry.

`lux.exportFile` describes whole-scene export and has no documented node-selection argument. Looping over model names changes filenames, not export scope. Preserve per-model export as an unresolved workflow until isolation is verified. GLTF with a `.glb` extension produces GLB according to this contract.

`lux.saveMaterial(name, folder=...)` uses a **relative folder within the material library**. It is not an arbitrary absolute output directory. `lux.saveMaterialPackage(mat, path)` accepts an explicit package path and includes textures. Shader node display names are not automatically registered material names, and an in-memory saved-name set does not protect existing library files. Do not invent a library collision API.

`lux.setSceneUnit(unit, keep=True)` has a parameter named `keep`, not `rescale`. Preserve intended physical size versus rescaling explicitly and test the actual result. Its return type is unspecified, and the setter and UNIT constants are absent from official headless declarations.

## Cameras, rendering and time

`lux.newCamera` makes a new camera active; it documents False on a nonunique collision, without a complete successful return-type contract. `lux.getCamera` does not establish a rich camera object. Use dedicated position, direction, look-at and lens getters/setters; those positioning operations are documented. Projection choice is separate from a standard-view orientation.

`lux.getCameraLens` is a dictionary with key `lens`; `type` is not the described key. Its optional FOV/perspective, shift and panoramic mode entries depend on projection. FOV is strictly between 0 and 180 degrees; focal length is 5–200 mm. Setting both does not establish independent persistence. Do not claim XMP recreation from a hardcoded camera table or omit shift while promising exact recreation.

`lux.getSceneInfo` documents a dictionary but does not explicitly enumerate the exact spelling of every key. Supplied vendor examples use `width`/`height`; historical `render_width`/`render_height` usages are not established by the prose. Inspect the returned dictionary before assuming keys. `lux.getMetaData()` is scene metadata; assigning the function without parentheses does not call it.

`lux.RenderOptions.setMaxSamplesRendering` and `setAdvancedRendering` are documented. Supply output dimensions to `lux.renderImage`; do not invent a resolution setter. Adding a job to the queue is distinct from `lux.processQueue` and from a completed render. `lux.screenshot` captures the current real-time view and returns its path; it is GUI-only in the reference comparison and does not establish convergence or offline-render quality.

Use `lux.setAnimationTime`/`lux.getAnimationTime` in **seconds**, with frame getters/setters for frame positions. `lux.pause`/`lux.unpause` control the renderer, not animation playback. Do not invent timeline playback or duration functions; inspect `lux.getAnimationInfo` instead. The two supplied animation-list accessors are flagged as absent from official 2026.1 pages.

Held frames require unique output positions. Preserve inclusive range and total-copy intent: three copies means three output positions for that source frame. At FPS `f`, `n` encoded frames last `n/f` seconds. Accept padded formats deliberately, validate every expected input, and keep encoding separate from rendering. A falsey unspecified return is not automatically failure; historical cancellation guidance supports checking specifically for False, while actual output still needs validation.

## Materials, edges and colors

`lux.createMultiMaterial` requires both the new name and existing `mat`; it does not guarantee every nested node gets fresh IDs, textures are independent, or all specialized data is cloned. Its successful return shape is unspecified. Retrieve by the explicitly chosen name and test structure/appearance. `lux.createSceneMaterial(name)` creates a diffuse scene material, not an arbitrary shader type.

`lux.ShaderNode.getType` describes internal and human-friendly names without a complete return container contract. Do not stringify an unknown tuple/dictionary and feed it to `newNode`. Pure parameters forbid concrete `getValue`, `getColor` and `setValue`. Check both source and target pure/type status. Equal type codes do not prove complex values are independent or safely copyable.

`lux.MaterialGraph.newEdge` takes source node, target node and the **target input parameter name**. An edge ID is not that name. `lux.ShaderEdge` declares source/target-node accessors but no parameter accessor. When inspecting ports, enumerate target ShaderNode parameter names and match documented `getInputEdge(name)` IDs; report missing/ambiguous relationships instead of inventing an accessor. Multi-material membership is not established by two connections into the same surface port. Disabling multi-material mode removes inactive submaterials.

There is no declared generic texture parameter enum. COLOR=13, COLORALPHA=14, STRING=9 and shader bump/label/geometry ports are distinct. Numeric types 20 and 4096 occur in the historical 3D Paint inventory but have no named enum in the supplied reference; preserve them as unresolved observations.

The versioned 2026 Material Graph manual documents RGB shader values as normalized triples or known library color names. This useful workflow is retained. It does not establish the same representation for COLORALPHA or scene multi/sub-color objects. The manual's SceneNode parameter-owner typo is corrected by the supplied ShaderNode declarations.

`lux.ColorParameter.setRGBA` uses 0–255, `setRGBAf` uses 0–1, and `setHSV` uses hue [0,360), saturation/value 0–100. Kelvin is 2500–9500. Do not apply one universal normalization rule. `setSubColors` is only for multi-colors and preserves order; active sub-colors must be members. Colorway append/update methods associate an existing multi/sub pair, rather than create arbitrary RGB variants or automatically bind them to geometry. Direct constructor calls do not establish a registered scene object.

`lux.newEnvironment` and `lux.newStudio` have unspecified successful return shapes. Use documented retrieval after explicit creation/activation. Do not interpret an unspecified setter return as boolean success. Resolve exact resources and every requested setting before mutation.

## Transformations, dialogs and complete delivery

`luxmath.Matrix.makeIdentity` is the explicit identity factory. Retain copies returned by named transforms. `rotateAroundAxis` takes **degrees**; Python `sin`/`cos` take radians. Named Vector/Matrix operations avoid assuming undeclared arithmetic operator overloads. Only object nodes support absolute `SceneNode.applyTransform`. Multiplication order, coordinate conventions, parent transforms and pivot effects need a concrete scene test; do not infer a fourth-column convention from another library or transform both a parent and all its descendants accidentally.

Native GUI input tuples have documented field-specific shapes. `DIALOG_ITEM` needs choices and returns an index/display pair; cancellation is None. A text field does not universally require a nonempty default. The fifth True/file-filter additions in historical `DIALOG_FILE` tuples are undocumented; `lux.getInputFile(multiple=True, ...)` is the documented multifile picker. Its exact returned representation still needs a runtime observation before iteration. Numeric fields require ranges; extra tooltip slots and a textarea constant are not documented.

No automatic log files, terminal input loops, external GUI libraries, package installation, guessed fallback calls or hidden helper dependencies. Complete scripts include imports, helpers, configuration, validation and invocation. Explicitly label teaching fragments, simulated actions and missing bodies. Runtime gaps cannot be filled with an invented implementation.
