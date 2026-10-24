# -*- coding: utf-8 -*-
"""Connect a Color Gradient node to the diffuse parameter of a material."""
import lux


def connect_color_gradient(material_name):
    graph = lux.getMaterialGraph(name=material_name)
    if graph is None:
        print("Material not found:", material_name)
        return False

    gradient = graph.newNode("lux_color_gradient")
    if gradient is None:
        print("Failed to create Color Gradient node")
        return False

    connected = False
    for node in graph.getNodesFromType("lux_diffuse") or []:
        param = node.getParameter("diffuse")
        if param is None:
            continue
        graph.newEdge(source=gradient, target=node, param="diffuse")
        print("Connected Color Gradient to", node.getName())
        connected = True
        break

    if not connected:
        print("No lux_diffuse node with a diffuse parameter")
    return connected


# Replace with a material that exists in the scene.
connect_color_gradient("Rainbow Gradient Material")
