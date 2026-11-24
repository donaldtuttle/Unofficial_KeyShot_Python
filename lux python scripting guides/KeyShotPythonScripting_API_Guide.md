# KeyShot Python Scripting Guide

## Table of Contents

1. [Chapter 1: Introduction to KeyShot Scripting](#chapter-1-introduction-to-keyshot-scripting)
   - [1.1 Overview of KeyShot Scripting](#11-overview-of-keyshot-scripting)
   - [1.2 Getting Started with Python in KeyShot](#12-getting-started-with-python-in-keyshot)
   - [1.3 Basic Python Concepts for KeyShot Scripting](#13-basic-python-concepts-for-keyshot-scripting)
   
2. [Chapter 2: lux.SceneTree Class](#chapter-2-luxscenetree-class-and-node-management)
   - [2.1 Accessing Scene Nodes Using lux.getSceneTree()](#21-accessing-scene-nodes-using-luxgetscenetree)
   - [2.2 Finding Nodes in the Scene](#22-finding-nodes-in-the-scene)
   - [2.3 Showing All Hidden Nodes](#23-showing-all-hidden-nodes)
   - [2.4 Changing Materials of Nodes](#24-changing-materials-of-nodes)
   - [2.5 Moving Nodes Between Groups](#25-moving-nodes-between-groups)
   - [2.6 Additional lux.SceneNode Functions](#26-additional-luxscenenode-functions)
   - [2.7 Best Practices for Managing Scene Nodes](#27-best-practices-for-managing-scene-nodes)

3. [Chapter 3: lux.Node Class](#chapter-3-luxnode-class)
   - [3.1 Overview of the Node Class](#31-overview-of-the-node-class)
   - [3.2 Node Properties and Methods](#32-node-properties-and-methods)
   - [3.3 Node Types: MODEL, OBJECT, GROUP](#33-node-types-model-object-group)
   - [3.4 Working with Node Transforms](#34-working-with-node-transforms)
   - [3.5 Best Practices for Scene Organization](#35-best-practices-for-scene-organization)

4. [Chapter 4: luxmath.Matrix and Transformations](#chapter-4-luxmathmatrix-and-transformations)
   - [4.1 Matrix Basics](#41-matrix-basics)
   - [4.2 Understanding Bounding Boxes and Transformations in KeyShot](#42-understanding-bounding-boxes-and-transformations-in-keyshot)
   - [4.3 Translation (Moving an Object)](#43-translation-moving-an-object)
   - [4.4 Rotation](#44-rotation)
   - [4.5 Scaling](#45-scaling)
   - [4.6 Combining Transformations](#46-combining-transformations)
   - [4.7 Pattern Matrix Construction](#47-pattern-matrix-construction)
   - [4.8 Scene Tree and Node Management](#48-scene-tree-and-node-management)

5. [Chapter 5: lux.Material and Materials Management](#chapter-5-luxmaterial-and-materials-management)
   - [5.1 Accessing and Manipulating the Material Graph](#51-accessing-and-manipulating-the-material-graph)
   - [5.2 Accessing the Material Graph](#52-accessing-the-material-graph)
   - [5.3 Accessing the Root Node](#53-accessing-the-root-node)
   - [5.4 Getting Input and Output Edges of a Node](#54-getting-input-and-output-edges-of-a-node)
   - [5.5 Accessing and Modifying Node Parameters](#55-accessing-and-modifying-node-parameters)
   - [5.6 Creating and Removing Nodes](#56-creating-and-removing-nodes)
   - [5.7 Creating and Removing Edges](#57-creating-and-removing-edges)
   - [5.8 Best Practices for Material Graph Manipulation](#58-best-practices-for-material-graph-manipulation)

6. [Chapter 6: lux.Animation and Animation Scripting](#chapter-6-luxanimation-and-animation-scripting)
   - [6.1 Overview of the lux.Animation Class](#61-overview-of-the-luxanimation-class)
   - [6.2 Controlling the Animation Timeline](#62-controlling-the-animation-timeline)
   - [6.3 Navigating Through Keyframes](#63-navigating-through-keyframes)
   - [6.4 Accessing the Animation Duration](#64-accessing-the-animation-duration)
   - [6.5 Batch Rendering Animation Frames](#65-batch-rendering-animation-frames)
   - [6.6 Playing and Pausing Animations](#66-playing-and-pausing-animations)
   - [6.7 Best Practices for Timeline Navigation](#67-best-practices-for-timeline-navigation)

7. [Chapter 7: lux.Dialog and Custom GUIs](#chapter-7-luxdialog-and-custom-guis)
   - [7.1 Creating Custom Dialogs with lux.Dialog](#71-creating-custom-dialogs-with-luxdialog)
   - [7.2 Batch Operations Using GUI Dialogs](#72-batch-operations-using-gui-dialogs)
   - [7.3 Renaming Materials Using GUI Dialog](#73-renaming-materials-using-gui-dialog)
   - [7.4 Retrieving Camera Information](#74-retrieving-camera-information)
   - [7.5 Retrieving Material Parameters via GUI](#75-retrieving-material-parameters-via-gui)
   - [7.6 Common Errors in GUI Scripting](#76-common-errors-in-gui-scripting)
   - [7.7 Best Practices for GUI Development in KeyShot](#77-best-practices-for-gui-development-in-keyshot)

8. [Chapter 8: Headless Operations with lux](#chapter-8-headless-operations-with-lux)
   - [8.1 Running Scripts in Headless Mode](#81-running-scripts-in-headless-mode)
   - [8.2 Automating Batch Processes](#82-automating-batch-processes)
   - [8.3 Integrating KeyShot with External Systems](#83-integrating-keyshot-with-external-systems)
   - [8.4 Example Scripts for Headless Operations](#84-example-scripts-for-headless-operations)

9. [Chapter 9: Advanced Topics and Special Cases](#chapter-9-advanced-topics-and-special-cases)
   - [9.1 Optimizing Scene Performance with Scripting](#91-optimizing-scene-performance-with-scripting)
   - [9.2 Working with Complex Material Graphs](#92-working-with-complex-material-graphs)
   - [9.3 Headless Scripting and Automation](#93-headless-scripting-and-automation)
   - [9.4 Advanced Error Handling and Debugging](#94-advanced-error-handling-and-debugging)
   - [9.5 Special Use Cases](#95-special-use-cases)
   - [9.6 Best Practices for Advanced Scripting](#96-best-practices-for-advanced-scripting)

10. [Chapter 10: Best Practices](#chapter-10-best-practices)
    - [10.1 Efficient Scene Management](#101-efficient-scene-management)
    - [10.2 Managing Material Complexity](#102-managing-material-complexity)
    - [10.3 Writing Modular and Reusable Code](#103-writing-modular-and-reusable-code)
    - [10.4 Error Handling and Debugging](#104-error-handling-and-debugging)
    - [10.5 Performance Optimization Tips](#105-performance-optimization-tips)
    - [10.6 Best Practices for Batch Processing and Automation](#106-best-practices-for-batch-processing-and-automation)
    - [10.7 Version Control and Documentation](#107-version-control-and-documentation)
    - [10.8 Summary of Best Practices](#108-summary-of-best-practices)

11. [Chapter 11: Common Issues and Solutions](#chapter-11-common-issues-and-solutions)
    - [11.1 Node-Related Issues](#111-node-related-issues)
    - [11.2 Material and Shader Issues](#112-material-and-shader-issues)
    - [11.3 Transformation and Matrix Issues](#113-transformation-and-matrix-issues)
    - [11.4 Camera Issues](#114-camera-issues)
    - [11.5 Render and Output Issues](#115-render-and-output-issues)
    - [11.6 Headless Scripting Issues](#116-headless-scripting-issues)
    - [11.7 Common Errors and Solutions](#117-common-errors-and-solutions)

12. [Chapter 12: Reference and Resources](#chapter-12-reference-and-resources)
    - [12.1 KeyShot Python API Reference](#121-keyshot-python-api-reference)
    - [12.2 Glossary of Terms](#122-glossary-of-terms)
    - [12.3 Scripting Workflow Best Practices](#123-scripting-workflow-best-practices)
    - [12.4 External Resources](#124-external-resources)
    - [12.5 Additional Resources](#125-additional-resources)
    - [12.6 Conclusion](#126-conclusion)


---

## Chapter 1: Introduction to KeyShot Scripting

---

### **1.1 Overview of KeyShot Scripting**

KeyShot provides Python scripting support, enabling users to automate workflows, customize processes, and manipulate scene elements programmatically. With KeyShot scripting, you can access the KeyShot API to manipulate the scene tree, create animations, modify materials, and automate rendering tasks.

KeyShot scripting can be useful in several scenarios:
- Automating repetitive tasks.
- Customizing rendering and scene management.
- Enhancing workflows with custom tools and user interfaces.

---

### **1.2 Getting Started with Python in KeyShot**

To begin using Python scripting in KeyShot:
1. **Access the Python Console**: In KeyShot, navigate to the `Scripts` tab in the toolbar and open the Python Console.
2. **Write and Execute Code**: Python scripts can be executed within this console or saved as `.py` files for batch processing or automation.
3. **Import KeyShot Libraries**: The `lux` library contains functions for manipulating scene objects, materials, cameras, lights, and animations.

#### Example: Basic Python Script in KeyShot
```python
import lux

# Get the root of the scene tree
scene = lux.getSceneTree()

# Print the names of all nodes in the scene
for node in scene.getChildren():
    print(node.getName())
```

---

### **1.3 Basic Python Concepts for KeyShot Scripting**

Familiarity with basic Python programming concepts is necessary for writing KeyShot scripts. Some concepts to focus on include:
- **Variables**: Used to store data.
- **Functions**: Reusable blocks of code.
- **Conditionals**: For controlling flow (`if-else` statements).
- **Loops**: For iterating over elements (`for`, `while` loops).

#### Example: Conditional in KeyShot Script
```python
if scene.getChildren():
    print("There are nodes in the scene.")
else:
    print("The scene is empty.")
```

---

## Chapter 2: lux.SceneTree Class and Node Management

---

### **2.1 Accessing Scene Nodes Using `lux.getSceneTree()`**

In KeyShot scripting, accessing and manipulating scene elements is done via the scene tree. The scene tree contains all the models, parts, groups, cameras, and lights within the scene, and each node in this tree is of the type `lux.SceneNode`.

By using `lux.getSceneTree()`, you can retrieve the root node of the scene and perform various operations like hiding, showing, selecting, applying transformations, changing materials, and moving nodes.

#### Example: Retrieving the Scene Tree
```python
# Get the root of the scene tree
root = lux.getSceneTree()
print(f"Root node: {root.getName()}")
```

---

### **2.2 Finding Nodes in the Scene**

To find specific nodes in the scene, you can use the `find()` method on the root node. You can search nodes by name, type, material, or other attributes.

#### Example: Hiding Nodes Containing "Cord" in the Name
```python
# Get the scene tree root node
root = lux.getSceneTree()

# Find and hide all nodes with "Cord" in their name
for node in root.find(name="Cord"):
    node.hide()
    print(f"Hiding node: {node.getName()}")
```

#### Example: Selecting Children of a Group Named "Padding"
```python
# Find groups named "Padding" and select child nodes named "Ear Pad"
for node in root.find(name="Padding", types=lux.NODE_TYPE_GROUP):
    for child in node.getChildren():
        if child.getName() == "Ear Pad":
            child.select()
            print(f"Selected node: {child.getName()}")
```

---

### **2.3 Showing All Hidden Nodes**

If you've hidden some parts of the scene and want to show everything again, you can call `show()` on the root node to make all nodes visible.

#### Example: Show All Hidden Nodes
```python
# Show all nodes in the scene
root.show()
print("All nodes are now visible.")
```

---

### **2.4 Changing Materials of Nodes**

You can change the material of any node by using the `setMaterial()` function. This is particularly useful for applying batch changes to nodes in the scene, such as simulating ambient occlusion by applying a uniform matte material.

#### Example: Apply Matte White Material to All Nodes
```python
# Apply the "Matte White" material to all nodes
for node in root.find(""):
    node.setMaterial("Matte White")
    print(f"Set material to Matte White for node: {node.getName()}")
```

**Tip**: Use `root.find("")` to find all nodes in the scene.

---

### **2.5 Moving Nodes Between Groups**

KeyShot scripting allows you to move nodes between groups in the scene, just like using drag-and-drop in the KeyShot UI. This feature is especially useful when organizing complex scenes with many elements.

#### Example: Moving Nodes Based on Material to a Specific Group
```python
# Find the group "Headphone #1"
group_node = root.find(name="Headphone #1")[0]  # Take the first group node

# Find all nodes using a material that contains "Padding" and move them to "Headphone #1"
for node in root.find(mat="Padding"):
    node.moveToGroup(group_node)
    print(f"Moved node: {node.getName()} to group: {group_node.getName()}")
```

---

### **2.6 Additional lux.SceneNode Functions**

- **`hide()`**: Hides the node in the scene.
- **`show()`**: Makes the node visible.
- **`select()`**: Selects the node in the scene (highlighted in the KeyShot UI).
- **`deselect()`**: Deselects the node.
- **`lock()`**: Locks the node, preventing further transformations or changes.
- **`unlock()`**: Unlocks the node.
- **`duplicate()`**: Duplicates the node.
- **`applyTransform()`**: Applies a transformation matrix to the node.
- **`getChildren()`**: Returns all child nodes of a group node.
- **`setMaterial(material_name)`**: Sets the material of the node to the specified material.
- **`moveToGroup(group)`**: Moves the node to the specified group.

#### Example: Locking and Unlocking Nodes
```python
# Find a node by name and lock it
node = root.find(name="MyNode")[0]  # Assume only one node with this name
node.lock()
print(f"Locked node: {node.getName()}")

# Unlock the node later
node.unlock()
print(f"Unlocked node: {node.getName()}")
```

---

### **2.7 Best Practices for Managing Scene Nodes**

- **Efficient Node Management**: Use `find()` with specific parameters (name, type, material) to efficiently manage large scenes with many nodes.
- **Use Groups for Organization**: Group related objects together and manipulate them as a unit for easier scene management.
- **Batch Operations**: Use loops to batch process node operations, such as hiding, showing, or applying materials.
- **Visibility Control**: Use `hide()` and `show()` to control visibility, especially in scenes with many objects.

---

## Chapter 3: lux.Node Class

---

### **3.1 Overview of the Node Class**

The `lux.Node` class represents an element in the scene tree (a model, object, or group). This class provides methods to manipulate the node's properties, such as position, rotation, and scale.

---

### **3.2 Node Properties and Methods**

Nodes have several key properties and methods:
- **`getName()`**: Returns the name of the node.
- **`applyTransform()`**: Applies a transformation (e.g., translation, rotation) to the node.
- **`duplicate()`**: Creates a copy of the node.
- **`delete()`**: Removes the node from the scene.

#### Example: Get Node Properties
```python
if node:
    print("Node name:", node.getName())
```

---

### **3.3 Node Types: MODEL, OBJECT, GROUP**

Nodes can be one of the following types:
- **MODEL**: Represents an imported 3D model.
- **OBJECT**: Represents individual geometry or parts of a model.
- **GROUP**: Used to organize multiple nodes.

---

### **3.4 Working with Node Transforms**

You can manipulate the position, rotation, and scale of a node using the `applyTransform()` method. Transformations are applied using matrices (covered in more detail in Chapter 4).

#### Example: Applying a Translation to a Node
```python
import luxmath

# Create a translation matrix to move the node by 10 units along the X-axis
translation_matrix = luxmath.Matrix().makeIdentity().translate(luxmath.Vector(10, 0, 0))

# Apply the translation to the node
if node:
    node.applyTransform(translation_matrix)
    print(f"Node '{node.getName()}' moved by 10 units along the X-axis.")
```

---

### **3.5 Best Practices for Scene Organization**

1. **Organize models and parts early**: Establish a clear hierarchy in your scene tree for easier manipulation.
2. **Use grouping**: Use groups to bundle related parts and models together, making it easier to apply transformations or materials.
3. **Check node types**: Always verify node types before applying transformations to avoid errors.

---

## Chapter 4: luxmath.Matrix and Transformations

---

### **4.1 Matrix Basics**

Matrices in 3D graphics are used to perform transformations such as translation (moving), rotation, and scaling. A matrix in KeyShot is a 4x4 matrix that allows for complex object manipulations.

#### Example: Identity Matrix
```python
import luxmath

# Create an identity matrix (no transformation)
identity_matrix = luxmath.Matrix().makeIdentity()
```

---

### **4.2 Understanding Bounding Boxes and Transformations in KeyShot**

Bounding boxes define the spatial limits of an object, which is crucial for transformations like translation, rotation, and scaling.

#### **4.2.1 Bounding Box Definition**
A bounding box is the smallest box that encloses an object, defined by its minimum and maximum points along the X, Y, and Z axes.

#### **4.2.2 Retrieving Bounding Boxes for Objects**
You can retrieve the bounding box of an object using the `lux.getObjectBoundingBox()` method.

##### Example: Retrieving the Bounding Box for an Object
```python
bbox_min, bbox_max = lux.getObjectBoundingBox(node)
print(f"Bounding Box - Min: {bbox_min}, Max: {bbox_max}")
```

#### **4.2.3 Common Errors and Solutions with Bounding Boxes**
**Error**: Misalignment after applying transformations.
**Solution**: Ensure transformations are applied in the correct order: scale, rotate, then translate.

---

### **4.3 Translation (Moving an Object)**

Translation moves an object along the X, Y, and Z axes. This can be done using a translation matrix.

#### Example: Translating an Object
```python
translation_vector = luxmath.Vector(10, 5, 0)
translation_matrix = luxmath.Matrix().makeIdentity().translate(

translation_vector)

# Apply the translation to the node
node.applyTransform(translation_matrix)
```

---

## Chapter 4: luxmath.Matrix and Transformations (Continued)

---

### **4.4 Rotation**

Rotation involves turning an object around a specified axis by a given angle. KeyShot uses rotation matrices to define the amount of rotation along the X, Y, or Z axis.

#### Example: Rotating an Object
```python
import math

# Rotate by 45 degrees around the Z-axis
rotation_angle = math.radians(45)
rotation_axis = luxmath.Vector(0, 0, 1)
rotation_matrix = luxmath.Matrix().makeIdentity().rotateAroundAxis(rotation_axis, rotation_angle)

# Apply the rotation to the node
node.applyTransform(rotation_matrix)
print(f"Node '{node.getName()}' rotated 45 degrees around the Z-axis.")
```

---

### **4.5 Scaling**

Scaling changes the size of an object along the X, Y, and Z axes. You can scale uniformly (same factor in all directions) or non-uniformly (different factors for each axis).

#### Example: Scaling an Object
```python
# Scale the object by 2x along the X, Y, and Z axes
scaling_vector = luxmath.Vector(2.0, 2.0, 2.0)
scaling_matrix = luxmath.Matrix().makeIdentity().scale(scaling_vector)

# Apply the scaling transformation to the node
node.applyTransform(scaling_matrix)
print(f"Node '{node.getName()}' scaled by 2x.")
```

---

### **4.6 Combining Transformations**

In most cases, you’ll need to combine multiple transformations like scaling, rotation, and translation. The order of applying transformations matters (scaling should be applied before translation, for example).

#### Example: Applying Multiple Transformations
```python
# Create scaling, rotation, and translation matrices
scaling_matrix = luxmath.Matrix().makeIdentity().scale(luxmath.Vector(2.0, 2.0, 2.0))
rotation_matrix = luxmath.Matrix().makeIdentity().rotateAroundAxis(luxmath.Vector(0, 0, 1), math.radians(45))
translation_matrix = luxmath.Matrix().makeIdentity().translate(luxmath.Vector(10, 5, 0))

# Combine transformations: Scaling -> Rotation -> Translation
combined_matrix = scaling_matrix.mul(rotation_matrix).mul(translation_matrix)

# Apply the combined transformations to the node
node.applyTransform(combined_matrix)
print(f"Node '{node.getName()}' scaled, rotated, and translated.")
```

---

### **4.7 Pattern Matrix Construction**

Sometimes you need to arrange objects in specific patterns like grids, circles, or pyramids. You can calculate transformation matrices to position objects in these patterns.

#### **4.7.1 Spiral Pattern**
In a spiral pattern, objects are arranged in an increasing radial and angular position from a central point.

##### Example: Spiral Pattern Matrix
```python
def create_spiral_matrix(i, spacing, angle_increment, height_increment):
    angle_rad = i * angle_increment * (math.pi / 180.0)
    x_offset = math.sin(angle_rad) * spacing * i
    y_offset = math.cos(angle_rad) * spacing * i + i * height_increment
    z_offset = 0  # Maintain constant Z
    return luxmath.Matrix().makeIdentity().translate(luxmath.Vector(x_offset, y_offset, z_offset))
```

#### **4.7.2 Grid Pattern**
Objects are arranged in a grid pattern based on rows and columns.

##### Example: Grid Pattern Matrix
```python
def create_grid_matrix(i, spacing, rows, cols):
    row = i // cols
    col = i % cols
    x_offset = col * spacing
    y_offset = row * spacing
    return luxmath.Matrix().makeIdentity().translate(luxmath.Vector(x_offset, 0, y_offset))
```

#### **4.7.3 Circle Pattern**
Objects are arranged along the circumference of a circle.

##### Example: Circle Pattern Matrix
```python
def create_circle_matrix(i, radius, num_objects):
    angle = (2 * math.pi / num_objects) * i
    x_offset = math.cos(angle) * radius
    y_offset = math.sin(angle) * radius
    return luxmath.Matrix().makeIdentity().translate(luxmath.Vector(x_offset, 0, y_offset))
```

#### **4.7.4 Pyramid Pattern**
Objects are arranged in a pyramid shape, with layers decreasing in size.

##### Example: Pyramid Pattern Matrix
```python
def create_pyramid_matrix(i, spacing, base_width):
    layer = int((1 + math.sqrt(1 + 8 * i)) // 2)
    index_in_layer = i - layer * (layer - 1) // 2
    layer_width = max(base_width - layer + 1, 1)
    row = index_in_layer // layer_width
    col = index_in_layer % layer_width
    x_offset = (col - (layer_width - 1) / 2) * spacing
    z_offset = (row - (layer_width - 1) / 2) * spacing
    return luxmath.Matrix().makeIdentity().translate(luxmath.Vector(x_offset, 0, z_offset))
```

---

### **4.8 Scene Tree and Node Management**

Managing multiple nodes efficiently is critical in large scenes. Scene tree management allows for easy duplication, deletion, and transformation of multiple objects.

#### Example: Accessing and Transforming Nodes in Bulk
```python
root = lux.getSceneTree()
objects = root.find("", types=[lux.NODE_TYPE_OBJECT])

# Apply a scaling transformation to all objects
for obj in objects:
    scaling_matrix = luxmath.Matrix().makeIdentity().scale(luxmath.Vector(1.5, 1.5, 1.5))
    obj.applyTransform(scaling_matrix)
    print(f"Scaled object: {obj.getName()}")
```

---

## Chapter 5: lux.Material and Materials Management

---

### Chapter 5: Updated lux.Material and Materials Management

---

### **5.1 Accessing and Manipulating the Material Graph**

The material graph in KeyShot allows you to manipulate materials in a more advanced and flexible way. By using the `lux.getMaterialGraph()` function, you can access and modify the material nodes, parameters, and connections. The following examples cover the material graph, nodes, edges, and parameters.

---

### **5.2 Accessing the Material Graph**

You can access the material graph of a specific material by using the `lux.getMaterialGraph()` function. The material graph is an instance of the `lux.MaterialGraph` class.

#### Example: Accessing a Material Graph
```python
# Get the material graph of a material named "Matte"
graph = lux.getMaterialGraph("Matte")

# Check if the graph was retrieved successfully
if graph:
    print(f"Material graph for 'Matte' retrieved.")
else:
    print("Material graph not found.")
```

---

### **5.3 Accessing the Root Node**

Once you have the material graph, you can access the root node. The root node is an instance of the `lux.ShaderNode` class, which represents the primary shader of the material.

#### Example: Accessing the Root Node of a Material Graph
```python
# Access the root node of the material graph
root_node = graph.getRoot()

# Display information about the root node
if root_node:
    print(f"Root node: {root_node.getName()}, Type: {root_node.getType()}")
```

---

### **5.4 Getting Input and Output Edges of a Node**

Shader nodes in the material graph are connected by edges. You can retrieve the input and output edges of a node to understand how shaders are linked in the material.

#### Example: Getting Input Edges of a Node
```python
# Get input edges of the root node
input_edges = root_node.getInputEdges()

# Print details of each input edge
for edge in input_edges:
    print(f"Input edge from {edge.getSource().getName()} to {root_node.getName()}")
```

#### Example: Getting Output Edges of a Node
```python
# Get output edges of the root node
output_edges = root_node.getOutputEdges()

# Print details of each output edge
for edge in output_edges:
    print(f"Output edge from {root_node.getName()} to {edge.getTarget().getName()}")
```

---

### **5.5 Accessing and Modifying Node Parameters**

Each shader node has parameters that define its behavior (e.g., color, reflectivity). You can retrieve and modify these parameters using the `getParameter()` and `setParameter()` functions.

#### Example: Getting and Changing a Parameter Value
```python
# Get a specific parameter (e.g., "diffuse color") of the root node
diffuse_param = root_node.getParameter("diffuse")

# Check if the parameter exists and change its value
if diffuse_param:
    print(f"Current diffuse color: {diffuse_param.getValue()}")
    diffuse_param.setValue((0.8, 0.2, 0.2))  # Change to a red color
    print(f"New diffuse color set to: {diffuse_param.getValue()}")
else:
    print("Diffuse parameter not found.")
```

**Key Points**:
- Parameters can have different types (e.g., booleans, colors, floats).
- Ensure that you provide valid values for the parameter types to avoid errors.

---

### **5.6 Creating and Removing Nodes**

In KeyShot, you can create new shader nodes in the material graph to build more complex materials. For example, you can create a metal shader node and connect it to the graph.

#### Example: Creating a New Metal Shader Node
```python
# Create a new metal shader node in the material graph
metal_node = graph.newNode(lux.SHADER_TYPE_METAL)

if metal_node:
    print(f"Created a new metal shader node: {metal_node.getName()}")
else:
    print("Failed to create metal node.")
```

#### Example: Removing a Node from the Material Graph
```python
# Remove the metal shader node by instance
if metal_node:
    graph.removeNode(metal_node)
    print(f"Removed node: {metal_node.getName()}")
```

---

### **5.7 Creating and Removing Edges**

Edges in the material graph connect shader nodes. You can create edges between nodes to link shader outputs to inputs, such as connecting a texture node to the diffuse input of a shader.

#### Example: Creating an Edge Between Two Nodes
```python
# Assuming you have two nodes (e.g., root_node and metal_node)
if root_node and metal_node:
    edge = graph.newEdge(source=metal_node, target=root_node, param="surface")
    print(f"Created an edge from {metal_node.getName()} to {root_node.getName()} on the 'surface' parameter.")
```

#### Example: Removing an Edge
```python
# Remove an edge by instance
if edge:
    graph.removeEdge(edge)
    print("Edge removed.")
```

---

### **5.8 Best Practices for Material Graph Manipulation**

- **Error Handling**: Always check if nodes, parameters, and edges exist before performing operations. This ensures that your scripts handle cases where materials or connections may not be present.
- **Testing Parameter Types**: Use `getParameter()` to retrieve the parameter type and ensure you are setting the correct values.
- **Performance Considerations**: Complex material graphs with many nodes and connections can impact performance. Be mindful of how many nodes and edges you add to a material graph.

---

## Chapter 6: lux.Animation and Animation Scripting

---

### **6.1 Overview of the lux.Animation Class**

In KeyShot, while object transformations such as translation, rotation, and scaling cannot be animated directly via scripts, you can navigate the animation timeline, control time-based actions, and manipulate the existing keyframe animations through scripting.

Scripting in KeyShot for animations is primarily focused on:
- **Navigating the Animation Timeline**: Jumping to specific points in time.
- **Rendering Frames at Specific Points in Time**: This is useful for creating batch renders of an animation sequence.
- **Playing, pausing, or stopping animations**.
- **Accessing and adjusting timeline parameters**.

---

### **6.2 Controlling the Animation Timeline**

Using KeyShot’s Python API, you can control the timeline and access specific points within the animation for rendering or other purposes.

#### Key Methods:
- **`lux.setCurrentTime(time)`**: Sets the current time in the animation timeline.
- **`lux.getCurrentTime()`**: Gets the current time in the animation timeline.
- **`lux.getAnimationDuration()`**: Returns the total duration of the animation.
- **`lux.play()`**: Starts playing the animation from the current time.
- **`lux.stop()`**: Stops the animation at the current time.
- **`lux.pause()`**: Pauses the animation at the current time.

#### Example: Setting the Animation Time
```python
import lux

# Set the animation timeline to 5 seconds
lux.setCurrentTime(5.0)

# Get the current time (should be 5.0)
current_time = lux.getCurrentTime()
print(f"Current animation time: {current_time} seconds")
```

---

### **6.3 Navigating Through Keyframes**

If an animation is already set up in the scene (created via the KeyShot UI), you can navigate through the timeline to access specific keyframes.

#### Example: Moving to a Specific Time in the Animation
```python
# Move the timeline to the 3-second mark
lux.setCurrentTime(3.0)

# Render the frame at the 3-second mark
lux.renderImage("output_at_3_seconds.png", width=1920, height=1080)
```

---

### **6.4 Accessing the Animation Duration**

You can retrieve the total duration of an animation sequence using `lux.getAnimationDuration()`.

#### Example: Retrieving and Printing the Animation Duration
```python
# Get the total animation duration
animation_duration = lux.getAnimationDuration()

print(f"Total animation duration: {animation_duration} seconds")
```

---

### **6.5 Batch Rendering Animation Frames**

One practical application of timeline navigation in KeyShot scripting is batch rendering animation frames. By iterating through the timeline and rendering frames at each step, you can generate images for the entire animation sequence.

#### Example: Batch Rendering Animation Frames at Regular Intervals
```python
# Define animation duration and time step between renders
animation_duration = lux.getAnimationDuration()
time_step = 1.0  # Render a frame every second

# Loop through the timeline, rendering frames
for t in range(0, int(animation_duration), int(time_step)):
    lux.setCurrentTime(t)
    output_filename = f"render_at_{t}_seconds.png"
    lux.renderImage(output_filename, width=1920, height=1080)
    print(f"Rendered frame at {t} seconds")
```

---

### **6.6 Playing and Pausing Animations**

Using the `lux.play()`, `lux.pause()`, and `lux.stop()` functions, you can control the playback of an animation directly in KeyShot.

#### Example: Playing and Pausing the Animation
```python
# Play the animation
lux.play()

# Pause the animation after 5 seconds
lux.setCurrentTime(5.0)
lux.pause()

print("Animation paused at 5 seconds")
```

---

### **6.7 Best Practices for Timeline Navigation**

- **Batch Rendering**: Use scripts to render frames at regular intervals, particularly for high-resolution animations.
- **Time Control**: Always ensure that the `lux.setCurrentTime()` is correctly set before performing time-sensitive operations like rendering or saving.
- **Efficiency**: When batch rendering, render only at necessary intervals to avoid performance issues.

---

## Chapter 7: lux.Dialog and Custom GUIs

---

### Chapter 7: Updated GUI and Custom Dialogs in KeyShot

---

### **7.1 Creating Custom Dialogs with lux.Dialog**

KeyShot’s Python API allows you to create custom graphical user interfaces (GUIs) to collect user inputs via dialogs. These dialogs are crucial when building interactive scripts that require user input for executing actions like batch operations, material handling, and scene manipulation.

The `lux.getInputDialog()` function is the primary method for creating these dialogs. It allows you to define various types of inputs such as text, file paths, folder paths, and numerical inputs.

---

### **7.2 Batch Operations Using GUI Dialogs**

#### **7.2.1 Batch Importing Models**

This example demonstrates how to use a GUI dialog to select multiple model files for batch importing into KeyShot. It utilizes the `lux.DIALOG_FILE` type to allow users to select files.

```python
import lux
import os

def batch_import_models():
    # Ask user to select model files for import
    file_paths = lux.getInputDialog(
        title="Batch Import Models",
        desc="Select model files to import",
        values=[("model_files", lux.DIALOG_FILE, "Model files:", None, True)])  # True allows multiple file selection
    
    if file_paths:
        for file_path in file_paths["model_files"]:
            lux.importFile(file_path)
            print(f"Imported: {file_path}")

batch_import_models()
```

**Key Concepts:**
- `lux.DIALOG_FILE` enables file selection dialogs, where the user can choose one or more files.
- The batch import operation loops through the selected files and imports them into the scene.

---

### **7.2.2 Assigning Textures to Multi-Materials in Batch**

This example demonstrates how to use a GUI to select a folder containing textures and batch-assign them to the multi-materials in a KeyShot scene.

```python
import lux
import os

def batch_assign_textures():
    # Ask user to select a folder containing textures
    folder_path = lux.getInputDialog(
        title="Batch Assign Textures",
        desc="Select the folder containing textures",
        values=[("texture_folder", lux.DIALOG_FOLDER, "Texture folder:", None)])

    if folder_path:
        texture_folder = folder_path["texture_folder"]
        for texture_file in os.listdir(texture_folder):
            # Here you would add the logic to assign textures to multi-materials
            print(f"Assigning {texture_file} to a multi-material")

batch_assign_textures()
```

**Key Concepts:**
- `lux.DIALOG_FOLDER` allows for folder selection.
- Use `os.listdir()` to iterate over files in the selected folder, facilitating the batch assignment of textures.

---

### **7.3 Renaming Materials Using GUI Dialog**

You can rename materials in a scene to avoid name clashes or to improve organization. This example provides a GUI dialog that accepts find-and-replace terms for renaming materials.

```python
import lux

def rename_materials():
    rename_opts = lux.getInputDialog(
        title="Rename Materials",
        desc="Specify find and replace terms for material names",
        values=[("find", lux.DIALOG_TEXT, "Find:", ""),
                ("replace", lux.DIALOG_TEXT, "Replace with:", "")])

    if rename_opts:
        find_term = rename_opts["find"]
        replace_term = rename_opts["replace"]
        
        # Logic to iterate through materials and rename them
        materials = lux.getSceneMaterials()
        for material in materials:
            if find_term in material.getName():
                new_name = material.getName().replace(find_term, replace_term)
                material.setName(new_name)
                print(f"Renamed material to: {new_name}")

rename_materials()
```

**Key Concepts:**
- The `lux.DIALOG_TEXT` type allows users to input strings, which are used here for find-and-replace operations.
- The `lux.getSceneMaterials()` function retrieves all materials in the scene for iteration.

---

### **7.4 Retrieving Camera Information**

This script provides a GUI that retrieves and displays information about the currently active camera, such as its name, position, and field of view.

```python
import lux

def get_camera_info():
    # Get the active camera
    camera = lux.getActiveCamera()
    
    # Assuming camera properties like name, position, and FOV can be retrieved
    camera_info = f"Camera Name: {camera.name}, Position: {camera.getPosition()}, FOV: {camera.getFieldOfView()}"
    
    # Display camera info in a message box
    lux.messageBox("Camera Information", camera_info)

get_camera_info()
```

**Key Concepts:**
- `lux.getActiveCamera()` retrieves the current active camera.
- `lux.messageBox()` displays a dialog with information for the user.

---

### **7.5 Retrieving Material Parameters via GUI**

This example shows how to use a GUI to input a material name and retrieve its parameters for display or further manipulation.

```python
import lux

def get_material_parameters():
    # Ask user for the material name
    material_name_input = lux.getInputDialog(
        title="Get Material Parameters",
        desc="Enter the name of the material",
        values=[("material_name", lux.DIALOG_TEXT, "Material Name:", "")])

    if material_name_input:
        material_name = material_name_input["material_name"]
        material = lux.getMaterial(material_name)
        
        if material:
            # Retrieve material parameters (replace with actual parameter retrieval)
            material_params = f"Material Name: {material.getName()}\nType: {material.getType()}"
            lux.messageBox("Material Parameters", material_params)
        else:
            lux.messageBox("Error", f"Material '{material_name}' not found")

get_material_parameters()
```

**Key Concepts:**
- The script uses `lux.getInputDialog()` to get a material name from the user.
- `lux.getMaterial()` fetches the material object for the given name, and its properties are retrieved and displayed.

---

### **7.6 Common Errors in GUI Scripting**

#### **Error: Empty Dialog Fields**
The `lux.getInputDialog()` function cannot have empty fields. Ensure every `lux.DIALOG_TEXT` or similar input has a default value to prevent errors.

#### Example: Setting a Default Value
```python
# Ensure default values are non-empty
values=[("material_name", lux.DIALOG_TEXT, "Material Name:", "DefaultMaterial")]
```

---

### **7.7 Best Practices for GUI Development in KeyShot**

- **Validation**: Always validate user inputs to ensure correct data types and values before processing them.
- **Feedback**: Provide clear feedback to the user through dialogs and message boxes to indicate success or failure.
- **Error Handling**: Handle errors gracefully by checking for null values, missing files, or invalid inputs.
- **Use Defaults**: Ensure that all dialog fields have sensible default values to prevent errors.

---

With these examples and explanations, you can efficiently create interactive and user-friendly scripts in KeyShot that make use of custom GUI dialogs. Now, we will proceed to **Chapter 9: Headless Operations with lux** for further scripting capabilities. If there are any other adjustments you'd like before moving on, feel free to let me know!

---

## Chapter 8: Headless Operations with lux

---

### **8.1 Running Scripts in Headless Mode**

KeyShot can run in "headless" mode, which allows you to perform automated tasks such as batch rendering without the need for a graphical user interface. This is particularly useful for render farms or automated pipelines.

#### Example: Command-Line Script Execution in Headless Mode
To run KeyShot in headless mode, you can use the following command in the terminal:

```bash
keyshot -script /path/to/script.py -headless
```

---

### **8.2 Automating Batch Processes**

In headless mode, batch processes such as rendering multiple scenes or exporting assets can be automated via scripts.

#### Example: Batch Rendering Multiple Scenes
```python
scenes = ["scene1.bip", "scene2.bip", "scene3.bip"]

for scene in scenes:
    lux.loadScene(scene)
    lux.renderImage(f"{scene}_render.png", width=1920, height=1080)
    print(f"Rendered {scene}")
```

---

### **8.3 Integrating KeyShot with External Systems**

Scripts can be used to integrate KeyShot with other software systems, such as asset management or content delivery systems. By combining KeyShot's headless mode with Python’s extensive library ecosystem, you can automate complex workflows involving external tools.

---

### **8.4 Example Scripts for Headless Operations**

#### Example: Automating Scene Setup and Render in Headless Mode
```python
# Load a specific scene and set render parameters
lux.loadScene("my_scene.bip")

# Set up render options
render_options = lux.getRenderOptions()
render_options.setMaxSamples(128)
render_options.setResolution(1920, 1080)

# Render the image in headless mode
lux.renderImage("render_output.png", opts=render_options)
```


---

## Chapter 8: Camera Manipulation in KeyShot

In KeyShot, scripting allows you to create, manipulate, and save cameras, just like using the Camera tab in the GUI. You can also change the view, set up standard views, and switch between cameras programmatically.

---

### **8.1 Creating and Manipulating Cameras**

You can create new cameras, adjust their orientation, and save their configurations.

#### Example: Creating a New Camera
```python
# Create a new camera named "NewCamera"
lux.newCamera("NewCamera")

# Verify the camera was created
cameras = lux.getCameras()
print(f"Available Cameras: {cameras}")
```

---

### **8.2 Manipulating Camera Position and Orientation**

After creating a camera, you can manipulate its position, orientation, and field of view. The camera can be adjusted using the `lux.setCameraLookAt()` function to specify what the camera should focus on.

#### Example: Setting the Camera LookAt Point
```python
# Set the active camera to "NewCamera"
lux.setCamera("NewCamera")

# Adjust the camera to look at a specific point
lux.setCameraLookAt(pt=(0, 0, 0))  # Look at the origin

# Save the changes to the camera
lux.saveCamera()
```

---

### **8.3 Switching Between Cameras**

KeyShot allows you to switch between available cameras in the scene using the `lux.setCamera()` function.

#### Example: Switching to a Specific Camera
```python
# List available cameras
cameras = lux.getCameras()
print(f"Available Cameras: {cameras}")

# Switch to the "default" camera
lux.setCamera("default")
```

---

### **8.4 Removing Cameras**

You can remove any camera that has been created, except for the active camera. If you remove the active camera, KeyShot will automatically switch to the "Free Camera."

#### Example: Removing a Camera
```python
# Remove the "NewCamera"
lux.removeCamera("NewCamera")

# Verify that the camera was removed
cameras = lux.getCameras()
print(f"Available Cameras after removal: {cameras}")
```

---

### **8.5 Setting Standard Views**

KeyShot provides several standard views (e.g., top, front, back) that you can use to manipulate the active camera. Setting a standard view moves the active camera to predefined positions.

#### Example: Setting a Standard View (Top View)
```python
# Set the camera to the top view
lux.setStandardView(lux.VIEW_TOP)

# Save the new camera configuration
lux.saveCamera()
```

#### Available Standard Views:
- `lux.VIEW_FRONT`
- `lux.VIEW_BACK`
- `lux.VIEW_TOP`
- `lux.VIEW_BOTTOM`
- `lux.VIEW_LEFT`
- `lux.VIEW_RIGHT`
- `lux.VIEW_ISOMETRIC`

By using these standard views, you can quickly change the orientation of the active camera to predefined angles.

---

### **8.6 Best Practices for Camera Manipulation**

- **Always Save Camera Changes**: After making any adjustments to a camera (position, orientation, view), use `lux.saveCamera()` to save those changes.
- **Use Standard Views for Consistency**: Standard views provide a consistent way to set up cameras across different scenes.
- **Switch Between Cameras**: Use `lux.setCamera()` to switch between different cameras quickly for rendering or scene inspection.

---
## Chapter 9: Advanced Topics and Special Cases

---

Chapter 9 covers advanced scripting topics in KeyShot, including more intricate operations involving material graphs, node management, scene optimization, and special use cases. These advanced functions are essential for streamlining workflows, automating processes, and handling complex scenes in both GUI and headless modes.

---

### **9.1 Optimizing Scene Performance with Scripting**

As scenes grow in complexity, managing performance becomes crucial, especially in KeyShot where large datasets and detailed materials can significantly impact rendering times. Below are strategies for optimizing performance through scripting:

#### **9.1.1 Scene Tree Management**
Managing the scene tree efficiently can reduce the load on KeyShot, especially with large assemblies. You can group nodes, hide unused nodes, and lock elements to prevent unnecessary updates.

##### Example: Hiding Unused Nodes
```python
# Hide all nodes that are not currently needed for rendering
root = lux.getSceneTree()
for node in root.find():
    if "unused" in node.getName():
        node.hide()
        print(f"Hiding node: {node.getName()}")
```

#### **9.1.2 Reducing Material Complexity**
One method to optimize a scene is to replace complex materials with simpler alternatives during certain stages of the workflow, such as test renders.

##### Example: Replacing Complex Materials with Matte Materials
```python
# Replace all complex materials with "Matte White" for test renders
for node in root.find(""):
    node.setMaterial("Matte White")
    print(f"Replaced material for node: {node.getName()}")
```

---

### **9.2 Working with Complex Material Graphs**

In certain scenarios, you'll work with complex material graphs involving multiple shaders and connections. Handling these efficiently is crucial when creating advanced materials or performing batch operations.

#### **9.2.1 Combining Multiple Shaders**

You can combine multiple shader nodes into one material graph to create custom materials. This allows for more complex visual effects such as multi-layered textures, bump maps, or procedural materials.

##### Example: Adding a Bump Map Shader to an Existing Material
```python
# Access the material graph
graph = lux.getMaterialGraph("PlasticMaterial")

# Create a new bump map shader node
bump_node = graph.newNode(lux.SHADER_TYPE_BUMP)
bump_node.setParameter("bumpMap", "path/to/bump_map.png")

# Connect the bump node to the root node
root_node = graph.getRoot()
graph.newEdge(source=bump_node, target=root_node, param="bump")
print("Bump map added to material.")
```

#### **9.2.2 Automating Complex Material Assignments**

For repetitive tasks, such as applying certain material settings across multiple objects, automation via scripting can drastically reduce the time required.

##### Example: Assigning Multi-Layered Materials to Multiple Nodes
```python
# Apply a complex multi-layer material to nodes based on certain criteria
for node in root.find(name="ComplexObject"):
    graph = lux.getMaterialGraph(node.getMaterial().getName())
    
    # Create and assign additional shader nodes as needed
    metal_node = graph.newNode(lux.SHADER_TYPE_METAL)
    root_node = graph.getRoot()
    graph.newEdge(source=metal_node, target=root_node, param="specular")
    
    print(f"Assigned multi-layer material to: {node.getName()}")
```

---

### **9.3 Headless Scripting and Automation**

Running KeyShot in headless mode allows for full automation without the graphical interface, which is useful for batch rendering, material application, and other large-scale operations.

#### **9.3.1 Setting Up Headless Operations**

To run KeyShot in headless mode, use the following command in the terminal:
```bash
keyshot.exe -script path/to/script.py -scene path/to/scene.bip -renderoutput path/to/output.png
```

#### **9.3.2 Automating Batch Rendering in Headless Mode**

You can automate batch rendering of multiple views or frames using scripting in headless mode. This is particularly useful for rendering product shots from different angles or producing animations.

##### Example: Rendering Multiple Angles in Headless Mode
```python
# Define different camera angles
angles = [lux.VIEW_FRONT, lux.VIEW_BACK, lux.VIEW_TOP, lux.VIEW_LEFT, lux.VIEW_RIGHT]

# Loop through each angle and render the scene
for angle in angles:
    lux.setStandardView(angle)
    lux.renderImage(f"render_{angle}.png", width=1920, height=1080)
    print(f"Rendered view: {angle}")
```

---

### **9.4 Advanced Error Handling and Debugging**

Advanced scripting in KeyShot often involves complex scenarios where errors may occur due to node types, parameter mismatches, or file system issues. Proper error handling and debugging are essential for preventing script failures.

#### **9.4.1 Catching and Logging Errors**

Use Python’s try-except blocks to catch exceptions and log errors for debugging purposes. This approach is useful for long-running scripts where failures can interrupt large workflows.

##### Example: Catching and Logging Errors During Node Manipulation
```python
try:
    # Example code that may cause an error
    node = root.find("NonExistentNode")[0]
    node.applyTransform(luxmath.Matrix().makeIdentity())
except IndexError as e:
    lux.logError(f"Node not found: {e}")
```

#### **9.4.2 Logging Information for Debugging**

Use the `lux.logInfo()` function to output useful debugging information during the execution of scripts. This is especially important when working with complex scenes or material graphs.

##### Example: Logging Material Graph Information
```python
# Log information about the material graph for debugging purposes
graph = lux.getMaterialGraph("PlasticMaterial")
root_node = graph.getRoot()
lux.logInfo(f"Root node: {root_node.getName()}, Type: {root_node.getType()}")

for edge in root_node.getInputEdges():
    lux.logInfo(f"Input from: {edge.getSource().getName()} to {root_node.getName()}")
```

---

### **9.5 Special Use Cases**

There are various special cases in KeyShot scripting where advanced customization is required, such as working with procedural geometry, creating custom materials, or integrating with external systems.

#### **9.5.1 Procedural Geometry Manipulation**

You can use scripting to dynamically manipulate procedural geometry, such as adjusting parameters for custom shapes or generating patterns on-the-fly.

##### Example: Adjusting Procedural Geometry Parameters
```python
# Access and modify parameters of a procedural geometry shader node
graph = lux.getMaterialGraph("ProceduralShape")
root_node = graph.getRoot()
scale_param = root_node.getParameter("scale")

# Adjust the scale of the procedural shape
if scale_param:
    scale_param.setValue(2.0)
    lux.logInfo("Adjusted procedural shape scale.")
```

#### **9.5.2 Integration with External Systems**

KeyShot can be integrated with external systems via Python scripts to automate tasks such as importing CAD data, processing textures, or exporting renders to specific directories.

##### Example: Automating CAD File Import and Render
```python
# Automate the process of importing a CAD file and rendering it
cad_file = "path/to/cadfile.step"
lux.importFile(cad_file)

# Set camera and render settings
lux.setCamera("default")
lux.renderImage("render_output.png", width=1920, height=1080)
lux.logInfo("CAD file imported and rendered successfully.")
```

---

### **9.6 Best Practices for Advanced Scripting**

- **Modularization**: Break scripts into reusable functions to reduce complexity and improve maintainability.
- **Error Handling**: Always wrap critical sections in try-except blocks to prevent unexpected crashes during execution.
- **Performance Optimization**: Use efficient node and material management techniques to reduce script runtime, especially when working with large scenes.
- **Testing**: Test scripts on smaller datasets before applying them to large scenes or batch processes.

---

## Chapter 10: Best Practices

---

This chapter focuses on best practices when scripting in KeyShot to ensure efficiency, performance, maintainability, and reliability. Following these guidelines can help reduce script errors, improve execution time, and streamline your workflow.

---

### **10.1 Efficient Scene Management**

Efficient scene management is critical when working with large, complex scenes in KeyShot. Proper organization and optimization of the scene tree can significantly reduce the impact on performance during rendering or animation tasks.

#### **10.1.1 Grouping and Organizing Nodes**
Grouping related objects together can make it easier to manage transformations, materials, and other properties.

##### Example: Grouping Objects in the Scene
```python
# Find all objects with a common prefix and group them together
root = lux.getSceneTree()
group = root.newNode(lux.NODE_TYPE_GROUP, "GroupedObjects")

for node in root.find(name="Object_"):
    node.moveToGroup(group)
    print(f"Moved {node.getName()} to 'GroupedObjects'")
```

---

### **10.2 Managing Material Complexity**

Materials can quickly become a performance bottleneck, especially when dealing with high-resolution textures, complex shaders, and multi-layer materials. Simplifying materials for draft rendering or optimizing texture resolutions can greatly enhance performance.

#### **10.2.1 Using Simple Materials for Test Renders**
For test renders or previews, you can replace complex materials with simpler ones to save rendering time.

##### Example: Replace Complex Materials with Matte for Test Renders
```python
# Replace all materials with "Matte" for faster test renders
for node in root.find(""):
    node.setMaterial("Matte White")
    print(f"Replaced material on {node.getName()}")
```

#### **10.2.2 Reducing Texture Resolutions**
Large texture files can increase memory usage and slow down rendering. By using lower-resolution textures during test phases, you can reduce the strain on system resources.

##### Example: Assigning Lower-Resolution Textures for Drafts
```python
# Assign lower-resolution textures to all materials
for node in root.find(""):
    mat = node.getMaterial()
    if mat and mat.hasTexture():
        mat.setTextureResolution(512)  # Set texture resolution to 512px
        print(f"Set low-res texture for {node.getName()}")
```

---

### **10.3 Writing Modular and Reusable Code**

When writing scripts for KeyShot, aim for modularity by breaking your code into small, reusable functions. This makes it easier to debug, maintain, and update scripts over time.

#### **10.3.1 Creating Modular Functions**
Breaking down complex scripts into smaller, more manageable functions increases readability and reusability.

##### Example: Modular Code for Node Transformation
```python
# Function to apply a transformation to a node
def apply_transformation(node, translation_vector):
    matrix = luxmath.Matrix().makeIdentity().translate(translation_vector)
    node.applyTransform(matrix)
    print(f"Applied transformation to {node.getName()}")

# Apply transformation to multiple nodes
for node in root.find(name="Object_"):
    apply_transformation(node, luxmath.Vector(10, 0, 0))
```

#### **10.3.2 Reusing Code Across Projects**
Create libraries of common functions that can be reused across multiple scripts or projects. This improves efficiency and ensures consistency in your scripts.

---

### **10.4 Error Handling and Debugging**

Effective error handling is key to ensuring that your scripts run smoothly, especially when working with large datasets or automated processes.

#### **10.4.1 Using Try-Except for Error Handling**
Wrapping code that might fail in a try-except block helps catch and log errors without breaking the script entirely.

##### Example: Handling Errors During Material Assignment
```python
try:
    node = root.find("NonExistentNode")[0]
    node.setMaterial("Matte White")
except IndexError as e:
    lux.logError(f"Node not found: {e}")
except Exception as e:
    lux.logError(f"An error occurred: {e}")
```

#### **10.4.2 Debugging with Logging**
Use `lux.logInfo()` and `lux.logError()` to output helpful debugging information when testing scripts.

##### Example: Logging Scene Node Information
```python
for node in root.find(""):
    lux.logInfo(f"Node: {node.getName()}, Type: {node.getKind()}")
```

---

### **10.5 Performance Optimization Tips**

When dealing with large or complex scenes, performance optimization becomes a priority. Here are some tips to optimize performance while scripting in KeyShot:

#### **10.5.1 Minimizing Scene Updates**
Avoid constantly updating the scene or applying changes unless necessary. Apply bulk updates in a single operation where possible.

##### Example: Apply Bulk Node Transformations in One Operation
```python
lux.beginUndoSession()
for node in root.find(""):
    matrix = luxmath.Matrix().makeIdentity().translate(luxmath.Vector(10, 0, 0))
    node.applyTransform(matrix)
lux.endUndoSession()
```

#### **10.5.2 Reducing the Number of Nodes in View**
Hide parts of the scene that are not currently being worked on to improve navigation and manipulation performance.

##### Example: Hide Non-Essential Nodes to Improve Performance
```python
# Hide all nodes except the ones needed for current work
for node in root.find(""):
    if not node.getName().startswith("Important"):
        node.hide()
        print(f"Hid node: {node.getName()}")
```

---

### **10.6 Best Practices for Batch Processing and Automation**

When automating processes in KeyShot, especially in headless mode, it is important to manage memory, file handling, and error recovery efficiently.

#### **10.6.1 Automating Render Processes**
Use batch processing scripts to automate rendering tasks, ensuring that KeyShot efficiently handles large numbers of images or views.

##### Example: Batch Rendering Multiple Views
```python
# Define multiple camera angles for batch rendering
angles = [lux.VIEW_FRONT, lux.VIEW_BACK, lux.VIEW_TOP, lux.VIEW_LEFT, lux.VIEW_RIGHT]

# Render each view in a loop
for angle in angles:
    lux.setStandardView(angle)
    lux.renderImage(f"view_{angle}.png", width=1920, height=1080)
    print(f"Rendered view: {angle}")
```

#### **10.6.2 Managing System Resources in Headless Mode**
When running KeyShot in headless mode for long periods, make sure to clean up resources such as file handles and temporary data to avoid memory leaks.

---

### **10.7 Version Control and Documentation**

When working on complex scripting projects, it's essential to maintain proper version control and documentation for future reference and team collaboration.

#### **10.7.1 Commenting Code**
Always comment your code, especially when performing complex operations or using KeyShot-specific functions that may not be intuitive to other developers.

#### **10.7.2 Using Version Control Systems (VCS)**
Consider using a version control system like Git to manage changes to your scripts. This helps track revisions, resolve conflicts, and collaborate with others.

---

### **10.8 Summary of Best Practices**

1. **Scene Management**: Use grouping, layers, and visibility controls to organize scenes and improve performance.
2. **Material Management**: Replace complex materials with simpler ones for test renders, and reduce texture resolutions when appropriate.
3. **Modular Code**: Write reusable, modular functions to improve script maintainability.
4. **Error Handling**: Implement try-except blocks for error handling and use logging for debugging.
5. **Performance Optimization**: Minimize scene updates, reduce the number of visible nodes, and apply bulk changes to improve performance.
6. **Automation**: Automate batch processes and manage resources carefully, especially in headless mode.
7. **Documentation**: Comment your code and use version control systems to manage script revisions.

---

## Chapter 11: Common Issues and Solutions

---

This chapter highlights some of the most common issues that arise when scripting in KeyShot, along with solutions and troubleshooting tips. It will help you diagnose problems and provide guidance on how to resolve them effectively.

---

### **11.1 Node-Related Issues**

#### **11.1.1 Issue: Node Not Found**
When trying to find or manipulate a node, you may encounter an error if the node does not exist or if the name is misspelled.

##### **Solution: Check Node Existence**
Before performing any operations on a node, always check if the node exists. Use proper error handling to avoid script failure.

##### Example: Handling Non-Existent Nodes
```python
node = root.find("NonExistentNode")
if node:
    # Perform operations
    print(f"Node {node.getName()} found.")
else:
    print("Node not found. Please check the node name.")
```

#### **11.1.2 Issue: Incorrect Node Type for Operation**
You may encounter issues when trying to apply a transformation or material to a node that is of the wrong type (e.g., trying to apply a material to a group instead of a part).

##### **Solution: Check Node Type**
Verify the node type before applying any transformations or materials. This ensures that the operation is appropriate for that specific node.

##### Example: Checking Node Type
```python
node = root.find("MyNode")[0]
if node.getKind() == lux.NODE_TYPE_OBJECT:
    node.setMaterial("Matte White")
else:
    print("This operation can only be applied to object nodes.")
```

---

### **11.2 Material and Shader Issues**

#### **11.2.1 Issue: Incorrect Parameter Type for Material**
When modifying material properties, you might encounter errors if the input value type is incorrect (e.g., setting a boolean value for a color parameter).

##### **Solution: Verify Parameter Type**
Check the parameter type before setting its value. This helps prevent invalid input types and reduces script errors.

##### Example: Setting Material Parameters
```python
material = lux.getMaterialGraph("PlasticMaterial")
root_node = material.getRoot()
color_param = root_node.getParameter("diffuse")

# Ensure the parameter accepts a color tuple
if color_param:
    try:
        color_param.setValue((0.5, 0.5, 0.5))  # RGB tuple
        print("Diffuse color set successfully.")
    except Exception as e:
        print(f"Error: {e}")
else:
    print("Diffuse color parameter not found.")
```

#### **11.2.2 Issue: Missing Material Graph**
When attempting to access the material graph of a node or material, you may encounter an issue where the graph is missing or not found.

##### **Solution: Verify Material Graph Existence**
Always check if the material graph exists before attempting to manipulate it.

##### Example: Handling Missing Material Graph
```python
graph = lux.getMaterialGraph("MyMaterial")
if graph:
    print("Material graph found.")
else:
    print("Material graph not found. Verify the material name.")
```

---

### **11.3 Transformation and Matrix Issues**

#### **11.3.1 Issue: Incorrect Transformation Matrix**
Improper transformations, such as incorrect scaling or rotation, can lead to unexpected results like object distortion or misalignment.

##### **Solution: Apply Transformations in the Correct Order**
The order in which transformations are applied (scaling, rotation, and translation) is critical for achieving the correct result.

##### Example: Applying Transformations in Correct Order
```python
scaling_matrix = luxmath.Matrix().makeIdentity().scale(luxmath.Vector(2.0, 2.0, 2.0))  # Scale first
rotation_matrix = luxmath.Matrix().makeIdentity().rotateAroundAxis(luxmath.Vector(0, 1, 0), math.radians(45))  # Rotate second
translation_matrix = luxmath.Matrix().makeIdentity().translate(luxmath.Vector(10.0, 0.0, 0.0))  # Translate last

# Combine transformations
transform_matrix = scaling_matrix.mul(rotation_matrix).mul(translation_matrix)
node.applyTransform(transform_matrix)
```

#### **11.3.2 Issue: Transformation Misalignment**
When applying multiple transformations (e.g., scaling, rotation, translation), you might experience misalignment of objects in the scene.

##### **Solution: Use Local vs. Global Coordinates**
Ensure you are applying transformations relative to the correct coordinate system, especially when rotating or translating objects.

---

### **11.4 Camera Issues**

#### **11.4.1 Issue: Camera Not Found**
Sometimes you may attempt to manipulate or render from a camera that does not exist in the scene.

##### **Solution: Verify Camera Existence**
Before applying transformations or rendering, check if the camera is present in the scene.

##### Example: Handling Missing Camera
```python
cameras = lux.getCameras()
if "MyCamera" in cameras:
    lux.setCamera("MyCamera")
else:
    print("Camera not found. Please check the camera name.")
```

#### **11.4.2 Issue: Incorrect Camera Angle or Position**
The camera might be positioned incorrectly, leading to undesired render outputs, especially in headless mode.

##### **Solution: Set the Camera View and Position Accurately**
Use functions like `setStandardView()` or `setCameraLookAt()` to ensure the correct positioning of the camera.

##### Example: Setting Standard Views
```python
# Set the camera to the front view
lux.setStandardView(lux.VIEW_FRONT)
lux.renderImage("front_view.png", width=1920, height=1080)
```

---

### **11.5 Render and Output Issues**

#### **11.5.1 Issue: Render Output Not Generated**
In some cases, the render output might not be generated due to incorrect file paths or missing render settings.

##### **Solution: Check File Path and Render Settings**
Verify that the output path is valid and the render settings are correctly applied.

##### Example: Handling Missing Render Output
```python
try:
    lux.renderImage("output_image.png", width=1920, height=1080)
    print("Render completed successfully.")
except Exception as e:
    print(f"Render failed: {e}")
```

#### **11.5.2 Issue: Low-Quality Output**
Renders may appear pixelated or low quality if insufficient samples or incorrect settings are used.

##### **Solution: Adjust Render Quality Settings**
Increase the sample count and ensure the resolution and other render settings are configured properly.

##### Example: Improving Render Quality
```python
render_options = lux.getRenderOptions()
render_options.setMaxSamples(128)  # Increase sample count for higher quality
lux.renderImage("high_quality_render.png", width=1920, height=1080, opts=render_options)
```

---

### **11.6 Headless Scripting Issues**

#### **11.6.1 Issue: Script Fails in Headless Mode**
Scripts that run correctly in the GUI may fail when executed in headless mode, often due to the absence of user input dialogs or missing render settings.

##### **Solution: Ensure Headless Compatibility**
Remove or replace any GUI-related functionality (e.g., dialogs) with hardcoded values or file-based inputs to ensure compatibility with headless mode.

##### Example: Replacing Dialogs with Hardcoded Values for Headless Mode
```python
# In headless mode, hardcode the values that would normally be gathered from the GUI
file_path = "path/to/scene.bip"
lux.importFile(file_path)

# Set render options and render
render_options = lux.getRenderOptions()
lux.renderImage("headless_render.png", width=1920, height=1080, opts=render_options)
```

---

### **11.7 Common Errors and Solutions**

#### **11.7.1 Error: Tuple Mismatch**
A common error involves passing tuples or lists with incorrect lengths to functions that expect specific parameter types, such as RGB colors or transformation vectors.

##### **Solution: Ensure Correct Tuple Length**
Check that the tuple or list contains the correct number of elements and that they match the expected types.

##### Example: Correcting Tuple Mismatch
```python
# Incorrect: Only two values provided
# translation_vector = luxmath.Vector(10.0, 5.0)

# Correct: Three values provided for X, Y, and Z
translation_vector = luxmath.Vector(10.0, 5.0, 0.0)
node.applyTransform(luxmath.Matrix().makeIdentity().translate(translation_vector))
```

#### **11.7.2 Error: Parameter Type Mismatch**
If a parameter is provided in an unsupported format, an error will occur, such as passing a string where a number is expected.

##### **Solution: Validate Parameter Types**
Always validate the parameter type before passing it to a function.

##### Example: Validating Parameter Type
```python
parameter = node.getParameter("scale")
if isinstance(parameter.getValue(), (float, int)):
    parameter.setValue(2.0)
else:
    print("Invalid parameter type. Expected a number.")
```

---

### **11.8 Summary of Common Issues and Solutions**

1. **Node Issues**: Always check if nodes exist and ensure correct node types are used for operations.
2. **Material and Shader Issues**: Verify parameter types and material graph existence before making changes.
3. **Transformation and Matrix Issues**: Apply transformations in the correct order and check for misalignment.
4. **Camera Issues**: Ensure that the camera is present and positioned correctly before rendering.
5. **Render Issues**: Validate render settings and file paths to ensure successful output.
6. **Headless Scripting Issues**: Replace GUI-dependent features with hardcoded values for headless mode.
7. **Common

 Errors**: Address tuple mismatches, type mismatches, and ensure valid input values.

---


## Chapter 12: Reference and Resources

---

This chapter provides an extensive reference guide to commonly used KeyShot scripting functions, constants, and resources. It also includes a glossary of important terms and a list of external resources for further learning. This reference will act as a quick lookup for script functions and offer resources to deepen your understanding of KeyShot’s scripting environment.

---

### **12.1 KeyShot Python API Reference**

This section provides a quick reference for common classes, functions, and constants used in KeyShot scripting.

---

#### **12.1.1 Key Functions and Classes**

| Function/Class                      | Description                                                                             |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| `lux.getSceneTree()`                | Retrieves the root of the scene tree, enabling access to nodes and groups.               |
| `lux.getMaterialGraph(name)`        | Retrieves the material graph of a specific material by name.                             |
| `lux.renderImage(output_path, width, height, opts)` | Renders the scene to an image file with specified width and height.                    |
| `lux.getCameras()`                  | Returns a list of all available cameras in the scene.                                    |
| `lux.setCamera(camera_name)`        | Sets the active camera by name.                                                          |
| `lux.setStandardView(view_constant)`| Sets the camera to a standard view (e.g., front, top, left, etc.).                       |
| `lux.setAnimationTime(time)`        | Sets the animation timeline to a specific time, where `time` is a float between 0 and 1. |
| `lux.newNode(node_type, name)`      | Creates a new node in the scene tree with a specified type and name.                     |
| `lux.deleteObject(node)`            | Deletes a specified node or object from the scene.                                       |
| `lux.getMaterial(name)`             | Retrieves a material by name from the scene.                                             |
| `lux.createMaterial(material_type)` | Creates a new material of the specified type (e.g., diffuse, glossy, metal).             |
| `lux.setMaterial(material)`         | Assigns a material to a node.                                                            |
| `lux.getRenderOptions()`            | Retrieves the current render options.                                                    |
| `lux.getInputDialog()`              | Opens a dialog box for user input.                                                       |

---

#### **12.1.2 Constants and Enums**

| Constant/Enum               | Description                                                  |
|-----------------------------|--------------------------------------------------------------|
| `lux.NODE_TYPE_MODEL`        | Represents a model node in the scene tree.                   |
| `lux.NODE_TYPE_OBJECT`       | Represents an object node (geometry) in the scene tree.       |
| `lux.NODE_TYPE_GROUP`        | Represents a group node in the scene tree.                   |
| `lux.VIEW_FRONT`             | Sets the camera to the front view.                           |
| `lux.VIEW_BACK`              | Sets the camera to the back view.                            |
| `lux.VIEW_TOP`               | Sets the camera to the top view.                             |
| `lux.VIEW_BOTTOM`            | Sets the camera to the bottom view.                          |
| `lux.VIEW_LEFT`              | Sets the camera to the left view.                            |
| `lux.VIEW_RIGHT`             | Sets the camera to the right view.                           |
| `lux.SHADER_TYPE_METAL`      | Represents the metal shader type in the material graph.       |
| `lux.SHADER_TYPE_DIFFUSE`    | Represents the diffuse shader type in the material graph.     |
| `lux.SHADER_TYPE_BUMP`       | Represents the bump shader type in the material graph.        |

---

### **12.2 Glossary of Terms**

This glossary defines important terms used in KeyShot scripting and rendering.

---

| Term                         | Definition                                                                             |
|------------------------------|-----------------------------------------------------------------------------------------|
| **Scene Tree**                | A hierarchical structure of nodes in KeyShot that represent models, objects, and groups.|
| **Node**                      | A fundamental element in the scene tree, representing a model, part, group, or object.  |
| **Material Graph**            | A graphical representation of a material’s shader nodes and how they are connected.    |
| **Shader Node**               | A node in the material graph that represents a specific type of shader (e.g., metal, bump).|
| **Transformation Matrix**     | A 4x4 matrix used to translate, rotate, or scale objects in 3D space.                 |
| **Viewport**                  | The window in KeyShot where the 3D scene is displayed and manipulated.                  |
| **Headless Mode**             | Running KeyShot without a graphical interface, used for batch processing and automation.|
| **Render Options**            | Settings that control how an image is rendered (e.g., resolution, samples, output path). |
| **Texture Mapping**           | The process of applying a 2D image (texture) to a 3D object’s surface.                  |
| **Multi-Material**            | A material that contains multiple sub-materials, which can be swapped dynamically.      |
| **HDRI**                      | High Dynamic Range Image, used for image-based lighting in KeyShot.                     |

---

### **12.3 Scripting Workflow Best Practices**

#### **12.3.1 Modular Code**
Write modular, reusable functions to improve the maintainability of your scripts. Each function should perform a single task and should be tested independently.

##### Example: A Modular Function for Node Translation
```python
def translate_node(node, x, y, z):
    translation_matrix = luxmath.Matrix().makeIdentity().translate(luxmath.Vector(x, y, z))
    node.applyTransform(translation_matrix)
```

#### **12.3.2 Debugging and Logging**
Use Python’s `try-except` blocks to handle errors and `lux.logInfo()` or `lux.logError()` to log useful information when debugging scripts.

##### Example: Logging Information for Debugging
```python
try:
    node = root.find("MyNode")[0]
    lux.logInfo(f"Node found: {node.getName()}")
except Exception as e:
    lux.logError(f"Error: {e}")
```

---

### **12.4 External Resources**

Here is a list of helpful external resources to further your knowledge of KeyShot scripting and Python development.

#### **12.4.1 KeyShot Documentation**
- [KeyShot Studio 2026.3 Python API](KeyShotPythonScripting_API_Documentation.md)
- Official KeyShot documentation with detailed information on the scripting API and examples.

#### **12.4.2 Python Resources**
- [Python 3.13 documentation](https://docs.python.org/3.13/)
- Python’s official documentation covering all language features, modules, and tutorials.

#### **12.4.3 3D Graphics and Rendering**
- [Real-Time Rendering](https://www.realtimerendering.com/)
- A comprehensive book and website covering topics related to 3D rendering, shaders, and graphics.

#### **12.4.4 KeyShot Community and Forums**
- [KeyShot Forum](https://community.keyshot.com/forum)
- The official KeyShot forum where users share tips, scripts, and troubleshooting advice.

---

### **12.5 Additional Resources**

- **KeyShot Blog**: Keep up-to-date with new releases, tips, and user stories on the [KeyShot Blog](https://www.keyshot.com/blog/).
- **KeyShot Tutorials**: Access tutorials on rendering, materials, and animation at [KeyShot Learning](https://www.keyshot.com/learning/).
- **Python Programming for 3D**: For those looking to dive deeper into Python scripting for 3D, explore resources like [CG Cookie](https://cgcookie.com/), which offers Python courses for 3D applications.

---

### **12.6 Conclusion**

This reference chapter offers a wide range of resources and key functions to help you quickly navigate the KeyShot scripting API. By combining the functions and best practices from previous chapters, you will be able to efficiently create powerful automation workflows, optimize your scenes, and improve your render quality. Use this section as a quick guide when scripting in KeyShot, and continue expanding your knowledge through the additional resources provided.

---

