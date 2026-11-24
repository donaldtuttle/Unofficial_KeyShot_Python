# -*- coding: utf-8 -*-
"""
KeyShot Get Information | Unified Inspector
Version: 1.2.1
Target: KeyShot 2026.x (supplied 2026 lux module reference)
Mode: read-only, KeyShot GUI (not headless)

1.2.1: animation-name teaching removed. Not a new KeyShot runtime test.

Consolidates user-supplied Information, animation, camera, material, and diagnostic scripts.
Use KeyShot Scripts > Run Script to execute this file.

GUI:
  1. Select information categories, output mode and TXT destination.
  2. Optionally select individual GET operations in each enabled category.
  3. Review results in the scripting console and/or UTF-8 TXT file.

Standard mode does not alter scene state. Opt-in full camera/environment/image-style
inspection temporarily changes the active item and restores it when Python continues.
A native process crash cannot guarantee restoration. Do not use on an unsaved scene.
"""
# kpsa: allow S-FILE-IO -- writes inspection reports
import os
import re
import pprint
from datetime import datetime
import time

import lux

VERSION = "1.2.0"
DIALOG_ID = "kpsa_unified_information_inspector_v120"
EMPTY = "(none)"

# Safety limits for diagnostic runs. The normal path only writes files.
# Explicit opt-in enables setCamera / setActiveEnvironment / setActiveImageStyle,
# with immediate attempt to restore each active selection.
SETTINGS = {
    "node_detail_limit": 80,
    "max_scene_nodes": 700,
    "max_graph_nodes": 120,
    "max_materials": 40,
    "max_report_chars": 18000,
    "console_chars": 1800,
    "allow_slow": False,
    "allow_animation_tree": False,
    "allow_temporary_switch": False,
    "exhaustive": False,
    "output_folder": "",
    "output_base": "KeyShot_Information_Report",
    "library_metadata_name": "",
}
CRASH_TRACE_PATH = None

def checkpoint(stage):
    """Persist the currently entered KeyShot operation, even if KeyShot exits.

    This is an I/O checkpoint, not a try/except for native KeyShot crashes.
    """
    if not CRASH_TRACE_PATH:
        return
    try:
        with open(CRASH_TRACE_PATH, "a", encoding="utf-8") as fh:
            fh.write("{} | {}\n".format(
                datetime.now().isoformat(timespec="seconds"), stage))
            fh.flush()
            os.fsync(fh.fileno())
    except OSError as exc:
        print("[Inspector] Could not write crash trace: {}".format(exc))

def begin_trace(folder):
    global CRASH_TRACE_PATH
    root = folder if isinstance(folder, str) and os.path.isdir(folder) else get_default_directory()
    if not os.path.isdir(root):
        root = os.path.expanduser("~")
    CRASH_TRACE_PATH = os.path.join(root, "KeyShot_Inspector_v1_2_0_Trace.txt")
    try:
        with open(CRASH_TRACE_PATH, "w", encoding="utf-8") as fh:
            fh.write("KeyShot Inspector 1.2.0 - most recent operation is last.\n")
            fh.write("A START without a corresponding END can identify a suspect getter.\n")
            fh.flush()
            os.fsync(fh.fileno())
    except OSError:
        CRASH_TRACE_PATH = None
    checkpoint("SCRIPT START")

def capped_items(values, key, max_default=100):
    """Bound the number of *displayed* records from an API collection."""
    limit = max(1, int(SETTINGS.get(key, max_default)))
    items = list(values or [])
    return items if SETTINGS.get("exhaustive", False) else items[:limit]

def graph_nodes(graph):
    """KeyShot returns its full node list; bound further per-node calls."""
    return capped_items(safe_value(graph.getNodes, []), "max_graph_nodes", 120)

def safe_output(text, label="operation"):
    """Bound output from unexpected long native metadata/string values."""
    if SETTINGS.get("exhaustive", False):
        return text
    limit = max(1000, int(SETTINGS.get("max_report_chars", 18000)))
    if len(text) > limit:
        return (text[:limit] + "\n[TRUNCATED: {} characters omitted in {}. "
                "Reduce categories or raise output limit.]".format(
                    len(text) - limit, label))
    return text

# --- Low-level formatting / defensive readers --------------------------------

def display(value):
    """Render values from KeyShot's mixed Python/native return types."""
    if value is None:
        return EMPTY
    if isinstance(value, str):
        return value if value else EMPTY
    if isinstance(value, (dict, list, tuple, set)):
        return pprint.pformat(value, width=110, sort_dicts=True)
    return str(value)


def try_get(description, getter):
    """Always preserve the report even when one API call is unavailable."""
    try:
        return "{}: {}".format(description, display(getter()))
    except Exception as exc:
        return "{}: [ERROR: {}: {}]".format(
            description, type(exc).__name__, str(exc))


def safe_value(getter, default=None):
    try:
        result = getter()
        return default if result is None else result
    except Exception:
        return default


def rows_from_mapping(mapping, indent="  "):
    if isinstance(mapping, dict):
        if not mapping:
            return [indent + EMPTY]
        lines = []
        for key in sorted(mapping, key=lambda k: str(k)):
            val = mapping[key]
            text = display(val)
            parts = text.splitlines() or [EMPTY]
            lines.append("{}{}: {}".format(indent, key, parts[0]))
            for extra in parts[1:]:
                lines.append(indent + "    " + extra)
        return lines
    return [indent + display(mapping)]


def records(lines):
    return "\n".join(lines)


def api_values(names):
    return records([try_get(label, getter) for label, getter in names])


def enum_names(result):
    """Render lists returned as names, keeping native objects readable."""
    if result is None:
        return EMPTY
    if isinstance(result, dict):
        return records(rows_from_mapping(result))
    if isinstance(result, (list, tuple, set)):
        items = list(result)
        if not items:
            return EMPTY
        cap = max(10, int(SETTINGS.get("max_scene_nodes", 700)))
        shown = items if SETTINGS.get("exhaustive", False) else items[:cap]
        lines = ["  {}. {}".format(i, display(val)) for i, val in enumerate(shown, 1)]
        if not SETTINGS.get("exhaustive", False) and len(items) > cap:
            lines.append("  [TRUNCATED: {} more entries]".format(len(items) - cap))
        return records(lines)
    return display(result)


def list_api(label, getter):
    return "{}:\n{}".format(label, enum_names(getter()))


def node_type(node):
    kinds = {
        lux.NODE_TYPE_GROUP: "Group",
        lux.NODE_TYPE_OBJECT: "Object/Part",
        lux.NODE_TYPE_ANIMATION: "Animation",
        lux.NODE_TYPE_MODEL_SET: "Model Set",
        lux.NODE_TYPE_MODEL: "Model",
        lux.NODE_TYPE_CAMERA: "Camera",
    }
    kind = safe_value(node.getKind)
    return "{} ({})".format(kinds.get(kind, "Unknown"), kind)


def walk_scene():
    """Iterative traversal also reaches children of models and other nodes."""
    root = lux.getSceneTree()
    if root is None:
        return []
    pending = [(root, 0)]
    result = []
    max_nodes = (2**62 if SETTINGS.get("exhaustive", False) else
                 max(1, int(SETTINGS.get("max_scene_nodes", 700))))
    while pending and len(result) < max_nodes:
        node, depth = pending.pop()
        result.append((node, depth))
        kind = safe_value(node.getKind)
        if kind in (lux.NODE_TYPE_GROUP, lux.NODE_TYPE_MODEL, lux.NODE_TYPE_MODEL_SET):
            children = safe_value(node.getChildren, []) or []
            for child in reversed(list(children)):
                pending.append((child, depth + 1))
    if pending:
        checkpoint("NOTE scene tree traversal capped at {} nodes".format(max_nodes))
    return result


def node_label(node):
    return display(safe_value(node.getName, "<unnamed>"))


def fmt_node(node, depth, detail=False):
    prefix = "  " * depth
    items = [prefix + "{} | {}".format(node_label(node), node_type(node))]
    if detail:
        detail_getters = [
            ("ID (session-specific)", node.getID),
            ("Material", node.getMaterial),
            ("Hidden", node.isHidden),
            ("Locked", node.isLocked),
            ("Selected", node.isSelected),
            ("Path", lambda: node.getPath(text=True)),
        ]
        if safe_value(node.getKind) in (lux.NODE_TYPE_GROUP, lux.NODE_TYPE_OBJECT):
            detail_getters.insert(2, ("Render layer", node.getRenderLayer))
        detail_getters.append(("Node metadata", lambda n=node: n.getMetadata()))
        items.extend(prefix + "  " + try_get(label, getter)
                     for label, getter in detail_getters)
    return records(items)


# --- Scene, hierarchy, models --------------------------------------------------

def scene_info():
    return records(rows_from_mapping(lux.getSceneInfo()))


def config_info():
    return records(rows_from_mapping(lux.getActiveConfiguration()))


def metadata_simple():
    return display(lux.getMetaData(format=lux.META_DATA_SIMPLE))


def metadata_xmp():
    return display(lux.getMetaData(format=lux.META_DATA_XMP))


def _color_detail(color, indent="  "):
    if color is None:
        return [indent + "(not available)"]
    lines = [indent + try_get("Name", color.getName),
             indent + try_get("Is multi-color", color.isMultiColor)]
    if safe_value(color.isMultiColor, False):
        lines.append(indent + try_get("Sub-colors", color.getSubColors))
        lines.append(indent + try_get("Active sub-color", color.getActiveSubColor))
    else:
        lines.append(indent + try_get("RGBA (native KeyShot value)", color.getColor))
    return lines


def scene_colors():
    colors = lux.getSceneColors() or []
    lines = ["getSceneColors() raw:", display(colors)]
    if isinstance(colors, dict):
        color_names = list(colors.keys())
    elif isinstance(colors, (tuple, list)):
        color_names = list(colors)
    else:
        color_names = [colors]
    lines.append("getSceneColor(name, multi) - named color inspection:")
    for item in color_names:
        if hasattr(item, "getName"):
            lines.extend(_color_detail(item, "    "))
            continue
        name = str(item)
        if not name:
            continue
        color = safe_value(lambda n=name: lux.getSceneColor(name=n, multi=False))
        if color is None:
            color = safe_value(lambda n=name: lux.getSceneColor(name=n, multi=True))
        lines.append("  {}".format(name))
        if color is None:
            lines.append("    Color instance unavailable for either multi=False or True")
        else:
            lines.extend(_color_detail(color, "    "))
    return records(lines)


def scene_color_lookup():
    """Targeted named lookup, including scenes where the list API is unusual."""
    colors = lux.getSceneColors() or []
    if isinstance(colors, dict):
        names = list(colors)
    elif isinstance(colors, (list, tuple)):
        names = [c.getName() if hasattr(c, "getName") else str(c) for c in colors]
    else:
        names = [str(colors)] if colors else []
    lines = []
    for name in names:
        result = safe_value(lambda n=name: lux.getSceneColor(name=n, multi=False))
        is_multi = False
        if result is None:
            result = safe_value(lambda n=name: lux.getSceneColor(name=n, multi=True))
            is_multi = True
        lines.append("{} | multi={} | {}".format(name, is_multi,
                     display(result.getColor()) if result is not None and
                     not safe_value(result.isMultiColor, False) else
                     display(safe_value(result.getSubColors)) if result is not None else "Unavailable"))
    return records(lines) if lines else EMPTY

def scene_colorways():
    names = lux.getColorways() or []
    lines = ["Colorways ({}):".format(len(names))]
    for name in names:
        lines.append("  " + display(name))
        colorway = safe_value(lambda n=name: lux.getColorway(n))
        if colorway is not None:
            lines.append("    " + try_get("Colorway name", colorway.getName))
            lines.append("    " + try_get("Colors", colorway.getColors))
    return records(lines)


def scene_tree():
    return records([fmt_node(node, depth) for node, depth in walk_scene()])


def detailed_scene_tree():
    return records([fmt_node(node, depth, detail=True)
                    for node, depth in walk_scene()])


def tree_selected():
    root = lux.getSceneTree()
    if root is None:
        return EMPTY
    selected = root.getSelected() or []
    return records([fmt_node(node, 1, detail=True) for node in selected]) \
        if selected else EMPTY


def tree_transforms():
    lines = []
    for node, depth in walk_scene():
        prefix = "  " * depth
        lines.append(prefix + "{} | {}".format(node_label(node), node_type(node)))
        for title, getter in [
            ("Local transform", lambda n=node: n.getTransform(world=False)),
            ("World transform", lambda n=node: n.getTransform(world=True)),
            ("World center", lambda n=node: n.getCenter(world=True)),
            ("World bounding box", lambda n=node: n.getBoundingBox(world=True)),
        ]:
            lines.append(prefix + "  " + try_get(title, getter))
    return records(lines)


def json_scene_tree():
    return display(lux.dumpTree())


def active_model_sets():
    return list_api("Active model sets", lux.getModelSets)


def model_set_tree():
    """Grouped hierarchy with all descendants, rather than model set names alone."""
    lines = []
    for node, depth in walk_scene():
        if safe_value(node.isModelSet, False):
            lines.append("Model set: {}".format(node_label(node)))
            lines.append("  " + try_get("Model set ID", node.getID))
            pending = [(child, 1) for child in reversed(safe_value(node.getChildren, []) or [])]
            max_nodes = (2**62 if SETTINGS.get("exhaustive", False) else
                 max(1, int(SETTINGS.get("max_scene_nodes", 700))))
            count = 0
            while pending and count < max_nodes:
                current, inner = pending.pop()
                count += 1
                lines.append("{}{} | {} | path={}".format(
                    "  " * inner, node_label(current), node_type(current),
                    display(safe_value(lambda n=current: n.getPath(text=True)))))
                if safe_value(current.getKind) in (
                        lux.NODE_TYPE_GROUP, lux.NODE_TYPE_MODEL, lux.NODE_TYPE_MODEL_SET):
                    children = safe_value(current.getChildren, []) or []
                    pending.extend((c, inner + 1) for c in reversed(children))
            if pending:
                lines.append("  [TRUNCATED: model set hierarchy capped at {} nodes]".format(max_nodes))
    return records(lines) if lines else EMPTY


def scene_node_names():
    return records([node_label(n) for n, _d in walk_scene()])


def scene_node_names_types():
    return records(["{} | {}".format(node_label(n), node_type(n))
                    for n, _d in walk_scene()])


def scene_node_paths():
    return records([try_get(node_label(n), lambda n=n: n.getPath(text=True))
                    for n, _d in walk_scene()])


def scene_node_collections():
    root = lux.getSceneTree()
    if root is None:
        return EMPTY
    lines = []
    for label, getter in [
        ("Hidden nodes (recursive)", root.getHidden),
        ("Locked nodes (recursive)", root.getLocked),
        ("Deleted nodes (recursive)", root.getDeleted),
        ("Selected nodes (recursive)", root.getSelected),
    ]:
        lines.append(label + ":")
        try:
            nodes = getter() or []
            lines.extend("  " + node_label(n) for n in nodes)
            if not nodes:
                lines.append("  " + EMPTY)
        except Exception as e:
            lines.append("  [ERROR: {}: {}]".format(type(e).__name__, e))
    return records(lines)


def scene_node_metadata():
    lines = []
    for node, _d in walk_scene():
        try:
            data = node.getMetadata()
            if data:
                lines.append("{} (ID={}): {}".format(node_label(node),
                             display(safe_value(node.getID)), display(data)))
        except Exception as e:
            lines.append("{}: [ERROR: {}: {}]".format(node_label(node), type(e).__name__, e))
    return records(lines) if lines else "No node metadata reported"


def node_parent_relationships():
    lines = []
    for node, _d in walk_scene():
        parent = safe_value(node.getParent)
        lines.append("{} -> {}".format(node_label(node),
                      node_label(parent) if parent is not None else "(scene root)"))
    return records(lines) if lines else EMPTY

def object_ids():
    return list_api("Scene object IDs (session-specific)", lux.getObjects)


def material_mapping():
    return records(rows_from_mapping(lux.getMaterialMapping()))


def render_layers():
    return list_api("Render layers", lux.getRenderLayers)


# --- Material graph / shaders --------------------------------------------------

def material_names():
    return list_api("Currently used scene materials", lux.getSceneMaterials)


def get_graphs():
    """Yield scene material names and graphs, including unavailable graphs."""
    materials = lux.getSceneMaterials() or []
    for name in capped_items(materials, "max_materials", 40):
        try:
            graph = lux.getMaterialGraph(name)
            yield name, graph, None
        except Exception as exc:
            yield name, None, "{}: {}".format(type(exc).__name__, exc)


def graph_outline():
    lines = []
    for name, graph, problem in get_graphs():
        lines.append("Material: {}".format(display(name)))
        if problem or graph is None:
            lines.append("  Unavailable graph: {}".format(problem or "None"))
            continue
        lines.append("  " + try_get("Material name", graph.getMaterialName))
        roots = safe_value(graph.getMaterialNodes, []) or []
        lines.append("  Root/sub-material nodes: {}".format(len(roots)))
        for root in roots:
            lines.append("    {} [{}]".format(
                safe_value(root.getName, "<unnamed>"),
                display(safe_value(root.getType, "?"))))
        nodes = graph_nodes(graph)
        lines.append("  Graph node count: {}".format(len(nodes)))
        for n in nodes:
            lines.append("    {} | type={} | ID={}".format(
                display(safe_value(n.getName)),
                display(safe_value(n.getType)),
                display(safe_value(n.getID))))
    return records(lines) if lines else EMPTY


def parameter_value(parameter):
    """Never read a pure shader parameter; do not guess when isPure fails.

    Per KeyShot 2026 ShaderParameter, getValue() is invalid for pure params.
    Lookup of the method itself is inside try/except for unexpected objects.
    """
    try:
        pure = parameter.isPure()
    except Exception as exc:
        return "[UNREADABLE: isPure() {}: {}]".format(type(exc).__name__, exc)
    if pure:
        return "<pure/connection parameter>"
    try:
        return display(parameter.getValue())
    except Exception as exc:
        return "[ERROR: unreadable {}: {}]".format(type(exc).__name__, exc)


def graph_parameters():
    lines = []
    for name, graph, problem in get_graphs():
        lines.append("Material: {}".format(display(name)))
        if problem or graph is None:
            lines.append("  Unavailable graph: {}".format(problem or "None"))
            continue
        for node in graph_nodes(graph):
            lines.append("  Shader: {} | {} | ID {}".format(
                display(safe_value(node.getName)),
                display(safe_value(node.getType)),
                display(safe_value(node.getID))))
            for param in safe_value(node.getParameters, []) or []:
                try:
                    lines.append("    {} [{}; type {}] = {}".format(
                        param.getName(), param.getDisplayName(),
                        param.getType(), parameter_value(param)))
                except Exception as exc:
                    lines.append("    [Parameter error: {}]".format(exc))
    return records(lines) if lines else EMPTY


def graph_connections():
    lines = []
    for name, graph, problem in get_graphs():
        lines.append("Material: {}".format(display(name)))
        if problem or graph is None:
            lines.append("  Unavailable graph: {}".format(problem or "None"))
            continue
        found = False
        for node in graph_nodes(graph):
            for edge in safe_value(node.getOutputEdges, []) or []:
                found = True
                source = safe_value(edge.getSourceNode)
                target = safe_value(edge.getTargetNode)
                lines.append("  {} -> {} | Edge ID {} | Enabled {}".format(
                    node_label(source) if source is not None else EMPTY,
                    node_label(target) if target is not None else EMPTY,
                    display(safe_value(edge.getID)),
                    display(safe_value(edge.isEnabled))))
        if not found:
            lines.append("  No graph edges reported")
    return records(lines) if lines else EMPTY


def multi_materials():
    lines = []
    for name in lux.getSceneMaterials() or []:
        mm = safe_value(lambda n=name: lux.getMultiMaterial(n))
        if mm is None:
            continue
        lines.append("Multi-material: {}".format(display(name)))
        lines.append("  " + try_get("Multi-material name", mm.getName))
        lines.append("  " + try_get("Active sub-material", mm.getActiveMaterial))
        lines.append("  " + try_get("Sub-materials", mm.getSubMaterials))
    return records(lines) if lines else EMPTY


# --- Cameras: only active camera settings can be safely read without switching

def camera_list():
    return list_api("Saved scene cameras", lux.getCameras)


def camera_active():
    return api_values([
        ("Active camera", lux.getCamera),
        ("Lens dictionary", lux.getCameraLens),
        ("Spherical camera angles (degrees)", lux.getSphericalCamera),
    ])


def camera_geometry():
    return api_values([
        ("Camera position", lux.getCameraPosition),
        ("Camera direction", lux.getCameraDirection),
        ("Camera look-at", lux.getCameraLookAt),
        ("Camera pivot", lux.getCameraPivot),
        ("Camera up vector", lux.getCameraUp),
        ("Camera distance", lux.getCameraDistance),
    ])


def camera_optics():
    return api_values([
        ("Lens", lux.getCameraLens),
        ("Field of view", lux.getCameraFieldOfView),
        ("Focal length", lux.getCameraFocalLength),
    ])




# --- Complete saved-camera / environment / image-style inspections ------------

def _traced_properties(scope, properties):
    """Trace each actual native getter, not only the parent report operation."""
    result = []
    for label, getter in properties:
        checkpoint("{} GET START: {}".format(scope, label))
        result.append("    " + try_get(label, getter))
        checkpoint("{} GET END: {}".format(scope, label))
    return result


def _inspect_all_saved_items(kind, names_getter, active_name_getter, activate,
                             properties_getter):
    """Collect every saved item using a temporary active-state switch.

    The documented 2026 API exposes detailed getters for the active item only.
    This routine NEVER creates or saves a camera/environment/style. Switching
    is opt-in and each attempt is restored in finally (including exceptions).
    A native KeyShot process crash cannot execute Python's finally block.
    """
    if not SETTINGS.get("allow_temporary_switch", False):
        return ("[SKIPPED SAFELY] Inspecting every saved {} needs temporarily "
                "selecting each item. Tick 'Allow temporary camera/environment/"
                "image-style switching' in the main dialog. Current active-item "
                "reporters remain available without it.").format(kind)

    checkpoint("{} INVENTORY START".format(kind.upper()))
    try:
        initial = active_name_getter()
    except Exception as exc:
        return "[ERROR: Cannot identify initial {} for restoration: {}]".format(
            kind, exc)
    if not isinstance(initial, str) or not initial:
        return "[ERROR: Cannot safely restore {}: initial name not readable]".format(kind)

    try:
        names = names_getter() or []
    except Exception as exc:
        return "[ERROR: Cannot list saved {}: {}]".format(kind, exc)

    if not isinstance(names, (list, tuple)):
        return "[ERROR: Unexpected {} list shape: {}]".format(kind, type(names).__name__)

    result = [
        "Saved {} count: {}".format(kind, len(names)),
        "Original active {}: {}".format(kind, initial),
        "Each selection is restored immediately after inspection.",
        "An unhandled native KeyShot crash can interrupt restoration.",
    ]

    for index, name in enumerate(names, 1):
        result.append("\n  {} {}: {}".format(kind.title(), index, display(name)))
        if not isinstance(name, str) or not name:
            result.append("    [ERROR: Invalid saved-item name; skipped]")
            continue

        switching_attempted = name != initial
        restoration_failed = False
        try:
            if switching_attempted:
                checkpoint("{} SWITCH START: {}".format(kind.upper(), name))
                activate(name)
                checkpoint("{} SWITCH END: {}".format(kind.upper(), name))
            checkpoint("{} VERIFY ACTIVE START: {}".format(kind.upper(), name))
            actual = active_name_getter()
            checkpoint("{} VERIFY ACTIVE END: {}".format(kind.upper(), name))
            if actual != name:
                raise ValueError(
                    "Selection mismatch: expected {!r}, active {!r}".format(
                        name, actual))
            checkpoint("{} READ START: {}".format(kind.upper(), name))
            try:
                result.extend(_traced_properties(
                    "{} [{}]".format(kind.upper(), name), properties_getter()))
            except Exception as exc:
                result.append(
                    "    [ERROR: {} getter setup failed: {}]".format(kind, exc))
            checkpoint("{} READ END: {}".format(kind.upper(), name))
        except Exception as exc:
            result.append("    [ERROR: Selecting or reading {} failed: {}]".format(
                name, exc))
        finally:
            if switching_attempted:
                checkpoint("{} RESTORE START: {}".format(kind.upper(), initial))
                try:
                    activate(initial)
                    restored = active_name_getter()
                    if restored == initial:
                        result.append("    [RESTORED] Active {}: {}".format(kind, initial))
                    else:
                        restoration_failed = True
                        result.append(
                            "    [ERROR: RESTORE FAILED: {} active is {!r}, "
                            "expected {!r}]".format(kind, restored, initial))
                except Exception as exc:
                    restoration_failed = True
                    result.append(
                        "    [ERROR: RESTORE FAILED for {}: {}]".format(kind, exc))
                checkpoint("{} RESTORE END: {}".format(kind.upper(), initial))
        if restoration_failed:
            result.append(
                "[STOPPED] {} inventory aborted to avoid further state changes "
                "after restoration failure.".format(kind))
            checkpoint("{} ABORT: restoration failed".format(kind.upper()))
            break

    # Attempt a final verification even if one per-item restoration failed.
    try:
        if active_name_getter() != initial:
            checkpoint("{} FINAL RESTORE START".format(kind.upper()))
            activate(initial)
            checkpoint("{} FINAL RESTORE END".format(kind.upper()))
        result.append("Final active {}: {}".format(kind, active_name_getter()))
    except Exception as exc:
        result.append("[ERROR: Final {} restoration failed: {}]".format(kind, exc))
    return records(result)


def _camera_all_properties():
    return [
        ("Name", lux.getCamera),
        ("Lens information", lux.getCameraLens),
        ("Field of view (degrees)", lux.getCameraFieldOfView),
        ("Focal length (mm)", lux.getCameraFocalLength),
        ("Position (world)", lux.getCameraPosition),
        ("Direction", lux.getCameraDirection),
        ("Up vector", lux.getCameraUp),
        ("Look-at point", lux.getCameraLookAt),
        ("Pivot point", lux.getCameraPivot),
        ("Distance to pivot/look-at", lux.getCameraDistance),
        ("Spherical angles (degrees)", lux.getSphericalCamera),
        ("Unsaved changes", lux.isCameraUnsaved),
    ]


def all_saved_camera_details():
    """Guard unsaved camera changes before switching any camera."""
    if not SETTINGS.get("allow_temporary_switch", False):
        return _inspect_all_saved_items(
            "camera", lux.getCameras, lux.getCamera,
            lambda name: lux.setCamera(name),
            _camera_all_properties)
    checkpoint("CAMERA UNSAVED CHECK START")
    try:
        unsaved = lux.isCameraUnsaved()
    except Exception as exc:
        return ("[SKIPPED SAFELY] Could not verify camera save state: {}. "
                "No camera switching occurred.").format(exc)
    checkpoint("CAMERA UNSAVED CHECK END")
    if unsaved:
        return (
            "[SKIPPED SAFELY] The current camera has UNSAVED changes. "
            "Switching cameras could discard them. Save the camera or "
            "revert changes before running all-camera inspection. "
            "No camera switching occurred.")
    return _inspect_all_saved_items(
        "camera", lux.getCameras, lux.getCamera,
            lambda name: lux.setCamera(name),
        _camera_all_properties)


def _active_env_name():
    env = lux.getActiveEnvironment()
    if env is None:
        raise ValueError("No active environment")
    return env.getName()


def _all_env_properties():
    env = lux.getActiveEnvironment()
    if env is None:
        raise ValueError("No active environment")
    return [
        ("Name", env.getName),
        ("Background color", env.getBackgroundColor),
        ("Backplate image", env.getBackplateImage),
        ("Brightness", env.getBrightness),
        ("Flatten ground", env.getFlattenGround),
        ("Ground reflections", env.getGroundReflections),
        ("Ground shadows", env.getGroundShadows),
        ("Ground shadows color", env.getGroundShadowsColor),
        ("Ground size", env.getGroundSize),
        ("Height", env.getHeight),
        ("Lighting environment image", env.getLightingEnvironment),
        ("Occlusion ground shadows", env.getOcclusionGroundShadows),
        ("Rotation", env.getRotation),
        ("Size", env.getSize),
    ]


def all_saved_environment_details():
    return _inspect_all_saved_items(
        "environment", lux.getEnvironments, _active_env_name,
        lambda name: lux.setActiveEnvironment(name), _all_env_properties)


def _active_image_style_name():
    sty = lux.getActiveImageStyle()
    if sty is None:
        raise ValueError("No active image style")
    return sty.getName()


def _all_style_properties():
    sty = lux.getActiveImageStyle()
    if sty is None:
        raise ValueError("No active image style")
    values = [
        ("Name", sty.getName),
        ("Kind", sty.getKind),
        ("Bloom", sty.getBloom),
        ("Chromatic aberration", sty.getChromaticAberration),
        ("Denoise", sty.getDenoise),
        ("Vignette", sty.getVignette),
    ]
    if safe_value(sty.getKind) == lux.IMAGE_STYLE_PHOTOGRAPHIC:
        values.extend([("Photographic color", sty.getColor),
                       ("Photographic curve", sty.getCurve)])
    else:
        values.extend([("Photographic color", lambda: "N/A (Basic style)"),
                       ("Photographic curve", lambda: "N/A (Basic style)")])
    return values


def all_saved_image_style_details():
    return _inspect_all_saved_items(
        "image style", lux.getImageStyles, _active_image_style_name,
        lambda name: lux.setActiveImageStyle(name), _all_style_properties)


def export_native_scene_metadata():
    """Export the unmodified KeyShot simple and XML metadata payloads.

    No JSON conversion, field reduction, or unnecessary KeyShot GUI dialogs.
    Writes separately named .metadata and .xmp files, never overwrites.
    """
    folder = SETTINGS.get("output_folder", "")
    if not isinstance(folder, str) or not os.path.isdir(folder):
        return "[ERROR: Choose an existing output folder to export metadata]"
    stem = os.path.splitext(safe_filename(SETTINGS.get("output_base", "")))[0]
    lines = []
    for title, fmt, ext in [
        ("KeyShot simple metadata", lux.META_DATA_SIMPLE, ".metadata"),
        ("KeyShot XMP/XML metadata", lux.META_DATA_XMP, ".xmp"),
    ]:
        checkpoint("NATIVE METADATA GET START: " + ext)
        try:
            raw = lux.getMetaData(format=fmt)
            if raw is None:
                raise ValueError("KeyShot returned no metadata")
            if not isinstance(raw, str):
                raw = str(raw)
            path = non_overwriting_path(folder, stem + ext)
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(raw)
                handle.flush()
                os.fsync(handle.fileno())
            lines.append("{} saved: {}".format(title, path))
            lines.append("  Characters: {}".format(len(raw)))
        except Exception as exc:
            lines.append("[ERROR: {} export failed: {}]".format(title, exc))
        checkpoint("NATIVE METADATA GET END: " + ext)
    return records(lines)

# --- Environment, image styles, studios ---------------------------------------

def environments_list():
    return list_api("Saved scene environments", lux.getEnvironments)


def active_environment():
    env = lux.getActiveEnvironment()
    if env is None:
        return EMPTY
    return api_values([
        ("Name", env.getName),
        ("Lighting environment", env.getLightingEnvironment),
        ("Background color", env.getBackgroundColor),
        ("Backplate image", env.getBackplateImage),
        ("Brightness", env.getBrightness),
        ("Rotation", env.getRotation),
        ("Height", env.getHeight),
        ("Size", env.getSize),
        ("Ground size", env.getGroundSize),
        ("Ground reflections", env.getGroundReflections),
        ("Ground shadows", env.getGroundShadows),
        ("Ground shadows color", env.getGroundShadowsColor),
        ("Occlusion ground shadows", env.getOcclusionGroundShadows),
        ("Flatten ground", env.getFlattenGround),
    ])


def image_style_names():
    return list_api("Saved image styles", lux.getImageStyles)


def active_image_style():
    style = lux.getActiveImageStyle()
    if style is None:
        return EMPTY
    rows = [
        ("Name", style.getName),
        ("Kind", style.getKind),
        ("Bloom", style.getBloom),
        ("Chromatic aberration", style.getChromaticAberration),
        ("Denoise", style.getDenoise),
        ("Vignette", style.getVignette),
    ]
    kind = safe_value(style.getKind)
    if kind == lux.IMAGE_STYLE_PHOTOGRAPHIC:
        rows += [("Color", style.getColor), ("Curve", style.getCurve)]
    else:
        rows += [("Color", lambda: "N/A (Basic image style)"),
                 ("Curve", lambda: "N/A (Basic image style)")]
    return api_values(rows)

def studios_list():
    return list_api("Saved studios", lux.getStudios)


def active_studio():
    return try_get("Active studio", lux.getActiveStudio)


def studios_detail():
    lines = []
    for name in lux.getStudios() or []:
        lines.append("Studio: {}".format(display(name)))
        try:
            studio = lux.getStudio(name)
            if studio is None:
                lines.append("  Studio instance unavailable")
                continue
            for label, getter in [
                ("Name", studio.getName),
                ("Camera", studio.getCamera),
                ("Environment", studio.getEnvironment),
                ("Image style", studio.getImageStyle),
                ("Model sets", studio.getModelSets),
                ("Multi-materials", studio.getMultiMaterials),
                ("Multi-materials enabled", studio.isMultiMaterialsEnabled),
            ]:
                lines.append("  " + try_get(label, getter))
        except Exception as exc:
            lines.append("  [ERROR: {}]".format(exc))
    return records(lines) if lines else EMPTY


# --- Rendering, animation, resource folders, system ----------------------------

def render_options():
    opts = lux.getRenderOptions()
    if opts is None:
        return EMPTY
    return records(rows_from_mapping(opts.getDict()))


def render_engine():
    return try_get("Active render engine", lux.getRenderEngine)


def lighting_current():
    return try_get("Active lighting preset", lux.getLightingPreset)


def lighting_presets():
    return list_api("Available lighting presets", lux.getLightingPresets)


def render_resolution_locks():
    return api_values([
        ("Keep aspect ratio", lux.getKeepAspectRatio),
        ("Resolution locked", lux.getLockResolution),
    ])


def animation_status():
    """Only basic animation status GETs previously worked in the user's report.

    Each call gets its own flushed checkpoint so a fatal native crash can
    be attributed to a specific API function rather than the whole group.
    No frame/time setters or animation-object API calls are used.
    """
    items = [
        ("getAnimationInfo", "Animation info (duration / frames)"),
        ("getAnimationTime", "Animation time (seconds)"),
        ("getAnimationFrame", "Animation frame"),
    ]
    lines = []
    for method_name, label in items:
        checkpoint("ANIMATION STATUS START: lux." + method_name + "()")
        method = getattr(lux, method_name, None)
        if callable(method):
            lines.append(try_get(label, method))
        else:
            lines.append("{}: [UNAVAILABLE]".format(label))
        checkpoint("ANIMATION STATUS END: lux." + method_name + "()")
    return records(lines)


def external_files():
    return list_api("External files referenced by scene", lux.getExternalFiles)


FOLDERS = [
    ("Resource root", "FOLDER_RESOURCE_ROOT"),
    ("Animations", "FOLDER_ANIMATIONS"),
    ("Backplates", "FOLDER_BACKPLATES"),
    ("Colors", "FOLDER_COLORS"),
    ("Config root", "FOLDER_CONFIG_ROOT"),
    ("Downloads", "FOLDER_DOWNLOADS"),
    ("Environments", "FOLDER_ENVIRONMENTS"),
    ("External plugins", "FOLDER_EXTERNAL_PLUGIN"),
    ("Favorites", "FOLDER_FAVORITES"),
    ("Materials", "FOLDER_MATERIALS"),
    ("Material templates", "FOLDER_MATERIAL_TEMPLATES"),
    ("Models", "FOLDER_MODELS"),
    ("Scenes", "FOLDER_SCENES"),
    ("Screenshots", "FOLDER_SCREENSHOTS"),
    ("Scripts", "FOLDER_SCRIPTS"),
    ("Textures", "FOLDER_TEXTURES"),
]


def resource_folders():
    lines = []
    for title, constant in FOLDERS:
        lines.append(try_get(title, lambda c=constant: lux.getKeyShotFolder(
            getattr(lux, c))))
    return records(lines)


def resource_models():
    """Opt-in bounded disk scan. Does not run in default safe mode."""
    if not SETTINGS.get("allow_slow", False):
        return "[SKIPPED] Resource Models scans the filesystem. Enable 'Allow slow scans' first."
    folder = lux.getKeyShotFolder(lux.FOLDER_MODELS)
    if not folder or not os.path.isdir(folder):
        return "Model folder not found: {}".format(display(folder))
    items = []
    directories_seen = 0
    max_directories, max_matches = 150, 300
    for parent, directories, filenames in os.walk(folder):
        directories_seen += 1
        directories.sort()
        for filename in sorted(filenames):
            if filename.lower().endswith((".bip", ".ksp")):
                items.append(os.path.relpath(os.path.join(parent, filename), folder))
                if len(items) >= max_matches:
                    break
        if directories_seen >= max_directories or len(items) >= max_matches:
            break
    return ("BIP/KSP model files (first {} matches; visited <= {} directories):\n"
            "{}\n[Scan intentionally limited]".format(
                len(items), directories_seen, enum_names(items)))


def material_templates():
    return list_api("Material templates", lux.getMaterialTemplates)


def library_inventory():
    """Opt-in only: the 2026 API explicitly warns resource loading can block."""
    if not SETTINGS.get("allow_slow", False):
        return ("[SKIPPED] KeyShot getLibrary* calls can block while loading "
                "resource libraries. Enable 'Allow slow scans' to run them.")
    sections = []
    for label, getter in [
        ("Library materials", lux.getLibraryMaterials),
        ("Library textures", lux.getLibraryTextures),
        ("Library colors", lux.getLibraryColors),
        ("Library environments", lux.getLibraryEnvironments),
        ("Library backplates", lux.getLibraryBackplates),
    ]:
        checkpoint("LIBRARY START: {}".format(label))
        try:
            items = getter() or []
            first = capped_items(items, "max_graph_nodes", 120)
            sections.append("{} (showing {} of {}):\n{}".format(
                label, len(first), len(items), enum_names(first)))
        except Exception as exc:
            sections.append("{}: [ERROR: {}]".format(label, exc))
        checkpoint("LIBRARY END: {}".format(label))
    return "\n\n".join(sections)


def import_options():
    return records(rows_from_mapping(lux.getImportOptions()))


def versions():
    return api_values([
        ("KeyShot display version", lux.getKeyShotDisplayVersion),
        ("KeyShot full version", lux.getKeyShotVersion),
        ("OS", lux.getOS),
    ])


def system_info():
    return records(rows_from_mapping(lux.getSystemInfo()))



# --- KeyShot 2026 extended read-only information and diagnostics ---------------
# These reporters intentionally use only getters, predicates and Python output.
# In particular they NEVER set the active camera/frame or mutate a material graph.

def limited_nodes():
    limit = max(1, int(SETTINGS.get("node_detail_limit", 80)))
    all_nodes = walk_scene()
    if SETTINGS.get("exhaustive", False):
        return all_nodes, 0
    return all_nodes[:limit], len(all_nodes) - min(len(all_nodes), limit)


def type_info(shader):
    """2026 ShaderNode.getType() yields dict {'name', 'display_name'}."""
    value = safe_value(shader.getType, {})
    if isinstance(value, dict):
        return str(value.get("name", "")), str(value.get("display_name", ""))
    return str(value), str(value)


def shader_id(node):
    return safe_value(node.getID)


def shader_title(node):
    code, friendly = type_info(node)
    return "{} [type={} / {}, ID={}]".format(
        display(safe_value(node.getName)), code, friendly,
        display(shader_id(node)))


def graph_roots(graph):
    roots = safe_value(graph.getMaterialNodes, []) or []
    primary = safe_value(graph.getRoot)
    if primary is not None and primary not in roots:
        roots = [primary] + roots
    return roots


def edge_target_parameter(edge):
    """Infer edge target socket via ShaderNode.getInputEdge(param).

    Multi-edge sockets may not expose every edge through getInputEdge; in
    those cases report 'unresolved', not a fabricated target parameter.
    """
    target = safe_value(edge.getTargetNode)
    if target is None:
        return "(no target)"
    eid = safe_value(edge.getID)
    for param in safe_value(target.getParameters, []) or []:
        pname = safe_value(param.getName)
        if not pname:
            continue
        candidate = safe_value(lambda p=pname: target.getInputEdge(p))
        if candidate is not None and safe_value(candidate.getID) == eid:
            return str(pname)
    return "(multi-input/unresolved)"


def object_materials():
    """Use 2026 getObjectMaterial(obj), accepting scalar or list of IDs."""
    ids = lux.getObjects() or []
    if not ids:
        return "No object IDs available"
    total = len(ids)
    ids = list(ids)
    if not SETTINGS.get("exhaustive", False):
        ids = ids[:min(100, int(SETTINGS.get("max_scene_nodes", 700)))]
    # Smaller batches prevent passing thousands of native IDs in one call.
    raw = lux.getObjectMaterial(obj=ids)
    lines = ["Object IDs inspected: {} / {} (bounded bulk call)".format(len(ids), total),
             "getObjectMaterial(obj=[IDs]): {}".format(display(raw))]
    # Mapping supplies object-to-material association with stable per-row text.
    mapping = safe_value(lux.getMaterialMapping, {})
    lines.append("getMaterialMapping():")
    lines.extend(rows_from_mapping(mapping))
    return records(lines)


def graph_getter_lookup_tests():
    """Read-only class-level lookup getters using existing valid IDs/types."""
    lines = []
    for mat, graph, error in get_graphs():
        lines.append("Material: {}".format(mat))
        if graph is None:
            lines.append("  Graph unavailable: {}".format(error or EMPTY))
            continue
        roots = graph_roots(graph)
        lines.append("  " + try_get("Primary root", graph.getRoot))
        nodes = graph_nodes(graph)
        if nodes:
            node = nodes[0]
            nid = safe_value(node.getID)
            if nid is not None:
                lines.append("  " + try_get("getNodeFromID({})".format(nid),
                                                lambda n=nid: graph.getNodeFromID(n)))
            shader_type_name, _name = type_info(node)
            # Only actual runtime type names, not arbitrary invented strings.
            if shader_type_name and shader_type_name != "__root":
                lines.append("  " + try_get("getNodesFromType({})".format(shader_type_name),
                                                lambda t=shader_type_name: graph.getNodesFromType(t)))
            elif len(nodes) > 1:
                typ, _ = type_info(nodes[1])
                if typ:
                    lines.append("  " + try_get("getNodesFromType({})".format(typ),
                                                lambda t=typ: graph.getNodesFromType(t)))
            lines.append("  " + try_get("ShaderNode.getParameters", node.getParameters))
            params = safe_value(node.getParameters, []) or []
            if params:
                pname = safe_value(params[0].getName)
                if pname:
                    lines.append("  " + try_get("ShaderNode.getParameter({})".format(pname),
                                                lambda p=pname: node.getParameter(p)))
            edges = safe_value(node.getOutputEdges, []) or []
            if not edges:
                for n in nodes[1:]:
                    edges = safe_value(n.getOutputEdges, []) or []
                    if edges:
                        node = n
                        break
            if edges:
                eid = safe_value(edges[0].getID)
                if eid is not None:
                    lines.append("  " + try_get("getEdgeFromID({})".format(eid),
                                                lambda e=eid: graph.getEdgeFromID(e)))
    return records(lines) if lines else EMPTY


def graph_parameter_connections():
    """Full 2026 parameter-to-edge map, including connected parameter values."""
    lines = []
    for mat, graph, error in get_graphs():
        lines.append("Material: {}".format(mat))
        if graph is None:
            lines.append("  Unavailable graph: {}".format(error or EMPTY))
            continue
        for node in graph_nodes(graph):
            lines.append("  {}".format(shader_title(node)))
            for p in safe_value(node.getParameters, []) or []:
                pname = safe_value(p.getName)
                if pname is None:
                    continue
                ptype = safe_value(p.getType)
                pure = safe_value(lambda q=p: q.isPure(), True)
                edge = safe_value(lambda n=node, nm=pname: n.getInputEdge(nm))
                src = safe_value(edge.getSourceNode) if edge is not None else None
                literal = "<pure>" if pure else parameter_value(p)
                lines.append("    {} [{}] (type={} pure={}) literal={}".format(
                    pname, display(safe_value(p.getDisplayName)), ptype, pure, literal))
                if edge is not None:
                    lines.append("      <- {} | edge={} enabled={}".format(
                        shader_title(src) if src is not None else "(unknown source)",
                        display(safe_value(edge.getID)),
                        display(safe_value(edge.isEnabled))))
                if not pure and ptype in (
                    lux.PARAMETER_TYPE_COLOR, lux.PARAMETER_TYPE_COLORALPHA):
                    lines.append("      " + try_get("getColor() native", lambda q=p: q.getColor()))
            in_edges = safe_value(node.getInputEdges, []) or []
            out_edges = safe_value(node.getOutputEdges, []) or []
            lines.append("    input edges={}, output edges={}".format(
                len(in_edges), len(out_edges)))
    return records(lines) if lines else EMPTY


def graph_connections_detailed():
    """All shader edges with socket name and disabled status where available."""
    lines = []
    for mat, graph, error in get_graphs():
        lines.append("Material: {}".format(mat))
        if graph is None:
            lines.append("  Graph unavailable: {}".format(error or EMPTY))
            continue
        seen = set()
        for node in graph_nodes(graph):
            for edge in safe_value(node.getOutputEdges, []) or []:
                eid = safe_value(edge.getID)
                if eid is not None and eid in seen:
                    continue
                seen.add(eid)
                src = safe_value(edge.getSourceNode)
                tgt = safe_value(edge.getTargetNode)
                lines.append("  {} -> {} . {} [edge={}, enabled={}]".format(
                    shader_title(src) if src is not None else "(missing)",
                    shader_title(tgt) if tgt is not None else "(missing)",
                    edge_target_parameter(edge), display(eid),
                    display(safe_value(edge.isEnabled))))
        if not seen:
            lines.append("  No output edges found")
    return records(lines) if lines else EMPTY


def _reachable_shader_ids(graph):
    """Traverse backwards from all root sockets; do not change the graph."""
    pending = list(graph_roots(graph))
    reachable = set()
    while pending:
        n = pending.pop()
        if n is None:
            continue
        nid = shader_id(n)
        if nid in reachable:
            continue
        reachable.add(nid)
        for edge in safe_value(n.getInputEdges, []) or []:
            src = safe_value(edge.getSourceNode)
            if src is not None:
                pending.append(src)
    return reachable


def disconnected_shader_nodes():
    """Conservative diagnostics, never a command to delete nodes."""
    lines = []
    summary = 0
    guarded_types = {
        "lux_const_color",
        getattr(lux, "SHADER_TYPE_CURVE_FADE", "animation_curve"),
        getattr(lux, "SHADER_TYPE_COLOR_FADE", "animation_color"),
    }
    for mat, graph, error in get_graphs():
        if graph is None:
            lines.append("{}: [ERROR: graph unavailable: {}]".format(mat, error or EMPTY))
            continue
        roots = {shader_id(n) for n in graph_roots(graph)}
        reachable = _reachable_shader_ids(graph)
        candidates = []
        for node in graph_nodes(graph):
            nid = shader_id(node)
            code, _ = type_info(node)
            if nid in roots or code in guarded_types:
                continue
            inbound = len(safe_value(node.getInputEdges, []) or [])
            outbound = len(safe_value(node.getOutputEdges, []) or [])
            if nid not in reachable:
                status = "isolated (zero input/output)" if not (inbound or outbound) \
                    else "disconnected branch (not reachable from material roots)"
                candidates.append((node, status, inbound, outbound))
        if candidates:
            lines.append("Material: {}".format(mat))
            summary += len(candidates)
            for n, status, inc, outc in candidates:
                lines.append("  POTENTIALLY UNUSED: {} | {} | in={} out={}".format(
                    shader_title(n), status, inc, outc))
    lines.insert(0, "Potentially disconnected nodes: {}. Not a deletion recommendation.".format(summary))
    return records(lines)


GEO_TYPES = {
    getattr(lux, "SHADER_TYPE_FUZZ", "lux_fuzz"),
    getattr(lux, "SHADER_TYPE_FLAKES", "lux_flakes"),
    getattr(lux, "SHADER_TYPE_BUBBLES", "lux_bubbles"),
    getattr(lux, "SHADER_TYPE_DISPLACE", "lux_displace"),
}


def geometry_node_report():
    lines = []
    total = 0
    for mat, graph, error in get_graphs():
        if graph is None:
            lines.append("{}: [ERROR: {}]".format(mat, error or EMPTY))
            continue
        for n in graph_nodes(graph):
            code, _ = type_info(n)
            if code not in GEO_TYPES:
                continue
            total += 1
            outbound = safe_value(n.getOutputEdges, []) or []
            lines.append("Material: {} | {}".format(mat, shader_title(n)))
            lines.append("  Output edges: {}; status: {}".format(len(outbound),
                "connected" if outbound else "no outputs (potentially inactive)"))
            for edge in outbound:
                lines.append("    -> {} | socket={} | enabled={}".format(
                    shader_title(safe_value(edge.getTargetNode))
                    if safe_value(edge.getTargetNode) is not None else EMPTY,
                    edge_target_parameter(edge),
                    display(safe_value(edge.isEnabled))))
            lines.append("  Input edges: {}".format(
                len(safe_value(n.getInputEdges, []) or [])))
    lines.insert(0, "Geometry shader nodes: {}".format(total))
    return records(lines)


def material_labels_report():
    """Read root labels using documented shader-label parameter types.

    Multi-label sockets can have multiple edges. Classify incoming root edges
    after excluding edges attached to non-label sockets.
    """
    label_type = lux.PARAMETER_TYPE_SHADERLABEL
    lines = []
    total = 0
    for mat, graph, error in get_graphs():
        if graph is None:
            lines.append("{}: [ERROR: {}]".format(mat, error or EMPTY))
            continue
        for root in graph_roots(graph):
            params = safe_value(root.getParameters, []) or []
            nonlabel_ids = set()
            label_names = []
            for p in params:
                pname = safe_value(p.getName)
                if not pname:
                    continue
                if safe_value(p.getType) == label_type:
                    label_names.append(pname)
                else:
                    e = safe_value(lambda nm=pname: root.getInputEdge(nm))
                    if e is not None:
                        nonlabel_ids.add(safe_value(e.getID))
            if not label_names:
                continue
            for edge in safe_value(root.getInputEdges, []) or []:
                if safe_value(edge.getID) in nonlabel_ids:
                    continue
                src = safe_value(edge.getSourceNode)
                total += 1
                lines.append("Material '{}' root '{}' | label candidate {} | edge={} enabled={}".format(
                    mat, node_label(root), shader_title(src) if src is not None else EMPTY,
                    display(safe_value(edge.getID)), display(safe_value(edge.isEnabled))))
    lines.insert(0, "Root label edges: {} (candidate classification by socket type).".format(total))
    return records(lines)


def shader_types_inventory():
    counts = {}
    materials = {}
    for mat, graph, error in get_graphs():
        if graph is None:
            continue
        for node in graph_nodes(graph):
            code, friendly = type_info(node)
            label = "{} [{}]".format(code, friendly)
            counts[label] = counts.get(label, 0) + 1
            materials.setdefault(label, set()).add(str(mat))
    lines = []
    for code in sorted(counts):
        lines.append("{} | nodes={} | materials={}".format(
            code, counts[code], ", ".join(sorted(materials[code]))))
    return records(lines) if lines else EMPTY


def material_animation_shader_report():
    """Animation-driven shader nodes do not require a scene animation node."""
    kinds = {
        getattr(lux, "SHADER_TYPE_COLOR_FADE", "animation_color"),
        getattr(lux, "SHADER_TYPE_CURVE_FADE", "animation_curve"),
    }
    lines = []
    for mat, graph, error in get_graphs():
        if graph is None:
            continue
        for node in graph_nodes(graph):
            typ, friendly = type_info(node)
            if typ not in kinds:
                continue
            lines.append("Material: {} | {}".format(mat, shader_title(node)))
            for p in safe_value(node.getParameters, []) or []:
                lines.append("  {} [type={}] = {}".format(
                    safe_value(p.getName), safe_value(p.getType), parameter_value(p)))
    return records(lines) if lines else EMPTY


def material_library_metadata():
    """CMF metadata: library-only. User specifies an EXACT known material name."""
    name = str(SETTINGS.get("library_metadata_name") or "").strip()
    if name in ("", "LibraryMaterialName"):
        return "Skipped: specify an exact library material name in the main dialog."
    info = lux.findMaterialMetadata(name=name)
    if info is None:
        return "No library metadata object for {!r}".format(name)
    lines = ["Material library metadata: {!r}".format(name)]
    for field in safe_value(info.getFieldNames, []) or []:
        try:
            value = info.readField(field)
            lines.append("  {}: {}".format(field, display(value)))
        except Exception as e:
            # KeyShot 2026 does not allow reading image metadata fields.
            lines.append("  {}: [UNREADABLE OR IMAGE FIELD: {}]".format(field, e))
    return records(lines)


def all_animation_objects():
    """Scene-tree animation inventory only. No undeclared animation object calls."""
    return animation_nodes_hierarchy()


def node_animation_objects():
    """Scene-tree animation inventory only. No undeclared animation object calls."""
    return animation_nodes_hierarchy()


def animation_nodes_hierarchy():
    lines = []
    for n, depth in walk_scene():
        if safe_value(n.isAnimation, False):
            parent = safe_value(n.getParent)
            lines.append("{}{} | ID {} | parent {}".format(
                "  " * depth, node_label(n), display(safe_value(n.getID)),
                node_label(parent) if parent else "(none)"))
    return records(lines) if lines else "No scene-tree animation nodes"


def animation_bounds_current_frame():
    """Read current frame only. setAnimationFrame is intentionally prohibited."""
    lines = ["Current animation frame: {}".format(display(lux.getAnimationFrame()))]
    seen = set()
    for anim, _d in walk_scene():
        if not safe_value(anim.isAnimation, False):
            continue
        parent = safe_value(anim.getParent)
        if parent is None:
            continue
        pid = safe_value(parent.getID)
        if pid in seen:
            continue
        seen.add(pid)
        lines.append("Animation parent: {}".format(node_label(parent)))
        lines.append("  " + try_get("World bounding box",
                         lambda n=parent: n.getBoundingBox(world=True)))
        lines.append("  " + try_get("World transform",
                         lambda n=parent: n.getTransform(world=True)))
        lines.append("  " + try_get("World center",
                         lambda n=parent: n.getCenter(world=True)))
    if len(lines) == 1:
        lines.append("No animation parent nodes")
    return records(lines)


def status_predicates():
    # 'is' and 'has' checks are information, even though they are not GET names.
    return api_values([
        ("Scene has contents", lux.hasContents),
        ("Scene changed", lux.isSceneChanged),
        ("Camera unsaved", lux.isCameraUnsaved),
        ("Headless", lux.isHeadless),
        ("Performance mode enabled", lux.isPerformanceModeEnabled),
        ("Renderer paused", lux.isPaused),
        ("Undo enabled", lux.isUndoEnabled),
    ])


def render_options_defaults():
    opts = lux.getRenderOptions(defaults=True)
    return records(rows_from_mapping(opts.getDict())) if opts is not None else EMPTY


def available_camera_only_notice():
    """API has no nonmutating getCamera(name); do not switch cameras."""
    return ("Saved camera names are available through getCameras(). "
            "Detailed camera getters describe the ACTIVE camera only. "
            "v1.2 offers an explicitly enabled saved-camera inspection "
            "which temporarily uses setCamera() and restores the original "
            "camera when Python execution continues. A native crash may "
            "prevent restoration; unsaved-camera edits block the scan.")


# All 59 documented non-GUI top-level lux.get* names, for the compliance report.
GETTERS_2026 = (
    "getActiveConfiguration", "getActiveEnvironment", "getActiveImageStyle",
    "getActiveStudio", "getAnimationFrame", "getAnimationInfo", "getAnimationTime",
    "getCameraFieldOfView", "getCameraFocalLength", "getCameraLens",
    "getCameraLookAt", "getCameraPivot", "getCameraPosition", "getCameraUp",
    "getCameras", "getColorway", "getColorways", "getEnvironments",
    "getExternalFiles", "getImageStyles", "getImportOptions",
    "getKeepAspectRatio", "getKeyShotDisplayVersion", "getKeyShotFolder",
    "getKeyShotVersion", "getLibraryBackplates", "getLibraryColors",
    "getLibraryEnvironments", "getLibraryMaterials", "getLibraryTextures",
    "getLightingPreset", "getLightingPresets", "getLockResolution",
    "getMaterialGraph", "getMaterialMapping", "getMaterialTemplates",
    "getOS", "getObjectMaterial", "getObjects", "getRenderEngine",
    "getRenderLayers", "getRenderOptions", "getSceneColor", "getSceneColors",
    "getSceneInfo", "getSceneMaterials", "getSceneTree",
    "getSphericalCamera", "getStudio", "getStudios", "getSystemInfo"
)


def api_getter_coverage():
    """Inventory API availability, not an unsafe automatic no-arg execution."""
    lines = [
        "KeyShot 2026 reference: {} information getters".format(len(GETTERS_2026)),
        "Availability is an inventory of declared getters only.",
        "Availability is checked on the runtime module; many getters require "
        "parameters, a loaded scene, or a selected object.",
    ]
    missing = []
    for name in GETTERS_2026:
        exists = callable(getattr(lux, name, None))
        if not exists:
            missing.append(name)
        lines.append("  {:<30} {}".format(name, "available" if exists else "MISSING"))
    lines.append("Missing in installed runtime: {}".format(len(missing)))
    return records(lines)


# --- Registry: list every supported GET as an independently selectable option --

# (id, checkbox label, reporter, default-enabled)
CATEGORIES = [
    ("scene", "Scene / configuration / metadata", [
        ("scene_info", "getSceneInfo() - Scene summary", scene_info, True),
        ("config", "getActiveConfiguration() - Configuration", config_info, True),
        ("colors", "getSceneColors() / getSceneColor() - Scene colors", scene_colors, False),
        ("color_lookup", "getSceneColor() - Individual color details", scene_color_lookup, False),
        ("colorways", "getColorways() - Colorways", scene_colorways, False),
        ("meta", "getMetaData() - Simple metadata", metadata_simple, False),
        ("xmp", "getMetaData() - XMP metadata (large)", metadata_xmp, False),
        ("metadata_files", "Export native .metadata and .xmp files (user folder)",
         export_native_scene_metadata, False),
    ]),
    ("tree", "Scene tree / node details", [
        ("tree", "getSceneTree() - Hierarchy", scene_tree, True),
        ("nodes", "SceneNode getters - IDs, states and paths", detailed_scene_tree, False),
        ("selected", "SceneNode.getSelected() - Selected nodes", tree_selected, False),
        ("transforms", "Node transforms / center / bounds", tree_transforms, False),
        ("dump", "dumpTree() - Full JSON tree (large)", json_scene_tree, False),
        ("names_only", "SceneNode.getName() - Names only", scene_node_names, False),
        ("names_types", "getName() / getKind() - Names and types", scene_node_names_types, False),
        ("paths", "getPath() - Node paths", scene_node_paths, False),
        ("node_sets", "getHidden / getLocked / getDeleted / getSelected", scene_node_collections, False),
        ("metadata_nodes", "SceneNode.getMetadata() - Per-node metadata", scene_node_metadata, False),
        ("parents", "SceneNode.getParent() - Parent relationships", node_parent_relationships, False),
    ]),
    ("models", "Model sets / objects / layers", [
        ("active_models", "getModelSets() - Active model sets", active_model_sets, True),
        ("model_tree", "Scene tree - All model sets", model_set_tree, True),
        ("object_ids", "getObjects() - Object IDs", object_ids, False),
        ("mapping", "getMaterialMapping() - Object materials", material_mapping, False),
        ("object_mat", "getObjectMaterial() - Object material assignments", object_materials, False),
        ("layers", "getRenderLayers() - Render layers", render_layers, True),
    ]),
    ("materials", "Materials / graphs / parameters", [
        ("names", "getSceneMaterials() - Material names", material_names, True),
        ("graphs", "getMaterialGraph() - Node IDs and types", graph_outline, True),
        ("params", "ShaderNode.getParameters() - All values", graph_parameters, False),
        ("edges", "ShaderNode edges - Connections", graph_connections, False),
        ("multi", "getMultiMaterial() - Sub-materials", multi_materials, True),
        ("params_connections", "Shader parameters / input sources (large)", graph_parameter_connections, False),
        ("edge_detail", "Graph edges, target sockets, enabled states", graph_connections_detailed, False),
        ("graph_lookups", "MaterialGraph lookup getters (IDs / type)", graph_getter_lookup_tests, False),
        ("shader_types", "Shader types inventory including OpenPBR", shader_types_inventory, False),
        ("geo", "Geometry-node connections (Fuzz/Flakes/Bubbles/Displace)", geometry_node_report, False),
        ("unused", "Potentially disconnected/orphan shader nodes", disconnected_shader_nodes, False),
        ("labels", "Material labels and root connections", material_labels_report, False),
        ("mat_anims", "Material graph Color/Curve Fade animation nodes", material_animation_shader_report, False),
        ("cmf", "MaterialMetadata.getFieldNames/readField (library)", material_library_metadata, False),
    ]),
    ("cameras", "Cameras / all saved camera settings", [
        ("camera_list", "getCameras() - Saved camera names", camera_list, True),
        ("camera_active", "getCamera() / Lens / Spherical", camera_active, True),
        ("camera_geo", "getCameraPosition(), direction, look-at", camera_geometry, True),
        ("camera_opt", "getCameraFieldOfView(), focal length", camera_optics, True),
        ("camera_all", "ALL saved cameras - all documented settings (switch/restore)",
         all_saved_camera_details, True),
    ]),
    ("environments", "Environments / all saved settings", [
        ("env_list", "getEnvironments() - Saved names", environments_list, True),
        ("env_active", "getActiveEnvironment() - Full settings", active_environment, True),
        ("env_all", "ALL saved environments - all Env getters (switch/restore)",
         all_saved_environment_details, True),
    ]),
    ("image", "Image styles", [
        ("image_list", "getImageStyles() - Saved styles", image_style_names, True),
        ("image_active", "getActiveImageStyle() - Active settings", active_image_style, True),
        ("style_all", "ALL saved image styles - full settings (switch/restore)",
         all_saved_image_style_details, False),
    ]),
    ("studios", "Studios", [
        ("studios_list", "getStudios() - Saved studios", studios_list, True),
        ("studio_active", "getActiveStudio()", active_studio, True),
        ("studio_detail", "getStudio() - All studio settings", studios_detail, True),
    ]),
    ("render", "Render / lighting settings", [
        ("render_opts", "getRenderOptions().getDict()", render_options, True),
        ("render_defaults", "getRenderOptions(defaults=True).getDict()", render_options_defaults, False),
        ("render_engine", "getRenderEngine()", render_engine, True),
        ("light_current", "getLightingPreset()", lighting_current, True),
        ("light_list", "getLightingPresets()", lighting_presets, True),
        ("locks", "getKeepAspectRatio() / getLockResolution()", render_resolution_locks, False),
    ]),
    ("animation", "Animation", [
        ("animation_status", "getAnimationInfo() / Time / Frame", animation_status, True),
        ("animation_tree", "Scene animation-node hierarchy (advanced opt-in)", animation_nodes_hierarchy, False),
        ("current_boxes", "Animated parent world bounds (advanced opt-in)", animation_bounds_current_frame, False),
    ]),
    ("resources", "Resources / libraries / imports", [
        ("folders", "getKeyShotFolder() - All resource paths", resource_folders, True),
        ("external", "getExternalFiles()", external_files, True),
        ("resource_models", "Resource Models - BIP/KSP files (disk scan)", resource_models, False),
        ("templates", "getMaterialTemplates()", material_templates, False),
        ("imports", "getImportOptions()", import_options, False),
        ("library", "getLibrary...() - All library inventories (slow)", library_inventory, False),
    ]),
    ("system", "KeyShot version / system", [
        ("versions", "getKeyShotVersion() / getOS()", versions, True),
        ("system", "getSystemInfo()", system_info, True),
        ("predicate", "hasContents()/is*() - Scene status flags", status_predicates, False),
        ("coverage", "2026 API getter availability audit", api_getter_coverage, False),
    ]),
]


# --- Interactive selection and report output ----------------------------------

def selected_mode(value):
    """DIALOG_ITEM returns [index, text] in KeyShot."""
    options = ["Print to console", "Save TXT only", "Print and save TXT"]
    if isinstance(value, (list, tuple)) and len(value) >= 2:
        return str(value[1])
    if isinstance(value, str) and value in options:
        return value
    if isinstance(value, int) and 0 <= value < len(options):
        return options[value]
    return options[2]


def get_default_directory():
    folder = safe_value(lambda: lux.getKeyShotFolder(lux.FOLDER_SCRIPTS))
    if folder and os.path.isdir(folder):
        return folder
    return os.path.expanduser("~")


def _item_value(raw, items):
    """KeyShot DIALOG_ITEM returns [index, value]; use value over stale index."""
    if isinstance(raw, (list, tuple)) and len(raw) >= 2:
        return str(raw[1])
    if isinstance(raw, str) and raw in items:
        return raw
    if isinstance(raw, int) and 0 <= raw < len(items):
        return items[raw]
    return items[0]


def select_report_options():
    """Single overview. Individual mode uses one category and one picker.

    This avoids opening up to 12 consecutive, large native KeyShot dialogs.
    """
    values = [(lux.DIALOG_LABEL, "Default mode: check the report categories below.")]
    defaults = {"scene", "tree", "materials", "cameras", "environments",
                "image", "studios", "render"}
    for key, title, _entries in CATEGORIES:
        values.append((key, lux.DIALOG_CHECK, title, key in defaults))
    category_titles = [title for _key, title, _items in CATEGORIES]
    values += [
        (lux.DIALOG_LABEL, "---------------------------------------"),
        ("individual", lux.DIALOG_CHECK,
         "Individual Gets mode: ONE category per run", False),
        ("individual_category", lux.DIALOG_ITEM,
         "Category for Individual Gets mode:", 0, category_titles),
        ("mode", lux.DIALOG_ITEM, "Report destination:", 2, [
            "Print to console", "Save TXT only", "Print and save TXT"]),
        ("folder", lux.DIALOG_FOLDER, "TXT output directory:",
         get_default_directory()),
        ("name", lux.DIALOG_TEXT, "TXT filename (without .txt):",
         "KeyShot_Information_Report"),
        ("node_limit", lux.DIALOG_INTEGER,
         "Max nodes for per-node animation scan:", 80, (1, 1000)),
        ("scene_cap", lux.DIALOG_INTEGER,
         "Max scene nodes to inspect:", 700, (10, 20000)),
        ("section_kb", lux.DIALOG_INTEGER,
         "Max output per GET (KB):", 18, (2, 500)),
        ("allow_slow", lux.DIALOG_CHECK,
         "Allow slow scans / library loading (OFF recommended)", False),
        ("allow_animation_tree", lux.DIALOG_CHECK,
         "Allow advanced animation scene-tree scanning (OFF recommended)", False),
        ("allow_temporary_switch", lux.DIALOG_CHECK,
         "Inspect ALL cameras/environments/styles via switching/restoring (OFF)", False),
        ("exhaustive", lux.DIALOG_CHECK,
         "Exhaustive output: no scene/material/section caps (can be huge)", False),
        ("library_material", lux.DIALOG_TEXT,
         "Optional library material for CMF metadata:", "LibraryMaterialName"),
    ]
    return lux.getInputDialog(
        title="KeyShot Information Inspector 1.2.0 - Expanded Information",
        desc="Read-only report. Advanced animation hierarchy and bounds require opt-in. "
             "Saved cameras, environments and styles switch temporarily and restore when execution continues.",
        values=values, id=DIALOG_ID)


def get_selected_operations(main_opts):
    granular = bool(main_opts.get("individual", False))
    if granular:
        titles = [title for _key, title, _ops in CATEGORIES]
        selected_title = _item_value(main_opts.get("individual_category"), titles)
        group, group_title, ops = next(
            (item for item in CATEGORIES if item[1] == selected_title), CATEGORIES[0])
        checkpoint("INDIVIDUAL DIALOG START: " + group_title)
        values = [(lux.DIALOG_LABEL,
                   "Select Get operations. Slow library & disk scans require opt-in above.")]
        values.extend((key, lux.DIALOG_CHECK, label, default)
                      for key, label, _func, default in ops)
        # No persisted ID: avoids old checkbox states being reused after edits.
        choices = lux.getInputDialog(
            title="Inspector 1.2.0 | {}".format(group_title),
            values=values)
        checkpoint("INDIVIDUAL DIALOG END: " + group_title)
        if choices is None:
            return None
        enabled = [(label, func) for key, label, func, _default in ops
                   if bool(choices.get(key, False))]
        return [(group_title, enabled)] if enabled else []

    chosen = []
    for _group, group_title, ops in CATEGORIES:
        if not bool(main_opts.get(_group, False)):
            continue
        enabled = [(label, func) for _key, label, func, default in ops
                   if default]
        if enabled:
            chosen.append((group_title, enabled))
    return chosen


def safe_filename(raw):
    """Never let a text field supply folders or escape the chosen directory."""
    name = str(raw or "KeyShot_Information_Report").strip()
    if name.lower().endswith(".txt"):
        name = name[:-4]
    name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name)
    name = name.strip(" .")
    return (name or "KeyShot_Information_Report")[:130] + ".txt"


def non_overwriting_path(folder, filename):
    """Save a new report rather than silently overwrite an earlier one."""
    candidate = os.path.join(folder, filename)
    if not os.path.exists(candidate):
        return candidate
    basename, ext = os.path.splitext(filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    candidate = os.path.join(folder, basename + "_" + timestamp + ext)
    index = 2
    while os.path.exists(candidate):
        candidate = os.path.join(
            folder, "{}_{}_{}{}".format(basename, timestamp, index, ext))
        index += 1
    return candidate


def stream_report(chosen, opts):
    """Write one GET at a time; preserve partial TXT and crash checkpoints.

    Unlike v1.1.0, this never concatenates all sections into a single string.
    Native KeyShot failures cannot be caught with Python; last START identifies
    which reporter was active when KeyShot exited.
    """
    mode = selected_mode(opts.get("mode"))
    save_report = mode != "Print to console"
    print_report = mode != "Save TXT only"
    out = None
    path = None
    if save_report:
        folder = opts.get("folder")
        if not isinstance(folder, str) or not os.path.isdir(folder):
            raise ValueError("Choose an existing TXT output directory.")
        path = non_overwriting_path(folder, safe_filename(opts.get("name")))
        out = open(path, "w", encoding="utf-8", newline="\n")
    failures, completed, skipped = 0, 0, 0
    started = time.monotonic()

    def put(message, console=False):
        if out is not None:
            out.write(message + "\n")
            out.flush()
        if console and print_report:
            print(message)

    header = [
        "KEYSHOT GET INFORMATION | SAFE INSPECTOR",
        "Version {} | KeyShot 2026 lux API".format(VERSION),
        "Report started: {}".format(datetime.now().isoformat(timespec="seconds")),
        "Scene cap: {} nodes; graph cap: {} nodes per material; material cap: {}".format(
            SETTINGS["max_scene_nodes"], SETTINGS["max_graph_nodes"], SETTINGS["max_materials"]),
        "Slow library/disk operations: {}".format(
            "EXPLICITLY ENABLED" if SETTINGS["allow_slow"] else "BLOCKED"),
        "Standard mode: no scene changes or timeline switching.",
        "Temporary active camera/environment/style switching: {}".format(
            "ENABLED (restores after each item; native crash cannot guarantee)"
            if SETTINGS.get("allow_temporary_switch") else "BLOCKED"),
        "Exhaustive output: {}".format("ENABLED (no safety caps)" if
              SETTINGS.get("exhaustive") else "OFF (safety caps active)"),
        "Trace file: {}".format(CRASH_TRACE_PATH),
        "=" * 76
    ]
    try:
        for line in header:
            put(line, console=True)
        # Guard the library calls even if an older cached dialog selection
        # supplied them, and flag expensive debug operations.
        dangerous = (
            "getLibrary...", "Resource Models - BIP/KSP files",
            "dumpTree() - Full JSON tree",
            "MaterialMetadata.getFieldNames/readField (library)",
        )
        animation_advanced = (
            "Scene animation-node hierarchy",
            "Animated parent world bounds",
        )
        native_animation_blocked = (
        )
        for category, operations in chosen:
            put("\n" + "=" * 76 + "\n" + category.upper()
                + "\n" + "=" * 76, console=True)
            for label, reporter in operations:
                checkpoint("GET START: " + category + " :: " + label)
                print("[Inspector] START: {} :: {}".format(category, label))
                put("\n" + "-" * 55 + "\n" + label + "\n" + "-" * 55)
                run_slow = SETTINGS.get("allow_slow", False)
                if any(x in label for x in native_animation_blocked):
                    # Hard stop even when slow scans / advanced animation are ON.
                    result = display(reporter())  # availability only; NEVER calls native getter
                    skipped += 1
                    checkpoint("ANIMATION NATIVE GETTER BLOCKED: " + label)
                elif (any(x in label for x in animation_advanced)
                      and not SETTINGS.get("allow_animation_tree", False)):
                    result = ("[SKIPPED SAFELY] This scene-tree animation analysis "
                              "requires the separate 'Allow advanced animation "
                              "scene-tree scanning' checkbox. No scan was run.")
                    skipped += 1
                elif not run_slow and any(x in label for x in dangerous):
                    result = ("[SKIPPED SAFELY] Operation requires the separate "
                              "'Allow slow scans' checkbox. No KeyShot getter called.")
                    skipped += 1
                else:
                    try:
                        result = display(reporter())
                    except Exception as exc:
                        result = "[ERROR] {}: {}".format(type(exc).__name__, exc)
                    # Each inline/top-level error marker is counted exactly once.
                    failures += result.count("[ERROR:") + result.count("[ERROR]")
                result = safe_output(result, label)
                put(result)
                if print_report:
                    console_len = max(200, int(SETTINGS["console_chars"]))
                    short = result[:console_len]
                    print(short)
                    if len(result) > console_len:
                        print("[Console preview truncated. TXT report has longer result.]")
                if out is not None:
                    os.fsync(out.fileno())
                completed += 1
                checkpoint("GET END: " + category + " :: " + label)
                print("[Inspector] END: {} :: {}".format(category, label))
        footer = ("\nREPORT END | {} completed, {} skipped, {} recorded error markers, "
                  "{:.1f}s".format(completed, skipped, failures,
                                   time.monotonic() - started))
        put(footer, console=True)
        checkpoint("REPORT COMPLETE: " + footer)
    finally:
        if out is not None:
            out.close()
    if path:
        print("[Inspector] Partial or full report written to: {}".format(path))
    print("[Inspector] Crash trace: {}".format(CRASH_TRACE_PATH))
    return path, failures, completed, skipped


def main():
    print("[Inspector] Starting safe inspector {}".format(VERSION))
    opts = select_report_options()
    if opts is None:
        print("[Inspector] Cancelled.")
        return
    SETTINGS["node_detail_limit"] = max(1, int(opts.get("node_limit", 80)))
    SETTINGS["max_scene_nodes"] = max(10, int(opts.get("scene_cap", 700)))
    SETTINGS["max_report_chars"] = max(2048, int(opts.get("section_kb", 18)) * 1024)
    SETTINGS["allow_slow"] = bool(opts.get("allow_slow", False))
    SETTINGS["allow_animation_tree"] = bool(opts.get("allow_animation_tree", False))
    SETTINGS["allow_temporary_switch"] = bool(opts.get("allow_temporary_switch", False))
    SETTINGS["exhaustive"] = bool(opts.get("exhaustive", False))
    SETTINGS["output_folder"] = str(opts.get("folder", ""))
    SETTINGS["output_base"] = str(opts.get("name", "KeyShot_Information_Report"))
    # More bounded graph calls for dense shader scenes.
    SETTINGS["max_graph_nodes"] = 120
    SETTINGS["max_materials"] = 40
    SETTINGS["library_metadata_name"] = str(
        opts.get("library_material", "")).strip()
    begin_trace(opts.get("folder"))
    checkpoint("MAIN OPTIONS ACCEPTED")
    chosen = get_selected_operations(opts)
    if chosen is None:
        checkpoint("CANCELLED individual selection")
        print("[Inspector] Individual selection cancelled.")
        return
    if not chosen:
        checkpoint("NO OPERATIONS CHOSEN")
        print("[Inspector] No GET operations selected.")
        return
    checkpoint("EXECUTING {} categories".format(len(chosen)))
    try:
        stream_report(chosen, opts)
    except Exception as exc:
        checkpoint("PYTHON ERROR: {}: {}".format(type(exc).__name__, exc))
        print("[Inspector] Failed: {}: {}".format(type(exc).__name__, exc))
        print("[Inspector] Review trace file: {}".format(CRASH_TRACE_PATH))


if __name__ == "__main__":
    main()
