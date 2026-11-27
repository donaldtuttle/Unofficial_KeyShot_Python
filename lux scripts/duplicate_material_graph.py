"""Rebuild one material graph in a named multi-material. KeyShot 2026.3 review script.

Run in KeyShot's Scripting Console for material selection and naming controls.
For headless runs, configure the settings below.
The new container can remain in the scene if reconstruction stops.
"""

import lux

# Headless material settings
SOURCE_MATERIAL = "MaterialName"
COPY_MATERIAL = "MaterialName_Copy"
PARENT_MULTI_MATERIAL = None  # Optional existing multi-material name, e.g. "Finishes".

NODE_PREFIX = ""
NODE_SUFFIX = "_Copy"  # Clear both affixes to preserve the original node labels.

# Concrete types covered by the repository's earlier parameter-copy correction.
# Pure sockets are handled independently, whatever their type.
VALUE_TYPES = {
    lux.PARAMETER_TYPE_BOOLEAN, lux.PARAMETER_TYPE_INTEGER,
    lux.PARAMETER_TYPE_FLOAT, lux.PARAMETER_TYPE_FLOAT2, lux.PARAMETER_TYPE_FLOAT3,
    lux.PARAMETER_TYPE_DOUBLE, lux.PARAMETER_TYPE_DOUBLE3,
    lux.PARAMETER_TYPE_STRING, lux.PARAMETER_TYPE_STRINGLIST,
    lux.PARAMETER_TYPE_COLOR, lux.PARAMETER_TYPE_COLORALPHA,
}


def read_connections(node, parameters):
    """Resolve every incoming edge on this node to exactly one named input."""
    pending = {edge.getID() for edge in node.getInputEdges() or []}
    connections = {}
    if not pending:
        return connections
    matched = set()
    for parameter in parameters:
        name = parameter.getName()
        try:
            candidate = node.getInputEdge(name)
        except Exception:
            # Some parameters have no readable edge. Coverage is checked below.
            continue
        if candidate is None:
            continue
        edge_id = candidate.getID()
        if edge_id not in pending or edge_id in matched or name in connections:
            raise ValueError(f"Ambiguous input {node.getName()!r}.{name}")
        if not candidate.isEnabled():
            raise ValueError(f"Disabled edge at {node.getName()!r}.{name} cannot be reproduced")
        connections[name] = candidate.getSourceNode().getID()
        matched.add(edge_id)
    if matched != pending:
        raise ValueError(f"Could not resolve every incoming edge of {node.getName()!r} to a named input")
    return connections


def read_source(graph):
    roots = graph.getMaterialNodes() or []
    if len(roots) != 1 or graph.getRoot() != roots[0]:
        raise ValueError("Select one regular source material with a single material root")
    root_id = roots[0].getID()
    nodes = {}
    for node in graph.getNodes() or []:
        node_id = node.getID()
        label = node.getName()
        kind = node.getType()["name"]
        parameters = list(node.getParameters() or [])
        values = {}
        for param in parameters:
            if param.isPure():
                continue
            name, param_type = param.getName(), param.getType()
            if param_type not in VALUE_TYPES:
                raise ValueError(f"Unsupported concrete parameter {label!r}.{name} (type {param_type})")
            values[name] = (param_type, param.getValue())
        nodes[node_id] = (label, kind, values, read_connections(node, parameters))
    if root_id not in nodes:
        raise ValueError("Source node list is missing its material root")
    for label, _, _, connections in nodes.values():
        if not set(connections.values()).issubset(nodes):
            raise ValueError(f"An edge into {label!r} refers outside the source node list")
    return root_id, nodes


def copy_values(target, values):
    for name, (kind, value) in values.items():
        try:
            param = target.getParameter(name)
            if param is None or param.isPure() or param.getType() != kind:
                raise ValueError("missing, pure, or different parameter type")
            param.setValue(value)
        except Exception as exc:
            raise RuntimeError(f"Cannot copy {target.getName()!r}.{name}: {exc}") from exc


def rebuild_graph(source, target, root_id, nodes, node_prefix, node_suffix):
    # The container can already contain a material. Keep its structural roots
    # and replace its seed shaders so the rebuilt network drives the actual output.
    roots = target.getMaterialNodes() or []
    outer = target.getRoot()
    if len(roots) != 1 or outer is None:
        raise ValueError("The new container must expose exactly one sub-material root")
    material_root = roots[0]
    seed = set(target.getNodes() or [])
    protected = {outer, material_root}
    if not protected.issubset(seed) or seed.intersection(source.getNodes() or []):
        raise ValueError("Could not isolate the new container's nodes from the source")
    if material_root.getType()["name"] != nodes[root_id][1]:
        raise ValueError("Source and destination material root types differ")
    if outer != material_root:
        for edge in outer.getInputEdges() or []:
            if edge.getSourceNode() != material_root:
                raise ValueError("Unexpected connection to the outer multi-material root")

    mapped = {root_id: material_root}
    for node_id, (label, kind, values, _) in nodes.items():
        if node_id != root_id:
            new_node = target.newNode(type=kind)
            if new_node is None:
                raise RuntimeError(f"Could not create {label!r} ({kind})")
            requested_name = f"{node_prefix}{label}{node_suffix}"
            new_node.setName(requested_name)
            if new_node.getName() != requested_name:
                raise RuntimeError(f"Requested node name {requested_name!r}, got {new_node.getName()!r}")
            mapped[node_id] = new_node
        copy_values(mapped[node_id], values)

    for edge in material_root.getInputEdges() or []:
        target.removeEdge(edge)
    for node in seed - protected:
        target.removeNode(node)

    edge_count = 0
    for node_id, (label, _, _, connections) in nodes.items():
        dest = mapped[node_id]
        for input_name, upstream_id in connections.items():
            try:
                target.newEdge(source=mapped[upstream_id], target=dest, param=input_name)
            except Exception as exc:
                raise RuntimeError(f"Could not connect {label!r}.{input_name}: {exc}") from exc
            edge_count += 1

    # Read the destination back using its own nodes and IDs.
    if set(target.getNodes() or []) != set(mapped.values()) | protected:
        raise RuntimeError("Unexpected nodes after the rebuild")
    for node_id, (label, _, _, connections) in nodes.items():
        dest = mapped[node_id]
        actual = read_connections(dest, dest.getParameters() or [])
        expected = {name: mapped[upstream].getID() for name, upstream in connections.items()}
        if actual != expected:
            raise RuntimeError(f"Connection read-back failed for {label!r}")
    print(f"Rebuilt {len(mapped)} material nodes (including the root) and checked {edge_count} edges.")


def member_names(parent):
    members = parent.getSubMaterials()
    if members is None or not all(isinstance(name, str) for name in members):
        raise ValueError(f"Could not read the ordered member names of {parent.getName()!r}")
    return list(members)


def copy_material_graph(source_name, copy_name, parent_name=None, node_prefix=NODE_PREFIX, node_suffix=NODE_SUFFIX):
    """Create the container, rebuild its graph, then optionally append to a parent."""
    names = [source_name, copy_name]
    if parent_name is not None:
        names.append(parent_name)
    if not all(isinstance(name, str) and name.strip() for name in names) or len(set(names)) != len(names):
        raise ValueError("Use distinct, nonempty material names")
    if copy_name in (lux.getSceneMaterials() or []):
        raise ValueError(f"Scene material {copy_name!r} already exists")

    # getSceneMaterials lists used materials. Also refuse a retrievable unused
    # graph. A lookup of an absent name can fail instead of returning a graph.
    try:
        existing = lux.getMaterialGraph(name=copy_name)
    except Exception as exc:
        print(f"Lookup of unlisted name {copy_name!r} returned an error: {exc}")
    else:
        if existing is not None:
            raise ValueError(f"A graph named {copy_name!r} already exists")

    source = lux.getMaterialGraph(name=source_name)
    if source is None or source.getMaterialName() != source_name:
        raise ValueError(f"Source material {source_name!r} was not found")
    parent = None
    if parent_name is not None:
        parent = lux.getMultiMaterial(name=parent_name)
        if parent is None or parent.getName() != parent_name:
            raise ValueError(f"Parent multi-material {parent_name!r} was not found")
        if copy_name in member_names(parent):
            raise ValueError(f"{copy_name!r} is already a member of {parent_name!r}")

    print(f"Reading source nodes, concrete parameters and named inputs from {source_name!r}...")
    root_id, nodes = read_source(source)
    print(f"Creating named container {copy_name!r}...")
    try:
        lux.createMultiMaterial(name=copy_name, mat=source_name)
        target = lux.getMaterialGraph(name=copy_name)
        if target is None or target.getMaterialName() != copy_name or target == source:
            raise RuntimeError("Could not retrieve a distinct graph by the requested name")
        print(f"Rebuilding nodes and connections in {copy_name!r}...")
        rebuild_graph(source, target, root_id, nodes, node_prefix, node_suffix)
        if parent is not None:
            members = member_names(parent)
            if copy_name in members:
                raise RuntimeError(f"{copy_name!r} already appears in {parent_name!r}")
            expected = members + [copy_name]
            parent.setSubMaterials(expected)
            if member_names(parent) != expected:
                raise RuntimeError(f"Membership read-back differs in {parent_name!r}")
            print(f"Appended {copy_name!r} to {parent_name!r}.")
    except Exception as exc:
        raise RuntimeError(f"Copy of {source_name!r} stopped. Inspect {copy_name!r} before retrying. {exc}") from exc


def main():
    headless = lux.isHeadless()
    title = "Duplicate material graph"
    try:
        if headless:
            settings = (SOURCE_MATERIAL, COPY_MATERIAL, PARENT_MULTI_MATERIAL, NODE_PREFIX, NODE_SUFFIX)
        else:
            materials = sorted(lux.getSceneMaterials() or [], key=str.casefold)
            if not materials:
                raise ValueError("The scene contains no materials to select.")
            options = lux.getInputDialog(
                title=title,
                desc="Select a regular material. Node naming applies to each rebuilt shader and texture.",
                values=[
                    ("source", lux.DIALOG_ITEM, "Source material", materials[0], materials),
                    ("copy", lux.DIALOG_TEXT, "New material name (blank uses source name + _Copy)", ""),
                    ("prefix", lux.DIALOG_TEXT, "Node name prefix", NODE_PREFIX),
                    ("suffix", lux.DIALOG_TEXT, "Node name suffix (clear both fields to keep labels)", NODE_SUFFIX),
                    ("parent", lux.DIALOG_TEXT, "Add to existing multi-material (optional name)", ""),
                ],
            )
            if options is None:
                print("Cancelled.")
                return
            source = materials[options["source"][0]]
            copy_name = options["copy"] or f"{source}_Copy"
            settings = (source, copy_name, options["parent"] or None, options["prefix"], options["suffix"])

        copy_material_graph(*settings)
        message = f"Created {settings[1]!r} from {settings[0]!r}."
        print(message)
        if not headless:
            lux.getMessageBox(msg=message, title=title)
    except Exception as error:
        print(f"Material graph duplication failed: {error}")
        if not headless:
            lux.getMessageBox(msg=str(error), title=title, type=lux.MESSAGE_BOX_CRITICAL)
        raise


if __name__ == "__main__":
    main()
