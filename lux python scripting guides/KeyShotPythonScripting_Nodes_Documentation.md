# Understanding KeyShot's Scene Hierarchy and Node Types

KeyShot organizes objects within the scene hierarchy, particularly how models, parts, and groups are categorized when you manipulate them (e.g., grouping or creating model sets). Understanding this hierarchy is crucial when writing Python scripts to automate tasks or apply transformations within a scene.


## Key Concepts in KeyShot's Scene Hierarchy

1. Model:
   - A model in KeyShot typically represents an imported 3D file or a group of parts and sub-groups. When you import an OBJ, FBX, or similar file, it becomes a model in the scene tree.
   - A model can contain multiple parts and/or groups, which are sub-elements within that model.

2. Part:
   - A part is a single, discrete piece of geometry within a model. For example, if you import a car model, the door, wheel, and chassis might be considered individual parts.
   - Parts cannot contain other parts or groups; they are the lowest level of geometry in the hierarchy.

3. Group:
   - A group is a collection of models, parts, or other groups. Grouping helps to organize the scene by bundling related elements together. A group can contain multiple parts or other groups, but it doesn’t represent a discrete piece of geometry by itself—it’s more of an organizational tool.

## Grouping Models and Parts

When you group a model, the grouping operation doesn't change the fundamental nature of the model itself—it remains recognized as a model. For example:

- Before Grouping: 
  - A cube, treated as a model, exists independently in the scene.

- After Grouping: 
  - Grouping the cube under a model set doesn’t change its classification—it remains a model. The hierarchy will appear as `Group -> Model (Cube)`.


## Why Doesn’t the Cube Become a Part?

In KeyShot, a part is typically an individual piece of geometry within a model. Grouping doesn't change the object's classification—it only changes its position in the hierarchy. A model will remain a model unless it's explicitly merged into another model where it becomes a part.

## How to Convert a Model to a Part

If you want the cube to be treated as a part instead of a model within a group, you would generally need to:

1. Combine with Another Model:
   - One approach is to merge or combine it with another model, effectively turning the cube into a part of that combined model. However, this approach is more common in modeling software before importing to KeyShot.

2. Scene Organization:
   - Instead of grouping, consider how you import and organize objects in your 3D modeling software. When objects are imported as part of the same model, they are typically treated as parts within KeyShot.

##  Summary

- When you group a model (like a cube), KeyShot maintains the original classification of that object. A model remains a model, even when grouped under another model or group.
- A model can contain parts, but a part cannot contain other parts or models. Grouping doesn’t change the classification of the object; it only changes its hierarchy.
- To treat the cube as a part rather than a model, it would need to be part of a larger model, not an independent entity.


##  Clarifying the Hierarchy and Terminology

KeyShot uses a specific structure for organizing and manipulating scene elements, and the terminology can be a bit rigid:

- Model: A higher-level entity that can contain multiple parts or sub-groups.
- Part: A lower-level, discrete piece of geometry within a model.
- Group: An organizational container that can hold models, parts, or other groups but is not a piece of geometry itself.
- Object: In some contexts, "object" might be used interchangeably with parts and models, but in KeyShot, it usually refers to any geometric entity in the scene that can be manipulated (e.g., models and parts).


## Working with Transformations

Transformation Limitations

KeyShot's hierarchy can complicate transformations:
- Groups are organizational tools and aren't always treated as "objects" that can be transformed directly.
- Models vs. Parts: Depending on how geometry is imported, a model might be treated as a collection of parts or as a single piece, affecting how transformations can be applied.

## Workarounds and Solutions

1. Transforming Groups:
   - If you need to apply transformations to a group, consider temporarily combining the group's contents into a single model, applying the transformation, and then reverting if necessary.

2. Using Scripts for Batch Operations:
   - Scripts can automate transformations across multiple parts or models, effectively allowing you to treat a group as a single object for transformations.


## Node Type Identification and Transformation Script

To correctly identify and work with different node types in KeyShot, especially when applying transformations, you can use the node type constants provided by the KeyShot Python API. This ensures your script can differentiate between models, groups, and parts, applying transformations appropriately.

```python
import lux

def transform_node(node_id, translation=(0, 0, 0), rotation=(0, 0, 0), scale=1.0):
    """
    Applies transformations to a node based on its type.
    
    :param node_id: The ID of the node to transform.
    :param translation: A tuple representing the translation (x, y, z).
    :param rotation: A tuple representing the rotation (pitch, yaw, roll).
    :param scale: A float representing the uniform scale factor.
    """
    # Identify the node type
    node_type = lux.getObjectType(node_id)
    
    # Apply transformations based on node type
    if node_type == lux.NODE_TYPE_MODEL or node_type == lux.NODE_TYPE_OBJECT:
        # Transform the model or part
        lux.setObjectPosition(node_id, *translation)
        lux.setObjectRotation(node_id, *rotation)
        lux.setObjectScale(node_id, scale)
        print(f"Transformed node ID {node_id} (Type: {node_type})")
    
    elif node_type == lux.NODE_TYPE_GROUP:
        # Skip groups, or alternatively, transform all children within the group
        print(f"Skipping transformation for group node ID {node_id} (Type: {node_type})")
    
    else:
        print(f"Node ID {node_id} (Type: {node_type}) is not supported for transformations.")

def transform_scene():
    """
    Apply transformations to all models and objects (parts) in the scene.
    """
    # Retrieve all node IDs in the scene
    scene_tree = lux.getSceneTree()
    node_ids = scene_tree.getChildren()
    
    for node_id in node_ids:
        transform_node(node_id, translation=(10, 0, 0), rotation=(0, 45, 0), scale=1.2)

# Run the transformation on the scene
transform_scene()
```

## Summary

This portion of the guide clarifies the differences between models, parts, and groups in KeyShot and provides a practical script to apply transformations based on node type. Understanding this hierarchy is crucial for effectively scripting within KeyShot and managing complex scenes.


## Exploring and Analyzing Your Scene in KeyShot

Understanding Your Scene's Structure

Before making changes or applying transformations, it's crucial to understand the structure of your scene. The following scripts will help you analyze your scene tree, identify different types of nodes, and inspect the materials and parameters associated with each element.

 Script: Get SceneTree Nodes
- Purpose: Identifies and lists all nodes in your scene, including models, parts, groups, and cameras.
- Usage: Run this script to get a quick overview of your scene’s structure.

 Script: Get Print Detailed SceneTree Node Information
- Purpose: Provides detailed information about each node, including its type and material properties.
- Usage: Use this script when you need to inspect the materials applied to different parts of your scene.

 Script: [Get Scene Tree Node Parameters](#3-get-scene-tree-node-parameters)
- Purpose: Extracts and prints detailed parameters for each node in the scene tree.
- Usage: Ideal for understanding the attributes and properties of each node, useful for advanced scene manipulation.

## Scene Tree Hierarchy Scripts

Here are scripts for exploring and working with KeyShot's scene hierarchy:

### 1. Get Print Detailed Scene Tree Node Information
   - Purpose: This script traverses the scene tree and prints detailed information about each node, including its type (Model, Part, Group, etc.) and associated materials.
   - Key Features:
     - Node Information: Prints the name, type, and other relevant details of each node.
     - Material Information: If a node has a material, it prints detailed parameters of that material.
   - Integration: This script is useful for understanding the structure of a scene and the materials applied to different parts. It can be included in the guide as a tool for users who need to inspect and debug complex scenes.
   - Reference: [Get Print Detailed SceneTree Node Information].

```python
# Traverse scene tree and print node and material information.
import lux

# Correct node type constants
NODE_TYPE_GROUP = 1
NODE_TYPE_MODEL = 5
NODE_TYPE_MODEL_SET = 4
NODE_TYPE_OBJECT = 2

def print_node_info(node, level=0):
    """
    Print basic information about a node.
    
    :param node: The node to print information about.
    :param level: The indentation level for pretty printing.
    """
    indent = '  ' * level
    node_type = node.getKind()
    
    if node_type == NODE_TYPE_MODEL_SET:
        type_name = "Model Set"
    elif node_type == NODE_TYPE_GROUP:
        type_name = "Group"
    elif node_type == NODE_TYPE_MODEL:
        type_name = "Model"
    elif node_type == NODE_TYPE_OBJECT:
        type_name = "Part"
    else:
        type_name = "Unknown"
    
    print(f"{indent}{node.getName()} (Type: {type_name})")
    print(f"{indent}Node Name: {node.getName()}")
    print(f"{indent}Node Type: {node.getKind()}")

def print_material_parameters(material, level=0):
    """
    Print parameters of the material.
    
    :param material: The material to print parameters for.
    :param level: The indentation level for pretty printing.
    """
    indent = '  ' * level
    if hasattr(material, 'getName'):
        print(f"{indent}### Material: {material.getName()}")
        parameters = material.getParameters()
        for param in parameters:
            param_name = param.getName()
            param_type = param.getType()
            param_value = param.getValue()
            print(f"{indent}- {param_name} (Type: {param_type}): {param_value}")
    else:
        print(f"{indent}Material: {material}")

def print_material_info(node, level=0):
    """
    Print material information for a given node.
    
    :param node: The node to print material information for.
    :param level: The indentation level for pretty printing.
    """
    try:
        material = node.getMaterial()
        if material:
            if hasattr(material, 'getMaterialGraph'):
                material_graph = material.getMaterialGraph()
                if material_graph:
                    print(f"{'  ' * level}Material graph found for part '{node.getName()}':")
                    print_material_graph_parameters(material_graph, level + 1)
                else:
                    print(f"{'  ' * level}No material graph found for part '{node.getName()}'.")
            else:
                print_material_parameters(material, level)
        else:
            print(f"{'  ' * level}No material assigned to '{node.getName()}'.")
    except Exception as e:
        print(f"{'  ' * level}Failed to get material for '{node.getName()}': {e}")

def traverse_scene_tree(node=None, level=0):
    """
    Recursively traverse the scene tree and print node information.
    
    :param node: The starting node of the scene tree. If None, start from the root.
    :param level: The current level in the tree (used for indentation).
    """
    if node is None:
        node = lux.getSceneTree()  # Get the root of the scene tree

    print_node_info(node, level)
    
    if node.getKind() in [NODE_TYPE_OBJECT, NODE_TYPE_GROUP, NODE_TYPE_MODEL]:
        print_material_info(node, level)
    
    # Recursively traverse child nodes if the node is a group, model, or model set
    if node.getKind() in [NODE_TYPE_GROUP, NODE_TYPE_MODEL, NODE_TYPE_MODEL_SET]:
        children = node.getChildren()
        for child in children:
            traverse_scene_tree(child, level + 1)

def print_material_graph_parameters(material_graph, level=0):
    """
    Print parameters of all nodes in the material graph.
    
    :param material_graph: The material graph to inspect.
    :param level: The indentation level for pretty printing.
    """
    indent = '  ' * level
    shader_nodes = material_graph.getNodes()
    for shader_node in shader_nodes:
        print(f"{indent}Shader Node: {shader_node.getName()}")
        parameters = shader_node.getParameters()
        for param in parameters:
            param_name = param.getName()
            param_type = param.getType()
            param_value = param.getValue()
            print(f"{indent}  Parameter Name: {param_name}, Type: {param_type}, Value: {param_value}")

# Example usage: Print the entire scene tree with node information
traverse_scene_tree()
```


###  2. Get Scene Tree Nodes
   - Purpose: This script identifies and lists different types of nodes (e.g., Group, Model, Object) in the scene tree.
   - Key Features:
     - Node Type Identification: Accurately identifies node types using functions like `isGroup()`, `isModel()`, etc.
     - Camera Listing: It also lists all cameras in the scene, ensuring they are not overlooked.
   - Integration: This script is ideal for users who need to quickly understand the structure of their scene, including the types of objects present and the cameras in use. It can be positioned in the guide as an initial step for scene analysis.

(Continued)




```python
# Example script that retrieves Scene Nodes; Group, Model, ModelSet, Object, Camera, Animation, and Unknown.

import lux

def get_node_type(node):
    """Determine the node's type and return it as a string based on the KeyShot Python API."""
    # Directly using documented functions to identify the node type
    if node.isGroup():
        return "Group"
    elif node.isModel():
        return "Model"
    elif node.isModelSet():
        return "Model Set"
    elif node.isObject():
        return "Object"
    elif node.isCamera():  # Ensuring cameras are correctly identified
        return "Camera"
    elif node.isAnimation():  # Including animation nodes based on your reference script
        return "Animation"
    else:
        return "Unknown"  # Fallback for nodes that don't match the above categories

def print_scene_structure(node, indent=0):
    """Recursively print the structure of the KeyShot scene, handling node types accurately."""
    node_type = get_node_type(node)
    print(" " * indent + f"{node_type}: {node.getName()}")

    # Recursively process child nodes if the current node is a group or a model set, as model sets can contain models or objects
    if node.isGroup() or node.isModelSet():
        if hasattr(node, 'getChildren'):  # Check if the node can have children to avoid errors
            for child in node.getChildren():
                print_scene_structure(child, indent + 2)

def list_cameras():
    """List all cameras in the KeyShot scene."""
    print("\nCameras in Scene:")
    for camera_name in lux.getCameras():
        print(f"  Camera: {camera_name}")

def main():
    print("Scene Structure:")
    root_node = lux.getSceneTree()
    print_scene_structure(root_node)

    # Directly list cameras to ensure they are included in the scene output
    list_cameras()

if __name__ == "__main__":
    main()

```
### 3. Get Scene Tree Node Parameters
   - Purpose: This script retrieves and prints detailed parameters for each node in the scene tree, focusing on identifying and understanding the attributes associated with different nodes.
   - Key Features:
   - Parameter Extraction: It delves into each node's parameters, providing a detailed overview of what can be manipulated or inspected.
   - Integration: This script complements the others by offering a deep dive into the properties of each node. It’s valuable for users who need to fine-tune specific elements of their scene or script more complex interactions.

```python
# Print Detailed Scene Treen Node Information.
import lux

# Correct node type constants
NODE_TYPE_GROUP = 1
NODE_TYPE_MODEL = 5
NODE_TYPE_MODEL_SET = 4
NODE_TYPE_OBJECT = 2

def print_node_info(node, level=0):
    """
    Print basic information about a node.
    
    :param node: The node to print information about.
    :param level: The indentation level for pretty printing.
    """
    indent = '  ' * level
    node_type = node.getKind()
    
    if node_type == NODE_TYPE_MODEL_SET:
        type_name = "Model Set"
    elif node_type == NODE_TYPE_GROUP:
        type_name = "Group"
    elif node_type == NODE_TYPE_MODEL:
        type_name = "Model"
    elif node_type == NODE_TYPE_OBJECT:
        type_name = "Part"
    else:
        type_name = "Unknown"
    
    print(f"{indent}{node.getName()} (Type: {type_name})")
    print(f"{indent}Node Name: {node.getName()}")
    print(f"{indent}Node Type: {node.getKind()}")

def traverse_scene_tree(node=None, level=0):
    """
    Recursively traverse the scene tree and print node information.
    
    :param node: The starting node of the scene tree. If None, start from the root.
    :param level: The current level in the tree (used for indentation).
    """
    if node is None:
        node = lux.getSceneTree()  # Get the root of the scene tree

    print_node_info(node, level)
    
    # Recursively traverse child nodes if the node is a group, model, or model set
    if node.getKind() in [NODE_TYPE_GROUP, NODE_TYPE_MODEL, NODE_TYPE_MODEL_SET]:
        children = node.getChildren()
        for child in children:
            traverse_scene_tree(child, level + 1)

# Example usage: Print the entire scene tree with node information
traverse_scene_tree()
```
---
