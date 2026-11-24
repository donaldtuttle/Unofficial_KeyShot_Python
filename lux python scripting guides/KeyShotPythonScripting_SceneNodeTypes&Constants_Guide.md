# KeyShot Python Scripting Node Types & Constants
## Table of Contents

1. [Introduction to Node Type Constants](#introduction-to-node-type-constants)
   - [1.1 Purpose of Node Type Constants](#purpose-of-node-type-constants)
   - [1.2 Breakdown of Constants](#breakdown-of-constants)

2. [How These Constants Are Used in the Script](#how-these-constants-are-used-in-the-script)
   - [2.1 Example Breakdown](#example-breakdown)
   - [2.2 Traversing the Scene Tree](#traversing-the-scene-tree)

3. [Purpose of Using Node Type Constants](#purpose-of-using-node-type-constants)

4. [Expanded Guide on Node Type Constants](#expanded-guide-on-node-type-constants)
   - [4.1 Node Types Overview](#node-types-overview)
   - [4.2 Groups](#groups)
   - [4.3 Models](#models)
   - [4.4 Parts](#parts)
   - [4.5 Objects](#objects)
   - [4.6 Children](#children)
   - [4.7 Constraints on Transformations and Operations](#constraints-on-transformations-and-operations)
   - [4.8 Material Applications](#material-applications)
   - [4.9 Best Practices](#best-practices)

5. [Conclusion](#conclusion)

## Introduction to Node Type Constants:

<a name="purpose-of-node-type-constants"></a>

In KeyShot’s Python scripting, node type constants are used to differentiate between various types of objects or nodes in the scene tree. This is important because different node types (such as groups, models, parts) have different properties and functions. These constants help the script to understand what kind of node it is interacting with and perform the appropriate operations.

<a name="breakdown-of-constants"></a>

Here’s a breakdown of the constants used in the example script:

	1.	NODE_TYPE_GROUP (1): Represents a group of nodes. Groups can contain other nodes like models or objects and serve as organizational containers.
	2.	NODE_TYPE_MODEL_SET (4): Represents a model set, which is a collection of model nodes.
	3.	NODE_TYPE_MODEL (5): Refers to a model node, which typically represents a 3D object loaded into the scene.
	4.	NODE_TYPE_OBJECT (2): This refers to a part or object node, typically used for individual parts of a model.

## How These Constants Are Used in the Script

In your script, the node type constants are used to identify the type of each node in the scene tree as you traverse it, and to execute specific operations (like printing node information or fetching material information) based on the type of node encountered.

### Example Breakdown:

```python
node_type = node.getKind()
```


The getKind() method retrieves the node type of the current node being processed. The node_type will be a numeric constant (e.g., 1, 2, 4, or 5) corresponding to one of the node types defined earlier.

Next, the script uses a dictionary to map these constants to human-readable names:

```python
type_name = {
    NODE_TYPE_MODEL_SET: "Model Set",
    NODE_TYPE_GROUP: "Group",
    NODE_TYPE_MODEL: "Model",
    NODE_TYPE_OBJECT: "Part"
}.get(node_type, "Unknown")
```


If the node_type is one of the predefined constants, the script will log the node as “Model Set,” “Group,” “Model,” or “Part.” If the node type is not recognized (i.e., not one of the predefined constants), it defaults to “Unknown.”

### Traversing the Scene Tree:

The traverse_scene_tree function recursively explores the scene, starting from the root node. It uses the node type constants to determine whether it should fetch child nodes (if it’s a group, model, or model set) or check for materials (if it’s a model or part):

```python
if node.getKind() in [NODE_TYPE_OBJECT, NODE_TYPE_GROUP, NODE_TYPE_MODEL]:
    print_material_info(node, level)
```


Here, it checks if the node is of type OBJECT, GROUP, or MODEL before trying to fetch material information.

For recursion, the script only proceeds to fetch children if the node is of type GROUP, MODEL, or MODEL_SET:

```python
if node.getKind() in [NODE_TYPE_GROUP, NODE_TYPE_MODEL, NODE_TYPE_MODEL_SET]:
    children = node.getChildren()
    for child in children:
        traverse_scene_tree(child, level + 1)
```


## Purpose of Using Node Type Constants

Using constants like NODE_TYPE_GROUP or NODE_TYPE_MODEL allows the script to dynamically adapt to different scene structures. For instance:

- Groups are purely organizational, so the script might not attempt to render or manipulate their geometry.
- Model Sets or Models could represent different objects, and the script might need to inspect their materials or properties.
- Objects are parts of models, and often contain the actual geometry and material assignments that the script might want to interact with.

By identifying node types, you can tailor the operations applied to each kind of node and avoid errors (e.g., attempting to fetch materials from a group).

## Expanded Guide on Node Type Constants

<a name="node-types-overview"></a>

#### **1. Node Types Overview**
In KeyShot scripting, nodes represent various elements in the scene such as groups, models, parts, and objects. The node type constants (like NODE_TYPE_GROUP and NODE_TYPE_MODEL) help the script distinguish between these different types so that appropriate operations can be applied.

<a name="groups"></a>

#### **2. Groups**
- **Node Type Constant**: NODE_TYPE_GROUP
- **Purpose**: Groups are containers that hold other nodes (models, objects, or even other groups) and are useful for organizing elements in a scene. Operations applied to a group (such as transformations) will affect all its children.
- **Script Functions**:
    - Use getChildren() to access the child nodes of a group.
    - **Example**:
      

```python
      if node.getKind() == NODE_TYPE_GROUP:
          children = node.getChildren()
          for child in children:
              traverse_scene_tree(child)
```



<a name="models"></a>

#### **3. Models**
- **Node Type Constant**: NODE_TYPE_MODEL
- **Purpose**: A model represents a complete 3D object that has been imported into the scene. It can contain multiple parts or objects.
- **Script Functions**:
    - Models are treated as a single entity but can be split into individual parts.
    - You can apply materials or transformations to models, or manipulate their parts individually.
    - **Example**:
      

```python
      if node.getKind() == NODE_TYPE_MODEL:
          applyTransform(model_node, transform_matrix)
```



<a name="parts"></a>

#### **4. Parts**
- **Node Type Constant**: NODE_TYPE_OBJECT
- **Purpose**: Parts are components of a model and represent individual 3D elements within the model (e.g., a wheel or a door in a car model).
- **Script Functions**:
    - Parts can inherit transformations from their parent model or have transformations applied directly.
    - **Example**:
      

```python
      if node.getKind() == NODE_TYPE_OBJECT:
          part_node.applyTransform(matrix)
```



<a name="objects"></a>

#### **5. Objects**
- **Node Type Constant**: NODE_TYPE_OBJECT
- **Purpose**: Objects represent the most granular elements of a scene, often corresponding to individual meshes or surfaces. They do not have children.
- **Script Functions**:
    - Objects support absolute transformations, allowing for precise placement in the scene.
    - **Example**:
      

```python
      obj.applyTransform(matrix, absolute=True)
```



<a name="children"></a>

#### **6. Children**
- **Definition**: Children refer to any node that is a descendant of a group or model node.
- **Script Functions**:
    - Recursively traverse and apply operations to child nodes.
    - **Example**:
      

```python
      for child in node.getChildren():
          traverse_scene_tree(child)
```



<a name="constraints-on-transformations-and-operations"></a>

### **7. Constraints on Transformations and Operations**
- **Absolute Transformations**: Only applicable to object nodes. Groups and models do not support absolute transformations.
- **Relative Transformations**: Both groups and models can support relative transformations (position, rotation, scale), but these transformations are relative to their current position.

<a name="material-applications"></a>

### **8. Material Applications**
- Materials can be applied to any node level (group, model, part, or object). Applying a material to a group or model will cascade to all its children unless explicitly overridden for a part or object.

<a name="best-practices"></a>

### **9. Best Practices**
- **Recursive Functions**: Use recursive functions to handle operations on groups and their children efficiently.
- **Type Checking**: Always check the node type before performing operations like transformations or material applications.

## Conclusion

In summary, node type constants help organize and categorize nodes in a scene, allowing your script to perform relevant operations based on the type of each node. These constants ensure that the correct logic is applied to each part of the scene tree, whether it’s a group, model set, individual model, or part.

Understanding how these constants guide the script’s behavior can allow you to build more complex scene traversal and material manipulation operations in KeyShot. By recognizing node types, you ensure that your script interacts with the correct data, preventing errors and maximizing efficiency. 