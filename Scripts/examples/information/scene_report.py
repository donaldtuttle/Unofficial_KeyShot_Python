"""KPSA 2026: inspect scene nodes with getKind and getMetadata.

Read-only. Evidence: lux.getSceneTree, lux.SceneNode getters.
Syntax/documentation checks only; KeyShot runtime untested.
"""
import lux

def walk(node):
    yield node
    for child in node.getChildren():
        yield from walk(child)

def main():
    root = lux.getSceneTree()
    for node in walk(root):
        print(f'id={node.getID()!r} kind={node.getKind()!r} name={node.getName()!r}')
        print(f'  metadata={node.getMetadata()!r}')

if __name__ == '__main__':
    main()
