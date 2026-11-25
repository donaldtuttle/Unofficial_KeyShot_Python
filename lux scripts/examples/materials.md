# Scripting Examples: Materials

[Scripting Examples TOC](../Scripting_Examples.md)

## Color Gradient ShaderEdge Diffuse Material Color Connect.py
<a name="material-color-gradient-shaderedge-diffuse-material-color-connect"></a>
```python
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example of graphing a Color Gradient shader edge node.

import lux  # Import the KeyShot built-in module 'lux'.

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return

    # Set up the Color Gradient node if necessary.
    # This step is customizable based on specific gradient requirements.

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "ColorGradient Rainbow"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)
```

# End of Material\Color Gradient ShaderEdge Diffuse Material Color Connect.py

## Create Python Material Output Script.py
<a name="material-create-python-material-output-script"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Create KeyShot Material
``` python
def save_keyshot_material_creation_script():
    # Define the name of the output Python script file
    output_script_name = "C:/Users/Public/Documents/KeyShot/Scripts/create_keyshot_material.py"

    # Script content to create a KeyShot material
    script_content = """
import lux

def create_material_with_metadata():
    # Ensure we have an active scene
    scene = lux.getSceneTree()

    # Create a new material graph for a multi-material
    material_name = "Custom Multi-Material"
    material_graph = lux.newMaterial(material_name, multi_material=True)
    
    # Example: Adding a Diffuse material node
    diffuse_node = material_graph.newNode(lux.SHADER_TYPE_DIFFUSE)
    diffuse_node.setParameter('diffuse', (0.3025, 0.3025, 0.3025, 1.0))
    diffuse_node.setParameter('roughness', 0.0)
    material_graph.connect(material_graph.getRoot(), diffuse_node, 'surface')

    # Example: Adding a Glass material node
    glass_node = material_graph.newNode(lux.SHADER_TYPE_GLASS)
    glass_node.setParameter('ior', 1.5)
    glass_node.setParameter('transmission', (0.3, 0.3, 0.3))
    glass_node.setParameter('two sided', True)
    material_graph.connect(material_graph.getRoot(), glass_node, 'surface')

    # Apply the material to an object, replace 'YourObjectNameHere' with the actual object name
    object_name = "YourObjectNameHere"
    obj = scene.find(object_name)
    if obj:
        obj.applyMaterial(material_name)
    else:
        print(f"Object '{object_name}' not found in the scene.")

create_material_with_metadata()
    """

    # Write the script content to the output file
    with open(output_script_name, 'w') as file:
        file.write(script_content)

    return output_script_name

# Save the KeyShot material creation script
script_file_path = save_keyshot_material_creation_script()
print(f"KeyShot material creation script saved as: {script_file_path}")
```

# End of Material\Create Python Material Output Script.py

## Delete Unused Nodes in Material Graph.py
<a name="material-delete-unused-nodes-in-material-graph"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Delete unused nodes from the material graph.  May need to be run multiple times.
``` python
import lux

MAX_ITERATIONS = 10  # Maximum number of cleanup iterations

def has_material_connections(node):
    """Check if a material node has connections."""
    input_edges = node.getInputEdges()
    output_edges = node.getOutputEdges()
    return bool(input_edges or output_edges)

def cleanup_unused_material_nodes(material_graph):
    """Clean up unconnected nodes within a material graph."""
    nodes_to_remove = []
    try:
        nodes = material_graph.getNodes()
        for node in nodes:
            if not has_material_connections(node):
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            material_graph.removeNode(node)
            print(f"Removed node: {node.getName()} from material: {material_graph.getMaterialName()}")
    except Exception as e:
        print(f"Exception encountered while processing material graph: {e}")
    return bool(nodes_to_remove)

def cleanup_scene():
    """Main function to clean up the scene."""
    any_changes = True
    iteration_count = 0

    while any_changes and iteration_count < MAX_ITERATIONS:
        any_changes = False
        iteration_count += 1

        # Cleanup material nodes
        material_names = lux.getSceneMaterials()
        for material_name in material_names:
            try:
                material_graph = lux.getMaterialGraph(name=material_name)
                if material_graph:
                    if cleanup_unused_material_nodes(material_graph):
                        any_changes = True
            except Exception as e:
                print(f"Exception encountered while processing material {material_name}: {e}")

    if iteration_count >= MAX_ITERATIONS:
        lux.getMessageBox("Scene cleanup stopped after reaching the maximum number of iterations.", "Cleanup Stopped", lux.MESSAGE_BOX_WARNING)
    else:
        lux.getMessageBox("Scene cleanup of unconnected nodes completed.", "Cleanup Complete", lux.MESSAGE_BOX_INFO)

cleanup_scene()
```

# End of Material\Delete Unused Nodes in Material Graph.py

## Delete Unused Shader Nodes.py
<a name="material-delete-unused-shader-nodes"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 1.1.0
# Script that deletes unused shader nodes.  May need to be run multiple times.  Use lux.getSceneMaterials() to locate unused material shaders.
``` python
import lux

MAX_ITERATIONS = 10  # Maximum number of cleanup iterations

def has_material_connections(node):
    """Check if a material node has connections."""
    input_edges = node.getInputEdges()
    output_edges = node.getOutputEdges()
    return bool(input_edges or output_edges)

def cleanup_unused_material_nodes(material_graph):
    """Clean up unconnected nodes within a material graph."""
    nodes_to_remove = []
    try:
        nodes = material_graph.getNodes()
        for node in nodes:
            if not has_material_connections(node):
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            material_graph.removeNode(node)
            print(f"Removed node: {node.getName()} from material: {material_graph.getMaterialName()}")
    except Exception as e:
        print(f"Exception encountered while processing material graph: {e}")
    return bool(nodes_to_remove)

def cleanup_scene():
    """Main function to clean up the scene."""
    any_changes = True
    iteration_count = 0

    while any_changes and iteration_count < MAX_ITERATIONS:
        any_changes = False
        iteration_count += 1

        # Cleanup material nodes
        material_names = lux.getSceneMaterials()
        for material_name in material_names:
            try:
                material_graph = lux.getMaterialGraph(material_name)
                if material_graph:
                    if cleanup_unused_material_nodes(material_graph):
                        any_changes = True
            except Exception as e:
                print(f"Exception encountered while processing material {material_name}: {e}")

    if iteration_count >= MAX_ITERATIONS:
        lux.getMessageBox("Scene cleanup stopped after reaching the maximum number of iterations.", "Cleanup Stopped", lux.MESSAGE_BOX_WARNING)
    else:
        lux.getMessageBox("Scene cleanup of unconnected nodes completed.", "Cleanup Complete", lux.MESSAGE_BOX_INFO)

cleanup_scene()
```

# End of Material\Delete Unused Shader Nodes.py

## Delete Unused Shader and Material Graph Nodes.py
<a name="material-delete-unused-shader-and-material-graph-nodes"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 1.1.0
# Script that deletes unused material shader and material graph nodes. May need to be run multiple times. Uses lux.getSceneMaterials() to locate unused material shaders.
``` python
import lux

MAX_ITERATIONS = 10  # Maximum number of cleanup iterations

def has_material_connections(node):
    """Check if a material node has connections."""
    input_edges = node.getInputEdges()
    output_edges = node.getOutputEdges()
    return bool(input_edges or output_edges)

def cleanup_unused_material_nodes(material_graph):
    """Clean up unconnected nodes within a material graph."""
    nodes_to_remove = []
    try:
        nodes = material_graph.getNodes()
        for node in nodes:
            if not has_material_connections(node):
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            material_graph.removeNode(node)
            print(f"Removed node: {node.getName()} from material: {material_graph.getMaterialName()}")
    except Exception as e:
        print(f"Exception encountered while processing material graph: {e}")
    return bool(nodes_to_remove)

def cleanup_scene():
    """Main function to clean up the scene."""
    any_changes = True
    iteration_count = 0

    while any_changes and iteration_count < MAX_ITERATIONS:
        any_changes = False
        iteration_count += 1

        # Cleanup material nodes
        material_names = lux.getSceneMaterials()
        for material_name in material_names:
            try:
                material_graph = lux.getMaterialGraph(name=material_name)
                if material_graph:
                    if cleanup_unused_material_nodes(material_graph):
                        any_changes = True
            except Exception as e:
                print(f"Exception encountered while processing material {material_name}: {e}")

    if iteration_count >= MAX_ITERATIONS:
        lux.getMessageBox("Scene cleanup stopped after reaching the maximum number of iterations.", "Cleanup Stopped", lux.MESSAGE_BOX_WARNING)
    else:
        lux.getMessageBox("Scene cleanup of unconnected nodes completed.", "Cleanup Complete", lux.MESSAGE_BOX_INFO)

cleanup_scene()
```

# End of Material\Delete Unused Shader and Material Graph Nodes.py

## Material Diffuse Color Apply Texture Example Agnostic.py
<a name="material-material-diffuse-color-apply-texture-example-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to apply a texture from the library to the diffuse color of a material in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def get_library_path():
    """Return the configured KeyShot resource folder."""
    return lux.getKeyShotFolder(type=lux.FOLDER_RESOURCE_ROOT)

def connect_shader_edge_to_diffuse_color(material_name, texture_relative_path):
    """
    Connects a texture file to the diffuse color parameter of a given material.

    :param material_name: The name of the material to apply the texture to.
    :param texture_relative_path: The relative path of the texture from the KeyShot "Resources Library" directory.
    """
    library_path = get_library_path()  # Get the library path based on the OS.
    texture_file_path = os.path.join(library_path, texture_relative_path)  # Full path to the texture file.

    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Retrieve the texture parameter from the texture node.
    file_param = texture_node.getParameter("texture")  # Assuming 'texture' is the correct parameter.
    if file_param:
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    else:
        print("Texture parameter not found.")
        return

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        if shader_node.getParameter("diffuse"):
            # Connect the texture node to the diffuse parameter of the shader node.
            graph.newEdge(source=texture_node, target=shader_node, param="diffuse")
            print("Shader edge successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name and relative path to the texture file.
material_name = "Cube Material"
texture_relative_path = "Textures/Color Maps/asphalt.jpg"

# Apply the texture to the diffuse color of the specified material.
connect_shader_edge_to_diffuse_color(material_name, texture_relative_path)
```

# End of Material\Material Diffuse Color Apply Texture Example Agnostic.py

## Material Diffuse Color Apply Texture Example.py
<a name="material-material-diffuse-color-apply-texture-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to apply a texture to the diffuse color of a material in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edge_to_diffuse_color(material_name, texture_file_path):
    """
    Connects a texture file to the diffuse color parameter of a given material.

    :param material_name: The name of the material to apply the texture to.
    :param texture_file_path: The file path of the texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Retrieve the texture parameter from the texture node.
    file_param = texture_node.getParameter("texture")  # Assuming 'texture' is the correct parameter.
    if file_param:
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    else:
        print("Texture parameter not found.")
        return

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        if shader_node.getParameter("diffuse"):
            # Connect the texture node to the diffuse parameter of the shader node.
            graph.newEdge(source=texture_node, target=shader_node, param="diffuse")
            print("Shader edge successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name and texture file path.
material_name = "Cube Material"
texture_file_path = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "Color Maps", "asphalt.jpg")

# Apply the texture to the diffuse color of the specified material.
connect_shader_edge_to_diffuse_color(material_name, texture_file_path)
```

# End of Material\Material Diffuse Color Apply Texture Example.py

## Material Diffuse Color Change Example.py
<a name="material-material-diffuse-color-change-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example Change Diffuse Material Color
``` python
import lux

def display_material_selection():
    scene_materials = lux.getSceneMaterials()
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def change_diffuse_color(material_name, new_color):
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    for shader_node in material_graph.getNodesFromType('lux_diffuse'):
        try:
            diffuse_param = shader_node.getParameter('diffuse')
            if diffuse_param and diffuse_param.getType() == lux.PARAMETER_TYPE_COLORALPHA:
                diffuse_param.setValue(new_color)
                print(f"Diffuse color of '{material_name}' changed to {new_color}.")
                return
        except Exception as e:
            print(f"Error setting diffuse color in shader node: {e}")

def main():
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_color = (1.0, 0.0, 0.0, 1.0)  # Example: Red color with full opacity in RGBA format

    for material_name in selected_materials:
        change_diffuse_color(material_name, new_color)

main()
```

# End of Material\Material Diffuse Color Change Example.py

## Material Diffuse Color Texture Example.py
<a name="material-material-diffuse-color-texture-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to apply a texture to the diffuse color of a material in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edge_to_diffuse_color(material_name, texture_file_path):
    """
    Connects a texture file to the diffuse color parameter of a given material.

    :param material_name: The name of the material to apply the texture to.
    :param texture_file_path: The file path of the texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Retrieve the texture parameter from the texture node.
    file_param = texture_node.getParameter("texture")  # Assuming 'texture' is the correct parameter.
    if file_param:
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    else:
        print("Texture parameter not found.")
        return

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        if shader_node.getParameter("diffuse"):
            # Connect the texture node to the diffuse parameter of the shader node.
            graph.newEdge(source=texture_node, target=shader_node, param="diffuse")
            print("Shader edge successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name and texture file path.
material_name = "Cube Material"
texture_file_path = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "Color Maps", "asphalt.jpg")

# Apply the texture to the diffuse color of the specified material.
connect_shader_edge_to_diffuse_color(material_name, texture_file_path)
```

# End of Material\Material Diffuse Color Texture Example.py

## Material IES Light Properties Change.py
<a name="material-material-ies-light-properties-change"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.6
``` python
import lux

def display_material_selection():
    """
    Display a dialog for the user to select materials from the current scene.
    """
    scene_materials = lux.getSceneMaterials()
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def change_ies_light_properties(material_name, new_properties):
    """
    Changes the color and file of IES lights in the specified material.
    """
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    changes_applied = {key: False for key in new_properties}
    for shader_node in material_graph.getNodes():
        try:
            for param_name, param_value in new_properties.items():
                param = shader_node.getParameter(param_name)
                if param and param.getType() == lux.PARAMETER_TYPE_COLOR if param_name == 'color' else lux.PARAMETER_TYPE_STRING:
                    param.setValue(param_value)
                    changes_applied[param_name] = True
                    print(f"IES light {param_name} in '{material_name}' changed to {param_value}.")

            if all(changes_applied.values()):
                return

        except Exception as e:
            print(f"Error setting IES light properties in shader node: {e}")

def main():
    """
    Main function to execute the script.
    """
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_properties = {
        'color': (1.0, 1.0, 1.0),
        'file': "C:/Users/Public/Documents/KeyShot/Textures/IES Profiles/IES Spot Light/keyshot_spot_45.ies"
    }

    for material_name in selected_materials:
        change_ies_light_properties(material_name, new_properties)

main()
```

# End of Material\Material IES Light Properties Change.py

## Material IES Light Color and File Change.py
<a name="material-material-ies-light-color-and-file-change"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Change IES Light Color and File
``` python
import os
import lux

def display_material_selection():
    scene_materials = lux.getSceneMaterials()
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def change_ies_light_properties(material_name, new_color, new_ies_file):
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    color_changed, file_changed = False, False
    for shader_node in material_graph.getNodes():
        try:
            if not color_changed:
                color_param = shader_node.getParameter('color')
                if color_param and color_param.getType() == lux.PARAMETER_TYPE_COLOR:
                    color_param.setValue(new_color)
                    print(f"IES light color in '{material_name}' changed to {new_color}.")
                    color_changed = True

            if not file_changed:
                file_param = shader_node.getParameter('file')
                if file_param and file_param.getType() == lux.PARAMETER_TYPE_STRING:
                    file_param.setValue(new_ies_file)
                    print(f"IES file in '{material_name}' changed to {new_ies_file}.")
                    file_changed = True

            if color_changed and file_changed:
                return

        except Exception as e:
            print(f"Error setting IES light properties in shader node: {e}")

def main():
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_color = (1.0, 1.0, 1.0)  # Example: White color in RGB format
    new_ies_file = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "IES Profiles", "IES Spot Light", "keyshot_spot_45.ies")  # Replace with the path to your texture file

    for material_name in selected_materials:
        change_ies_light_properties(material_name, new_color, new_ies_file)

main()
```

# End of Material\Material IES Light Color and File Change.py

## Material Physical Light Color Change.py
<a name="material-material-physical-light-color-change"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to change the color of light materials in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def display_material_selection():
    """
    Display a dialog for the user to select materials from the scene.
    """
    scene_materials = lux.getSceneMaterials()  # Get all materials in the current scene.
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    # Create a list of tuples for each material for the dialog.
    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    # Display a dialog to the user to select materials.
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None  # Return None if the user does not make a selection.
    # Return a list of materials selected by the user.
    return [mat for mat, selected in user_selection.items() if selected]

def change_spotlight_color(material_name, new_color):
    """
    Change the color parameter of a spotlight material.

    :param material_name: Name of the material to change.
    :param new_color: New color as an RGB tuple.
    """
    # Get the material graph of the specified material.
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    # Iterate through each shader node in the material graph.
    for shader_node in material_graph.getNodes():
        try:
            # Get the color parameter of the shader node.
            color_param = shader_node.getParameter('color')
            # Check if the color parameter exists and is of type color.
            if color_param and color_param.getType() == lux.PARAMETER_TYPE_COLOR:
                color_param.setValue(new_color)  # Set the new color.
                print(f"Spotlight color of '{material_name}' changed to {new_color}.")
                return
        except Exception as e:
            print(f"Error setting spotlight color in shader node: {e}")

def main():
    """
    Main function to execute the script.
    """
    # Get the user's selection of materials.
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_color = (1.0, 1.0, 1.0)  # Define the new color (white in this case).

    # Change the spotlight color for each selected material.
    for material_name in selected_materials:
        change_spotlight_color(material_name, new_color)

# Execute the main function.
main()
```

# End of Material\Material Physical Light Color Change.py

## Saves All Materials to the Library.py
<a name="material-saves-all-materials-to-the-library"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.1
# Script to save all scene materials to the material libray.
``` python
import lux
import os

def load_environment_from_library(env_filename):
    """
    Loads an environment from the KeyShot library and sets it as the active environment.
    """
    library_envs = lux.getLibraryEnvironments()
    full_env_path = None
    for lib_env_path in library_envs:
        if env_filename.lower() in os.path.basename(lib_env_path).lower():
            full_env_path = lib_env_path
            break
    
    if full_env_path is not None:
        try:
            env_name = os.path.splitext(env_filename)[0].replace(" ", "_")
            new_env = lux.newEnvironment(name=env_name, activate=True)
            if new_env.setLightingEnvironment(full_env_path):
                print(f"Environment '{env_filename}' has been successfully loaded and set.")
                return new_env
            else:
                print(f"Failed to apply environment '{env_filename}'.")
        except Exception as e:
            print(f"An error occurred while setting the environment '{env_filename}': {e}")
    else:
        print(f"The environment '{env_filename}' could not be found in the KeyShot library.")
    return None

def set_environment_parameters(env, parameters):
    """
    Sets various parameters for the specified environment.
    """
    try:
        if env:
            for param, value in parameters.items():
                if isinstance(value, tuple):
                    getattr(env, f"set{param}")(*value)
                else:
                    getattr(env, f"set{param}")(value)
            lux.setActiveEnvironment(env.getName())
            print(f"Parameters for environment '{env.getName()}' have been successfully set.")
        else:
            print("Environment not found.")
    except Exception as e:
        print(f"An error occurred while setting parameters for environment '{env.getName()}': {e}")

def configure_environment():
    """
    Configures the "3 Panels Straight 4K" environment with specific parameters.
    """
    env_filename = "3 Panels Straight 4K.klf"
    parameters = {
        'Brightness': 1.0,
        'Size': 300.0,
        'Height': 0.0,
        'Rotation': 0.0,
        'BackgroundColor': ((255, 255, 255),),  # Needs to be a tuple of a tuple for colors
        'GroundSize': 0.01,
        'GroundShadows': False,
        'OcclusionGroundShadows': False,
        'GroundReflections': False,
        'FlattenGround': False
    }
    
    environment = load_environment_from_library(env_filename)
    if environment:
        set_environment_parameters(environment, parameters)

configure_environment()
```

# End of Material\Saves All Materials to the Library.py

## ShaderEdge Connect.py
<a name="material-shaderedge-connect"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example of graphing a Color Gradient shader edge node.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return

    # Set up the Color Gradient node if necessary.
    # This step is customizable based on specific gradient requirements.

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "ColorGradient Rainbow"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)
```

# End of Material\ShaderEdge Connect.py

## Batch Create Multi-Material Sub-Materials with Custom Advanced Shader Parameters.py
<a name="batch-create-multi-material-sub-materials-with-custom-advanced-shader-parameters"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Batch Create Multi-Material Sub-Materials with Custom Advanced Shader Parameters.
```python
import lux  # Import the KeyShot built-in module 'lux'
import re  # Import the regular expression module for renaming

# Constants for Shader Types
SHADER_TYPE_ADVANCED = 'lux_advanced'

# Constants for Parameter Types
PARAMETER_TYPE_COLOR = 13
PARAMETER_TYPE_COLORALPHA = 14
PARAMETER_TYPE_FLOAT = 4
PARAMETER_TYPE_BOOLEAN = 1
PARAMETER_TYPE_INTEGER = 2
PARAMETER_TYPE_TEXTURE = 14
PARAMETER_TYPE_BUMP = 65539

# Parameters for the Advanced Shader
PARAMETERS = [
    ("alpha", PARAMETER_TYPE_FLOAT, 1.0),
    ("ambient", PARAMETER_TYPE_COLOR, (0, 0, 0)),
    ("apply_bump_to_labels", PARAMETER_TYPE_BOOLEAN, False),
    ("bumpmap", PARAMETER_TYPE_BUMP, None),
    ("diffuse", PARAMETER_TYPE_COLORALPHA, (0, 0, 0, 1.0)),
    ("diffuse_transmission", PARAMETER_TYPE_COLOR, (0, 0, 0)),
    ("fresnel", PARAMETER_TYPE_BOOLEAN, True),
    ("glossy", PARAMETER_TYPE_BOOLEAN, True),
    ("glossy_samples", PARAMETER_TYPE_INTEGER, 9),
    ("ior", PARAMETER_TYPE_FLOAT, 1.5),
    ("opacity_mode", PARAMETER_TYPE_INTEGER, 0),
    ("opacitymap", PARAMETER_TYPE_TEXTURE, None),
    ("opacitymap_mode", PARAMETER_TYPE_INTEGER, 0),
    ("roughness", PARAMETER_TYPE_FLOAT, 0.0),
    ("roughness_transmission", PARAMETER_TYPE_FLOAT, 0.0),
    ("specular", PARAMETER_TYPE_COLOR, (1.0, 1.0, 1.0)),
    ("specular_transmission", PARAMETER_TYPE_COLOR, (0, 0, 0)),
    ("use_diffuse_map_alpha", PARAMETER_TYPE_BOOLEAN, False)
]

def display_material_selection():
    scene_materials = lux.getSceneMaterials()  # Retrieve all materials from the current scene
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def display_color_selection():
    colors = {
        "Red": (1.0, 0.0, 0.0, 1.0),
        "Green": (0.0, 1.0, 0.0, 1.0),
        "Blue": (0.0, 0.0, 1.0, 1.0)
    }
    color_selection_elements = [(name, lux.DIALOG_CHECK, name, False) for name in colors.keys()]
    user_selection = lux.getInputDialog(title="Select Colors", values=color_selection_elements)
    if not user_selection:
        return None

    selected_colors = [name for name, selected in user_selection.items() if selected]
    if not selected_colors:
        return None

    return [(name, colors[name]) for name in selected_colors]

def create_sub_material(material_name, color_name, color_value):
    new_material_name = f"{material_name}_{color_name}"
    lux.createSceneMaterial(new_material_name)  # Create a new material
    material_graph = lux.getMaterialGraph(new_material_name)  # Get the material graph

    if material_graph is None:
        print(f"Failed to create material graph for '{new_material_name}'.")
        return None

    advanced_shader = material_graph.newNode(SHADER_TYPE_ADVANCED)
    for param_name, param_type, default_value in PARAMETERS:
        param = advanced_shader.getParameter(param_name)
        if param and not param.isPure():
            param.setValue(default_value)

    diffuse_param = advanced_shader.getParameter('diffuse')
    if diffuse_param and diffuse_param.getType() == PARAMETER_TYPE_COLORALPHA:
        diffuse_param.setValue(color_value)
        print(f"Diffuse color of '{color_name}' sub-material set to {color_value}.")

    material_graph.newEdge(advanced_shader, material_graph.getRoot(), 'surface')
    print(f"Created sub-material '{new_material_name}' with diffuse color {color_value}.")
    return new_material_name

def create_multi_material_with_sub_materials(material_name, colors):
    sub_material_names = []
    for color_name, color_value in colors:
        sub_material_name = create_sub_material(material_name, color_name, color_value)
        if sub_material_name:
            sub_material_names.append(sub_material_name)

    material_graph = lux.getMaterialGraph(material_name)
    if material_graph is None:
        print(f"Material graph for {material_name} not found.")
        return

    material_graph.setMultiMaterial(enable=True)
    multi_material = lux.getMultiMaterial(material_name)

    multi_material.setSubMaterials(sub_material_names)
    print(f"Multi-Material '{material_name}' now contains sub-materials: {sub_material_names}")

def rename_multi_material(material_name, name_count):
    """Rename multi-material and its sub-materials by sanitizing their names."""
    try:
        multi_material = lux.getMultiMaterial(material_name)
        if multi_material:
            old_name = multi_material.getName()
            new_name = sanitize_material_name(old_name, name_count)
            if new_name != old_name:
                multi_material.setName(new_name)
                if multi_material.getName() == new_name:
                    print(f"Renamed multi-material from '{old_name}' to '{new_name}'")
                else:
                    print(f"Failed to rename multi-material from '{old_name}' to '{new_name}'")

            sub_materials = multi_material.getSubMaterials()
            for sub_material in sub_materials:
                old_sub_name = sub_material.getName()
                new_sub_name = sanitize_material_name(old_sub_name, name_count)
                if new_sub_name != old_sub_name:
                    sub_material.setName(new_sub_name)
                    if sub_material.getName() == new_sub_name:
                        print(f"Renamed sub-material from '{old_sub_name}' to '{new_sub_name}'")
                    else:
                        print(f"Failed to rename sub-material from '{old_sub_name}' to '{new_sub_name}'")
    except Exception as e:
        print(f"Error with multi-material '{material_name}': {e}")

def sanitize_material_name(name, name_count):
    new_name = re.sub(r'#\d+', '', name).strip() + "_MM"
    if new_name in name_count:
        name_count[new_name] += 1
        new_name = f"{new_name}_{name_count[new_name]}"
    else:
        name_count[new_name] = 1
    return new_name

def main():
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    selected_colors = display_color_selection()
    if not selected_colors:
        print("No colors selected or operation cancelled.")
        return

    for material_name in selected_materials:
        create_multi_material_with_sub_materials(material_name, selected_colors)
        rename_multi_material(material_name, {})  # Ensure renaming after converting to multi-material

main()
```

# End of Batch Create Multi-Material Sub-Materials with Custom Advanced Shader Parameters.py
<a name="end-material-batch-create-multi-material-sub-materials-with-custom-advanced-shader-parameters"></a>

## Material Color Gradient ShaderEdge Diffuse Material Color Connect.py
<a name="color-gradient-shaderedge-diffuse-material-color-connect"></a>

# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example of graphing a Color Gradient shader edge node.
## Example: Connecting a Color Gradient to Diffuse Color
#This script demonstrates how to connect a Color Gradient shader to the diffuse color parameter of a given material in KeyShot.
```python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return

    # Set up the Color Gradient node if necessary.
    # This step is customizable based on specific gradient requirements.

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "Center"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)

## End of Color Gradient ShaderEdge Diffuse Material Color Connect.py
<a name="color-gradient-shaderedge-diffuse-material-color-connect"></a>
```

## Material Gradient View Direction.py
<a name="material-color-gradient-view-direction"></a>

# AUTHOR LUX DT ChatGPT
# VERSION 0.2.6
# Example of graphing a Color Gradient shader edge node with manual parameter setting.
```python
import lux  # Import the KeyShot built-in module 'lux'.

def create_rainbow_gradient_node(graph):
    """
    Creates a simplified Color Gradient shader node and adds it to the provided material graph.
    
    :param graph: The material graph where the Color Gradient node will be added.
    :return: The created Color Gradient node.
    """
    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return None

    # Print available parameters for debugging
    parameters = gradient_node.getParameters()
    print("Available parameters for 'lux_color_gradient' node:")
    for param in parameters:
        print(f"Parameter Name: {param.getName()}")

    # Set other gradient properties
    try:
        gradient_node.getParameter("gradient_type").setValue(9)  # View-dependent gradient
        gradient_node.getParameter("blend").setValue(True)
        gradient_node.getParameter("invert").setValue(False)
        gradient_node.getParameter("scale").setValue(1.0)
        gradient_node.getParameter("shift").setValue(0.0)
        gradient_node.getParameter("angle").setValue(0.0)
        gradient_node.getParameter("repeat").setValue(False)
        print("Other gradient properties set successfully.")
    except Exception as e:
        print(f"Error setting gradient properties: {e}")

    return gradient_node

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create the Color Gradient node and configure it
    gradient_node = create_rainbow_gradient_node(graph)
    if gradient_node is None:
        return

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "Rainbow Gradient Material"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)
```

## End of Color Gradient View Direction.py
<a name="color-gradient-view-direction"></a>
