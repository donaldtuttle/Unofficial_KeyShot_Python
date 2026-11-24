# Debugging in KeyShot

<a name="11-keyshot-debugging-environment-limitations"></a>

## 1. KeyShot Debugging Environment Limitations

<a name="111-no-native-interactive-debugger"></a>

No Native Interactive Debugger: KeyShot's scripting environment lacks a native debugger comparable to full-fledged IDEs (like PyCharm or Visual Studio). This means that traditional debugging features such as setting breakpoints, stepping through code, inspecting live variables, and modifying values during execution are not available directly in the KeyShot environment.

<a name="112-script-running-context"></a>

Script Running Context: Scripts in KeyShot are typically executed in an environment without terminal access or direct interaction, which restricts the ability to use interactive debugging tools like pdb effectively.

<a name="12-practical-alternatives-for-debugging-in-keyshot"></a>

## 2. Practical Alternatives for Debugging in KeyShot
Given these constraints, your outlined practical alternatives are highly effective for achieving a similar level of debugging within the KeyShot Python API:

<a name="121-logging"></a>

### A. Logging:
Logging is essential for tracing script execution, inspecting variable values, and understanding the flow of operations.

The Python logging module can be configured to write debug messages to both the console and a file:

```python
import logging

logging.basicConfig(level=logging.DEBUG, filename="keyshot_debug.log", filemode="w", format='%(asctime)s - %(message)s')
logging.debug("Debugging message with variable value: %s", my_variable)
```

Benefit: This approach allows you to capture a detailed log of actions taken by the script, any variables of interest, and helps pinpoint where something went wrong. The timestamps included in logs help analyze the exact sequence of operations.

<a name="122-conditional-logging-as-breakpoints"></a>

### B. Conditional Logging as Breakpoints:
Using conditional statements to simulate breakpoints allows the script to pause at critical stages based on specific conditions:

```python
if some_condition:
    logging.debug("Condition met, breaking with value: %s", my_variable)
    input("Press Enter to continue...")
```

Benefit: This allows for manual inspection of the program's state at specific points without completely stopping the script's flow. It is similar to using watchpoints or breakpoints where you need the script to pause when a condition is met.

<a name="123-step-by-step-execution-with-user-input"></a>

### C. Step-by-Step Execution with User Input:
The input() function can be used to create a manual stepping mechanism:

```python
for i in range(10):
    print(f"Step {i}")
    input("Press Enter to continue to the next step...")
```

Benefit: This simulates stepping through the code line by line or loop by loop, giving you control over the execution sequence and enabling you to observe the effect of each operation interactively.

<a name="13-implementation-example-for-debugging"></a>

## 3. Implementation Example for Debugging
The provided implementation examples show how to effectively use logging and manual checks for debugging in KeyShot. Here are some highlights:

<a name="131-logging-scene-information"></a>

### Logging Scene Information:

```python
def debug_scene_objects():
    scene = lux.getSceneTree()
    if scene is None:
        logging.error("Failed to retrieve scene tree.")
        return
    
    # Log details about each node in the scene
    for node in scene.getChildren():
        logging.debug(f"Node: {node.getName()}, Type: {node.getKind()}")
```

This logs each node's name and type in the scene, which helps in verifying that all parts of the scene are being accessed correctly.

<a name="132-transforming-nodes-with-logging"></a>

### Transforming Nodes with Logging:

```python
def transform_node(node_name):
    node = lux.findNode(node_name)
    if node is None:
        logging.error(f"Node '{node_name}' not found.")
        return
    
    logging.info(f"Transforming node: {node_name}")
    try:
        matrix = luxmath.Matrix().makeIdentity().rotate((0, 1, 0), 90)
        node.setTransformation(matrix)
        logging.debug(f"Applied transformation matrix: {matrix}")
    except Exception as e:
        logging.error(f"Error applying transformation: {e}")
```

This function attempts to find and transform a specific node, logging success or failure. This is useful for debugging transformations applied to models.

<a name="14-challenges-with-real-breakpoints"></a>

## 4. Challenges with Real Breakpoints

<a name="141-no-interactive-debugger"></a>

No Interactive Debugger: Due to the non-interactive nature of KeyShot's scripting console, traditional debuggers like pdb aren’t practical for debugging KeyShot scripts.

<a name="142-manual-inspection-with-logging-and-print-statements"></a>

Manual Inspection with Logging and Print Statements: Instead, manual inspection can be achieved with logging.debug(), print(), or conditional breaks. This allows the developer to examine script flow through logs.

<a name="15-using-python-tools-for-external-debugging"></a>

## 5. Using Python Tools for External Debugging

<a name="151-pdb-debugger"></a>

Pdb Debugger: In a regular Python environment, pdb could be used for stepping through the code interactively:

```python
import pdb
pdb.set_trace()  # Set a breakpoint
```

Limitation: This is only useful if the script can be run in an interactive terminal, which isn’t feasible directly inside KeyShot due to its isolated scripting environment.

<a name="16-summary-for-debugging-documentation"></a>

## Summary for Debugging Documentation:

<a name="161-no-native-debugger-in-keyshot"></a>

### No Native Debugger in KeyShot:
Traditional debugging methods like setting breakpoints or stepping through code are not supported directly in KeyShot’s scripting environment.

<a name="162-alternatives-for-effective-debugging"></a>

### Alternatives for Effective Debugging:
Logging: Use Python's logging module to record script progress, variable values, and errors to a log file. This is the primary method to understand what’s happening inside your script.
Conditional Logging (Breakpoints): Simulate breakpoints using if statements to check conditions and pause execution with input().
Step-by-Step Execution: Implement manual stepping with input() to control the flow of the script interactively.

<a name="163-implementation-guidance"></a>

### Implementation Guidance:
Utilize logging to trace nodes and materials in a KeyShot scene.
Use detailed logs to track transformations, verify material assignments, and ensure that the scene structure is being traversed correctly.

<a name="164-challenges-and-limitations"></a>

### Challenges and Limitations:
Since KeyShot lacks a live script runtime, interactive tools like pdb are impractical for direct use.
Manual inspection through logging is currently the best method for debugging and ensuring correctness.

<a name="17-best-practices-for-debugging-keyshot-scripts"></a>

## Best Practices for Debugging KeyShot Scripts:

<a name="171-use-logging-extensively-to-trace-script-execution"></a>

### Use Logging Extensively to Trace Script Execution:

Why: Logging helps in tracking the flow of execution and provides valuable information on the state of variables, nodes, and the scene at various points in time.
How: The Python logging module can be used to log messages to both the console and a log file, allowing for post-execution analysis.
Example:

```python
import logging
logging.basicConfig(level=logging.DEBUG, filename="keyshot_debug.log", filemode="w", format='%(asctime)s - %(message)s')
logging.debug("Node details: %s", node.getName())
```

Best Practice Guidance:
Always use detailed log messages that include the context of what’s happening, such as the node name or the operation being performed.
Log both successes and errors to ensure complete visibility into the script’s behavior.

<a name="172-simulate-breakpoints-with-conditional-logging"></a>

### Simulate Breakpoints with Conditional Logging:

Why: Since KeyShot does not support interactive debugging, conditional logging provides a way to create breakpoints that can help pause execution when certain conditions are met, allowing you to observe the state.
How: Use an if statement to add a conditional check and use logging.debug() or print() to log the current state.
Example:

```python
if some_condition:
    logging.debug("Condition met at iteration %d with value: %s", i, my_variable)
    input("Press Enter to continue...")
```

Best Practice Guidance:
Use conditional checks at critical points in the code where errors or unexpected behavior are most likely.
Provide meaningful messages that indicate why the breakpoint was triggered.

<a name="173-manual-stepping-using-input-for-line-by-line-execution"></a>

### Manual Stepping Using Input for Line-by-Line Execution:

Why: For complex scripts, being able to execute code line by line helps to observe the effect of each operation before proceeding to the next, akin to a manual debug step.
How: Incorporate input() at critical points where you need to observe the impact before moving forward.
Example:

```python
for i in range(5):
    logging.debug("Loop iteration: %d", i)
    input("Press Enter to continue to the next step...")
```

Best Practice Guidance:
Use manual stepping sparingly for long loops or complex logic that’s difficult to follow in logs.
Make sure this approach is only used during active debugging sessions and remove input() statements in production scripts to avoid halting the script unintentionally.

<a name="174-create-debug-functions-for-scene-and-material-inspection"></a>

### Create Debug Functions for Scene and Material Inspection:

Why: Centralized debug functions make it easy to reuse debugging logic throughout the script. They help maintain consistency in how scene details are logged.
How: Implement functions like debug_scene_objects() or log_material_info() to inspect and log scene properties or material attributes.
Example:

```python
def debug_scene_objects():
    scene = lux.getSceneTree()
    if scene is None:
        logging.error("Failed to retrieve scene tree.")
    for node in scene.getChildren():
        logging.debug(f"Node: {node.getName()}, Type: {node.getKind()}")
```

Best Practice Guidance:
Abstract debugging logic into separate functions to keep the main script clean and modular.
### Consistently use these functions whenever you need to debug different parts of the script.

<a name="175-centralize-logging-configuration"></a>

Centralize Logging Configuration:

Why: Configuring logging in a centralized manner ensures that all logs are formatted consistently and that any changes to the log output (e.g., adding a file handler) only need to be made in one place.
How: Set up logging in the script initialization:

```python
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', handlers=[
    logging.FileHandler("keyshot_debug.log"),
    logging.StreamHandler()
])
```

Best Practice Guidance:
Configure different logging levels (DEBUG, INFO, ERROR) to categorize log messages, making it easier to filter and find relevant information.
Use different handlers (console and file) to ensure logs are visible during execution and available for later analysis.

<a name="176-document-logging-intent-in-your-script"></a>

### Document Logging Intent in Your Script:

Why: Developers working on the script later will need to understand why certain logs are placed where they are.
How: Include comments explaining the purpose of key logging statements, especially conditional logs and manual stepping points.
Example:

```python
# Log the start of node transformation to debug whether transformations are applied correctly
logging.info(f"Starting transformation on node: {node.getName()}")
```

<a name="177-error-handling-and-logging-exceptions"></a>

### Error Handling and Logging Exceptions:

Why: Catching and logging exceptions helps you understand where and why the script failed.
How: Use try...except blocks to catch exceptions and log the errors:

```python
try:
    matrix = luxmath.Matrix().makeIdentity().rotate((0, 1, 0), 90)
    node.setTransformation(matrix)
except Exception as e:
    logging.error(f"Error applying transformation to {node.getName()}: {e}")
```



Here's how the formatting is effective and how users can leverage it for debugging purposes:

### Log Formatting:
#### Timestamp (2024-10-04 12:19:49,671):

Every log entry is preceded by a timestamp. This helps track when each operation occurred, which is valuable for performance analysis and understanding the sequence of operations.
#### Node Information (Node: lux_root (Type: Group)):

Logs about nodes provide the name of the node, its type, and hierarchical relationships (through indentation).
This information allows users to understand how nodes are organized in the scene.
#### Material Information (Material: Cube Material MM):

Materials assigned to nodes are logged. This helps verify that nodes have the correct materials.
If materials are missing from nodes where they’re expected, this could point to an issue in how materials were assigned.
#### Indentation for Hierarchy:

The indentation clearly represents the scene hierarchy. This makes it easy to visualize which nodes are parents and which are children, providing insights into how materials or transformations propagate through the scene.
### How Users Utilize This Log for Debugging:
#### Verify Scene Hierarchy:

Users can use the logs to verify the scene structure. The log shows the root (lux_root) and then traverses through groups, models, and parts.
By following the indentation, users can see how each node fits into the overall hierarchy, which is crucial when trying to understand how transformations and materials affect different parts of the scene.
#### Check Material Assignments:

Material logging helps users ensure that all nodes that require materials have them assigned.
In the logs provided, the materials like Cube Material MM, Cube Material Red MM, and Cube Material Gradient are shown at the correct levels.
If a node unexpectedly has no material assigned (e.g., No material assigned to 'Cube #2'), users can identify and correct potential issues with material assignment scripts or ensure the material is applied properly in KeyShot.
#### Debugging Transformations and Errors:

The logs also show errors and transformations applied to nodes, such as:

```text
2024-10-04 12:04:23,182 - Transforming node: Cube #1
2024-10-04 12:04:23,237 - Applied translation of 10 units to node: Cube #1
```

Errors like 'lux.SceneNode' object has no attribute 'setTransformation' indicate a missing or incorrect function, which is useful for developers to fix scripting issues.
Users can use these logs to confirm that transformations are applied correctly and that API functions are being called with the correct attributes.
#### Diagnose Missing Elements:

If a part of the scene doesn’t appear in the rendered output, users can refer to the logs to see if it’s correctly defined and assigned in the hierarchy.
For example, if a node (Cube) does not have a material when it should, it’s straightforward to trace the logs and identify exactly where and why a material was not applied.
#### Material Graphs and Multi-Materials:

The logs also track multi-materials and their sub-materials. This is valuable for ensuring that all elements of a complex material setup are correctly assigned:

```text
2024-10-04 12:18:12,455 -   Material: Cube Material MM
2024-10-04 12:18:12,455 -   Cube Material MM is a multi-material. Listing sub-materials:
2024-10-04 12:18:12,455 -     Sub-material: Cube Material
```

Understanding the entire material graph helps troubleshoot issues where, for example, the wrong material version or a missing sub-material might be causing visual discrepancies.
### How To Improve and Optimize Usage of These Logs:
#### Filter by Log Level:

Not all log entries are equally critical. You could implement log levels like INFO, DEBUG, ERROR, and WARNING to allow filtering:
INFO for basic node traversal.
DEBUG for detailed material and parameter logging.
ERROR for any script failures, such as missing attributes or functions.
#### Automated Issue Detection:

You could create additional scripts to analyze these logs post-run. For instance, a script could search for "No material assigned" entries and compile a report on which nodes require attention.
#### Consistent Formatting for Searchability:

Having consistent prefixes for different log types (e.g., Node Info:, Material Info:, Error:) allows users to quickly search through large log files for specific issues.

<a name="18-example-scenarios-for-using-logs-in-debugging"></a>

## Example Scenarios for Using Logs in Debugging:

<a name="181-incorrect-material-assignment"></a>

### Incorrect Material Assignment:

If a material is missing or incorrectly assigned, users can identify the exact node and correct the issue directly in KeyShot or by updating the script logic.

<a name="182-hierarchy-mismatch"></a>

### Hierarchy Mismatch:

When expected parts are not rendered correctly, users can verify if the node is even present in the hierarchy. If the log shows missing nodes, it might indicate a problem during import or setup in KeyShot.

<a name="183-api-function-errors"></a>

### API Function Errors:

By observing logs like AttributeError: 'lux.SceneNode' object has no attribute 'setTransformation', users can identify unsupported or deprecated API calls and adjust their scripts accordingly.

## Conclusion:
### Effectiveness of the Log Format:
The provided log format is practical and well-suited for debugging in KeyShot. It combines timestamped, hierarchical node information with detailed material logging, making it easy to navigate through the scene and identify any issues.
### How Users Use These Logs:
Users leverage these logs to verify the scene structure, material assignments, transformations, and quickly spot API-related errors.
The structured log helps in maintaining a comprehensive overview of both nodes and materials, ensuring all configurations are correct and identifying potential problem areas.


### Best Practice Guidance:
Log all caught exceptions with as much detail as possible, including variable states and context around the failure.

<a name="19-conclusion-for-debugging-best-practices-in-keyshot"></a>

## Conclusion for Debugging Best Practices in KeyShot:
Logging and Conditionals: Since KeyShot doesn’t support traditional debugging, extensive logging is the best practice to understand and debug script behavior. This includes conditional logging for creating pseudo-breakpoints.
Manual Stepping: Implementing manual steps with input() is a powerful method for interactive debugging. It simulates stepping through code, which is especially helpful in complex logic.
Centralized Debug Functions: Abstract common debugging tasks into reusable functions. This maintains consistency and modularity in how you handle debugging across scripts.
Error Handling: Use exception logging to ensure all script failures are well-documented, helping trace errors to their root cause quickly.

