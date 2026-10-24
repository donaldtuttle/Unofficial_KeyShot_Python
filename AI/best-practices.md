# Best practices

**Source:** private KeyShot-Python-AI-Knowledge `knowledge/best-practices/README.md` (reviewed 2026-10-23)

Read `AI/constraints.md` before implementation. **The AI MUST NOT use non-standard or external libraries, unless the user gives explicit instructions to do so.** KeyShot scripting knowledge must come from the 2026.2 `help(lux)` dump ([`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md)) and relevant supplied examples, with errors corrected explicitly. General Python knowledge cannot substitute for KeyShot evidence. The public 2026.1 website is secondary and lags.

## 1. Structure and readability

Use descriptive snake_case names for functions/variables and PascalCase for classes when a class helps. Keep explicit imports, consistent indentation and readable formatting. Put configuration and prerequisites near the top. Use documented constants instead of unexplained numeric identifiers; do not invent constants because another API uses similar names. Divide complex work into focused functions without burying scene changes in helpers.

## 2. Script creation process

Establish the intended result, build, GUI/headless mode, target scene elements, units, scope and output destination. Retrieve exact declarations from the 2026.2 dump and the full applicable source passages. List material assumptions and unresolved behavior. Plan preflight, requested changes and verification before implementation. Preserve requested functionality when repairing a script, and explain deliberate behavior changes.

## 3. Error handling and debugging

Check documented missing values and input types before calls. Catch exceptions narrowly where useful context can be added; report the operation, target and relevant values. Do not silently continue after a partial failure. Console `print` is available as ordinary Python feedback; do not invent KeyShot logging methods. File logs require task authorization and a deliberate non-overwriting path. A broad exception handler is not rollback.

## 4. User interaction and feedback

Use documented native KeyShot dialogs for interactive GUI tasks. Prefer one dialog for related inputs. Supply field-appropriate labels, descriptions, meaningful defaults, numeric limits and selection choices. Check cancellation before indexing the result and validate returned values. Use a stable script-specific ID only when persistence is intended. Report batch progress with mechanisms actually documented for the target mode; do not invent a progress bar or cancellation API.

## 5. Common errors and their diagnosis

An empty-item-tuple error calls for checking the selection item's complete tuple and choices; it is not evidence that every text field always requires a nonempty default. A string/list mismatch calls for selecting or constructing the correct value, not blindly converting the whole list. A missing graph/node/parameter requires a contextual stop or skip policy. An attribute error calls for checking API ownership and version against the 2026.2 dump, not guessing a similar name. Treat incomplete examples and broken indentation as documentation issues before presenting code as executable.

## 6. Performance and batching

Cache stable lookups and calculations outside loops, use dictionaries/sets for repeated matching, and limit unnecessary scene traversal or repeated graph reads. Snapshot intended targets before changing hierarchy or names. Do not add undocumented undo sessions, transactions, threads or parallel workers as an optimization. Measure changes in a real target scene before claiming a speedup. Avoid applying a transform to both a parent and its children when that would repeat the effect.

## 7. Material graphs, nodes, edges and parameters

Retrieve the graph for the exact material and validate its existence. Resolve nodes by stable identifiers and verified types; do not assume display names are unique or that type results are plain strings. Parameters belong to shader nodes. Check parameter existence, type, pure status and compatible values before access or mutation. Build edges using the documented source, target and target input; an edge ID is not automatically an input parameter name. Preserve texture paths and specialized material relationships.

## 8. Cameras

Use documented module camera accessors and the actual return representation. Do not assume a rich camera object with `.name`, `.position` or `.fov`. Distinguish camera selection, creation, position, direction/look-at, lens properties and saving changes. Save camera changes when intended by the task and required by the documented workflow. Preserve the user's camera unless changing it is part of the request.

## 9. Testing and debugging workflow

Develop in small steps: read-only observation, validated preflight, a limited mutation in a disposable scene, and inspection of resulting state and appearance. Keep tests for ordinary Python logic outside KeyShot clearly separate from runtime tests. Mocks validate selected control flow, not API truth. Do not add terminal `input()`, `pdb` or GUI pauses to unattended/headless runs. Record exact build, mode, scene, expected result, observed result and remaining limitations.

## 10. Resource and file management

Use context managers for task-authorized ordinary file I/O. Validate paths, permissions, source existence, extensions and destination collisions before work. Do not silently create log directories, overwrite outputs or choose a desktop fallback. Delete objects/materials only when explicitly part of the requested cleanup; an unconnected node is not automatically safe to delete. Restrict cleanup to resources created or expressly selected by the operation. No invented delete or memory-release API.

## 11. Documentation and provenance

State target build/mode, configuration, side effects, imports, invocation, expected result and troubleshooting steps. Explain complex transforms and graph relationships in comments. Cite exact source symbols from the 2026.2 dump. Keep originals, source hashes and correction reasons; record behavior changes.

## 12. KeyShot modules and transformations

Use `lux` for documented KeyShot operations and `luxmath` for documented vector/matrix work. Start from the documented identity construction. Verify whether a method mutates an object or returns one before chaining. Make units, rotation convention, multiplication order, pivot and local/world space explicit. Distinguish grouping, model hierarchy, parts and object nodes through the documented node kind. Check object-only absolute-transform restrictions instead of transferring generic 3D assumptions.

## 13. Operational checks and summaries

Validate targets and all necessary preconditions, preserve originals, make the requested changes, then check the resulting state. Summarize processed, skipped and failed targets with reasons; do not report intended operations as completed. Keep user feedback proportional to the task. Successful setters do not establish correct visible output, and script completion does not establish a successful render.

## 14. Modularity with manual verification

Use reusable helpers for validated operations and targeted comparisons, while retaining per-material or per-node checks where required. Generic automation must not erase specialized graph relationships. Verify compatible values, connections, texture references and visible output. Manual verification is part of quality control, not justification for inventing methods. Multi-material creation is not a universal material-copy or graph-cloning operation.

## 15. Workflow, portability and cancellation

Separate initialization, input, target resolution, preflight, mutation and reporting. Do not reset camera/environment state unless requested. Use documented cancellation where available and stop cleanly without claiming rollback. Design material-template automation for headless execution and OS portability where supported; label GUI-only workflows explicitly. Use task-necessary standard-library path handling supported by the embedded runtime. Do not assume an IDE's interpreter can run KeyShot APIs or that an external dependency is available.

## 16. Complete examples and safe adaptation

Deliver full supported scripts with defined helpers and no omitted core operations. Label fragments as fragments. Validate each borrowed call, parameter, constant and return shape from the full historical example and the 2026.2 dump; preserve its useful intent without inheriting its errors. Retain original timing, frame rate, ranges, naming and visual behavior when correcting examples. Refuse to fabricate a missing operation to satisfy a full-script requirement.

API source of truth: [`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md) (2026.2 `help(lux)`). Public 2026.1 website is secondary only.
