"""KPSA 2026: copy explicitly selected compatible concrete shader values.

This helper does not duplicate materials or clone graph connections. Obtain two
ShaderNode instances in KeyShot and call copy_concrete_parameters with their
verified parameter names. Dry-run is the default. No transaction/rollback exists.
Evidence: ShaderNode.getParameter and ShaderParameter name/type/isPure/value.
Offline mock tests exercise preconditions; KeyShot runtime remains untested.
"""

def copy_concrete_parameters(source_node, target_node, names, *, dry_run=True):
    names = tuple(names)
    if not names or any(not isinstance(name, str) or not name for name in names):
        raise ValueError('Provide at least one nonempty verified parameter name.')
    if len(set(names)) != len(names):
        raise ValueError('Parameter names must be unique.')
    prepared = []
    for name in names:
        # Unknown names may raise from KeyShot. Complete preflight before setters.
        source = source_node.getParameter(name)
        target = target_node.getParameter(name)
        if source is None or target is None:
            raise ValueError(f'Parameter missing: {name!r}')
        if source.isPure() or target.isPure():
            raise ValueError(f'Pure parameter cannot copy a concrete value: {name!r}')
        if source.getType() != target.getType():
            raise ValueError(f'Parameter types differ: {name!r}')
        value = source.getValue()
        # Restrict this example to plain scalar values. No texture/color/object
        # copying or deep-copy guarantees are inferred from equal API types.
        if type(value) not in (bool, int, float, str):
            raise ValueError(f'Only plain scalar values are supported: {name!r}')
        prepared.append((name, target, value))
    if not dry_run:
        for _, target, value in prepared:
            target.setValue(value)
    return [dict(name=name, value=value, applied=not dry_run) for name, _, value in prepared]

if __name__ == '__main__':
    print('Import this helper in KeyShot and pass two verified ShaderNode instances; see scripts/README.md.')
