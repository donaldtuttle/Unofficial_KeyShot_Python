# Scripting Examples: Loading and Materials

[Scripting Examples TOC](../Scripting_Examples.md)

## Load Enviorment From Library and Apply Settings.py
<a name="load-load-enviorment-from-library-and-apply-settings"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Script Applies Enviorment from library.  Uses the "ENV" class.
``` python
import lux
import os

# Function to load environments
def load_environment_from_library(env_filename):
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

# Function to set environment parameters
def set_environment_parameters(env, brightness, size, height, rotation):
    try:
        if env:
            env.setBrightness(brightness)
            env.setSize(size)
            env.setHeight(height)
            env.setRotation(rotation)
            env.setBackgroundColor((255, 255, 255))
            env.setGroundSize(0.01)
            env.setGroundShadows(False)
            env.setOcclusionGroundShadows(False)
            env.setGroundReflections(False)
            env.setFlattenGround(False)
            lux.setActiveEnvironment(env.getName())
            lux.getActiveEnvironment().setBackgroundColor((255, 255, 255))
            print(f"Parameters for environment '{env.getName()}' have been successfully set.")
        else:
            print("Environment not found.")
    except Exception as e:
        print(f"An error occurred while setting parameters for environment '{env.getName()}': {e}")

# Combined function to configure the "3 Panel 4K" environment
def configure_environment():
    env_filename = "3 Panels Straight 4K.klf"
    brightness = 1.0
    size = 1.0
    height = 0.0
    rotation = 0.0
    
    environment = load_environment_from_library(env_filename)
    if environment:
        set_environment_parameters(environment, brightness, size, height, rotation)

# Run the configuration
configure_environment()
```
# End of Load\Load Enviorment From Library and Apply Settings.py

## Load Enviorment From Library.py
<a name="load-load-enviorment-from-library"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Script Applies Enviorment from library.  Uses the "ENV" class.
``` python
import lux
import os

def load_environment_from_library(env_filename):
    # Define the KeyShot library path. This may need to be adapted for your specific system or KeyShot version.
    keyshot_lib_path = "C:/Users/Public/Documents/KeyShot/Environments"
    
    # Normalize the KeyShot library path
    keyshot_lib_path = os.path.normpath(keyshot_lib_path)
    
    # Retrieve the list of environments from KeyShot's library
    library_envs = lux.getLibraryEnvironments()
    
    # Attempt to find the full path of the desired environment file in the library
    full_env_path = None
    for lib_env_path in library_envs:
        if env_filename.lower() in os.path.basename(lib_env_path).lower():
            full_env_path = lib_env_path
            break
    
    # Check if the desired environment file was found
    if full_env_path is not None:
        try:
            # Create and activate a new environment in the scene with the found environment file
            new_env = lux.newEnvironment(name=os.path.splitext(env_filename)[0], activate=True)
            if new_env.setLightingEnvironment(full_env_path):
                print(f"Environment '{env_filename}' has been successfully loaded and set.")
            else:
                print(f"Failed to apply environment '{env_filename}'.")
        except Exception as e:
            print(f"An error occurred while setting the environment '{env_filename}': {e}")
    else:
        print(f"The environment '{env_filename}' could not be found in the KeyShot library.")

# Example usage
env_filename = "3 Panels Straight 4K.klf"  # Update this with the exact filename of the environment you wish to load
load_environment_from_library(env_filename)
```
# End of Load\Load Enviorment From Library.py

## Load Ground Plane into Default Model Set.py
<a name="load-load-ground-plane-into-default-model-set"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script that loads a ground plane from the keyshot resources library.  Must have Ground Plane Model. 
``` python
import lux
import os

def get_library_path():
    return os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_MODELS), "Ground")

def add_ground_plane_to_default_model_set():
    default_model_set_name = "Default"

    # Ensure the default model set exists
    lux.newModelSet(name=default_model_set_name)
    lux.setModelSets([default_model_set_name])
    print(f"Activated or created model set: {default_model_set_name}")
    
    library_path = get_library_path()
    ground_plane_model = "Ground.bip"
    ground_plane_path = os.path.join(library_path, ground_plane_model)
    
    if not os.path.exists(ground_plane_path):
        print(f"Ground plane model '{ground_plane_model}' not found in the KeyShot Resources Library.")
        return
    
    print(f"Importing ground plane model from: {ground_plane_path}")
    import_options = {
        'import_type': 0,
        'snap_to_ground': True,
        'center_geometry': False,
        'merge_objects': False
    }
    lux.importFile(ground_plane_path, opts=import_options)
    print("Ground plane model imported and assigned to the default model set.")

def main():
    add_ground_plane_to_default_model_set()

if __name__ == "__main__":
    main()
```

# End of Load\Load Ground Plane into Default Model Set.py

## Load Ground Plane.py
<a name="load-load-ground-plane"></a>
# AUTHOR LUX DT ChatGPT4
# VERSION 0.1.5
# Import Ground Plane Model from Resources Library and assign to Default Model Set.
``` python
import lux
import os

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system.
    """
    if os.name == 'nt':  # Windows
        library_path = os.path.join(os.environ['PUBLIC'], "Documents", "KeyShot", "Models", "Ground Plane")
    else:  # macOS and Unix/Linux
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot", "Models", "Ground Plane")
    return library_path

def add_ground_plane_to_default_model_set():
    """
    Imports the ground plane model from the KeyShot Resources Model Library and assigns it to the default model set.
    """
    default_model_set_name = "Default"
    
    # Check if the default model set exists and set it as active
    model_sets = lux.getModelSets()
    if default_model_set_name in model_sets:
        lux.setModelSets([default_model_set_name])
        print(f"Activated model set: {default_model_set_name}")
    else:
        print(f"Model set '{default_model_set_name}' not found. Creating a new one.")
        lux.newModelSet(name=default_model_set_name)
        lux.setModelSets([default_model_set_name])
    
    # Determine the path to the ground plane model
    library_path = get_library_path()
    ground_plane_model = "Ground Plane.bip"  # Example ground plane model filename
    ground_plane_path = os.path.join(library_path, ground_plane_model)
    
    if not os.path.exists(ground_plane_path):
        print(f"Ground plane model '{ground_plane_model}' not found in the KeyShot Resources Library.")
        return
    
    # Import the ground plane model without clearing the scene
    print(f"Importing ground plane model from: {ground_plane_path}")
    import_options = {
        'import_type': 0,  # Add to scene
        'snap_to_ground': True,
        'center_geometry': False,
        'merge_objects': False
    }
    lux.importFile(ground_plane_path, opts=import_options)
    print("Ground plane model imported and assigned to the default model set.")

def main():
    add_ground_plane_to_default_model_set()

if __name__ == "__main__":
    main()
```

# End of Load\Load Ground Plane.py

## Load Library Texture Assign to Diffuse Material Bump Add.py
<a name="load-load-library-texture-assign-to-diffuse-material-bump-add"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.5
# Script to apply a texture to the bump map of a diffuse material in KeyShot.
``` python
import lux

def create_texture_node(graph, texture_file_path):
    """
    Creates a texture node and sets the texture file path.
    """
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node:
        try:
            file_param = texture_node.getParameter("texture")
            file_param.setValue(texture_file_path)
            return texture_node
        except Exception as e:
            print(f"Error setting texture file path: {e}")
    return None

def connect_textures_to_bump(material_name, texture_file_paths):
    """
    Connects multiple textures to the bump parameters of a given material.
    """
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    texture_nodes = [create_texture_node(graph, path) for path in texture_file_paths]
    if any(node is None for node in texture_nodes):
        print("Failed to create all texture nodes.")
        return

    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    try:
        for idx, node in enumerate(texture_nodes):
            graph.newEdge(source=node, target=bump_add_node, param=f"bump_{idx + 1}")
            print(f"Successfully created edge from texture node to bump add node (bump_{idx + 1}).")
    except Exception as e:
        print(f"Failed to create edge from texture node to bump add node: {e}")
        return

    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump textures successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
material_name = "Cube Material"
texture_file_paths = [
    "C:/Users/Public/Documents/KeyShot/Textures/ash.jpg",
    "C:/Users/Public/Documents/KeyShot/Textures/Color Maps/asphalt.jpg"
]

connect_textures_to_bump(material_name, texture_file_paths)
```

# End of Load\Load Library Texture Assign to Diffuse Material Bump Add.py

## Adjust Texture Scale Scene Units 1cm.py
<a name="material-adjust-texture-scale-scene-units-1cm"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Resets the texture Scale Width and Height to 1cm.  KeyShot imports in Meters.
``` python
import os
import lux

# Replace with your material name
material_name = "Cube Material"

# Access the Material Graph
graph = lux.getMaterialGraph(material_name)

# Create an Image Texture Node
texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)

# Set the texture file
texture_file_parameter_name = "texture"
texture_path = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "Color Maps", "asphalt.jpg")
texture_node.getParameter(texture_file_parameter_name).setValue(texture_path)

# Adjust the UV scale to 1 cm (assuming scene units are in meters)
texture_node.getParameter("uv_scale_u").setValue(0.01)  # Adjusting U scale to 1 cm
texture_node.getParameter("uv_scale_v").setValue(0.01)  # Adjusting V scale to 1 cm

# Access the Material's Root Node
root_node = graph.getRoot()

# Get the shader node connected to the surface parameter of the root node
surface_shader_edge = root_node.getInputEdge("surface")
if not surface_shader_edge:
    print("No shader connected to the surface parameter.")
    exit()

surface_shader_node = surface_shader_edge.getSourceNode()

# Find the diffuse color parameter and connect the texture node
for parameter in surface_shader_node.getParameters():
    if parameter.getType() in [lux.PARAMETER_TYPE_COLOR, lux.PARAMETER_TYPE_COLORALPHA]:
        try:
            graph.newEdge(texture_node, surface_shader_node, parameter.getName())
            print(f"Texture applied to '{parameter.getName()}' parameter of surface shader in '{material_name}'.")
            exit()
        except Exception as e:
            print(f"Error applying texture to '{parameter.getName()}': {e}")

print("No suitable color parameter found in the surface shader node.")
```

# End of Material\Adjust Texture Scale Scene Units 1cm.py

## Apply 2 Library Textures to Diffuse Material Bump Add.py
<a name="material-apply-2-library-textures-to-diffuse-material-bump-add"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.6
# Script to apply two textures to the bump map of a diffuse material in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edges_to_bump(material_name, texture_file_path_1, texture_file_path_2):
    """
    Connects two texture files to the bump parameters of a given material.

    :param material_name: The name of the material to apply the bump textures to.
    :param texture_file_path_1: The file path of the first bump texture to apply.
    :param texture_file_path_2: The file path of the second bump texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node for the first texture.
    texture_node_1 = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node_1 is None:
        print("Failed to create first texture node.")
        return

    # Set the first texture file path using the correct parameter name.
    try:
        file_param_1 = texture_node_1.getParameter("texture")
        file_param_1.setValue(texture_file_path_1)  # Set the file path of the first texture.
    except Exception as e:
        print(f"Error setting first texture file path: {e}")
        return

    # Create a new texture node for the second texture.
    texture_node_2 = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node_2 is None:
        print("Failed to create second texture node.")
        return

    # Set the second texture file path using the correct parameter name.
    try:
        file_param_2 = texture_node_2.getParameter("texture")
        file_param_2.setValue(texture_file_path_2)  # Set the file path of the second texture.
    except Exception as e:
        print(f"Error setting second texture file path: {e}")
        return

    # Create a bump add node in the material graph.
    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    # Debugging: Print IDs and parameter names
    print(f"Texture Node 1 ID: {texture_node_1.getID()}, Texture Node 2 ID: {texture_node_2.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
    print(f"Connecting texture node 1's 'texture' parameter to bump add node's 'bump_1' parameter")
    print(f"Connecting texture node 2's 'texture' parameter to bump add node's 'bump_2' parameter")

    # Connect the first texture node to the bump add node.
    try:
        graph.newEdge(source=texture_node_1, target=bump_add_node, param="bump_1")
        print("Successfully created edge from first texture node to bump add node.")
    except Exception as e:
        print(f"Failed to create edge from first texture node to bump add node: {e}")
        return

    # Connect the second texture node to the bump add node.
    try:
        graph.newEdge(source=texture_node_2, target=bump_add_node, param="bump_2")
        print("Successfully created edge from second texture node to bump add node.")
    except Exception as e:
        print(f"Failed to create edge from second texture node to bump add node: {e}")
        return

    # Connect the bump add node to the diffuse material's bumpmap parameter.
    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            print(f"Diffuse Node ID: {shader_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump textures successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
# Define the material name and texture file paths.
material_name = "Cube Material"
texture_file_path_1 = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "ash.jpg")
texture_file_path_2 = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "Color Maps", "asphalt.jpg")

# Apply the bump textures to the specified material.
connect_shader_edges_to_bump(material_name, texture_file_path_1, texture_file_path_2)
```

# End of Material\Apply 2 Library Textures to Diffuse Material Bump Add.py

## Apply Library Color by Name to Diffuse Material Color.py
<a name="material-apply-library-color-by-name-to-diffuse-material-color"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example Script Applies Color from library to a material.
``` python
import lux

def assign_library_color_to_material_by_name(material_name, color_name):
    # Retrieve the material graph for the specified material
    material_graph = lux.getMaterialGraph(material_name)
    if not material_graph:
        print(f"Material '{material_name}' not found in the current scene.")
        return

    # Correct approach to iterate through nodes and find the 'diffuse' parameter
    success = False
    for shader_node in material_graph.getNodes():
        # Iterate through parameters to find 'diffuse'
        for parameter in shader_node.getParameters():
            if parameter.getName() == 'diffuse' and parameter.getType() == 14:  # Type 14 for color
                try:
                    # Set the diffuse color by name, assuming it exists in KeyShot's color library
                    parameter.setValue(color_name)
                    print(f"Color '{color_name}' successfully assigned to material '{material_name}'.")
                    success = True
                    break  # Exit after successfully setting the color
                except Exception as e:
                    print(f"Failed to assign color '{color_name}' to material '{material_name}': {e}")
        if success:
            break

    if not success:
        print(f"Failed to find a 'diffuse' parameter for material '{material_name}' or apply color '{color_name}'.")

# Example usage
assign_library_color_to_material_by_name("Cube Material", "PANTONE 186 C")
```

# End of Material\Apply Library Color by Name to Diffuse Material Color.py

## Apply Multiple Library Textures to Diffuse Material Bump Add.py
<a name="material-apply-multiple-library-textures-to-diffuse-material-bump-add"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.5
# Script to apply a texture to the bump map of a diffuse material in KeyShot.
``` python
import lux

def create_texture_node(graph, texture_file_path):
    """
    Creates a texture node and sets the texture file path.
    """
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node:
        try:
            file_param = texture_node.getParameter("texture")
            file_param.setValue(texture_file_path)
            return texture_node
        except Exception as e:
            print(f"Error setting texture file path: {e}")
    return None

def connect_textures_to_bump(material_name, texture_file_paths):
    """
    Connects multiple textures to the bump parameters of a given material.
    """
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    texture_nodes = [create_texture_node(graph, path) for path in texture_file_paths]
    if any(node is None for node in texture_nodes):
        print("Failed to create all texture nodes.")
        return

    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    try:
        for idx, node in enumerate(texture_nodes):
            graph.newEdge(source=node, target=bump_add_node, param=f"bump_{idx + 1}")
            print(f"Successfully created edge from texture node to bump add node (bump_{idx + 1}).")
    except Exception as e:
        print(f"Failed to create edge from texture node to bump add node: {e}")
        return

    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump textures successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
material_name = "Cube Material"
texture_file_paths = [
    "C:/Users/Public/Documents/KeyShot/Textures/ash.jpg",
    "C:/Users/Public/Documents/KeyShot/Textures/Color Maps/asphalt.jpg"
]

connect_textures_to_bump(material_name, texture_file_paths)
```

# End of Material\Apply Multiple Library Textures to Diffuse Material Bump Add.py

## Apply Library Texture to Diffuse Material Bump Add.py
<a name="material-apply-library-texture-to-diffuse-material-bump-add"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.5
# Script to apply a texture to the bump map of a diffuse material in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edge_to_bump(material_name, texture_file_path):
    """
    Connects a texture file to the bump parameter of a given material.

    :param material_name: The name of the material to apply the bump texture to.
    :param texture_file_path: The file path of the bump texture to apply.
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

    # Set the texture file path using the correct parameter name.
    try:
        file_param = texture_node.getParameter("texture")
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    except Exception as e:
        print(f"Error setting texture file path: {e}")
        return

    # Create a bump add node in the material graph.
    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    # Debugging: Print IDs and parameter names
    print(f"Texture Node ID: {texture_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
    print(f"Connecting texture node's 'texture' parameter to bump add node's 'bump_1' parameter")

    # Connect the texture node to the bump add node.
    try:
        texture_to_bump_edge = graph.newEdge(source=texture_node, target=bump_add_node, param="bump_1")
        print("Successfully created edge from texture node to bump add node.")
    except Exception as e:
        print(f"Failed to create edge from texture node to bump add node: {e}")
        return

    # Connect the bump add node to the diffuse material's bumpmap parameter.
    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            print(f"Diffuse Node ID: {shader_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump texture successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
# Define the material name and texture file path.
material_name = "Cube Material"
texture_file_path = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "Color Maps", "asphalt.jpg")

# Apply the bump texture to the specified material.
connect_shader_edge_to_bump(material_name, texture_file_path)
```

# End of Material\Apply Library Texture to Diffuse Material Bump Add.py

## Apply Library Texture to Diffuse Material Bump.py
<a name="material-apply-library-texture-to-diffuse-material-bump"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.5
# Script to apply a texture to the bump map of a diffuse material in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edge_to_bump(material_name, texture_file_path):
    """
    Connects a texture file to the bump parameter of a given material.

    :param material_name: The name of the material to apply the bump texture to.
    :param texture_file_path: The file path of the bump texture to apply.
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

    # Set the texture file path using the correct parameter name.
    try:
        file_param = texture_node.getParameter("texture")
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    except Exception as e:
        print(f"Error setting texture file path: {e}")
        return

    # Create a bump add node in the material graph.
    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    # Debugging: Print IDs and parameter names
    print(f"Texture Node ID: {texture_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
    print(f"Connecting texture node's 'texture' parameter to bump add node's 'bump_1' parameter")

    # Connect the texture node to the bump add node.
    try:
        texture_to_bump_edge = graph.newEdge(source=texture_node, target=bump_add_node, param="bump_1")
        print("Successfully created edge from texture node to bump add node.")
    except Exception as e:
        print(f"Failed to create edge from texture node to bump add node: {e}")
        return

    # Connect the bump add node to the diffuse material's bumpmap parameter.
    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            print(f"Diffuse Node ID: {shader_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump texture successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
# Define the material name and texture file path.
material_name = "Cube Material"
texture_file_path = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "Color Maps", "asphalt.jpg")

# Apply the bump texture to the specified material.
connect_shader_edge_to_bump(material_name, texture_file_path)
```

# End of Material\Apply Library Texture to Diffuse Material Bump.py

## Apply Library Texture to Diffuse Material Color.py
<a name="material-apply-library-texture-to-diffuse-material-color"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Assign Texture from Library to the Color of a Diffuse Material.
``` python
import os
import lux

def connect_texture_to_diffuse_color(material_name, texture_file_path):
    """
    Connects a texture file to the diffuse color parameter of a given material.

    Parameters:
    material_name (str): The name of the material to apply the texture to.
    texture_file_path (str): The file path of the texture to apply.
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

    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    connected = False
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the texture node to the diffuse parameter of the shader node.
            graph.newEdge(source=texture_node, target=shader_node, param="diffuse")
            print(f"Texture '{texture_file_path}' connected to the diffuse color of '{material_name}'.")
            connected = True
            break

    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
material_name = "Cube Material"
texture_file_path = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "Color Maps", "asphalt.jpg")
connect_texture_to_diffuse_color(material_name, texture_file_path)
```

# End of Material\Apply Library Texture to Diffuse Material Color.py

## Batch Multi-Material Diffuse Sub-Material Assign Texture Default Units m.py
<a name="material-batch-multi-material-diffuse-sub-material-assign-texture-default-units-m"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script for automating multi-material creation and Sub-Material (Diffuse) texture application in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.
import os  # Import the os module for file path operations.

def display_material_selection_and_directory():
    """
    Display a dialog for the user to select materials and a directory for textures.
    """
    scene_materials = lux.getSceneMaterials()  # Get all materials in the current scene.
    if not scene_materials:
        lux.getMessageBox("No materials found in the scene.", "Error", lux.MESSAGE_BOX_CRITICAL)
        return None, None

    # Create a list of tuples for each material for the dialog.
    material_values = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    directory_values = [("directory", lux.DIALOG_FOLDER, "Bitmap directory:", None)]
    # Display a dialog to get user's selection of materials and directory.
    opts = lux.getInputDialog(title="Select Material and Directory", values=material_values + directory_values)
    if not opts:
        return None, None  # Return None if the user does not make a selection.

    selected_materials = [mat for mat, selected in opts.items() if selected and mat in scene_materials]
    directory = opts['directory']
    return selected_materials, directory

def create_and_apply_texture(material_name, texture_path):
    """
    Create a new material node and apply a texture to it.

    :param material_name: Name of the material to apply the texture to.
    :param texture_path: Path of the texture file.
    """
    material_graph = lux.getMaterialGraph(material_name)  # Get the material graph.
    texture_node = material_graph.newNode('__texture')  # Create a new texture node.
    texture_node.getParameter('texture').setValue(texture_path)  # Set the texture file.

    # Connect the texture node to the color parameter of the material.
    for node in material_graph.getNodes():
        for param in node.getParameters():
            if param.getType() in [lux.PARAMETER_TYPE_COLOR, lux.PARAMETER_TYPE_COLORALPHA]:
                material_graph.newEdge(texture_node, node, param.getName())
                return

def process_material(material_name, directory):
    """
    Process each material to create sub-materials with textures from the directory.

    :param material_name: Name of the material to process.
    :param directory: Directory containing texture files.
    """
    bitmap_files = [f for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in ['.png', '.jpg', '.jpeg']]
    if not bitmap_files:
        print(f"No bitmap files found in directory: {directory}")
        return

    # Convert to MultiMaterial if necessary.
    multi_material = lux.getMultiMaterial(material_name)
    if not multi_material:
        lux.createMultiMaterial(material_name)
        multi_material = lux.getMultiMaterial(material_name)

    # Create a new sub-material for each texture file and apply the texture.
    for file in bitmap_files:
        texture_path = os.path.join(directory, file)
        new_material_name = f"{material_name}_{os.path.splitext(file)[0]}"
        lux.createSceneMaterial(new_material_name)  # Create a new material.
        create_and_apply_texture(new_material_name, texture_path)  # Apply texture.

        # Update the multi-material with the new sub-material.
        sub_materials = multi_material.getSubMaterials()
        sub_materials.append(new_material_name)
        multi_material.setSubMaterials(sub_materials)

        print(f"Added sub-material '{new_material_name}' with texture '{file}' to '{material_name}'.")

def main():
    """
    Main function to execute the script.
    """
    selected_materials, directory = display_material_selection_and_directory()
    if not selected_materials or not directory:
        print("Operation cancelled or invalid input.")
        return

    # Process each selected material.
    for material_name in selected_materials:
        process_material(material_name, directory)

# Execute the main function.
main()
```

# End of Material\Batch Multi-Material Diffuse Sub-Material Assign Texture Default Units m.py

## Batch Multi-Material Diffuse Sub-Material Assign Texture Scale Units cm.py
<a name="material-batch-multi-material-diffuse-sub-material-assign-texture-scale-units-cm"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Script for automating the creation of sub-materials and applying textures with UV scale adjustment in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.
import os  # Import the os module for file path operations.

def display_material_selection_and_directory():
    """
    Display a dialog for the user to select materials and a directory for textures.
    """
    scene_materials = lux.getSceneMaterials()  # Get all materials in the current scene.
    if not scene_materials:
        lux.getMessageBox("No materials found in the scene.", "Error", lux.MESSAGE_BOX_CRITICAL)
        return None, None

    # Create dialog fields for material selection and directory.
    material_values = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    directory_values = [("directory", lux.DIALOG_FOLDER, "Bitmap directory:", None)]
    opts = lux.getInputDialog(title="Select Material and Directory", values=material_values + directory_values)
    if not opts:
        return None, None  # Return None if the user does not make a selection.

    selected_materials = [mat for mat, selected in opts.items() if selected and mat in scene_materials]
    directory = opts['directory']
    return selected_materials, directory

def create_and_apply_texture(material_name, texture_path):
    """
    Create a new material node, apply a texture, and set UV scale.

    :param material_name: Name of the material to apply the texture to.
    :param texture_path: Path of the texture file.
    """
    material_graph = lux.getMaterialGraph(material_name)  # Get the material graph.
    texture_node = material_graph.newNode('__texture')  # Create a new texture node.
    texture_node.getParameter('texture').setValue(texture_path)  # Set the texture file.

    # Set the UV scale for the texture.
    texture_node.getParameter("uv_scale_u").setValue(0.01)  # Set scale for U coordinate.
    texture_node.getParameter("uv_scale_v").setValue(0.01)  # Set scale for V coordinate.

    # Connect the texture node to the color parameter of the material.
    for node in material_graph.getNodes():
        for param in node.getParameters():
            if param.getType() in [lux.PARAMETER_TYPE_COLOR, lux.PARAMETER_TYPE_COLORALPHA]:
                material_graph.newEdge(texture_node, node, param.getName())
                return

def process_material(material_name, directory):
    """
    Process each material to create sub-materials with textures from the directory.

    :param material_name: Name of the material to process.
    :param directory: Directory containing texture files.
    """
    bitmap_files = [f for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in ['.png', '.jpg', '.jpeg']]
    if not bitmap_files:
        print(f"No bitmap files found in directory: {directory}")
        return

    # Convert to MultiMaterial if necessary.
    multi_material = lux.getMultiMaterial(material_name)
    if not multi_material:
        lux.createMultiMaterial(material_name)
        multi_material = lux.getMultiMaterial(material_name)

    # Create a new sub-material for each texture file and apply the texture with UV scaling.
    for file in bitmap_files:
        texture_path = os.path.join(directory, file)
        new_material_name = f"{material_name}_{os.path.splitext(file)[0]}"
        lux.createSceneMaterial(new_material_name)  # Create a new material.
        create_and_apply_texture(new_material_name, texture_path)  # Apply texture.

        # Update the multi-material with the new sub-material.
        sub_materials = multi_material.getSubMaterials()
        sub_materials.append(new_material_name)
        multi_material.setSubMaterials(sub_materials)

        print(f"Added sub-material '{new_material_name}' with texture '{file}' to '{material_name}'.")

def main():
    """
    Main function to execute the script.
    """
    selected_materials, directory = display_material_selection_and_directory()
    if not selected_materials or not directory:
        print("Operation cancelled or invalid input.")
        return

    # Process each selected material.
    for material_name in selected_materials:
        process_material(material_name, directory)

# Execute the main function.
main()
```

# End of Material\Batch Multi-Material Diffuse Sub-Material Assign Texture Scale Units cm.py

## Batch Save Scene Sub-Materials to Material Library.py
<a name="material-batch-save-scene-sub-materials-to-material-library"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to save the scene's materials and multi-material sub-materials to the material library in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def get_library_path():
    """Return the folder relative to the KeyShot Materials library."""
    return "."

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The parent node from which children are to be gathered.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def save_sub_materials_to_library(multi_material_name, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: Name of the multi-material.
    :param saved_materials: Set of already saved material names to avoid duplication.
    """
    library_path = get_library_path()  # The folder is relative to the Materials library.
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Retrieve sub-materials of the multi-material.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        # Check if the sub-material has not been saved already.
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene():
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Iterate through all nodes in the scene and process their materials.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name:
            save_sub_materials_to_library(material_name, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    # Process the currently open KeyShot scene.
    process_current_scene()

# Execute the main function.
main()
```

# End of Material\Batch Save Scene Sub-Materials to Material Library.py

## Batch Save All Scene Materials Without Duplicates.py
<a name="material-batch-save-all-scene-materials-without-duplicates"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.1
# Script to save all scene materials to the material libray.
``` python
import lux

def get_library_path():
    """Return the folder relative to the KeyShot Materials library."""
    return "."

def get_all_children(node):
    """
    Recursively get all children of a node.
    """
    all_children = []
    try:
        children = node.getChildren()
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))
    except Exception:
        pass
    return all_children

def save_material(material_name, saved_materials, library_path):
    """
    Saves a material to the library if it hasn't been saved yet.
    """
    if material_name not in saved_materials:
        lux.saveMaterial(name=material_name, folder=library_path)
        print(f"Saved material '{material_name}' to library at '{library_path}'.")
        saved_materials.add(material_name)

def save_sub_materials_to_library(multi_material_name, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.
    """
    library_path = get_library_path()
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        save_material(sub_material.getName(), saved_materials, library_path)

def process_current_scene():
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name:
            save_sub_materials_to_library(material_name, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    process_current_scene()

main()
```

# End of Material\Batch Save All Scene Materials Without Duplicates.py

## Batch Save All Scene Materials to Material Library Agnostic.py
<a name="material-batch-save-all-scene-materials-to-material-library-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to save the scene's materials and multi-material sub-materials to the material library in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def get_library_path():
    """Return the folder relative to the KeyShot Materials library."""
    return "."

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The parent node from which children are to be gathered.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def save_sub_materials_to_library(multi_material_name, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: Name of the multi-material.
    :param saved_materials: Set of already saved material names to avoid duplication.
    """
    library_path = get_library_path()  # The folder is relative to the Materials library.
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Retrieve sub-materials of the multi-material.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        # Check if the sub-material has not been saved already.
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene():
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Iterate through all nodes in the scene and process their materials.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name:
            save_sub_materials_to_library(material_name, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    # Process the currently open KeyShot scene.
    process_current_scene()

# Execute the main function.
main()
```

# End of Material\Batch Save All Scene Materials to Material Library Agnostic.py

## Batch Save All Scene Materials to Material Library.py
<a name="material-batch-save-all-scene-materials-to-material-library"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to save the scene's materials and multi-material sub-materials to the material library in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The parent node from which children are to be gathered.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def save_sub_materials_to_library(multi_material_name, library_path, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: Name of the multi-material.
    :param library_path: Folder relative to the configured Materials library.
    :param saved_materials: Set of already saved material names to avoid duplication.
    """
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Retrieve sub-materials of the multi-material.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        # Check if the sub-material has not been saved already.
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene(library_path):
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.

    :param library_path: Folder relative to the configured Materials library.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Iterate through all nodes in the scene and process their materials.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name:
            save_sub_materials_to_library(material_name, library_path, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    library_path = "."  # Relative to the configured Materials library.

    # Process the currently open KeyShot scene.
    process_current_scene(library_path)

# Execute the main function.
main()
```

# End of Material\Batch Save All Scene Materials to Material Library.py

## Batch Save Multi-Material Sub-Materials Without Duplicates.py
<a name="material-batch-save-multi-material-sub-materials-without-duplicates"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Script to save multi-material sub-materials to the material library in KeyShot, compatible with PC and Apple systems.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The node from which to start the recursion.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def is_multi_material(material_name):
    """
    Check if the given material is a multi-material.

    :param material_name: The name of the material to check.
    :return: True if the material is a multi-material, False otherwise.
    """
    material_graph = lux.getMaterialGraph(name=material_name)
    return material_graph and len(material_graph.getMaterialNodes()) > 1  # True if more than one sub-material.

def save_sub_materials_to_library(multi_material_name, library_path, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: The name of the multi-material.
    :param library_path: Folder relative to the configured Materials library.
    :param saved_materials: A set to keep track of already saved materials.
    """
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Save each sub-material to the library, avoiding duplicates.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene(library_path):
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.

    :param library_path: Folder relative to the configured Materials library.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Process each node in the scene.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name and is_multi_material(material_name):
            save_sub_materials_to_library(material_name, library_path, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    library_path = "."  # Relative to the configured Materials library.

    # Process the currently open KeyShot scene.
    process_current_scene(library_path)

# Execute the main function.
main()
```

# End of Material\Batch Save Multi-Material Sub-Materials Without Duplicates.py

## Batch Save Multi-Material Sub-Materials to Material Library Agnostic.py
<a name="material-batch-save-multi-material-sub-materials-to-material-library-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Script to save multi-material sub-materials to the material library in KeyShot, compatible with PC and Apple systems.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The node from which to start the recursion.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def is_multi_material(material_name):
    """
    Check if the given material is a multi-material.

    :param material_name: The name of the material to check.
    :return: True if the material is a multi-material, False otherwise.
    """
    material_graph = lux.getMaterialGraph(name=material_name)
    return material_graph and len(material_graph.getMaterialNodes()) > 1  # True if more than one sub-material.

def save_sub_materials_to_library(multi_material_name, library_path, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: The name of the multi-material.
    :param library_path: Folder relative to the configured Materials library.
    :param saved_materials: A set to keep track of already saved materials.
    """
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Save each sub-material to the library, avoiding duplicates.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene(library_path):
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.

    :param library_path: Folder relative to the configured Materials library.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Process each node in the scene.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name and is_multi_material(material_name):
            save_sub_materials_to_library(material_name, library_path, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    library_path = "."  # Relative to the configured Materials library.

    # Process the currently open KeyShot scene.
    process_current_scene(library_path)

# Execute the main function.
main()
```

# End of Material\Batch Save Multi-Material Sub-Materials to Material Library Agnostic.py

## Change IES Light Color and File Agnostic.py
<a name="material-change-ies-light-color-and-file-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Change IES Light Color and File
``` python
import os
import lux

def get_ies_library_path():
    """Find the IES profiles in the configured textures folder."""
    return os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_TEXTURES), "IES Profiles")

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

def change_ies_light_properties(material_name, new_color, ies_file_name):
    ies_library_path = get_ies_library_path()  # Get the IES library path based on the OS.
    new_ies_file = os.path.join(ies_library_path, ies_file_name)  # Full path to the IES file.

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
    ies_file_name = "IES Spot Light/keyshot_spot_45.ies"  # Relative path from the IES Profiles directory

    for material_name in selected_materials:
        change_ies_light_properties(material_name, new_color, ies_file_name)

main()
```

# End of Material\Change IES Light Color and File Agnostic.py

## Color Gradient ShaderEdge Cube Material Color Connect.py
<a name="material-color-gradient-shaderedge-cube-material-color-connect"></a>
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
material_name = "Cube Material"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)


```
# End of Material\Color Gradient ShaderEdge Cube Material Color Connect.py

