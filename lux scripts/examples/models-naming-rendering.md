# Scripting Examples: Models, Naming, and Rendering

[Scripting Examples TOC](../Scripting_Examples.md)

## Delete Model Set by Name.py
<a name="model-delete-model-set-by-name"></a>
# AUTHOR Donald Tuttle
# VERSION 0.1.0
# Delete Model Set by Name.
``` python
import lux

def delete_model_set(model_set_name):
    # Retrieve all model set names
    model_sets = lux.getModelSets()
    
    # Check if the specified model set exists
    if model_set_name in model_sets:
        # Delete the specified model set
        lux.removeModelSet(model_set_name)
        print(f"Model set '{model_set_name}' has been deleted.")
    else:
        print(f"Model set '{model_set_name}' does not exist.")

# Example usage
delete_model_set("Default")
```

# End of Model\Delete Model Set by Name.py

## Hide All Model Set Children.py
<a name="model-hide-all-model-set-children"></a>
# AUTHOR Donald Tuttle
# VERSION 0.1.0
# Script to Hide All Model Set Children
``` python
import lux

def hide_all_model_sets():
    # Get the root of the scene tree
    root = lux.getSceneTree()
    
    # Retrieve all model sets in the scene
    model_sets = [node for node in root.getChildren() if node.isModelSet()]
    
    # Hide each model set
    for model_set in model_sets:
        model_set.hide()

# Run the function to hide all model sets
hide_all_model_sets()
```

# End of Model\Hide All Model Set Children.py

## Hide All Model Sets Children.py
<a name="model-hide-all-model-sets-children"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to Hide All Model Sets
``` python
import lux

def hide_model_sets_contents():
    root_node = lux.getSceneTree()  # Get the root node of the scene tree
    for node in root_node.getChildren():  # Iterate through all child nodes
        if node.isModelSet():  # Check if the node is a model set
            for model in node.getChildren():  # Iterate through all models in the model set
                model.hide()  # Hide each model
            print(f'Model set {node.getName()} contents hidden')

hide_model_sets_contents()
```

# End of Model\Hide All Model Sets Children.py

## Hide All Model Sets and Children.py
<a name="model-hide-all-model-sets-and-children"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.4
# Script to hide all model sets and their children.
``` python
import lux

def set_visibility(node, visible):
    """
    Set visibility for the node and its children.
    """
    node.setVisibility(visible)
    for child in node.getChildren():
        set_visibility(child, visible)

def hide_all_model_sets_and_children():
    """
    Hide all model sets and their children in the scene.
    """
    try:
        root_node = lux.getSceneTree()
        if not root_node:
            raise Exception("Could not find root group! Make sure to load a scene.")
        
        all_model_sets = [node for node in root_node.getChildren() if node.isModelSet()]

        for model_set in all_model_sets:
            set_visibility(model_set, False)
            print(f"Model set '{model_set.getName()}' and its children are now hidden.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    hide_all_model_sets_and_children()

if __name__ == "__main__":
    main()
```


# End of Model\Hide All Model Sets and Children.py

## Hide and Show Model Sets.py
<a name="model-hide-and-show-model-sets"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Hides the Default ModelSet and Shows Product ModelSet.
``` python
import lux

def set_active_model_set(active_model_set_name):
    # Retrieve all model sets (active and inactive)
    root_node = lux.getSceneTree()
    all_model_sets = [node for node in root_node.getChildren() if node.isModelSet()]

    # Collect the names of all model sets
    all_model_set_names = [model_set.getName() for model_set in all_model_sets]

    # Check if the specified model set exists in the list
    if active_model_set_name in all_model_set_names:
        # Set the specified model set as active, deactivating all others
        success = lux.setModelSets([active_model_set_name])
        if success:
            print(f"Model set '{active_model_set_name}' is now active.")
        else:
            print(f"Failed to set model set '{active_model_set_name}' as active.")
    else:
        print(f"Model set '{active_model_set_name}' not found.")

# Example usage: Hide "Default" and show "Product"
set_active_model_set("Product")
```

# End of Model\Hide and Show Model Sets.py

## Hides Node by Name.py
<a name="model-hides-node-by-name"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Hides Node by "YourNodeName" update name in script.
``` python
import lux

def hide_node_by_name(node_name):
    # Get the root node of the scene
    root_node = lux.getSceneTree()
    
    # Find nodes by name
    nodes = root_node.find(name=node_name)
    
    # Check if any nodes were found
    if nodes:
        # Hide each node found
        for node in nodes:
            node.hide()
            print(f"Node '{node.getName()}' has been hidden.")
    else:
        print(f"No nodes found with the name '{node_name}'.")

# Example usage: Hide a node with the name "YourNodeName"
hide_node_by_name("AO")
```

# End of Model\Hides Node by Name.py

## Model Set Remove Default .py
<a name="model-model-set-remove-default-"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# script uses the lux.removeModelSet function, where you specify the name of the model set you want to remove. If the model set you're trying to remove is the current model set, KeyShot will automatically switch to the default model set​​.
``` python
import lux

# Name of the model set to remove
model_set_name = "Default"

# Remove the model set
lux.removeModelSet(name=model_set_name)

print(f'Model set "{model_set_name}" has been removed.')
```

# End of Model\Model Set Remove Default .py

## Model Set Renamer.py
<a name="model-model-set-renamer"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 1.0.0
# GUI opens and cycles through model sets allow you to rename each manualy.
``` python
import lux

def main():
    root_node = lux.getSceneTree()
    for model_set in root_node.getChildren():
        if model_set.isModelSet():
            # Prompt for each model set
            new_name_input = lux.getInputDialog(title=f"Rename {model_set.getName()}", 
                                                values=[("new_name", lux.DIALOG_TEXT, "Enter New Name:", model_set.getName())])
            if new_name_input:
                model_set.setName(new_name_input["new_name"])

if __name__ == "__main__":
    main()
```

# End of Model\Model Set Renamer.py

## Model Translate and Rotate Example.py
<a name="model-model-translate-and-rotate-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Example Script to Translate and Rotate.
``` python
import lux
import luxmath

def get_user_input():
    """
    Display a dialog for the user to input the name of the part.
    """
    default_part_name = "Enter part name here"
    values = [("part_name", lux.DIALOG_TEXT, "Enter the part name:", default_part_name)]
    opts = lux.getInputDialog(title="Input Part Name", desc="Enter the name of the part to position", values=values)
    return opts

def position_part_on_ground_and_rotate(part_name):
    """
    Position the selected part based on the specified translation and apply a rotation.
    """
    scene_root = lux.getSceneTree()
    part_nodes = scene_root.find(part_name)

    if not part_nodes:
        print(f"Part {part_name} not found.")
        return

    for part_node in part_nodes:
        try:
            # Specify the desired translation and rotation
            translation_vector = luxmath.Vector(-27.6982, 106.1204, 80.7838)  # Translate -27.6982 units on X, 106.1204 on Y, and 80.7838 units on Z
            rotation_degrees = 0  # Rotate 0 degrees around Y-axis
            
            # Create translation and rotation matrices
            translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)
            rotation_matrix = luxmath.Matrix.makeRotate(luxmath.Vector(0, 0, 0), rotation_degrees)
            
            # Combine translation and rotation matrices
            transform_matrix = translation_matrix.mul(rotation_matrix)
            
            # Apply the combined transformation to the part
            part_node.applyTransform(transform_matrix, absolute=False)
        except AttributeError:
            print(f"{part_node.getName()} cannot be transformed.")

# Main script
user_input = get_user_input()

if user_input and "part_name" in user_input and user_input["part_name"] != "Enter part name here":
    selected_part = user_input["part_name"]
    position_part_on_ground_and_rotate(selected_part)
    print("Transformation applied.")
else:
    print("Operation cancelled or invalid input.")
```

# End of Model\Model Translate and Rotate Example.py

## New Model Set Template.py
<a name="model-new-model-set-template"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Template for creating new model sets.
``` python
import lux

def create_keyshot_scene():
    # Create 3 model sets: "Shadow", "Product", and "AO"
    lux.newModelSet("Product")
    lux.newModelSet("ProductPro")
    lux.newModelSet("Accessory")
    lux.newModelSet("ProductAccessory")
    lux.newModelSet("ProductProAccessory")
    lux.newModelSet("ProductAccessoryExploded")
    
    # Create 2 cameras: "Front" and "Back"
#   lux.newCamera("Front")
#   lux.newCamera("Back")

# Execute the scene creation function
create_keyshot_scene()
```

# End of Model\New Model Set Template.py

## Product Model Sets.py
<a name="model-product-model-sets"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Template for creating new model sets.
``` python
import lux

def create_keyshot_scene():
    # Create 3 model sets: "Shadow", "Product", and "AO"
    lux.newModelSet("Product")
    lux.newModelSet("ProductPro")
    lux.newModelSet("Accessory")
    lux.newModelSet("ProductAccessory")
    lux.newModelSet("ProductProAccessory")
    lux.newModelSet("ProductAccessoryExploded")
    
    # Create 2 cameras: "Front" and "Back"
#   lux.newCamera("Front")
#   lux.newCamera("Back")

# Execute the scene creation function
create_keyshot_scene()
```

# End of Model\Product Model Sets.py

## Show All Model Sets Children.py
<a name="model-show-all-model-sets-children"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to show all model sets and their children.
``` python
import lux

def set_visibility_recursive(node, visible):
    """
    Set visibility for the node and its children.
    """
    node.setVisibility(visible)
    for child in node.getChildren():
        set_visibility_recursive(child, visible)

def show_all_model_sets_and_children():
    """
    Show all model sets and their children in the scene.
    """
    try:
        root_node = lux.getSceneTree()
        if not root_node:
            raise Exception("Could not find root group! Make sure to load a scene.")
        
        all_model_sets = [node for node in root_node.getChildren() if node.isModelSet()]

        for model_set in all_model_sets:
            set_visibility_recursive(model_set, True)
            print(f"Model set '{model_set.getName()}' and its children are now visible.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    show_all_model_sets_and_children()

if __name__ == "__main__":
    main()
```

# End of Model\Show All Model Sets Children.py

## Show All Model Sets.py
<a name="model-show-all-model-sets"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Script to show all model sets.
``` python
import lux

def show_all_model_sets_and_children():
    """
    Show all model sets and their children in the scene.
    """
    root_node = lux.getSceneTree()
    all_model_sets = [node.getName() for node in root_node.getChildren() if node.isModelSet()]

    # Set all model sets as active
    if all_model_sets:
        success = lux.setModelSets(all_model_sets)
        if success:
            print("All model sets and their children are now visible.")
        else:
            print("Failed to activate all model sets.")
    else:
        print("No model sets found in the scene.")

def main():
    show_all_model_sets_and_children()

if __name__ == "__main__":
    main()
```

# End of Model\Show All Model Sets.py

## Show Model Set.py
<a name="model-show-model-set"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.0.0
# Shows a ModelSet.
``` python
import lux

def show_model_set(model_set_name):
    # Get the root node of the scene tree
    root_node = lux.getSceneTree()
    
    # Find the model sets
    model_sets = [node for node in root_node.getChildren() if node.isModelSet()]

    # Find the specified model set by name
    for model_set in model_sets:
        if model_set.getName() == model_set_name:
            model_set.show()
            print(f"Model set '{model_set_name}' shown successfully.")
            return
    
    print(f"Model set '{model_set_name}' not found.")

# Run the show_model_set function with the desired model set name
show_model_set("Product")
```

# End of Model\Show Model Set.py

## Transform Model Sets.py
<a name="model-transform-model-sets"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Consolidated script to translate and rotate parts in specified model sets.
``` python
import lux
import luxmath

def get_visible_model_sets():
    """Returns a list of currently visible model sets."""
    return lux.getModelSets()

def set_visible_model_set(model_set_name):
    """Sets the specified model set as visible and hides others."""
    lux.setModelSets([model_set_name])

def restore_visible_model_sets(model_sets):
    """Restores the visibility of the specified model sets."""
    lux.setModelSets(model_sets)

def position_part(part_name, translation_vector, rotation_degrees):
    """
    Apply translation and rotation to a specified part.
    :param part_name: The name of the part to transform.
    :param translation_vector: Vector specifying the translation.
    :param rotation_degrees: Degrees to rotate.
    """
    scene_root = lux.getSceneTree()
    part_nodes = scene_root.find(part_name)

    if not part_nodes:
        print(f"Part {part_name} not found.")
        return

    for part_node in part_nodes:
        try:
            translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)
            rotation_matrix = luxmath.Matrix.makeRotate(luxmath.Vector(0, 0, 0), rotation_degrees)
            transform_matrix = translation_matrix.mul(rotation_matrix)
            part_node.applyTransform(transform_matrix, absolute=False)
            print(f"Transformation applied to {part_node.getName()}.")
        except AttributeError:
            print(f"{part_node.getName()} cannot be transformed.")

def position_parts_in_model_set(model_set_name, translation_vector, rotation_degrees):
    """
    Position all parts in a specified model set with the given translation and rotation.
    :param model_set_name: The name of the model set.
    :param translation_vector: Vector specifying the translation.
    :param rotation_degrees: Degrees to rotate.
    """
    visible_model_sets = get_visible_model_sets()
    set_visible_model_set(model_set_name)

    scene_root = lux.getSceneTree()
    model_set_nodes = [node for node in scene_root.getChildren() if node.getName() == model_set_name and node.isModelSet()]

    if not model_set_nodes:
        print(f"Model set {model_set_name} not found.")
        restore_visible_model_sets(visible_model_sets)
        return

    for model_set_node in model_set_nodes:
        children = model_set_node.getChildren()
        if not children:
            print(f"Model set {model_set_name} has no children.")
            restore_visible_model_sets(visible_model_sets)
            return

        for child in children:
            part_name = child.getName()
            print(f"Positioning part {part_name} in model set {model_set_name}")
            position_part(part_name, translation_vector, rotation_degrees)
    
    restore_visible_model_sets(visible_model_sets)

def main():
    model_sets_translations = [
        {"model_set": "Case", "translation": luxmath.Vector(-27.6982, 106.1204, 80.7838), "rotation": 0},
        {"model_set": "Case Pro", "translation": luxmath.Vector(-27.6982, 107.1587, 80.7838), "rotation": 0},
        {"model_set": "Device", "translation": luxmath.Vector(-27.6982, 106.1204, 82.4664), "rotation": 0},
        {"model_set": "Device Pro", "translation": luxmath.Vector(-27.6982, 107.1587, 80.7838), "rotation": 0},
        {"model_set": "SP", "translation": luxmath.Vector(-27.4659, 109.0805, 85.8128), "rotation": 0},
        {"model_set": "SP Pro", "translation": luxmath.Vector(-27.4659, 109.0805, 85.8128), "rotation": 0},
        {"model_set": "Device Explode", "translation": luxmath.Vector(-27.6982, 106.1204, 51.4489), "rotation": 0},
        {"model_set": "Device Pro Explode", "translation": luxmath.Vector(-27.6982, 107.1587, 45.7345), "rotation": 0},
        {"model_set": "Default", "translation": luxmath.Vector(0, 0, 0), "rotation": 0}  # Adjust as necessary
    ]

    for entry in model_sets_translations:
        model_set_name = entry["model_set"]
        translation_vector = entry["translation"]
        rotation_degrees = entry["rotation"]
        position_parts_in_model_set(model_set_name, translation_vector, rotation_degrees)

if __name__ == "__main__":
    main()
```

# End of Model\Transform Model Sets.py

## Batch Rename Find Replace GUI.py
<a name="naming-batch-rename-find-replace-gui"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Find Replace Batch Rename
``` python
import lux

def get_all_children(node):
    """Recursively get all children of a node."""
    all_children = []
    try:
        children = node.getChildren()
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))
    except Exception:
        pass
    return all_children

def find_and_replace_name(original_name, find_string, replace_with):
    """Find and replace a specific string in the original name."""
    return original_name.replace(find_string, replace_with)

def rename_scene_nodes(all_nodes, find_string, replace_with):
    """Rename nodes by finding and replacing specific strings in their names."""
    for node in all_nodes:
        original_name = node.getName()
        new_name = find_and_replace_name(original_name, find_string, replace_with)
        if new_name != original_name:
            node.setName(new_name)
            print(f"Renamed '{original_name}' to '{new_name}'")

def main():
    # Define the input dialog fields with non-empty default values
    dialog_fields = [
        ("find_string", lux.DIALOG_TEXT, "Enter Name to Find:", "OldName"),
        ("replace_with", lux.DIALOG_TEXT, "Enter Replacement Name:", "NewName")
    ]

    # Display the input dialog
    user_input = lux.getInputDialog(title="Find and Replace Names",
                                    desc="Enter the name or part of the name to find and the name to replace it with.",
                                    values=dialog_fields)

    if user_input:
        find_string = user_input["find_string"]
        replace_with = user_input["replace_with"]

        root_node = lux.getSceneTree()
        all_nodes = get_all_children(root_node)

        rename_scene_nodes(all_nodes, find_string, replace_with)

if __name__ == "__main__":
    main()
```


# End of Naming\Batch Rename Find Replace GUI.py

## Batch Rename Material Clashing Node Names.py
<a name="naming-batch-rename-material-clashing-node-names"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Find Replace Batch Rename
```python
import lux

def get_all_children(node):
    """Recursively get all children of a node."""
    all_children = []
    try:
        children = node.getChildren()
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))
    except Exception:
        pass
    return all_children

def find_and_replace_name(original_name, find_string, replace_with):
    """Find and replace a specific string in the original name."""
    return original_name.replace(find_string, replace_with)

def rename_scene_nodes(all_nodes, find_string, replace_with):
    """Rename nodes by finding and replacing specific strings in their names."""
    for node in all_nodes:
        original_name = node.getName()
        new_name = find_and_replace_name(original_name, find_string, replace_with)
        if new_name != original_name:
            node.setName(new_name)
            print(f"Renamed '{original_name}' to '{new_name}'")

def main():
    # Define the input dialog fields with non-empty default values
    dialog_fields = [
        ("find_string", lux.DIALOG_TEXT, "Enter Name to Find:", "OldName"),
        ("replace_with", lux.DIALOG_TEXT, "Enter Replacement Name:", "NewName")
    ]

    # Display the input dialog
    user_input = lux.getInputDialog(title="Find and Replace Names",
                                    desc="Enter the name or part of the name to find and the name to replace it with.",
                                    values=dialog_fields)

    if user_input:
        find_string = user_input["find_string"]
        replace_with = user_input["replace_with"]

        root_node = lux.getSceneTree()
        all_nodes = get_all_children(root_node)

        rename_scene_nodes(all_nodes, find_string, replace_with)

if __name__ == "__main__":
    main()
```

# End of Naming\Batch Rename Material Clashing Node Names.py

## Batch Rename Model Sets.py
<a name="naming-batch-rename-model-sets"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 1.1.1
# Script for batch renaming model sets in KeyShot with a user interface.
```python
import lux  # Import the KeyShot built-in module 'lux'.

def rename_individual_model_set(model_set):
    """
    Display a dialog for renaming an individual model set with options for prefix, suffix, and separator.

    :param model_set: The model set object to be renamed.
    """
    # Define the GUI elements for renaming the model set.
    values = [
        ("prefix", lux.DIALOG_TEXT, "Enter Prefix:", " "),  # Default value is a space.
        ("name", lux.DIALOG_TEXT, "Enter Name:", model_set.getName()),  # Current name as default.
        ("suffix", lux.DIALOG_TEXT, "Enter Suffix:", " "),  # Default value is a space.
        ("separator", lux.DIALOG_TEXT, "Enter Separator (e.g., _, -, #):", "_")  # Default separator.
    ]

    # Display the dialog and get user input for the model set.
    opts = lux.getInputDialog(title=f"Rename {model_set.getName()}", values=values)

    if opts:
        # Extract and clean user inputs.
        prefix = opts["prefix"].strip()  # Remove leading/trailing spaces.
        name = opts["name"]
        suffix = opts["suffix"].strip()  # Remove leading/trailing spaces.
        separator = opts["separator"]

        # Construct the new name based on user inputs.
        new_name_parts = [part for part in [prefix, name, suffix] if part]  # Filter out empty parts.
        new_name = separator.join(new_name_parts)  # Join parts with the separator.
        model_set.setName(new_name)  # Set the new name for the model set.

def main():
    """
    Main function to execute the script.
    """
    # Get the root node of the scene tree.
    root_node = lux.getSceneTree()
    # Iterate through each child node and rename model sets.
    for model_set in root_node.getChildren():
        if model_set.isModelSet():
            rename_individual_model_set(model_set)

# Execute the main function.
if __name__ == "__main__":
    main()
```

# End of Naming\Batch Rename Model Sets.py

## Batch Rename Rhino CAD.py
<a name="naming-batch-rename-rhino-cad"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Batch Rename RHINO CAD "Clashing Node Names" with a unique UPPERCASE name, replaces spaces and colons with one underscore, 
# removes # from KeyShot duplicates, and removes any text within parentheses along with the parentheses themselves.
```python
import lux
import re  # Regular expression module

def get_all_children(node):
    """Recursively get all children of a node."""
    all_children = []
    try:
        children = node.getChildren()
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))
    except Exception:
        pass
    return all_children

def sanitize_name(name):
    """Sanitize the node name by replacing multiple spaces with a single underscore, removing '#', and converting to uppercase. 
    Also replaces colons with underscores and removes text within parentheses."""
    name = re.sub(r'\s+', '_', name)  # Replace multiple spaces with a single underscore
    name = name.replace('#', '')      # Remove '#'
    name = name.replace(':', '_')     # Replace ':' with '_'
    name = re.sub(r'\(.*?\)', '', name).strip()  # Remove text within parentheses
    return name.upper()  # Convert name to uppercase

def rename_nodes(all_nodes):
    """Rename nodes by sanitizing names and handling duplicates."""
    name_count = {}
    new_names = {}

    for node in all_nodes:
        try:
            node_name = node.getName() or f"Unnamed_{node.getType()}"  # Assign a default name if unnamed
            sanitized_name = sanitize_name(node_name)
            new_names[node] = sanitized_name
            name_count[sanitized_name] = name_count.get(sanitized_name, 0) + 1
        except AttributeError as e:
            print(f"Error with node: {e}")

    for node, new_name in new_names.items():
        if name_count[new_name] > 1:
            duplicate_number = 1
            original_new_name = new_name
            while f"{original_new_name}_{duplicate_number:03d}" in name_count:
                duplicate_number += 1
            final_name = f"{original_new_name}_{duplicate_number:03d}"
            node.setName(final_name)
            name_count[final_name] = 1
            print(f"Renamed node from '{node.getName()}' to '{final_name}'")
        elif new_name != node.getName():
            node.setName(new_name)
            print(f"Renamed node from '{node.getName()}' to '{new_name}'")

def rename_shader_nodes(material_name):
    """Rename shader nodes in the material graph to update the material name."""
    material_graph = lux.getMaterialGraph(material_name)
    if material_graph:
        shader_nodes = material_graph.getMaterialNodes()
        for node in shader_nodes:
            old_name = node.getName() or f"Unnamed_Shader_{node.getType()}"
            new_name = sanitize_name(old_name)
            if new_name != old_name:
                node.setName(new_name)
                print(f"Renamed shader node from '{old_name}' to '{new_name}'")

# Get the root node of the scene
root_node = lux.getSceneTree()

# Get all nodes in the scene
all_nodes = get_all_children(root_node)

# Rename scene nodes
rename_nodes(all_nodes)

# Rename shader nodes in materials for each node
for node in all_nodes:
    try:
        material_name = node.getMaterial()
        if material_name:
            rename_shader_nodes(material_name)
    except AttributeError:
        pass
```

# End of Naming\Batch Rename Rhino CAD.py

## Batch Rename Rhino Clashing Node Names Remove Underscores Colons.py
<a name="naming-batch-rename-rhino-clashing-node-names-remove-underscores-colons"></a>
```python
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Renames "Clashing Node Names" with a unique UPPERCASE name, replaces spaces and colons with one underscore, and removes # from keyshot duplicates.

import lux
import re  # Regular expression module

def get_all_children(node):
    """Recursively get all children of a node."""
    all_children = []
    try:
        children = node.getChildren()
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))
    except Exception:
        pass
    return all_children

def sanitize_name(name):
    """Sanitize the node name by replacing multiple spaces with a single underscore, removing '#', and converting to uppercase. Also replaces colons with underscores."""
    name = re.sub(r'\s+', '_', name)  # Replace multiple spaces with a single underscore
    name = name.replace('#', '')      # Remove '#'
    name = name.replace(':', '_')     # Replace ':' with '_'
    return name.upper()  # Convert name to uppercase

def rename_nodes(all_nodes):
    """Rename nodes by sanitizing names and handling duplicates."""
    name_count = {}
    new_names = {}

    for node in all_nodes:
        try:
            node_name = node.getName() or f"Unnamed_{node.getType()}"  # Assign a default name if unnamed
            sanitized_name = sanitize_name(node_name)
            new_names[node] = sanitized_name
            name_count[sanitized_name] = name_count.get(sanitized_name, 0) + 1
        except AttributeError as e:
            print(f"Error with node: {e}")

    for node, new_name in new_names.items():
        if name_count[new_name] > 1:
            duplicate_number = 1
            original_new_name = new_name
            while f"{original_new_name}_{duplicate_number:03d}" in name_count:
                duplicate_number += 1
            final_name = f"{original_new_name}_{duplicate_number:03d}"
            node.setName(final_name)
            name_count[final_name] = 1
            print(f"Renamed node from '{node.getName()}' to '{final_name}'")
        elif new_name != node.getName():
            node.setName(new_name)
            print(f"Renamed node from '{node.getName()}' to '{new_name}'")

def rename_shader_nodes(material_name):
    """Rename shader nodes in the material graph to update the material name."""
    material_graph = lux.getMaterialGraph(material_name)
    if material_graph:
        shader_nodes = material_graph.getMaterialNodes()
        for node in shader_nodes:
            old_name = node.getName() or f"Unnamed_Shader_{node.getType()}"
            new_name = sanitize_name(old_name)
            if new_name != old_name:
                node.setName(new_name)
                print(f"Renamed shader node from '{old_name}' to '{new_name}'")

# Get the root node of the scene
root_node = lux.getSceneTree()

# Get all nodes in the scene
all_nodes = get_all_children(root_node)

# Rename scene nodes
rename_nodes(all_nodes)

# Rename shader nodes in materials for each node
for node in all_nodes:
    try:
        material_name = node.getMaterial()
        if material_name:
            rename_shader_nodes(material_name)
    except AttributeError:
        pass

```

# End of Naming\Batch Rename Rhino Clashing Node Names Remove Underscores Colons.py

## Rename Clashing Node Names.py
<a name="naming-rename-clashing-node-names"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.1
# Script for renaming "Clashing Node Names" in KeyShot, making them unique, uppercase, and formatted properly.
```python
import lux
import re  # Import the regular expression module for string manipulation.

# Function to recursively get all child nodes of a given node.
def get_all_children(node):
    """Recursively get all children of a node."""
    all_children = []
    try:
        children = node.getChildren()
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call to get children of children.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

# Function to sanitize the name of a node.
def sanitize_name(name):
    """Sanitize the node name by replacing spaces with underscores, removing '#', and converting to uppercase."""
    name = re.sub(r'\s+', '_', name)  # Replace spaces with a single underscore.
    name = name.replace('#', '')     # Remove '#'.
    return name.upper()  # Convert the name to uppercase.

# Function to rename nodes in the scene.
def rename_nodes(all_nodes):
    """Rename nodes by sanitizing names and handling duplicates."""
    name_count = {}
    new_names = {}

    for node in all_nodes:
        try:
            node_name = node.getName() or f"Unnamed_{node.getType()}"  # Default name if node is unnamed.
            sanitized_name = sanitize_name(node_name)
            new_names[node] = sanitized_name
            name_count[sanitized_name] = name_count.get(sanitized_name, 0) + 1
        except AttributeError as e:
            print(f"Error with node: {e}")

    # Rename the nodes, adding numbers to duplicates.
    for node, new_name in new_names.items():
        if name_count[new_name] > 1:
            duplicate_number = 1
            original_new_name = new_name
            # Ensure the new name is unique by appending a number.
            while f"{original_new_name}_{duplicate_number:03d}" in name_count:
                duplicate_number += 1
            final_name = f"{original_new_name}_{duplicate_number:03d}"
            node.setName(final_name)
            name_count[final_name] = 1
            print(f"Renamed node from '{node.getName()}' to '{final_name}'")
        elif new_name != node.getName():
            node.setName(new_name)
            print(f"Renamed node from '{node.getName()}' to '{new_name}'")

# Function to rename shader nodes within a material graph.
def rename_shader_nodes(material_name):
    """Rename shader nodes in the material graph to update the material name."""
    material_graph = lux.getMaterialGraph(material_name)
    if material_graph:
        shader_nodes = material_graph.getMaterialNodes()
        for node in shader_nodes:
            old_name = node.getName() or f"Unnamed_Shader_{node.getType()}"
            new_name = sanitize_name(old_name)
            if new_name != old_name:
                node.setName(new_name)
                print(f"Renamed shader node from '{old_name}' to '{new_name}'")

# Main process starts here.
# Get the root node of the scene.
root_node = lux.getSceneTree()

# Get all nodes in the scene.
all_nodes = get_all_children(root_node)

# Rename scene nodes.
rename_nodes(all_nodes)

# Rename shader nodes in materials for each node.
for node in all_nodes:
    try:
        material_name = node.getMaterial()
        if material_name:
            rename_shader_nodes(material_name)  # Call function to rename shader nodes.
    except AttributeError:
        pass  # Ignore errors if node doesn't have a material attribute.
```

# End of Naming\Rename Clashing Node Names.py

## Rename Model Sets per Imported CAD.py
<a name="naming-rename-model-sets-per-imported-cad"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Rename Model Sets per CAD Model or first child.
```python
def renameModelSetAfterFirstChild():
    """
    Automatically renames model sets based on the name of the first child model.
    """
    root_node = lux.getSceneTree()
    for model_set in root_node.getChildren():
        if model_set.isModelSet():
            # Assuming the first child is the target for naming
            if model_set.getChildren():
                first_child = model_set.getChildren()[0]
                new_name = first_child.getName()
                model_set.setName(new_name)
                print(f"Model set renamed to: {new_name}")

def main():
    # Example import process
    # importModelFunction()

    # Rename model sets after the import
    renameModelSetAfterFirstChild()

if __name__ == "__main__":
    main()
```

# End of Naming\Rename Model Sets per Imported CAD.py

## Rename ModelSets Manual.py
<a name="naming-rename-modelsets-manual"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 1.0.0
# Script to open a GUI and allow manual renaming of each model set in KeyShot.
```python
import lux  # Import the KeyShot built-in module 'lux'.

def main():
    """
    Main function to execute the script.
    """
    # Get the root node of the scene tree.
    root_node = lux.getSceneTree()
    # Iterate through each child of the root node.
    for model_set in root_node.getChildren():
        # Check if the child is a model set.
        if model_set.isModelSet():
            # Display a dialog for renaming the model set.
            new_name_input = lux.getInputDialog(title=f"Rename {model_set.getName()}",
                                                values=[("new_name", lux.DIALOG_TEXT, "Enter New Name:", model_set.getName())])
            # Check if the user provided a new name.
            if new_name_input:
                # Set the new name to the model set.
                model_set.setName(new_name_input["new_name"])

# Check if the script is being run directly (not imported).
if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly.
```

# End of Naming\Rename ModelSets Manual.py

## Renames Nodes Parenthesis.py
<a name="naming-renames-nodes-parenthesis"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Renames Nodes with Parenthesis.
```python
import lux
import re

def get_all_children(node):
    """Recursively get all children of a node."""
    all_children = []
    try:
        children = node.getChildren()
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))
    except Exception:
        pass
    return all_children

def remove_text_in_parentheses(original_name, counter):
    """Remove text within parentheses and append a unique identifier if needed."""
    # Remove text within parentheses from the original name
    new_name = re.sub(r'\(.*?\)', '', original_name).strip()
    # Append a unique identifier if needed (e.g., if there are duplicates)
    if counter > 1:
        new_name += "_" + str(counter)
    return new_name

def rename_scene_nodes(all_nodes):
    """Rename nodes using the provided renaming function."""
    counter = 1
    names_tracker = {}
    for node in all_nodes:
        original_name = node.getName()
        new_name = remove_text_in_parentheses(original_name, names_tracker.get(original_name, 0) + 1)
        # Update or add the name to the tracker to keep count of duplicates
        names_tracker[original_name] = names_tracker.get(original_name, 0) + 1
        node.setName(new_name)
        print(f"Renamed '{original_name}' to '{new_name}'")

def main():
    # GUI Confirmation
    user_input = lux.getInputDialog(
        title="Confirm Node Renaming", 
        desc="This will rename all nodes by removing text within parentheses. Proceed?", 
        values=[("confirm", lux.DIALOG_CHECK, "Confirm Rename", False)]
    )

    if user_input and user_input.get("confirm"):
        root_node = lux.getSceneTree()
        all_nodes = get_all_children(root_node)
        rename_scene_nodes(all_nodes)
    else:
        print("Node renaming cancelled by the user.")

if __name__ == "__main__":
    main()
```


# End of Naming\Renames Nodes Parenthesis.py

## Add To Queue.py
<a name="render-add-to-queue"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# HEADLESS COMPLIANT
# Configure to add the rendering task to the queue instead of rendering immediately
```python
import lux

# Get current render options
opts = lux.getRenderOptions()

# Configure to add the rendering task to the queue instead of rendering immediately
opts.setAddToQueue(True)

# Add more configuration to opts as needed here

# Add your render task to the queue
# Note: You would typically also configure other render options before adding to the queue
lux.renderImage("/path/to/save/image.png", opts=opts)

# After adding all desired tasks to the queue, start processing the queue
# lux.processQueue()


```
# End of Render\Add To Queue.py

## Batch Render Incrmental Screenshots.py
<a name="render-batch-render-incrmental-screenshots"></a>
```python
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Batch render incrmental screenshots.

import lux

def take_and_save_screenshots(start_frame, end_frame, frame_step):
    for current_frame in range(start_frame, end_frame + 1, frame_step):
        # Directly set the animation frame
        lux.setAnimationFrame(current_frame)
        print(f"Frame {current_frame} set.")

        # Capture the screenshot immediately after setting the frame
        screenshot_path = lux.screenshot()
        print(f"Screenshot saved: {screenshot_path}")

def main():
    dialog_values = [
        ("start_frame", lux.DIALOG_INTEGER, "Start Frame:", 0, (0, 10000)),
        ("end_frame", lux.DIALOG_INTEGER, "End Frame:", 10, (0, 10000)),
        ("frame_step", lux.DIALOG_INTEGER, "Frame Step:", 1, (1, 100))
    ]
    user_input = lux.getInputDialog(title="Capture Animation Frames", 
                                    desc="Set frame range for screenshots. Starting at frame 0 is recommended.",
                                    values=dialog_values)
    if user_input:
        take_and_save_screenshots(int(user_input['start_frame']), int(user_input['end_frame']),
                                  int(user_input['frame_step']))
    else:
        print("User cancelled the dialog.")

if __name__ == "__main__":
    main()
```

# End of Render\Batch Render Incrmental Screenshots.py

## Queue Render And Name Per Image Style.py
<a name="render-queue-render-and-name-per-image-style"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Queue renders and name per image style.
```python
import lux

def render_with_style_based_name(output_folder):
    # Get all available image styles
    image_styles = lux.getImageStyles()
    
    # Get current render options
    render_options = lux.getRenderOptions()
    
    # Set to add renders to the queue
    render_options.setAddToQueue(True)
    
    for style in image_styles:
        # Set the active image style
        lux.setActiveImageStyle(style)
        
        # Get the current image style (now that it's set) to retrieve its name
        image_style = lux.getActiveImageStyle()
        image_style_name = image_style.getName()
        
        # Customize the file name based on the image style
        file_name = f"{output_folder}/{image_style_name}_render.png"
        
        # Render the image with the customized file name and current render options
        lux.renderImage(file_name, width=1920, height=1080, opts=render_options)
        print(f"Queued render for image style '{image_style_name}' as: {file_name}")

# Example usage
output_folder = "C:/Users/Public/Documents/KeyShot/Renderings/"
render_with_style_based_name(output_folder)
```

# End of Render\Queue Render And Name Per Image Style.py

## Queue Render SwapToggle Aspect Ratio.py
<a name="render-queue-render-swaptoggle-aspect-ratio"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Update aspect ratio changing from landscape to portrait (and vice versa) orientation and add to queue with a unique name based on time.
# Headless Compatible and OS agnostic.
```python
import lux
import os
import platform
from datetime import datetime

def get_default_render_path():
    if platform.system() == "Windows":
        library_path = "C:\\Users\\Public\\Documents\\KeyShot\\Renders"
    else:  # MacOS and Unix
        library_path = "/Library/Application Support/KeyShot/Renders"
    return library_path

def get_timestamped_file_name(base_file_name, extension=".png"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{base_file_name}_{timestamp}{extension}"
    return file_name

def queue_portrait_render_with_timestamp():
    current_width, current_height, base_file_name = get_current_render_resolution_and_filename()
    new_width, new_height = adjust_to_portrait_aspect(current_width, current_height)
    
    output_directory = get_default_render_path()
    output_file_name = get_timestamped_file_name(f"{base_file_name}_portrait")
    output_file_path = os.path.join(output_directory, output_file_name)
    
    render_options = lux.getRenderOptions()
    render_options.setAddToQueue(True)
    
    lux.renderImage(output_file_path, width=new_width, height=new_height, opts=render_options)
    print(f"Queued render with filename: {output_file_name}, to be saved to {output_directory}")

queue_portrait_render_with_timestamp()
```

# End of Render\Queue Render SwapToggle Aspect Ratio.py

## Render Images Commented.py
<a name="render-render-images-commented"></a>
# -*- coding: utf-8 -*-
# AUTHOR LUX DT ChatGPT
# VERSION 0.7.1
# HEADLESS COMPLIANT: Indicates the script can run without the KeyShot GUI, in a command-line environment.
# Renders all models with a chosen extension to images in KeyShot. Comments added.
```python
import os, re, sys
import os.path

# A generic input function to handle user input with validation and default values.
def genericInput(msg, default=None, check=lambda x: len(x) > 0):
    # If a default value is provided, append it to the message prompt.
    if default is not None:
        msg += " [{}] ".format(default)
    # Ensure the message prompt ends with a space.
    if not msg.endswith(" "):
        msg += " "
    # Loop until valid input is received.
    while True:
        try:
            value = input(msg)
            # If the input passes the check, return it.
            if check(value):
                return value
            # If no input is provided but a default exists, return the default.
            elif len(value) == 0 and default is not None:
                return default
        # Handle end-of-file (EOF) and keyboard interrupt exceptions gracefully.
        except EOFError:
            sys.stdout.write("\n")  # Yield a new line so next input isn't on the same line.
            continue
        except KeyboardInterrupt:
            sys.exit()

# Function to input a folder path, using genericInput for validation.
def inputFolder(msg):
    return genericInput(msg, check=lambda x: os.path.isdir(x))

# Function to input text with a default value.
def inputText(msg, default):
    return genericInput(msg, default=default)

# Checks if a given string represents an integer within an optional range.
def intInRange(value, valueRange=None):
    try:
        n = int(value)
        if valueRange is not None:
            return n >= valueRange[0] and n <= valueRange[1]
        else:
            return True
    except ValueError:
        return False

# Function to input an integer, ensuring it falls within an optional range.
def inputInt(msg, default, valueRange=None):
    return int(genericInput(msg, default=default, check=lambda x: intInRange(x, valueRange)))

# Allows the user to select an item from a list, displaying options with indices.
def inputItem(msg, defaultIndex, items):
    pre = ""
    for i in range(len(items)):
        pre += "[{}] {}\n".format(i + 1, items[i])
    idx = inputInt(pre + msg, defaultIndex + 1, (1, len(items))) - 1
    return (idx, items[idx])

# Function to input a boolean value, interpreting various affirmative responses as True.
def inputBool(msg, default=False):
    return str(genericInput(msg, default=default)).lower() in ["y", "yes", "true", "1"]

# Cleans the input file extension by removing leading periods and converting to lowercase.
def cleanExt(ext):
    while ext.startswith("."):
        ext = ext[1:]
    return ext.lower()

# The main function orchestrating the rendering process.
def main():
    # Fetches available material templates and scene information from KeyShot.
    tmpls = ["-- None --"] + lux.getMaterialTemplates()
    info = lux.getSceneInfo()
    opts = {}
    # Different input methods based on whether KeyShot is in GUI mode or headless.
    if not lux.isHeadless():
        # GUI input dialog for selecting options.
        values = [("folder", lux.DIALOG_FOLDER, "Folder to import from:", None),
                  ("iext", lux.DIALOG_TEXT, "Input file format to read:", "bip"),
                  ("oext", lux.DIALOG_TEXT, "Output image format:", "png"),
                  ("width", lux.DIALOG_INTEGER, "Output width:", info["width"]),
                  ("height", lux.DIALOG_INTEGER, "Output height:", info["height"]),
                  (lux.DIALOG_LABEL, "--"),
                  ("template", lux.DIALOG_ITEM, "Apply material template on each import (optional):",
                   tmpls[0], tmpls),
                  (lux.DIALOG_LABEL, "--"),
                  ("queue", lux.DIALOG_CHECK, "Add to queue", True),
                  ("process", lux.DIALOG_CHECK, "Process queue after running script", False)]
        desc = "Renders all models with a chosen input extension to images of chosen output extension."
        opts = lux.getInputDialog(title = "Render Images",
                                  desc = desc,
                                  values = values,
                                  id = "renderimages.py.luxion")
    else:
        # Headless mode input through command line prompts.
        opts["folder"] = inputFolder("Folder to import from:")
        opts["iext"] = inputText("Input file format to read:", "bip")
        opts["oext"] =  inputText("Output image format:", "png")
        opts["width"] =  inputInt("Output width:", info["width"])
        opts["height"] =  inputInt("Output height:", info["height"])
        opts["template"] = inputItem("Apply material template on each import (optional):", 0, tmpls)
        opts["queue"] = inputBool("Add to queue", True)
        opts["process"] = inputBool("Process queue after running script", False)
    # Exit if no options were provided.
    if not opts: return

    # Validation checks for folder, input extension, and output extension.
    if len(opts["folder"]) == 0:
        raise Exception("Folder cannot be empty!")
    fld = opts["folder"]

    if len(opts["iext"]) == 0:
        raise Exception("Input extension cannot be empty!")
    iext = cleanExt(opts["iext"])
    reFiles = re.compile(".*{}".format(iext), re.IGNORECASE)
    found = False
    for f in os.listdir(fld):
        if reFiles.match(f):
            found = True
            break
    if not found:
        raise Exception("Could not find any input files matching the extension \"{}\" in \"{}\"!"
                        .format(iext, fld))

    if len(opts["oext"]) == 0:
        raise Exception("Output extension cannot be empty!")
    oext = cleanExt(opts["oext"])

    # Extracting additional options for rendering.
    width = opts["width"]
    height = opts["height"]
    template = opts["template"]
    queue = opts["queue"]
    process = opts["process"]

    # Setting the material template if one was chosen.
    if template[0] == 0:
        template = None
    else:
        template = template[1]

    # Fetching render options and setting queue addition.
    opts = lux.getRenderOptions()
    opts.setAddToQueue(queue)

    # Importing and rendering each file found with the specified extension.
    for f in [f for f in os.listdir(fld) if f.lower().endswith(iext)]:
        path = fld + os.path.sep + f
        lux.newScene()

        print("Importing {}".format(path))
        lux.importFile(path)

        if template:
            print("Setting material template {}".format(template))
            lux.setMaterialTemplate(template)

        path = path + "." + oext
        print("Rendering {}".format(path))
        lux.renderImage(path = path, width = width, height = height, opts = opts)

    # Processing the queue if selected.
    if process:
        print("Processing queue")
        lux.processQueue()

main()  # Executes the main function.
```

# End of Render\Render Images Commented.py

## Render Optimal Ambient Occlusion Pass.py
<a name="render-render-optimal-ambient-occlusion-pass"></a>
# -*- coding: utf-8 -*-
# AUTHOR LUX DT ChatGPT
# VERSION 1.18.2
# DESCRIPTION: This script sets up a scene for ambient occlusion rendering.
# It configures the lighting settings, environment, hides all model sets except for the one named 'AO', and queues the cameras for rendering.
# Assumes Units are in meters.
```python
import lux
import luxmath
import os
import time

def clean_ext(ext):
    """Ensure the file extension is properly cleaned."""
    while ext.startswith("."):
        ext = ext[1:]
    return ext.lower()

def configure_render_settings(opts):
    """Configure global render settings."""
    opts.setMaxSamplesRendering(64)  # Set the maximum samples
    opts.setOutputAlphaChannel(True)  # Set alpha channel in output

    # Configure individual render passes
    opts.setOutputAmbientOcclusionPass(False)
    opts.setOutputCausticsPass(False)
    opts.setOutputClownPass(False)
    opts.setOutputDepthPass(False)
    opts.setOutputDiffusePass(False)
    opts.setOutputDirectLightingPass(False)
    opts.setOutputIndirectLightingPass(False)
    opts.setOutputLabelsPass(False)
    opts.setOutputNormalsPass(False)
    opts.setOutputRawPass(False)
    opts.setOutputReflectionPass(False)
    opts.setOutputRefractionPass(False)
    opts.setOutputRenderLayers(False)
    opts.setOutputShadowPass(False)

    opts.setAddToQueue(True)  # Add render job to queue
    print("Render settings configured with 64 samples and an Alpha Channel.")

def get_library_path():
    """Determine the KeyShot 'Resources Library' path based on the operating system."""
    if os.name == 'nt':  # Windows
        library_path = os.path.join(os.environ['PUBLIC'], "Documents", "KeyShot", "Renderings")
    else:  # macOS and Unix/Linux
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot", "Renderings")
    return library_path

def get_unique_file_name(base_name, ext):
    """Generate a unique file name using a timestamp."""
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    unique_file_name = f"{base_name}_{timestamp}.{ext}"
    return unique_file_name

def load_environment_from_library(env_filename):
    """Load an environment from the KeyShot library and apply it to the scene if not already present."""
    try:
        active_env = lux.getActiveEnvironment()
        if active_env and active_env.getName().lower() == "all black 4k ao":
            print(f"Environment 'All Black 4K AO' is already active.")
            return active_env
        
        if active_env and active_env.getName().lower() == env_filename.lower():
            # Rename active environment
            active_env.setName("All Black 4K AO")
            print(f"Environment '{env_filename}' is already loaded and renamed to 'All Black 4K AO'.")
            return active_env
        
        # Load environment from library
        library_envs = lux.getLibraryEnvironments()
        full_env_path = None
        for lib_env_path in library_envs:
            if env_filename.lower() in os.path.basename(lib_env_path).lower():
                full_env_path = lib_env_path
                break
        
        if full_env_path is not None:
            new_env = lux.newEnvironment(name="All Black 4K AO", activate=True)
            if new_env.setLightingEnvironment(full_env_path):
                print(f"Environment '{env_filename}' has been successfully loaded and set.")
                return new_env
            else:
                print(f"Failed to apply environment '{env_filename}'.")
        else:
            print(f"The environment '{env_filename}' could not be found in the KeyShot library.")
    except Exception as e:
        print(f"An error occurred while setting the environment '{env_filename}': {e}")
    return None

def set_environment_parameters(env, brightness, size, height, rotation):
    """Sets the parameters for the specified environment."""
    try:
        if env:
            env.setBrightness(brightness)
            env.setSize(size)
            env.setHeight(height)
            env.setRotation(rotation)
            env.setBackgroundColor((255, 255, 255))  # Set background to white color
            env.setGroundSize(0.00001)  # Set ground size to 0.01mm (minimum allowed value)
            env.setGroundShadows(False)  # Disable ground shadows
            env.setOcclusionGroundShadows(False)  # Disable occlusion ground shadows
            env.setGroundReflections(False)  # Disable ground reflections
            env.setFlattenGround(False)  # Disable flatten ground

            # Ensure background type is set to color
            lux.setActiveEnvironment(env.getName())
            lux.getActiveEnvironment().setBackgroundColor((255, 255, 255))  # Ensure background is set to color
            print(f"Parameters for environment '{env.getName()}' have been successfully set.")
        else:
            print(f"Environment not found.")
    except Exception as e:
        print(f"An error occurred while setting parameters for environment '{env.getName()}': {e}")

def set_active_model_set(active_model_set_name):
    """Set the specified model set as active, hiding all others."""
    try:
        root_node = lux.getSceneTree()
        all_model_sets = [node for node in root_node.getChildren() if node.isModelSet()]
        all_model_set_names = [model_set.getName() for model_set in all_model_sets]

        if active_model_set_name in all_model_set_names:
            lux.setModelSets([active_model_set_name])
            print(f"Model set '{active_model_set_name}' is now active.")
        else:
            print(f"Model set '{active_model_set_name}' not found.")
    except Exception as e:
        print(f"Failed to set active model set: {e}")

def hide_all_model_sets_except(active_model_set_name):
    """Hide all model sets except for the specified one."""
    try:
        root_node = lux.getSceneTree()
        for node in root_node.getChildren():
            if node.isModelSet() and node.getName() != active_model_set_name:
                node.hide()
                print(f"Model set '{node.getName()}' has been hidden.")
            elif node.getName() == active_model_set_name:
                node.show()
                print(f"Model set '{node.getName()}' is shown.")
    except Exception as e:
        print(f"Failed to hide model sets: {e}")

def queue_cameras():
    """Queue all cameras in the scene, naming the images after the scene and camera names."""
    try:
        scene_info = lux.getSceneInfo()
        scene_name = scene_info['name']
        cameras = lux.getCameras()
        opts = lux.getRenderOptions()
        configure_render_settings(opts)
        for camera_name in cameras:
            lux.setCamera(camera_name)
            image_name = f"{scene_name}_{camera_name}.png"
            lux.renderImage(path=image_name, width=3300, height=3300, opts=opts)
        print("All cameras in the scene have been queued.")
    except Exception as e:
        print(f"Failed to queue cameras: {e}")

def configure_lighting_settings():
    """Configure global lighting settings."""
    lighting_presets = lux.getLightingPresets()
    preset_name = "Basic"
    if preset_name in lighting_presets:
        lux.setLightingPreset(preset_name)
        print(f"Lighting settings configured using preset: {preset_name}")
    else:
        print(f"Lighting preset '{preset_name}' not found.")

def enable_denoise():
    """Enable denoise for the active image style."""
    try:
        image_style = lux.getActiveImageStyle()
        image_style.setDenoise(True)
        print("Denoise enabled for the active image style.")
    except Exception as e:
        print(f"Failed to enable denoise: {e}")

def main():
    try:
        configure_lighting_settings()
        env = load_environment_from_library("All Black 4K.klf")  # Load the "All Black 4K.klf" environment
        if env:
            set_environment_parameters(env, brightness=0.001, size=3, height=0, rotation=0)  # Set brightness to 0.001 and size to 3000mm
            set_active_model_set("AO")
            hide_all_model_sets_except("AO")
            enable_denoise()
            queue_cameras()
    except Exception as e:
        print(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    main()
```

# End of Render\Render Optimal Ambient Occlusion Pass.py

## Render SwapToggle Aspect Ratio.py
<a name="render-render-swaptoggle-aspect-ratio"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Update aspect ratio changing (Toggle) from landscape to portrait (and vice versa) orientation and render with a unique name.
# Headless Compatible and OS agnostic.
```python
from datetime import datetime
import lux
import os

def get_current_render_resolution_and_filename():
    scene_info = lux.getSceneInfo()
    current_width = scene_info['render_width']
    current_height = scene_info['render_height']
    file_path = scene_info['file']
    base_file_name = os.path.splitext(os.path.basename(file_path))[0] if file_path else "untitled"
    return current_width, current_height, base_file_name

def get_timestamped_file_name(base_file_name, extension=".png"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"{base_file_name}_{timestamp}{extension}"
    return file_name

def swap_aspect_ratio(current_width, current_height):
    return current_height, current_width

def render_with_toggled_orientation_and_unique_name():
    current_width, current_height, base_file_name = get_current_render_resolution_and_filename()
    new_width, new_height = swap_aspect_ratio(current_width, current_height)
    
    # Determine the output directory based on OS
    if os.name == 'nt':  # Windows
        output_directory = "C:\\Users\\Public\\Documents\\KeyShot\\Renderings\\"
    else:  # macOS and Unix/Linux
        output_directory = "/Library/Application Support/KeyShot/Renderings/"

    # Ensure the output directory exists
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Use the timestamp function to generate a unique file name
    output_file_name = get_timestamped_file_name(f"{base_file_name}_toggled", ".png")
    output_file_path = os.path.join(output_directory, output_file_name)

    # Get current render options
    render_options = lux.getRenderOptions()

    # Render the image with the new orientation immediately
    lux.renderImage(output_file_path, width=new_width, height=new_height, opts=render_options)
    print(f"Rendered image with toggled orientation: {new_width}x{new_height}, saved to {output_file_path}")

# Execute the function
render_with_toggled_orientation_and_unique_name()
```

# End of Render\Render SwapToggle Aspect Ratio.py

## Screenshot.py
<a name="render-screenshot"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Takes a screenshot saves it to Renders folder.
```python
import lux

def take_and_save_screenshot():
    # Take a screenshot of the current real-time view
    screenshot_path = lux.screenshot()
    
    # Print the path of the saved screenshot
    print(f"Screenshot saved: {screenshot_path}")

# Call the function to take and save the screenshot
take_and_save_screenshot()


```
# End of Render\Screenshot.py

