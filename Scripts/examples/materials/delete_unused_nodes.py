# -*- coding: utf-8 -*-
"""Delete unconnected material-graph nodes. May need more than one pass.

Read-only until removeNode. Skips root and constant-color nodes.
"""
import lux

MAX_PASSES = 10


def _edge_counts(node):
    try:
        inputs = node.getInputEdges() or []
    except Exception:
        inputs = []
    try:
        outputs = node.getOutputEdges() or []
    except Exception:
        outputs = []
    return len(inputs), len(outputs)


def _is_const_color(node):
    try:
        ntype = node.getType()
    except Exception:
        return False
    if isinstance(ntype, dict):
        return ntype.get("name", "") == "lux_const_color"
    return False


def _root_ids(graph):
    ids = set()
    try:
        root = graph.getRoot()
        if root is not None:
            ids.add(root.getID())
    except Exception:
        pass
    try:
        for rn in graph.getMaterialNodes() or []:
            try:
                ids.add(rn.getID())
            except Exception:
                pass
    except Exception:
        pass
    return ids


def cleanup_graph(graph):
    removed = 0
    for _ in range(MAX_PASSES):
        protected = _root_ids(graph)
        candidates = []
        try:
            nodes = graph.getNodes() or []
        except Exception:
            break
        for node in nodes:
            try:
                nid = node.getID()
            except Exception:
                continue
            if nid in protected or _is_const_color(node):
                continue
            if _edge_counts(node) == (0, 0):
                candidates.append(node)
        if not candidates:
            break
        for node in candidates:
            try:
                graph.removeNode(node)
                removed += 1
                print("Removed:", node.getName())
            except Exception as exc:
                print("Could not remove", node.getName(), exc)
    return removed


def main():
    names = lux.getSceneMaterials() or []
    total = 0
    for name in names:
        try:
            graph = lux.getMaterialGraph(name=name)
        except Exception as exc:
            print(name, exc)
            continue
        if not graph:
            continue
        n = cleanup_graph(graph)
        if n:
            print(name, "removed", n)
        total += n
    lux.sync()
    print("Total removed:", total)


main()
