"""KPSA 2026: translate one exact scene target, with absolute-node checks.

Set TARGET_ID and OFFSET. Dry-run prints intent. Relative transformations use
the node's local transform chain; absolute requires an object node.
Evidence: SceneNode.applyTransform/isObject and 2026.1 luxmath.Matrix/Vector.
Syntax/documentation checks only; KeyShot runtime untested.
"""
import math
import lux
import luxmath

TARGET_ID = None
OFFSET = (0.0, 0.0, 0.0)
ABSOLUTE = False
DRY_RUN = True

def walk(node):
    yield node
    for child in node.getChildren():
        yield from walk(child)

def translate(node, offset, *, absolute=False, dry_run=True):
    if len(offset) != 3 or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in offset):
        raise ValueError('Offset must contain exactly three finite numbers.')
    if absolute and not node.isObject():
        raise ValueError('An absolute transform requires an object node.')
    print(f'Target {node.getID()!r}, offset={tuple(offset)!r}, absolute={absolute}, dry_run={dry_run}')
    if dry_run:
        return
    matrix = luxmath.Matrix().makeIdentity().translate(luxmath.Vector(tuple(offset)))
    node.applyTransform(matrix, absolute=absolute)

def main():
    if TARGET_ID is None:
        raise ValueError('Set TARGET_ID using the scene report before running.')
    matches = [node for node in walk(lux.getSceneTree()) if node.getID() == TARGET_ID]
    if len(matches) != 1:
        raise ValueError(f'Expected exactly one target, found {len(matches)}.')
    translate(matches[0], OFFSET, absolute=ABSOLUTE, dry_run=DRY_RUN)

if __name__ == '__main__':
    main()
