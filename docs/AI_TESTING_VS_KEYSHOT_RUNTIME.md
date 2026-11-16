# Can AI Really Test KeyShot Python Scripts?

## Understanding simulation, API constraints, and runtime verification

**Audience:** KeyShot Studio Python users, AI-assisted scripters, educators, and code reviewers.  
**Status:** Educational guidance, not an assertion that any particular script has passed runtime testing.  
**Related repository policy:** [Mandatory AI constraints](../AI/constraints.md), especially **AI-01 through AI-05** and **AI-18**.

## The central distinction

**A Python script that passes an AI-generated simulation has not necessarily been tested in KeyShot.**

KeyShot's embedded Python can access KeyShot-specific modules such as `lux` and `luxmath`, which operate on a real scene and expose application objects. A regular Python environment such as Anaconda, Spyder, VS Code, or PyCharm does not automatically provide KeyShot's proprietary runtime simply because the Python versions match.

An IDE can **edit** a KeyShot script and, if configured, **launch KeyShot to run it**. An ordinary standalone Python interpreter cannot be assumed to execute the real KeyShot API. Installing a Python package or inventing a substitute `lux` module is not equivalent to executing KeyShot.

KeyShot's ability to import some locally installed Python libraries *into KeyShot* is a separate capability. It does not make `lux` available to arbitrary outside interpreters.

## What an AI can and cannot verify

| Check | Legitimate conclusion | What it does **not** prove |
| --- | --- | --- |
| Syntax parsing / compilation | The file parses for the selected Python version | Correct KeyShot calls or scene behavior |
| Static review | Potential problems in control flow, imports, argument usage, or dependencies were identified | The code was executed |
| API documentation comparison | A specified call appears in a particular API reference, with documented signature or limitations | It works in the target scene/build |
| Mocks / stubs / simulated `lux` | Code behaved as expected for the *invented or modeled* responses | The real `lux` API behaves identically |
| Standalone unit tests | Pure Python logic works under test inputs | Material graphs, scene state, or GUI operations work |
| Headless KeyShot integration test | The script or operation ran in the actual headless KeyShot process | GUI-only calls or visual results are correct |
| GUI KeyShot integration test | The script ran in the actual KeyShot GUI against a specified scene | Every scene/version/edge case is covered |
| Save/reopen/inspect/visual comparison | A defined persisted scene behavior or result was checked | Unchecked properties are correct |

**A green test result is only meaningful when its test environment and assertions are disclosed.**

### Example: a mock can pass while KeyShot fails

A developer might replace the `lux` dependency with a mock object that returns an expected list of materials. Tests then pass because the mock returns exactly what the test told it to return. That is useful for isolated algorithm testing, but **not evidence that the real API has that name, signature, return type, or scene behavior**.

Do not label such a result "tested in KeyShot," "fully verified," or "production ready."

## A KeyShot-specific risk: material graphs and identity

Material-graph automation may involve multi-material submaterials, nodes with blank or duplicate names, and connections that need to survive copying and reopening.

For graph-copy operations:

1. Enumerate the source graph and its submaterial membership using APIs confirmed for the target build.
2. Record each source node's type, parameters, and graph relationships, including the identity of connection endpoints and sockets.
3. Copy or reconstruct the destination graph using *actual* supported API operations.
4. Resolve source-to-destination node identity explicitly; **names are not guaranteed unique identifiers**.
5. Inspect the resulting graph's connections independently rather than trusting successful creation calls.
6. Save, close, and reopen a **test copy**, then inspect again. Treat session-specific/dynamic IDs as temporary identifiers, not stable IDs to compare across sessions.
7. Compare a canonical graph description based on structure, node types/parameters, submaterial membership, and connections. For duplicate or nameless nodes, preserve distinguishable structural relationships and connection endpoints rather than matching by name alone.

**Do not remove a verification pass merely because it appears to duplicate an earlier node-copy pass.** Creation and inspection serve different purposes.

A topology comparison should also identify unsupported API observations instead of silently declaring equivalence. Visual or render comparison can complement structural checks, not replace them.

## Headless is real KeyShot execution, not a simulation

KeyShot documents command-line and headless script execution. In a supported Windows installation, the documented syntax includes:

```powershell
keyshot_headless [options] [scene path] -script <script path> [script arguments]
```

Use your installed executable path, intended test scene, and explicit output paths as appropriate. **Headless exposes a subset of KeyShot API functionality**; the full GUI feature set is not guaranteed. Do not assume material-graph, dialog, rendering, or GUI calls are headless-compatible without checking the target version's documentation.

The exact executable, switches, exposed functions, and embedded Python version can differ by KeyShot release. Verify against the **target installation**. This repository includes API dumps captured from KeyShot Studio 2026.3 beta; they are direct evidence for that recorded build, not proof that a different build behaves identically.

## Minimum evidence standard for AI assistance

When asking an AI to create, review, or modify a KeyShot Python script, require a test report identifying:

- **Target KeyShot build:** exact version/build if known.
- **Execution mode:** not executed, standalone Python, mocked, KeyShot headless, or KeyShot GUI.
- **Evidence source:** API-dump section, official reference, runtime output, exception, scene inspection, screenshot, or render.
- **Scope:** which functions, paths, materials, graphs, and edge cases were actually checked.
- **Preservation:** what script behavior, GUI fields, filenames, data schemas, calculations, scene state, and safeguards must remain unchanged.
- **Remaining uncertainty:** what cannot be verified without a KeyShot runtime or a representative scene.

### Suggested confidence labels

- **STATIC REVIEW ONLY:** inspected or parsed; no real KeyShot execution.
- **MOCKED TEST ONLY:** simulation passed; KeyShot behavior unverified.
- **API-REFERENCED:** exact relevant API entries checked; runtime unverified.
- **KEYSHOT HEADLESS TESTED:** executed in specified headless build; scope and limitations recorded.
- **KEYSHOT GUI TESTED:** executed in specified GUI build and test scene; actual observations recorded.
- **SAVE/REOPEN VERIFIED:** target data and graph invariants compared after reopening a test scene.
- **VISUALLY VERIFIED:** specified rendered or GUI outcome compared with expectations.

Labels can be combined, but they must not be promoted from one category to another by inference.

## Reusable AI instruction

> Review the supplied KeyShot script against the repository's Mandatory AI Constraints and the API dump for the target build. Do not invent lux/luxmath functions, object methods, parameter names, signatures, or behaviors. Do not use third-party libraries without explicit authorization. Preserve working GUI, calculations, identifiers, output schemas, and existing verification logic unless a change is justified. Distinguish syntax, static review, documentation checks, mock tests, KeyShot headless execution, KeyShot GUI execution, and save/reopen or visual verification. Report precisely which checks you actually performed. Never claim that the script works inside KeyShot based solely on an external interpreter or simulated lux module. If runtime access is unavailable, clearly state that KeyShot execution remains unverified and provide a focused test plan.

## KeyShot documentation and repository references

- [KeyShot scripting overview](https://manual.keyshot.com/manual/scripting-2/)
- [KeyShot quick-start scripting (KeyShot 11 archival reference)](https://manual.keyshot.com/keyshot11/manual/scripting/quick-start-scripting/)
- [KeyShot headless scripting (KeyShot 11 archival reference)](https://manual.keyshot.com/keyshot11/manual/scripting/exposed-headless-scripting-functionality/)
- [Repository AI constraints](../AI/constraints.md)
- [Embedded API dump, recorded 2026.3 beta](../lux/KeyShot_lux_API.md)

**Version note:** Some official manual pages describe older KeyShot versions and older Python versions. They establish conceptual behavior and historical command syntax, **not** the exact current configuration of every 2026 installation. Use the installed application's introspection and matching version-specific documentation to resolve those details.
