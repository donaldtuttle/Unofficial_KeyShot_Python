"""Activate exact existing model sets; inspect inactive sets too. Dry-run default.

Activation is distinct from geometry visibility. This does not hide/show child
geometry, delete sets, or promise rollback after partial setModelSets failure.
Evidence: getSceneTree, SceneNode.getChildren/isModelSet/getName, setModelSets,
getModelSets. Documentation checks only; KeyShot runtime not passed.
"""
import lux

TARGET_NAMES = ['Product']
DRY_RUN = True

def activate(names, *, dry_run=True):
    if not isinstance(names,(list,tuple)) or not names or any(not isinstance(n,str) or not n.strip() for n in names):
        raise ValueError('Provide a nonempty list of exact model-set names.')
    if len(set(names))!=len(names):raise ValueError('Duplicate target names.')
    found=[n.getName() for n in lux.getSceneTree().getChildren() if n.isModelSet()]
    if any(found.count(name)!=1 for name in names):
        raise ValueError('A target is missing or ambiguous; no activation attempted.')
    print('Activate:',list(names),'; other sets will be deactivated; dry_run=',dry_run)
    if dry_run:return list(names)
    result=lux.setModelSets(list(names))
    if result is not True:
        raise RuntimeError('Not all sets activated; partial state may remain: '+repr(lux.getModelSets()))
    return list(names)

if __name__=='__main__':activate(TARGET_NAMES,dry_run=DRY_RUN)
