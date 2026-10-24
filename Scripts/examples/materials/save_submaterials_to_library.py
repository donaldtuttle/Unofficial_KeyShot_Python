# -*- coding: utf-8 -*-
"""Save multi-material sub-materials to the KeyShot material library.

Uses lux.getMaterialGraph and lux.saveMaterial. Skips names already saved.
"""
import os
import lux


def library_path():
    if os.name == "nt":
        return os.path.join(os.environ.get("PUBLIC", ""), "Documents", "KeyShot", "Materials")
    return os.path.join(os.path.expanduser("~"), "Library", "Application Support", "KeyShot", "Materials")


def is_multi(name):
    graph = lux.getMaterialGraph(name=name)
    if not graph:
        return False
    try:
        return len(graph.getMaterialNodes() or []) > 1
    except Exception:
        return False


def save_subs(multi_name, folder, saved):
    graph = lux.getMaterialGraph(name=multi_name)
    if not graph:
        print("Not found:", multi_name)
        return
    for node in graph.getMaterialNodes() or []:
        try:
            sub_name = node.getName()
        except Exception:
            continue
        if not sub_name or sub_name in saved:
            continue
        lux.saveMaterial(name=sub_name, folder=folder)
        saved.add(sub_name)
        print("Saved", sub_name)


def main():
    folder = library_path()
    saved = set()
    for name in lux.getSceneMaterials() or []:
        if is_multi(name):
            save_subs(name, folder, saved)
    print("Saved", len(saved), "sub-materials")


main()
