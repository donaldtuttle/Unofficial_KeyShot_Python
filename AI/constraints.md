# Mandatory AI constraints

**Source:** private KeyShot-Python-AI-Knowledge `knowledge/ai-constraints/README.md` (reviewed 2026-10-23)

Read this document before every KeyShot scripting task. General Python experience is not evidence that a KeyShot operation exists or works. Retrieve the relevant supplied documentation, verify the exact API against [`lux/KeyShot_lux_API.md`](../lux/KeyShot_lux_API.md) (2026.2 `help(lux)` dump), and honor the user's constraints before writing code.

The public 2026.1 website is secondary and lags. It is not the source of truth.

## Libraries and execution environment

**The AI MUST NOT use non-standard or external libraries, unless the user gives explicit instructions to do so.** This applies to generated scripts, workarounds, helper modules and GUI code. Do not use or recommend NumPy, pandas, SciPy, Pillow, OpenCV, requests, PySide, PyQt, package installation or an external service as an assumed dependency. Do not disguise a dependency behind a helper or dynamic import.

This constraint exists because external Python and third-party GUIs usually fail inside KeyShot’s embedded runtime. More often than not they do not work. Use them only when the user explicitly asks, and still warn that KeyShot may not have the library.

Use KeyShot's built-in `lux` and `luxmath` for KeyShot operations. Python language constructs are allowed. Use a standard-library module only when needed for the requested task and available in KeyShot's embedded Python. An import working in an external IDE does not establish that availability. Do not expand a scene task into unrelated Python work. Do not import a helper absent from the delivered script/package.

Do not add file reads/writes, file logging, network access, threads, subprocesses or background workers merely as conveniences. A request to import, export, render or save authorizes the necessary operation at the requested destination; it does not authorize unrelated logs, hidden files, extra scene saves or package installation. Prefer console feedback when file logging was not requested.

Run KeyShot operations inside the licensed KeyShot runtime. An ordinary interpreter, IDE, stub or mock does not supply working `lux`/`luxmath`. Do not suggest installing them with a package manager. Match the target build and embedded Python version. Check GUI/headless restrictions for each call.

## Evidence before implementation

- **AI-01 — Retrieve first.** Read these constraints, best practices, the relevant topic, exact API entries from the 2026.2 dump, full source passage and applicable findings. Model memory and generic Python patterns are not KeyShot evidence.
- **AI-02 — Respect API ownership.** Distinguish module functions from methods of scene nodes, graphs, shader nodes, edges, parameters and other objects. Verify the receiver.
- **AI-03 — Verify the full call.** Check argument names, required values, types, units, ranges, defaults, return representation, version and mode against the 2026.2 dump. Ellipsis signatures and prose-derived parameters remain incomplete. Do not invent overloads or attributes.
- **AI-04 — No invented facilities.** Do not invent logging, progress, cancellation, transaction, undo, camera, cloning, shader or material facilities. A plausible name or successful mock does not establish a feature.
- **AI-05 — Show uncertainty.** Identify unsupported steps and retrieve evidence or propose a focused runtime observation. Do not hide gaps behind `getattr`, broad exceptions, repeated guessed calls or fabricated fallbacks.
- **AI-06 — Preserve corrections.** Apply curated findings and user-requested removals to historical sources. Repetition does not validate an archived error. Absence from an index alone is not proof of impossibility.

## Preconditions, scene state and side effects

- **AI-07 — Validate before changing.** Resolve exact targets, scene state, materials, shader types, input types/ranges, paths and naming collisions before mutations. Handle documented missing-object and cancellation results. Do not stringify every invalid value to suppress type errors.
- **AI-08 — Respect dependencies.** Obtain the correct graph and nodes before parameters or edges. Check multi-material state only for operations that need it. Verify historical ordering against documentation instead of inferring universal API rules from an example.
- **AI-09 — Preserve material relationships.** Distinguish object/material duplication, linking, multi-material creation, shader copying and graph rebuilding. Do not force every duplicate through multi-material creation. Check parameter type and pure status; preserve connections and texture references.
- **AI-10 — Transform explicitly.** Establish node kind, coordinate space, pivot, units, order and relative/absolute intent. Do not transform parent and child accidentally. Verify matrix operations rather than copying another 3D library's syntax.
- **AI-11 — Use KeyShot GUI controls.** Use documented native dialogs for GUI tasks. Prefer one complete input dialog, validate field-specific tuple formats and ranges, handle cancellation, and use a stable unique ID for intended persistence. Do not use third-party toolkits or GUI calls in headless mode.
- **AI-12 — Protect the user's work.** Default risky examples to dry-run and collect preconditions before setters. Avoid unrequested overwrites, deletion, resets or cleanup. Exceptions and dry-run do not provide rollback. Do not silently choose output folders or change scene/camera state to simplify an example.
- **AI-13 — Preserve temporal and visual intent.** Retain requested frame rate, inclusive ranges, duration, sequence names, motion and transform behavior. A symbol check cannot establish the rendered result.

## Deliverables and user interaction

- **AI-14 — Complete means complete.** Deliver the full supported script with explicit imports, configuration, defined helpers, checks, comments and invocation. No `...`, TODOs, pseudocode, hypothetical calls or omitted core operations in code presented as ready. A requested teaching fragment may remain clearly labelled.
- **AI-15 — Accuracy comes first.** If a required operation is unsupported or unverified, identify the missing evidence and supportable alternatives. Do not fabricate a complete script or guarantee runtime success.
- **AI-16 — Respect the mode.** Material-template automation should support headless use and OS portability where documented functionality permits. A GUI-specific request is an explicit exception to headless design. Do not silently replace one workflow with the other.
- **AI-17 — Explain use and diagnosis.** State prerequisites, configuration, expected changes, invocation and failure diagnosis. Cite sources and include useful error context. Respect the user's experience; ask only when a missing choice changes correctness or scope.
- **AI-18 — Separate test evidence.** Distinguish syntax, declaration, static, mock, GUI, headless and visual/behavioral checks. Never call parsing, mocks or source presence runtime testing. Record exact build, mode and scene for real tests.
- **AI-19 — Preserve information.** Keep full supplied documents, examples, filenames, duplicate mappings and hashes available. Record corrections separately. Do not substitute summaries for detailed sources or call an automated scan a complete semantic audit.

## Source basis

The current user's external-library prohibition is mandatory. Historical file-I/O examples do not override authorization requirements. Unsupported historical calls remain source data and need correction before reuse. Full scripts are required when supportable; fabrication cannot satisfy that requirement.

Continue with `AI/best-practices.md` and the 2026.2 dump at `lux/KeyShot_lux_API.md`.

## Headless error handling

`lux.isHeadless()` is the mode check. GUI calls throw or fail in headless. Do not call them there.

GUI-only (guard or skip):
- `lux.getInputDialog` and the `DIALOG_*` constants
- `lux.getMessageBox`
- `lux.getBrowserDialog`
- `lux.getInputText`, `lux.getInputInt`, `lux.getInputDouble`, `lux.getInputFile`, `lux.getInputFolder`, `lux.getInputItem`
- Any call that opens a dialog when a path is omitted (`saveScene`, `saveSceneAs` without a path throws in headless)

Required pattern:

```python
if lux.isHeadless():
    # Headless: require explicit config. Do not open a dialog.
    opts = config  # paths, names, numbers supplied by the caller
    if not opts:
        raise RuntimeError("Headless run needs explicit config; no dialog available.")
else:
    opts = lux.getInputDialog(title="...", values=values)
    if not opts:
        print("Cancelled.")
        return
```

Rules:
- Check `lux.isHeadless()` before any GUI call.
- In headless, require explicit arguments. Do not invent a fallback dialog.
- In GUI, check cancellation (`if not opts`).
- Always pass an explicit path to save, export, or render in headless. An omitted path throws.
- Report the mode in the output so a failure is diagnosable.
- Do not use third-party GUI toolkits in either mode.

