# AUTHOR: LUX DT ChatGPT
# VERSION: 1.3.7
# PURPOSE: This script duplicates a material using lux.createMultiMaterial(), and then explicitly duplicates each node and edge
# from the original material graph into the copied material graph. This script also demonstrates adding the duplicated material
# as a sub-material into an existing Multi-Material in KeyShot.

# OPTIONAL NAMING REFERENCES:
# Rename Clashing Node Names v0.2.1 is an archived naming example in
# KeyShot-Python-AI-Knowledge, original-gpt-backup/AI_LLM_Knowledge/Scripting_Examples.txt.
# Name_Material_Graph_Nodes.py is a separately supplied material-node naming utility.
# Neither utility is included or run automatically by this script.

import lux

def add_copied_material_to_multimaterial(material_name, multi_material_name):
    """
    Duplicates the material specified by `material_name`, converts it to a Multi-Material, and adds it as a sub-material to
    the existing Multi-Material `multi_material_name`.

    Parameters:
    - material_name (str): Name of the original material to be duplicated.
    - multi_material_name (str): Name of the Multi-Material to which the duplicated material will be added.
    
    Notes:
    - It is crucial to validate that both the material to be copied and the target multi-material exist in the scene.
    - This function uses `lux.createMultiMaterial()` to handle the initial duplication efficiently.
    """
    try:
        # Step 1: Create a new Multi-Material (Copy of the Original)
        # This step clones the original material and gives it a new name.
        copied_material_name = f"{material_name}_Copy"
        clone_multi_material = lux.createMultiMaterial(name=copied_material_name, mat=material_name)

        if clone_multi_material is None:
            raise ValueError(f"Failed to create a copy of the material '{material_name}'")

        print(f"Material '{copied_material_name}' copied successfully using lux.createMultiMaterial().")

        # Step 2: Enable the copied material as a Multi-Material container
        # Once the material is copied, get the material graph and enable it for multi-material capabilities.
        copied_material_graph = lux.getMaterialGraph(name=copied_material_name)
        if copied_material_graph is None:
            raise ValueError(f"Material graph for '{copied_material_name}' not found")

        copied_material_graph.setMultiMaterial(enable=True)
        print(f"Material '{copied_material_name}' enabled as a multi-material.")

        # Step 3: Retrieve the Original Material Graph and Duplicate Nodes and Parameters
        # We now need to copy the nodes and connections from the original material graph.
        original_material_graph = lux.getMaterialGraph(name=material_name)
        if original_material_graph is None:
            raise ValueError(f"Original material graph for '{material_name}' not found.")

        print(f"Duplicating nodes and parameters from '{material_name}' to '{copied_material_name}'...")

        # Step 4: Use the explicit node and parameter duplication approach
        duplicate_material_graph(original_material_graph, copied_material_graph)

        # Step 5: Retrieve the MultiMaterial in which we want to add the copied material
        multi_material = lux.getMultiMaterial(multi_material_name)
        if multi_material is None:
            raise ValueError(f"Multi-material '{multi_material_name}' not found")

        # Display current sub-materials in the MultiMaterial for reference
        sub_materials = multi_material.getSubMaterials()
        current_sub_materials_names = [str(mat) for mat in sub_materials]
        print(f"Current sub-materials in '{multi_material_name}': {current_sub_materials_names}")

        # Step 6: Add the copied material as a sub-material by using its name
        # Use the setSubMaterials method to append the new copied material.
        if hasattr(multi_material, 'setSubMaterials'):
            new_sub_materials_names = current_sub_materials_names + [copied_material_name]
            multi_material.setSubMaterials(new_sub_materials_names)
            print(f"Copied material '{copied_material_name}' successfully added to '{multi_material_name}' as a sub-material.")
        else:
            raise AttributeError(f"'MultiMaterial' object has no method 'setSubMaterials'.")

        # Step 7: Visualize the updated list of sub-materials
        updated_sub_materials = multi_material.getSubMaterials()
        print(f"Updated sub-materials in '{multi_material_name}': {[str(mat) for mat in updated_sub_materials]}")

    except AttributeError as ae:
        print(f"An attribute error occurred: {ae}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to duplicate nodes and edges explicitly with enhanced error handling
def duplicate_material_graph(source_graph, target_graph):
    """
    Duplicate all nodes and parameters from one material graph to another, and attempt to reconnect edges.
    
    Parameters:
    - source_graph (MaterialGraph): The original material graph to be duplicated.
    - target_graph (MaterialGraph): The target material graph where nodes and edges will be copied.
    
    Notes:
    - This process involves both node creation and parameter copying, followed by reconnecting edges.
    - Ensure that all node types are supported in the target graph to avoid issues during node duplication.
    """
    node_mapping = {}  # Keep track of original and new nodes to reconnect edges

    # Step A: Duplicate nodes with detailed error handling
    for node in source_graph.getNodes():
        try:
            # Create a duplicate node in the target graph
            new_node = duplicate_node(node, target_graph)
            if new_node:
                # Duplicate all parameters from the original node to the new node
                duplicate_parameters(node, new_node)
                node_mapping[node] = new_node  # Map original node to its duplicate
                print(f"Node '{node.getName()}' duplicated successfully.")
        except Exception as e:
            print(f"Error duplicating node '{node.getName()}': {e}")

    # Step B: Duplicate edges with detailed error handling
    for node in source_graph.getNodes():
        if node in node_mapping:
            for edge in node.getOutputEdges():
                source_node = node_mapping.get(edge.getSourceNode())
                target_node = node_mapping.get(edge.getTargetNode())
                param_name = edge.getID()

                # Ensure parameter name is a string before using
                if not isinstance(param_name, str):
                    param_name = str(param_name)

                if source_node and target_node:
                    try:
                        # Create a new edge in the target graph to replicate the original connections
                        target_graph.newEdge(source_node, target_node, param_name)
                        print(f"Edge created between '{source_node.getName()}' and '{target_node.getName()}' using parameter '{param_name}'.")
                    except Exception as e:
                        print(f"Error creating edge between '{source_node.getName()}' and '{target_node.getName()}': {e}")
                else:
                    print(f"Invalid source or target node for edge: {source_node}, {target_node}")

# Function to duplicate a single node in the target graph
def duplicate_node(node, target_graph):
    """
    Duplicate a node from the source graph into the target graph.
    
    Parameters:
    - node (ShaderNode): The node from the source graph to be duplicated.
    - target_graph (MaterialGraph): The graph where the new node will be added.
    
    Returns:
    - new_node (ShaderNode): The duplicated node in the target graph.
    
    Notes:
    - Node names must be unique in the target graph, and a new name is assigned to the duplicated node.
    - Ensure the new node type matches the original for consistency in functionality.
    """
    try:
        # Create a new node in the target graph with the same type as the original
        new_node = target_graph.newNode(node.getType())
        new_node.setName(f"{node.getName()}_Copy")
        return new_node
    except Exception as e:
        print(f"Error creating a new node from '{node.getName()}': {e}")
        return None

# Function to duplicate all parameters from one node to another
def duplicate_parameters(original_node, new_node):
    """
    Duplicate all parameters of the original node into the new node.
    
    Parameters:
    - original_node (ShaderNode): The original node whose parameters will be duplicated.
    - new_node (ShaderNode): The new node where the parameters will be copied.
    
    Notes:
    - Ensure that parameter types are matched between original and new nodes to prevent errors.
    - Parameters without concrete values (pure parameters) are skipped during copying.
    """
    for param in original_node.getParameters():
        try:
            new_param = new_node.getParameter(param.getName())
            if new_param is None:
                print(f"Parameter '{param.getName()}' not found in new node.")
                continue

            if param.getType() == new_param.getType():
                new_param.setValue(param.getValue())
                print(f"Parameter '{param.getName()}' duplicated successfully.")
            else:
                print(f"Type mismatch for parameter '{param.getName()}' during duplication.")
        except Exception as e:
            print(f"Error duplicating parameter '{param.getName()}': {e}")


# Example usage
add_copied_material_to_multimaterial("MaterialName", "MultiMaterialName")
