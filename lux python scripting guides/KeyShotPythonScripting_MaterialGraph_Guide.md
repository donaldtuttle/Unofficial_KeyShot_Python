# KeyShot Python MaterialGraph Scripting

### Table of Contents

1. [Introduction to KeyShot Python Scripting for Material Graphs](#introduction-to-keyshot-python-scripting-for-material-graphs)
   - [1.1 Objective](#11-objective)
   - [1.2 Target Learning](#12-target-learning)

2. [Key Concepts and Components from the Provided Script](#key-concepts-and-components-from-the-provided-script)
   - [2.1 Named multi-material container](#21-multi-material-as-an-instance-copy)
   - [2.2 Node Duplication in Material Graph](#22-node-duplication-in-material-graph)

3. [Implementing GUI Elements in KeyShot Scripting](#implementing-gui-elements-in-keyshot-scripting)
   - [3.1 Challenges with GUI in KeyShot](#31-challenges-with-gui-in-keyshot)
   - [3.2 lux.getInputDialog() Usage](#32-luxgetinputdialog-usage)
   - [3.3 Practice Exercise](#33-practice-exercise)

4. [Deep Dive: Script Breakdown](#deep-dive-script-breakdown)
   - [4.1 Node Type Extraction](#41-node-type-extraction)
   - [4.2 Parameter Duplication](#42-parameter-duplication)

5. [Edge Handling in Material Graphs](#edge-handling-in-material-graphs)
   - [5.1 Duplicating Edges Between Nodes](#51-duplicating-edges-between-nodes)
   - [5.2 Hands-On Practice](#52-hands-on-practice)

6. [Adding and Verifying Sub-Materials in a Multi-Material](#adding-and-verifying-sub-materials-in-a-multi-material)
   - [6.1 KeyShot’s Multi-Material Limitations and Advantages](#61-keyshots-multi-material-limitations-and-advantages)
   - [6.2 Validation Check](#62-validation-check)

7. [Common Errors and Troubleshooting](#common-errors-and-troubleshooting)
   - [7.1 GUI Dialog Best Practices](#71-gui-dialog-best-practices)
   - [7.2 Robust Error Handling](#72-robust-error-handling)

8. [Advanced Concepts for Curious Participants](#advanced-concepts-for-curious-participants)

9. [Summary and Key Takeaways](#summary-and-key-takeaways)
   - [9.1 Multi-material and graph duplication](#91-multi-material-as-copyinstance)
   - [9.2 Importance of GUI and User Interaction](#92-importance-of-gui-and-user-interaction)

10. [Key Learning Takeaways](#key-learning-takeaways)
    - [10.1 Multi-Material Container](#101-multi-material-container)
    - [10.2 GUI Constraints in KeyShot](#102-gui-constraints-in-keyshot)
    - [10.3 Material Graph Manipulation](#103-material-graph-manipulation)

11. [Hands-On Exercises and Walkthrough](#hands-on-exercises-and-walkthrough)
    - [11.1 Modifying and Correcting Scripts](#111-modifying-and-correcting-scripts)
    - [11.2 Debugging Common Errors](#112-debugging-common-errors)
    - [11.3 Testing lux.getMaterialGraph() and Edge Creation Methods](#113-testing-luxgetmaterialgraph-and-edge-creation-methods)

12. [Author Information](#author-information)
    - [12.1 Version Information](#121-version-information)
    - [12.2 Script Purpose](#122-script-purpose)

---

### Additional Sections from Provided Script

13. [Traversing the KeyShot Material Graph](#traversing-the-keyshot-material-graph)
    - [13.1 Handling Node Names and IDs](#131-handling-node-names-and-ids)
    - [13.2 Consistent Naming Strategy for Nodes](#132-consistent-naming-strategy-for-nodes)
    - [13.3 Avoiding Ambiguity Between Material Graph and Node Graph](#133-avoiding-ambiguity-between-material-graph-and-node-graph)

14. [Scripting Materials Documentation](#scripting-materials-documentation)
    - [14.1 Material Graph Manipulation](#141-material-graph-manipulation)
    - [14.2 Accessing Material Graphs and Nodes](#142-accessing-material-graphs-and-nodes)
    - [14.3 Changing Parameters and Creating Edges](#143-changing-parameters-and-creating-edges)

15. [Key Enhancements for Handling Missing Node Names](#key-enhancements-for-handling-missing-node-names)
    - [15.1 Fallback Naming for Unnamed Nodes](#151-fallback-naming-for-unnamed-nodes)
    - [15.2 Assigning Names to New Nodes](#152-assigning-names-to-new-nodes)
    - [15.3 Primary Use of Node IDs for Identification and Logging](#153-primary-use-of-node-ids-for-identification-and-logging)

16. [Conclusion and Summary](#conclusion-and-summary)
    - [16.1 Differentiating Node Names vs. Material Names](#161-differentiating-node-names-vs-material-names)
    - [16.2 Avoiding Ambiguity Between Material Graph and Node Graph](#162-avoiding-ambiguity-between-material-graph-and-node-graph)


## <a name="introduction-to-keyshot-python-scripting-for-material-graphs"></a>1. Introduction to KeyShot Python Scripting for Material Graphs

- <a name="11-objective"></a>Objective: Explain what material graphs are in KeyShot and why they’re useful in 3D rendering.
- <a name="12-target-learning"></a>Target Learning: Understand how Python scripting interacts with the material graph to perform automated tasks, such as duplicating nodes and modifying materials.

## <a name="key-concepts-and-components-from-the-provided-script"></a>2. Key Concepts and Components from the Provided Script

- <a name="21-multi-material-as-an-instance-copy"></a>Named multi-material container. `lux.createMultiMaterial` supplies the destination container. A deep independent clone requires the explicit graph walk.
- <a name="22-node-duplication-in-material-graph"></a>Node Duplication in Material Graph:
- Introduce lux.getMaterialGraph(name) for accessing material graphs, and demonstrate how to duplicate nodes using target_graph.newNode() .
- Use the source-to-destination node mapping when rebuilding connections. Display names can repeat.

## <a name="implementing-gui-elements-in-keyshot-scripting"></a>3. Implementing GUI Elements in KeyShot Scripting

- <a name="31-challenges-with-gui-in-keyshot"></a>Challenges with GUI in KeyShot:
- Discuss common constraints and errors users encounter when creating input dialogs. Emphasize the requirement that input fields must not be empty and how type mismatches can lead to runtime errors .
- <a name="32-luxgetinputdialog-usage"></a>lux.getInputDialog() Usage: Walk through an example of how to gather user input with lux.getInputDialog() for selecting a multi-material or sub-material .
- <a name="33-practice-exercise"></a>Practice Exercise: Have participants modify the script to include an additional input dialog that lets users choose rendering parameters for each duplicated sub-material.

## <a name="deep-dive-script-breakdown"></a>4. Deep Dive: Script Breakdown

- <a name="41-node-type-extraction"></a>Node Type Extraction:
- Use the shader type of the source node when creating its counterpart.
- <a name="42-parameter-duplication"></a>Parameter duplication. Match source and destination parameters by name. Read and write a value only when both parameters are non-pure.

## <a name="edge-handling-in-material-graphs"></a>5. Edge Handling in Material Graphs

- <a name="51-duplicating-edges-between-nodes"></a>Duplicating Edges Between Nodes:
- Locate each source connection by its receiving parameter name. Use the mapped shader nodes and the same input name when calling `newEdge`. Pure inputs may have connections.
- <a name="52-hands-on-practice"></a>Hands-on practice. Inspect a node with two connected inputs and trace each connection to its corresponding input on the copy.

## <a name="adding-and-verifying-sub-materials-in-a-multi-material"></a>6. Adding and Verifying Sub-Materials in a Multi-Material

- <a name="61-keyshots-multi-material-limitations-and-advantages"></a>KeyShot’s Multi-Material Limitations and Advantages:
- Preserve the existing sub-material order when extending the list with `setSubMaterials()`, and re-read it using `getSubMaterials()`.
- <a name="62-validation-check"></a>Validation Check: Demonstrate how to handle situations when a material addition might fail and the steps required to debug using Python’s exception handling (try...except).

## <a name="common-errors-and-troubleshooting"></a>7. Common Errors and Troubleshooting

- <a name="71-gui-dialog-best-practices"></a>GUI Dialog Best Practices:
- Emphasize avoiding empty tuples and handling type mismatches in dialogs .
- <a name="72-robust-error-handling"></a>Highlight the need for robust error handling, especially when the material graph or input values could be incorrect.

## <a name="advanced-concepts-for-curious-participants"></a>8. Advanced Concepts for Curious Participants

- <a name="81-luxmath-for-node-transformations"></a>Luxmath for Node Transformations:
- Introduce luxmath, particularly luxmath.Matrix(), and explain how transformations like translating nodes apply in material graphs .
- <a name="82-practical-examples"></a>Practical examples to transform shader nodes or adjust their positioning in the material graph.

## <a name="summary-and-key-takeaways"></a>9. Summary and Key Takeaways

- <a name="91-multi-material-as-copyinstance"></a>Multi-material and graph duplication. Compare the receiving input names and concrete parameter values in the copy with those in the source.
- <a name="92-importance-of-gui-and-user-interaction"></a>Importance of GUI and User Interaction:
- Emphasize the importance of getting user feedback through dialogs and properly validating input to prevent errors.

## <a name="key-learning-takeaways"></a>Key Learning Takeaways

1. <a name="101-multi-material-container"></a>Multi-Material Container. The creation call supplies the destination name. The explicit walk rebuilds the graph.
2. <a name="102-gui-constraints-in-keyshot"></a>GUI Constraints in KeyShot: Understanding the limitations of GUI interactions, such as the requirement that input fields must not be empty, and learning effective error handling techniques for dialog interactions .
3. <a name="103-material-graph-manipulation"></a>Material Graph Manipulation: Learning to duplicate nodes and parameters effectively, including handling edge connections between nodes, is critical for creating sophisticated materials without redundant manual work.


- <a name="hands-on-exercises-and-walkthrough"></a><a name="111-modifying-and-correcting-scripts"></a>Trace a connection from a source shader to its receiving input in the standalone example.
- <a name="112-debugging-common-errors"></a>Introduce common errors (like type mismatches or null nodes) intentionally, and walk viewers through how to debug and resolve them.
- <a name="113-testing-luxgetmaterialgraph-and-edge-creation-methods"></a>Inspect the source and copy in the Material Graph. Check which input receives each connection.


<a name="author-information"></a><a name="121-version-information"></a><a name="122-script-purpose"></a>


The [Material Graph Copy of a Copy guide](KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.md) documents the explicit walk extracted from the v1.3.6 example. Use its standalone script for review and scene testing.

## Traversing the KeyShot Material Graph


<a name="131-handling-node-names-and-ids"></a>

My biggest takeaway is in regards to the dynamic nature of Node IDs and the need to properly handle node names, especially when dealing with new nodes that may also be created without names.

To ensure consistency even after saving and reopening a KeyShot project (which could change Node IDs), it’s crucial to:

1. Use a session-local label for an unnamed source node during traversal. Save descriptive names on newly created nodes that need to be identified in future sessions.
2. <a name="132-consistent-naming-strategy-for-nodes"></a>Define a Consistent Naming Convention: For unnamed nodes, use a systematic approach to generate names that are consistent, meaningful, and unique enough to reduce confusion during traversal or duplication.
3. Ensure Unique Naming for Newly Created Nodes: If the old node does not have a name, assign a generated name to the newly duplicated node, ensuring all nodes have a name for further operations or connections.

Script:

The script below prints the root and node names. It displays a fallback label for an unnamed source node.

```python
import lux

existing_multi_material_name = "Center_Material_MM"

# Step 1: Access the Material Graph of the Multi-Material
scene_material_names = lux.getSceneMaterials() or []
if existing_multi_material_name not in scene_material_names:
    raise ValueError(f"Multi-material '{existing_multi_material_name}' not found in the scene.")
existing_multi_material_graph = lux.getMaterialGraph(existing_multi_material_name)
if existing_multi_material_graph is None:
    raise ValueError(f"Material graph for '{existing_multi_material_name}' not found.")

# Step 2: Get the Root Node of the Multi-Material Graph
root_node = existing_multi_material_graph.getRoot()
if root_node is None:
    raise ValueError(f"Root node not found in the material graph for '{existing_multi_material_name}'.")

root_node_name = root_node.getName() or f"Unnamed_Root_{root_node.getID()}"
print(f"[INFO] Root node found: Name='{root_node_name}', ID='{root_node.getID()}'")

# Step 3: Traverse the nodes in the graph
all_nodes = existing_multi_material_graph.getNodes()
for node in all_nodes:
    node_id = node.getID()
    node_name = node.getName() or f"Unnamed_Node_{node_id}"
    node_type = node.getType()
    print(f"[INFO] Traversing Node: Name='{node_name}', ID='{node_id}', Type='{node_type}'")
```

## <a name="key-enhancements-for-handling-missing-node-names"></a>Key Enhancements for Handling Missing Node Names:

1. <a name="151-fallback-naming-for-unnamed-nodes"></a>Fallback Naming for Unnamed Nodes:
- A temporary label using the pattern `Unnamed_Node_<ID>` identifies the node in console output.
2. <a name="152-assigning-names-to-new-nodes"></a>Assigning Names to New Nodes:
- Assign descriptive names on newly created nodes to help identify them during review.
3. <a name="153-primary-use-of-node-ids-for-identification-and-logging"></a>Use of Node IDs:
- Node IDs identify individual nodes during traversal and help distinguish them in console output.
- This ensures that even if the name is not informative or absent, the Node ID provides unique identification within the session.
4. Persistent Naming for Future Sessions:
- Descriptive names on copied nodes remain useful when node IDs change after saving and reopening a file.

Summary:

- Node Name Fallbacks: The traversal prints `Unnamed_Node_<ID>` for a node without a name.
- Naming Duplicated Nodes: Choose names on newly created nodes that will be useful in future sessions.
- Primary Use of Node IDs for Identification and Logging: This ensures that every node is uniquely and dynamically tracked during operations, reducing the risk of errors when node names are missing.

## <a name="conclusion-and-summary"></a>**Conclusion**

## NODE vs. Material Names

1. <a name="161-differentiating-node-names-vs-material-names"></a>Node Names vs. Material Names:

- Material Names: These are distinct identifiers for different materials (or multi-materials) within the scene. For example, "Center_Material_MM" is a name for a specific material in the entire KeyShot scene.
- Node Names: These names represent specific nodes within a material graph, such as shaders, textures, or other graph components.

In the script:

- Material names are accessed using functions like lux.getSceneMaterials() and are directly referenced when accessing material graphs using lux.getMaterialGraph(material_name).
- Node names are internal to a material graph and represent specific nodes. This distinction is maintained by treating material-related functions and variables differently from node-related ones.

2. Clear Differentiation Between Node Names and IDs:

- Node IDs: These are unique identifiers assigned by KeyShot to each node within a material graph. They are used primarily when making connections, creating nodes, and ensuring the correct node is identified.

The use of Node IDs provides the following benefits:

- Uniqueness: Even if two nodes share the same name (or lack a name entirely), their Node IDs will be distinct.
- Connection Integrity: A node mapping identifies the source and destination nodes. Rebuilding a connection also requires the receiving parameter name.

3. Specific Use of Names and IDs:

- When traversing the material graph, the script:
- Uses getNodes() to collect all nodes and identifies nodes using their names and types if available.
- Falls back to Node IDs for logging and assigning fallback names if a node name is missing.
- To copy nodes and their connections into a separate graph, follow the explicit walk in the [Material Graph Copy of a Copy guide](KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.md).

4. <a name="133-avoiding-ambiguity-between-material-graph-and-node-graph"></a><a name="162-avoiding-ambiguity-between-material-graph-and-node-graph"></a>Avoiding Ambiguity Between Material Graph and Node Graph:

- Material Graph: When the script accesses a material graph, it does so using material names (lux.getMaterialGraph(material_name)), which provides the full graph of a given material, including all nodes.
- Node Operations: Once the material graph is accessed, `graph.getNodes()` and `node.getID()` identify individual nodes.

5. No Confusion Between Material Graph Nodes and Scene-Level Material Names:

- The scene-level material names (scene_material_names = lux.getSceneMaterials()) are distinct from the node names inside any given material graph.
- The script first accesses a material graph using a scene-level material name and then operates on the nodes within the graph by referencing node names or IDs.

### Detailed Example to Clarify Traversal and Connection Integrity:

Here’s a simplified example to demonstrate why this approach prevents confusion:

1. Access the Material Graph:


```python
existing_multi_material_graph = lux.getMaterialGraph(existing_multi_material_name)
```


- Here, existing_multi_material_name is a material name that represents a material at the scene level. The script retrieves the entire graph structure of this material.

2. Traverse the Nodes in the Material Graph:


```python
all_nodes = existing_multi_material_graph.getNodes()
```


- all_nodes contains nodes within the material graph, not to be confused with materials in the scene.

3. Identify Nodes Using Names and IDs:


```python
for node in all_nodes:
    node_id = node.getID()
    node_name = node.getName() or f"Unnamed_Node_{node_id}"
    print(node_id, node_name)
```


- node_name and node_id are used to identify nodes within the graph. Using a fallback name (`Unnamed_Node_<ID>`) ensures that all nodes are recognizable.

4. Rebuilding connections in the copy

Use the mapped nodes as the endpoints. Find the receiving input by its parameter name on the original target and pass that name to `newEdge` when rebuilding the edge.

## Takeaway:

- Clear Differentiation: The script maintains a clear differentiation between material-level operations and node-level operations. Materials are identified at the scene level using names, while nodes within a material graph are primarily identified using Node IDs and names when available.
- Fallback Mechanism: A label based on the current node ID makes an unnamed node recognizable in console output.
- Consistency Across Sessions: Descriptive names on the new nodes help when IDs change after reopening a scene.

The careful use of Node IDs, the clear separation of material names from node names, and the fallback naming mechanism make this approach robust, avoiding any ambiguity between different levels of operations within the KeyShot environment. This should allow for smooth duplication, traversal, and maintenance of material graph integrity even in complex scenarios.

## Scripting Materials Documentation

## Scripting: Material Graph

<a name="141-material-graph-manipulation"></a>

Material Graph Manipulation (GUI and Headless)

The following will go through the basic functions to manipulate the Material Graph. 


<a name="142-accessing-material-graphs-and-nodes"></a>

Access material graph
You can access the material graph like this:


```python
graph = lux.getMaterialGraph("name")
```

The graph is an instance is of the type lux.MaterialGraph which you can interact with.

Access root node
You can access the root node with the following:


```python
rootNode = graph.getRoot()
```

The rootNode is an instance is of the type lux.ShaderNode which you can interact with.

Get input edges of a node
However a node instance was obtained, you can get the edges from a Material Graph by typing:


```python
edges = node.getInputEdges()
```

Each edge instance is of the type lux.ShaderEdge that you can be interact with.

A specific edge can be obtained via:


```python
edge = node.getInputEdge("parameter name")
```

This will yield lux.ShaderEdge or an error if the name is unknown.

Get output edges of a node
However a node instance was obtained, you can get the edges from a Material Graph by typing:


```python
edges = node.getOutputEdges()
```

Each edge instance is of the type lux.ShaderEdge that you can be interact with.

Get parameters of a node
However a node instance was obtained, you can get the parameters from a Material Graph by typing:


```python
parameters = node.getParameters()
```

Each parameter instance is of the type lux.ShaderParameter that you can be interact with.

A specific parameter can be obtained via:


```python
parameter = node.getParameter("parameter name")
```

This will yield lux.ShaderParameter or error if unknown name.


<a name="143-changing-parameters-and-creating-edges"></a>

Change parameter value
A parameter, parameter, obtained via lux.SceneNode.getParameter() or lux.SceneNode.getParameters(), can have its value modified via lux.ShaderParameter.setValue().

If, for example, the parameter’s type was a boolean (true or false), you could change the value via:


```python
parameter.setValue(True)
```

Is the value supported as input but entered incorrectly it will be shown in a python exception.

If, for example, the parameter was an RGB color and you applied the boolean value, it would yield the error:

Color parameter only accepts values of type tuple or list of size 3 containing floats or ints within range [0.0,1.0], or a color name!
The following would therefore be the correct input for a color parameter:


```python
parameter.setValue((0.5, 0, 0))  # Red, (0x7F, 0x00, 0x00)
parameter.setValue("Amber")      # Color known by the color library in KeyShot
```

You can obtain a Python value via lux.ShaderParameter.getValue() to get an understanding of what’s supported or you can print a representation of the instance (str() or repr()).

Remove a node
You can remove a node, either via the instance:


```python
graph.removeNode(node)
```

Or its ID:


```python
graph.removeNode(node.getID())
```

Create a new node
You can for example create a metal node like this:


```python
metalNode = graph.newNode(lux.SHADER_TYPE_METAL)
```

Remove an edge
You can remove an edge, either via the instance:


```python
graph.removeEdge(edge)
```

Or its ID:


```python
graph.removeEdge(edge.getID())
```

Create an edge between two nodes
You can for example create an edge between node1 and node2 on the surface parameter:


```python
edge = graph.newEdge(source=node1, target=node2, param="surface")
```


### KeyShotPythonScripting MaterialGraph Copy Of A Copy Guide

See the [Material Graph Copy of a Copy guide](KeyShotPythonScripting_MaterialGraph_CopyOfaCopy_Guide.md) for the standalone script and the steps for checking the result in KeyShot.
