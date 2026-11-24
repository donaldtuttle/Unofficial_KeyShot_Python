# KeyShot Advanced Material Graph Cheat Sheet

Quick reference for safe, production-grade material graph manipulation.

## 1. Safe Graph Modification (Golden Rule)

**Never modify while reading.** Always use **Two-Phase** approach:

### Phase 1: Catalog (Read-only)
```python
graph = lux.getMaterialGraph(name=mat_name)
root = graph.getRoot()
source, shader_type = find_source_shader(graph)

edge_reconnections = []   # (src_node, new_param, old_param)
source_values = {}

for old_p, (new_p, strip) in param_map.items():
    edge = source.getInputEdge(old_p)
    if edge:
        edge_reconnections.append((edge.getSourceNode(), new_p, old_p))
    else:
        param = source.getParameter(old_p)
        if param and not param.isPure():
            val = param.getValue()
            if strip and len(val) == 4: val = val[:3]
            source_values[new_p] = val
```

### Phase 2: Modify
```python
new_node = graph.newNode('lux_openpbr')
graph.newEdge(new_node, root, 'surface')
graph.removeNode(source)

for p, v in source_values.items():
    converted, _ = apply_conversions(p, v)
    set_param(new_node, p, converted)

for src, new_p, _ in edge_reconnections:
    graph.newEdge(src, new_node, new_p)
```

## 2. Dictionary Mapping Pattern (schematic placeholders; not executable Python)

```python
COLOR_MAP = {lux.SHADER_TYPE_XXX: ('param', strip_alpha), ...}
ROUGHNESS_MAP = {lux.SHADER_TYPE_XXX: 'roughness', ...}
EXTRA_MAP = {
    lux.SHADER_TYPE_XXX: {
        'fixed':  {...},
        'colors': {...},
        'floats': {...},
    }
}
COMMON_EDGE_MAP = {'bumpmap': 'geometry_normal', ...}

def build_param_map(shader_type):
    # Combine all maps into one lookup
    ...
```

## 3. Value Conversion Helpers

```python
def convert_roughness(val):
    return min(float(val) * 4.0, 1.0)

def convert_thinfilm_thickness(nm):
    return max(0.0, min((nm - 380) / 400, 1.0))

def apply_conversions(param_name, value):
    if param_name in ROUGHNESS_PARAMS:
        return convert_roughness(value), True
    if param_name == 'thin_film_thickness':
        return convert_thinfilm_thickness(value), True
    return value, False
```

## 4. Orphan Node Inspection (deletion requires explicit authorization)

```python
def get_edge_counts(node):
    """Return (in_count, out_count) or None if inspection fails.
    Never treat a failed inspection as zero edges."""
    try:
        return len(node.getInputEdges() or []), len(node.getOutputEdges() or [])
    except Exception:
        return None

def is_animation_node(node):
    try:
        if 'fade' in str(node.getType()).lower():
            return True
        return all(node.getParameter(p) for p in ('duration', 'start_time', 'ease_mode'))
    except Exception:
        return True  # treat unknown as protected

def inspect_orphaned_nodes(graph):
    """Return list of nodes that appear to have zero edges.
    Does not delete. A zero-edge count is not proof a node is disposable."""
    candidates = []
    root_ids = {graph.getRoot().getID()}
    for n in (graph.getMaterialNodes() or []):
        root_ids.add(n.getID())
    for node in (graph.getNodes() or []):
        if node.getID() in root_ids or is_animation_node(node):
            continue
        counts = get_edge_counts(node)
        if counts is None:
            continue  # inspection failed — do not classify as orphan
        in_c, out_c = counts
        if in_c == 0 and out_c == 0:
            candidates.append(node)
    return candidates

# Deletion is opt-in only. Caller must explicitly authorize.
# def delete_authorized_nodes(graph, nodes):
#     for n in nodes:
#         graph.removeNode(n)
```

## 5. Key Robustness Rules

- Always check `if graph:`, `if node:`, `if param:`
- Wrap graph changes in `try/except`
- Call `lux.sync()` after major modifications
- Scan **whole graph** for animation nodes (not just direct edges)
- Protect root nodes + animation nodes during cleanup
- Have fallback values for emissive materials (intensity = 0)

## 6. Recommended Structure for Converters

```python
def convert_material(name):
    graph = lux.getMaterialGraph(name=name)
    if not graph: return False

    # Phase 1: Read
    source, stype = find_source_shader(graph)
    param_map = build_param_map(stype)
    edges, values = catalog(graph, source, param_map)

    # Phase 2: Modify
    new_node = create_and_connect_openpbr(graph)
    apply_values(new_node, values)
    reconnect_edges(graph, new_node, edges)

    # Phase 3: Cleanup
    cleanup_orphans(graph)
    return True
```

**Core Principle**: Read everything → Modify safely → Clean up.