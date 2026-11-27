# Copying a KeyShot material graph

The explicit graph walk from the v1.3.6 example is the consistent method for duplicating a material for independent editing. `lux.createMultiMaterial(name=..., mat=...)` is the entry point for creating the named destination container. The call alone does not guarantee a deep independent clone.

[Download or review the standalone script](../lux%20scripts/duplicate_material_graph.py). This revision is a review candidate for KeyShot Studio 2026.3. It still needs an in-scene test of the resulting material and its independence from the source.

## What the script copies

1. Read one regular source material. Record its nodes, supported non-pure values and each connection's receiving input. A disconnected node is included. Two nodes can share a display name.
2. Create the named multi-material container. Reuse its material output root, create the other nodes from their internal shader types, and copy each supported value to a non-pure parameter of the same name and type. This keeps the rebuilt network connected to the material output.
3. Remove seed connections into the destination material root and replace the new container's seed shaders. For each recorded connection, call `newEdge` with the mapped source node, mapped target node and the **target parameter name**. A pure parameter can receive a connection even though it has no concrete value to read or set.
4. Re-read the destination nodes and named connections. If an existing parent multi-material was specified, append the copy after those checks and read back the ordered membership list.

To identify a socket, the walk compares the edges returned by `getInputEdges()` with those returned by `getInputEdge(parameter.getName())` on the receiving node. An edge ID identifies a connection during this lookup. The string supplied to `newEdge` comes from the parameter.

## Running the review script

Open a disposable copy of a scene in KeyShot Studio 2026.3. Set these names at the top of the standalone file and run it in the Scripting Console.

| Setting | Value |
| --- | --- |
| `SOURCE_MATERIAL` | Exact name of one regular source material |
| `COPY_MATERIAL` | Unused name for the destination multi-material |
| `PARENT_MULTI_MATERIAL` | Leave as `None` for the first test. Set to an existing multi-material name to test appending the new copy. |

The source preflight stops for concrete types outside the script's supported set, including ColorGradient and AnimationCurve. It also stops for disabled edges or inputs it cannot resolve unambiguously, such as multiple edges exposed through only one named socket. If a later step fails after container creation, a partial destination can remain in the scene. The console identifies the failing step.

## Checking independence in KeyShot

Use a source with a recognizable color or roughness value and a texture connected to two compatible inputs. Include a connection to a pure input such as the material root's `surface` socket.

1. Open the source and copy in the Material Graph. Compare the shader connected to `surface`, trace both texture connections to their receiving inputs, and check the concrete values.
2. Change a value and disconnect one texture input **on the copy**. Reopen the source and confirm that its original value and both connections are intact.
3. For the optional parent test, use a fresh copy name and set `PARENT_MULTI_MATERIAL`. Check that the new entry appears after the existing members and select it to verify which material it displays.

The script's connection read-back checks topology. Record the KeyShot build and what happened during the edit-on-copy test before describing the revision as runtime-tested.

[KeyShot Studio 2026.3 `lux` API capture](../lux/KeyShot_lux_API.md)
