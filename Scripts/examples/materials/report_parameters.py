"""KPSA 2026: inspect a material graph without reading pure values.

Set MATERIAL_NAME to an existing scene material. Evidence:
lux.getMaterialGraph, MaterialGraph.getNodes, ShaderNode/ShaderParameter getters.
Syntax/documentation checks only; KeyShot runtime untested.
"""
import lux

MATERIAL_NAME = ''

def report_graph(graph):
    for node in graph.getNodes():
        print(f'node={node.getID()!r} name={node.getName()!r} type={node.getType()!r}')
        for parameter in node.getParameters():
            name = parameter.getName()
            kind = parameter.getType()
            if parameter.isPure():
                print(f'  {name!r} type={kind!r} pure=True')
            else:
                print(f'  {name!r} type={kind!r} pure=False value={parameter.getValue()!r}')

def main():
    if not MATERIAL_NAME:
        raise ValueError('Set MATERIAL_NAME to an existing scene material before running.')
    graph = lux.getMaterialGraph(MATERIAL_NAME)
    if graph is None:
        raise ValueError(f'Material graph not found: {MATERIAL_NAME!r}')
    report_graph(graph)

if __name__ == '__main__':
    main()
