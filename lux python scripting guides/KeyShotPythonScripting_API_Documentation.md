# KeyShot Studio 2026.3 Python Scripting API

## Module references

- [lux GUI API](../lux/KeyShot_lux_API.md)
- [luxmath GUI API](../luxmath/KeyShot_luxmath_API.md)
- [lux headless API](../lux_headless/KeyShot_headless_lux_API.md)
- [luxmath headless API](../luxmath_headless/KeyShot_headless_luxmath_API.md)

Use the reference for the execution mode you intend to use. In a KeyShot
scripting session, run help(lux) or help(luxmath) to inspect that build.

## Guides and examples

- [KeyShot Studio Scripting Console](https://manuals.keyshot.com/kss2026/en-us/manual/scripting-console.html)
- [KeyShot Studio headless scripting](https://manuals.keyshot.com/kss2026/en-us/manual/exposed-headless-scripting-functionality.html)
- [Repository scripting guides](KeyShotPythonScripting_ToC.md)
- [Repository script examples](../lux%20scripts/Scripting_Examples.md)

## Scripting examples

These examples illustrate scripting patterns. Check the calls and options against the relevant module reference before running an example.

## Scripting: Accessing scene nodes
Accessing scene nodes (GUI and Headless)
The elements of the scene can be accessed via lux.getSceneTree() with each scene tree node being of the type lux.SceneNode. It is useful because for each node you can hide/show, lock/unlock, select/deselect, change material, apply transformations, duplicate, move and more. Try help(lux.SceneNode) for more information.

Let’s say you wanted to hide all nodes having “Cord” as part of their name:

```python
root = lux.getSceneTree()
for node in root.find(name = "Cord"):
        node.hide()
Another example could be that you wanted to access all groups called “Padding” and selecting all child nodes (in the scene with outline) whose name is “Ear Pad”:

for node in root.find(name = "Padding", types = lux.NODE_TYPE_GROUP):
        for ch in node.getChildren():
            if ch.getName() == "Ear Pad":
                ch.select()
If you have hidden some parts and want to simply show everything again:

root.show()
Note
The root node itself is a lux.SceneNode so the same functions can be invoked on it as with child nodes.

It is also possible to change materials. To simulate ambient occlusion you could do the following:

for node in root.find(""):
        node.setMaterial("Matte White")
Tip
Use lux.SceneNode.find(“”) to simply find everything.

Nodes can be moved to other groups, just like in the scene tree with drag-and-drop. In the following we find the group “Headphone #1” and move all nodes to it that are using a material with “Padding” in it.

grp = root.find(name = "Headphone #1")[0] # Take first node of set.
for node in root.find(mat = "Padding"):
        node.moveToGroup(grp)
True

```

## Scripting: Camera manipulation
Camera Manipulation (GUI and Headless)
Working with cameras in scripting is just like using the Camera tab in Project → Camera: You can create a camera, manipulate it to suit your needs, and save it.

lux.newCamera("New")
lux.setCameraLookAt(pt = (1, 1, 1)) # Example manipulation.
lux.saveCamera()
Inspect the cameras available:

lux.getCameras()
['New', 'last_active', 'default']
Choose another camera:

lux.setCamera("default")
Remove the camera you just created:

lux.removeCamera("New")
['last_active', 'default']
If you remove the active camera it will choose the “Free Camera”.

You can also set a standard view:

lux.setStandardView(lux.VIEW_TOP)
The following 7 standard views are available:

lux.VIEW_FRONT
lux.VIEW_BACK
lux.VIEW_TOP
lux.VIEW_BOTTOM
lux.VIEW_LEFT
lux.VIEW_RIGHT
lux.VIEW_ISOMETRIC
Setting a standard view manipulates the active camera so you could create a camera for each standard view, but remember to save them.


## Scripting: Cancelling scripts
Cancelling Scripts (GUI only)
In general you can’t cancel a script but certain operations can, such as importing a file or rendering an image, animation or XR. Cancelling in those situations means to cancel the dialog associated, like the rendering output window or import progress dialog.

The only operations you can cancel are:

lux.importFile()
lux.renderImage()
lux.renderFrames()
lux.renderAnimation()
lux.renderXR()
lux.encodeVideo()
Simply check the return value to see if it was False and therefore cancelled, or failed.

Especially if you’re using a loop-structure you can do the following:

frames = 10
for frame in range(1, frames + 1):
lux.setAnimationFrame(frame)
if not lux.renderImage("/path/to/output.{}.png".format(frame)):
break


## Scripting Custom input dialog:
Custom input dialog (GUI only) NOT Headless Compliant

In scripts it is especially preferable to show a single dialog when multiple inputs are needed. For this you can use lux.getInputDialog(). The scripts provided by Luxion will use this.

GUI Example:

import lux

def create_input_dialog():
# Define the input fields for the dialog
values = [
("name", lux.DIALOG_TEXT, "Enter your name:", "John Doe"),  # Provide a non-empty default value
("age", lux.DIALOG_INTEGER, "Enter your age:", 30, (1, 100)),  # The last tuple defines the range (min, max)
("file", lux.DIALOG_FILE, "Select a file:", None),
("folder", lux.DIALOG_FOLDER, "Select a folder:", None)
]

# Show the dialog and get the user's input
opts = lux.getInputDialog(
title="User Information",
desc="Please fill in the information below:",
values=values,
id="user_info_dialog"  # Unique identifier to remember the last values entered
)

# Check if the user clicked OK and opts is not None
if opts:
print("User's Input:")
for key, value in opts.items():
print(f"{key}: {value}")
else:
print("User cancelled the dialog.")

# Call the function to show the dialog
create_input_dialog()

1. Importing Models in Batch

This example demonstrates how to use a GUI dialog to select multiple model files for batch import into KeyShot. It utilizes the `lux.getInputDialog()` for user input and `lux.importFile()` for importing models.

import os

def batch_import_models():
# Ask user to select model files for import
file_paths = lux.getInputDialog(title="Batch Import Models",
desc="Select model files to import",
values=[("model_files", lux.DIALOG_FILE, "Model files:", None, True)])
if file_paths:
for file_path in file_paths["model_files"]:
lux.importFile(file_path)

batch_import_models()


### 2. Assigning Textures to Multi-Materials in Batch

This script demonstrates how to assign diffuse textures to sub-materials of multi-materials in batch, using a GUI dialog for specifying a folder containing texture files.

# AUTHOR LUX DT ChatGPT
# VERSION 1.2.0
# Script for automating the creation of sub-materials and applying textures with UV scale adjustment in KeyShot.

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


### 3. Renaming Materials to Avoid Clashing

This script provides a GUI to rename materials in a KeyShot scene to avoid name clashes. It uses a find-and-replace approach.

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

def change_material_to_advanced(material_name):
    material_graph = lux.getMaterialGraph(material_name)
    if not material_graph:
        print(f"Material graph for {material_name} not found.")
        return

    root_node = material_graph.getRoot()
    if not root_node:
        print(f"Root node for {material_name} not found.")
        return

    if root_node.getType() == SHADER_TYPE_ADVANCED:
        print(f"Material {material_name} is already 'Advanced'.")
        return

    advanced_shader = material_graph.newNode(SHADER_TYPE_ADVANCED)
    for param_name, param_type, default_value in PARAMETERS:
        param = advanced_shader.getParameter(param_name)
        if param and not param.isPure():
            param.setValue(default_value)

    material_graph.newEdge(advanced_shader, root_node, 'surface')
    print(f"Material {material_name} has been changed to 'Advanced' and connected to the material graph.")

def sanitize_material_name(name, name_count):
    new_name = re.sub(r'#\d+', '', name).strip() + "_MM"
    if new_name in name_count:
        name_count[new_name] += 1
        new_name = f"{new_name}_{name_count[new_name]}"
    else:
        name_count[new_name] = 1
    return new_name

def rename_material(material_name, name_count):
    """Rename the material by sanitizing its name and check if the renaming was successful."""
    try:
        material_graph = lux.getMaterialGraph(material_name)
        if material_graph:
            root_node = material_graph.getRoot()
            old_name = root_node.getName()
            new_name = sanitize_material_name(old_name, name_count)
            root_node.setName(new_name)
            print(f"Renamed material from '{old_name}' to '{new_name}'")
            return new_name
    except Exception as e:
        print(f"Error with material '{material_name}': {e}")
    return material_name

def create_advanced_sub_material(material_graph, base_name, color_name, color_value):
    sub_material = material_graph.newNode(SHADER_TYPE_ADVANCED)
    sub_material.setName(f"{base_name}_{color_name}")

    for param_name, param_type, default_value in PARAMETERS:
        param = sub_material.getParameter(param_name)
        if param and not param.isPure():
            param.setValue(default_value)

    diffuse_param = sub_material.getParameter('diffuse')
    if diffuse_param and diffuse_param.getType() == PARAMETER_TYPE_COLORALPHA:
        diffuse_param.setValue(color_value)
        print(f"Diffuse color of '{color_name}' sub-material set to {color_value}.")

    return sub_material

def create_multi_material_with_advanced_sub_materials(material_name, colors):
    try:
        change_material_to_advanced(material_name)

        material_graph = lux.getMaterialGraph(material_name)
        if not material_graph:
            print(f"Material graph for {material_name} not found.")
            return

        sub_materials = []
        for color_name, color_value in colors:
            sub_material = create_advanced_sub_material(material_graph, material_name, color_name, color_value)
            sub_materials.append(sub_material)

        material_graph.setMultiMaterial(enable=True)
        multi_material = lux.getMultiMaterial(material_name)

        for sub_material in sub_materials:
            material_graph.setCurrentSubMaterial(sub_material)
            print(f"Sub-Material '{sub_material.getName()}' has been added to the Multi-Material '{material_name}'.")

        # Ensure all sub-materials are added to the multi-material
        sub_material_names = [sub_material.getName() for sub_material in sub_materials]
        multi_material.setSubMaterials(sub_material_names)

        print(f"Multi-Material with Advanced Sub-Materials has been created for {material_name}.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def rename_existing_multi_materials():
    """Rename all existing multi-materials in the scene that don't have '_MM' suffix."""
    materials = lux.getSceneMaterials()
    name_count = {}
    for mat in materials:
        if not mat.endswith("_MM"):
            rename_multi_material(mat, name_count)

def rename_multi_material(material_name, name_count):
    """Rename multi-material and its sub-materials by sanitizing their names."""
    try:
        multi_material = lux.getMultiMaterial(material_name + "_MM")
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

def main():
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    selected_colors = display_color_selection()
    if not selected_colors:
        print("No colors selected or operation cancelled.")
        return

    name_count = {}
    for material_name in selected_materials:
        create_multi_material_with_advanced_sub_materials(material_name, selected_colors)
        renamed_material_name = rename_material(material_name, name_count)
        rename_multi_material(renamed_material_name, name_count)

main()



### 4. Retrieving Camera Information

This example showcases how to create a GUI dialog that displays information about the currently active camera.

# AUTHOR LUX DT ChatGPT
# VERSION 1.2.4
# Get Camera settings and display the look-at point.
# Script to view camera details in a window in KeyShot.

import lux  # Import the KeyShot built-in module 'lux'.

def get_camera_info(camera_name):
    """
    Retrieve and format information for a specified camera, including look-at point.

    :param camera_name: Name of the camera to get information about.
    :return: Formatted string containing camera details.
    """
    # Set the selected camera as active.
    lux.setCamera(camera_name)

    # Retrieve various camera details.
    lens_info = lux.getCameraLens()  # Retrieves camera lens information
    fov = round(lux.getCameraFieldOfView(), 2)  # Field of view.
    focal_length = round(lux.getCameraFocalLength(), 2)  # Focal length.

    # Determine the lens type based on camera mode
    lens_type = lens_info.get('lens')
    if lens_type == lux.CAMERA_TYPE_PERSPECTIVE:
        lens_type_str = 'Perspective'
    elif lens_type == lux.CAMERA_TYPE_ORTHOGRAPHIC:
        lens_type_str = 'Orthographic'
    elif lens_type == lux.CAMERA_TYPE_PANORAMA:
        lens_type_str = 'Panoramic'
    else:
        lens_type_str = 'Unknown'

    direction = lux.getCameraDirection()  # Camera direction.
    distance = round(lux.getCameraDistance(), 2)  # Distance from pivot.
    position = lux.getCameraPosition()  # Camera position.
    up_vector = lux.getCameraUp()  # Up vector.
    look_at = lux.getCameraLookAt()  # Get the look-at point.

    # Format the camera information for display.
    camera_info = (
        "Lens Info:\n"
        f"FOV: {fov} degrees\n"
        f"Focal Length: {focal_length} mm\n"
        f"Lens Type: {lens_type_str}\n\n"
        f"Direction: {direction}\n"
        f"Distance: {distance}\n"
        f"Position: {position}\n"
        f"Up Vector: {up_vector}\n"
        f"Look-At Point: {look_at}"
    )
    return camera_info

def display_camera_info(cam):
    """
    Display information of a selected camera.

    :param cam: Name of the camera to display information for.
    :return: Boolean indicating if the user wants to go back to the camera list.
    """
    camera_info = get_camera_info(cam)  # Get camera info.
    info_label = (lux.DIALOG_LABEL, camera_info)  # Format for displaying.
    back_checkbox = ("backToList", lux.DIALOG_CHECK, "Back to Camera List", False)
    
    # Display the camera info in a dialog.
    user_response = lux.getInputDialog(title=f"Camera Info: {cam}", values=[info_label, back_checkbox])

    return user_response and user_response.get("backToList", False)

def display_camera_selection():
    """
    Display a selection dialog for all cameras and show their information.
    """
    cameras = lux.getCameras()  # Get a list of all cameras.
    while True:
        # Create dialog elements for camera selection.
        camera_selection_elements = [(cam, lux.DIALOG_CHECK, cam, False) for cam in cameras]
        user_selection = lux.getInputDialog(title="Select Camera", values=camera_selection_elements)

        if not user_selection:
            break  # Exit if no selection is made.

        # Loop through the selected cameras and display their information.
        for cam, selected in user_selection.items():
            if selected:
                back_to_list = display_camera_info(cam)
                if back_to_list:
                    break  # Return to the camera list if the user chooses.

# Execute the function to start the camera selection process.
display_camera_selection()


### 5. Getting Scene Material Parameters

# Get scene material parameters and saves them to a .txt.
import lux

def save_material_graph_info_to_file(file_path):
    all_materials = lux.getSceneMaterials()  # Get all materials from the scene
    material_info = []

    for material_name in all_materials:
        material_graph = lux.getMaterialGraph(material_name)
        if material_graph is not None:
            material_info.append(f"Material: {material_name}\n")
            nodes = material_graph.getNodes()
            for node in nodes:
                node_type_info = node.getType() if hasattr(node, 'getType') and node.getType() else "Unknown"
                parameters = node.getParameters()
                material_info.append(f"  Node: {node.getName()}, Type: {node_type_info}\n")
                for param in parameters:
                    try:
                        param_value = param.getValue() if not param.isPure() else "Pure Parameter"
                    except Exception as e:
                        param_value = f"Complex Type: {e}"  # Log exception or indicate complex type
                    material_info.append(f"    Param: {param.getName()}, Value: {param_value}\n")
            material_info.append("\n")

    with open(file_path, "w") as file:
        file.writelines(material_info)
    print(f"Material graph info saved to {file_path}")

# Specify the file path where you want to save the output
output_file_path = "C:/GLB_OBJ/material_graph_info.txt"
save_material_graph_info_to_file(output_file_path)


Common Errors:
The lux.getInputDialog() function cannot be empty. This means whenever you define a field of type lux.DIALOG_TEXT, you need to ensure that the default value (the fourth element in the tuple for that field) is a non-empty string.


## Scripting: Import file
Import file (GUI and Headless)
Importing models with scripting is easy:

lux.importFile("/path/to/your/file.obj")
In this case we imported an OBJ file.

By default no dialog will be shown with importing options, but it can be done using the showOpts option:

lux.importFile("/path/to/your/file.obj", showOpts = True)
For more advanced importing, a Python dictionary can be supplied using the opts option. An example could be to disable snap-to-ground, and not adjusting environment and camera look-at on import:

opts = lux.getImportOptions()
opts["snap_to_ground"] = False
opts["adjust_environment"] = False
opts["adjust_camera_look_at"] = False
lux.importFile("/path/to/your/file.obj", opts = opts)
When updating geometry you will want to set the following options before importing:

opts["import_type"] = 1
opts["merge"] = True


## Scripting: Render image
Render Image (GUI and Headless)
Assuming you have already loaded a BIP file, or imported some geometry, and you want to render to an image with scripting then do the following:

lux.renderImage("/path/to/save/image.png", width = 1200, height = 1000)
In this case we render the image to “/path/to/save/image.png” as a PNG file with dimensions 1200×1000 pixels. Notice that the format of the image is determined from the file extension.

As with importing, advanced options can be passed using the opts option. An example could be to setup for rendering with max time of 10 seconds:

opts = lux.getRenderOptions()
opts.setMaxTimeRendering(10)
lux.renderImage("/path/to/save/image.png", width = 1200, height = 1000, opts = opts)
Another example could be to render using advanced rendering method with 64 samples, 8 threads, and 64 ray bounces:

opts.setAdvancedRendering(64)
opts.setThreads(8)
opts.setRayBounces(64)


## Scripting: Transforming scene nodes
Transforming scene nodes (GUI and Headless)
Nodes can be translated, scaled, rotated etc. via scripting. It is possible by using 4×4 transformation matrices of type luxmath.Matrix. There are two ways to transform: relative or absolute. A relative transform means to apply the transform locally, i.e. it is multiplied last in the chain of existing transforms. That means that if you relatively translate by (1,0,0) then it will simply move the node one by the x-axis according to its position. In contrast, absolute transforms are not chained in the same fashion and absolutely translating by (1,0,0) will always position the node at (1,0,0).

When doing transforms it is important that an identity matrix (1s on the diagonal) is used as the base matrix. It is obtained in the following way:

M = luxmath.Matrix().makeIdentity()
print(M.dump())
| 1.00  0.00  0.00  0.00 |
| 0.00  1.00  0.00  0.00 |
| 0.00  0.00  1.00  0.00 |
| 0.00  0.00  0.00  1.00 |
To translate a node by (5,0,1):

M = luxmath.Matrix().makeIdentity().translate(luxmath.Vector((5, 0, 3)))
node.applyTransform(M)
print(M.dump()) # Let's have a look at the matrix.
| 5.00  0.00  3.00  1.00 |
If instead an absolute position adjustment is intended, then do the following:

node.applyTransform(M, absolute = True)
Only object nodes can have absolute transforms applied!

For further information about what transforms are possible have a look at the documentation for luxmath.Matrix.


## GUI scripting examples


### 1. Importing Models in Batch

KeyShot Python Custom Input Dialog (GUI only)
For this you must use lux.getInputDialog(). The GUI script examples below provided by Luxion will use this.

Importing Models in Batch

Assigning Textures to Multi-Materials in Batch

Renaming Materials to Avoid Clashing

Retrieving Camera Information

Getting Scene Material Parameters

Import Automation:

def main():
# Display a file selection dialog
values = [("file_path", lux.DIALOG_FILE, "Select a file to import:", None)]
opts = lux.getInputDialog(title="Import File and Create Model Set",
desc="Please select a model file to import.",
values=values,
id="import_file_model_set")

# Check if the user has selected a file
if opts is not None and "file_path" in opts and opts["file_path"]:
file_path = opts["file_path"]

# Import the file
lux.importFile(path=file_path)

# Extract the filename without extension to use as the model set name
model_set_name = os.path.splitext(os.path.basename(file_path))[0]

# Create a new model set with the extracted name
lux.newModelSet(name=model_set_name)

# Run the main function
main()

As an example, if we wanted to write a video encoding script the following dialog might suffice:

values = [("folder", lux.DIALOG_FOLDER, "Folder with frames:", None), \
("fmt", lux.DIALOG_TEXT, "Frame file format:", "frame.%d.jpg"), \
("start", lux.DIALOG_INTEGER, "Start frame:", 1, (1, 4096)), \
("end", lux.DIALOG_INTEGER, "End frame:", 10, (1, 4096)), \
("fps", lux.DIALOG_INTEGER, "FPS:", 10, (1, 1024)), \
("name", lux.DIALOG_TEXT, "Video name:", "video.mp4")]
opts = lux.getInputDialog(title = "Encode Video", \ # Shows the dialog.
desc = "Put a description here.", \
values = values)
opts
{'end': 10, 'fps': 10, 'fmt': 'frame.%d.jpg', 'name': 'video.mp4', 'start': 1, 'folder': ''}
If you click “OK” without changing any values then you will get the Python dictionary above. Each key is associated with the value from the dialog.

The “\” characters above indicates a continuation of the line, so it is not split into several lines, but understood as one line.

For scripts that are run often it is convenient to have KeyShot remember the last values for when the dialog is displayed again, and that is accomplished by using a unique value for the id option:

opts = lux.getInputDialog(title = "Encode Video", \
values = values, \
id = "something_unique_goes_here")
If the unique value is already used by some other script then you will get undesired results. However, keep in mind that your script must use the same unique value each time to retrieve your values.


### KeyShot Python Scripting: Common Errors and Solutions


## GUI Considerations:
Non-Empty Default Values for lux.getInputDialog():
When using lux.getInputDialog() to create custom input dialogs in KeyShot, ensure that all fields, especially those of type lux.DIALOG_TEXT, have non-empty default values. This requirement prevents runtime errors related to uninitialized or empty fields in the dialog.
Empty Item Tuple Exception:

Error Message: Exception: Items of item tuple must be specified!
Cause: This error occurs when a tuple expected by a function like lux.getInputDialog() is incomplete or improperly formatted, particularly for selection items (lux.DIALOG_ITEM).
Solution: Ensure that all tuples defining dialog items are complete and correctly formatted. For selection items (lux.DIALOG_ITEM), include all required elements: the label, item type, description, default selection, and a list of options.
Type Mismatch Error:

Error Message: TypeError: argument 1 must be str, not list
Cause: This error is typically raised when a function expects a string argument, but a list (or another non-string type) is provided instead.
Solution: Carefully review function calls to ensure that all arguments are of the expected type. For functions expecting a string, do not pass lists or other composite types without first converting or extracting the appropriate string value.
Implementation Tips:
Debugging: Use print statements or logging to debug argument types and values passed into functions. This can help identify where type mismatches occur.
Type Checking: Implement explicit type checks or use Python's type hinting to make your code clearer and catch type-related errors early.
Consistent Formatting: When dealing with functions that require tuples (like lux.getInputDialog()), double-check the consistency and completeness of your tuples to prevent formatting-related exceptions.
Example:
Here is an example illustrating how to correctly define a field in lux.getInputDialog() with a non-empty default value:

# Define input fields for the dialog
values = [
("name", lux.DIALOG_TEXT, "Model Name:", "DefaultModelName"),  # Non-empty default value
# Other fields as needed
]

# Create the dialog
opts = lux.getInputDialog(title="Model Import Settings",
desc="Configure settings for importing models.",
values=values)


## Material Graph

KeyShot Scripting: Handling Material Graphs
When working with material graphs in KeyShot via Python scripting, it's crucial to utilize the correct functions provided by the lux module for accessing and manipulating materials. The MaterialGraph class encapsulates a graph of material nodes constituting a material in the scene, enabling manipulation of material parameters, addition/removal of material nodes, and their association with input and output edges.

Accessing Material Graphs and Handling Errors
Function to Use:

To get a material graph, use lux.getMaterialGraph(name), where name is the name of the material.

AttributeError: module 'lux' has no attribute 'getMaterial'. Did you mean: 'MultiMaterial'?
AttributeError: module 'lux' has no attribute 'getMaterials'. Did you mean: 'getCameras'?
Solutions:

These errors typically occur when attempting to access materials or their properties using incorrect or non-existent lux module functions.
Use lux.getMaterialGraph(name) to access the material graph of a specific material by its name.
To obtain information about materials used in the scene, or to manipulate materials directly, consider using the following functions correctly:
lux.getSceneMaterials(): Retrieves currently used materials in the scene.
lux.getName(): Retrieves the name of a node, which can be useful when working with materials and model sets.
lux.getMaterialNodes(): Retrieves a list of material root nodes within a material graph. For multi-materials, it returns individual sub-material roots; for regular materials, it returns a list with a single item equivalent to getRoot().
Correcting Misused Functions
Incorrect Use: Attempting to use lux.getMaterial() or lux.getMaterials() directly, which are not valid functions and can lead to AttributeError.
Correction: Utilize the correct functions for your intended operations, such as lux.getSceneMaterials() for retrieving materials or lux.getMaterialGraph(name) for accessing a material's graph.
Implementation Tips
Review KeyShot Python API Documentation: Always refer to the most current KeyShot Python API documentation to understand available functions and their proper usage.
Debugging: Use print statements to debug the names and types of variables, especially when passing them as arguments to functions, to ensure they match the expected values.
By adhering to these guidelines and utilizing the correct functions for accessing and manipulating material graphs in KeyShot, you can avoid common errors and enhance your scripting workflow.


## Camera
KeyShot Scripting: Correcting Camera Access Error
Error Encounter:

AttributeError: AttributeError: module 'lux' has no attribute 'getActiveCamera'
This error indicates an attempt to use a non-existent function getActiveCamera in the lux module to retrieve the currently active camera.
Cause:

The error arises from a misunderstanding or incorrect reference to the available KeyShot Python API functions for camera manipulation.
Correct Usage:

The correct function to use for getting the active camera's information is lux.getCamera(), not lux.getActiveCamera.
Solution:

Review KeyShot Python API Documentation: Always consult the latest KeyShot Python API documentation to understand the correct naming and usage of functions related to camera operations.
Code Adjustment: Replace any incorrect usage of lux.getActiveCamera with lux.getCamera() in your scripts. This function retrieves the current camera settings, including its name, type, and parameters.

Example Correct Usage:
# Correctly getting the active camera's information
camera_info = lux.getCamera()
print("Active Camera:", camera_info)

Additional Tips:

Understanding Camera Functions: Familiarize yourself with other camera-related functions in the KeyShot Python API to fully leverage camera manipulation in your scripts. Functions such as lux.setCamera(), lux.saveCamera(), and lux.setStandardView() can be particularly useful.
Error Checking: Implement try-except blocks around your camera function calls to catch and handle potential errors gracefully, improving script robustness.
By adhering to the correct usage of lux.getCamera() for accessing the active camera's details, you can avoid common attribute errors and effectively control camera settings within your KeyShot Python scripts.

Additional real-world working KeyShot Python script examples are located in the "Scripting_Examples.txt".
