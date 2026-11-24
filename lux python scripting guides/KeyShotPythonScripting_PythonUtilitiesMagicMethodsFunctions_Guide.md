# KeyShot Python Scripting Utilities & Functions

## Table of Contents

1. [Introduction to Utilities and Modules](#introduction-to-utilities-and-modules)
   - [1.1 What is a Module?](#11-what-is-a-module)
   - [1.2 What is a Utility?](#12-what-is-a-utility)
   - [1.3 Difference Between Utilities and Modules](#13-difference-between-utilities-and-modules)

2. [Utility vs. Module in KeyShot Context](#utility-vs-module-in-keyshot-context)
   - [2.1 KeyShot Module Analogy](#21-keyshot-module-analogy)
   - [2.2 KeyShot Utility Analogy](#22-keyshot-utility-analogy)

3. [Examples of Utility Modules](#examples-of-utility-modules)
   - [3.1 Example of a Utility Module for Logging](#31-example-of-a-utility-module-for-logging)
   - [3.2 Example of a Utility Module for Calculations](#32-example-of-a-utility-module-for-calculations)

4. [Using Utility Modules in KeyShot Scripts](#using-utility-modules-in-keyshot-scripts)
   - [4.1 Importing and Using Utility Modules](#41-importing-and-using-utility-modules)
   - [4.2 Visual Example of Using Utility Modules in KeyShot Scripts](#42-visual-example-of-using-utility-modules-in-keyshot-scripts)

5. [Difference Between Utilities and Modules](#difference-between-utilities-and-modules)
   - [5.1 Key Features of a Module](#51-key-features-of-a-module)
   - [5.2 Key Features of a Utility](#52-key-features-of-a-utility)
   - [5.3 Comparison: Module vs Utility](#53-comparison-module-vs-utility)

6. [Real-World Analogy for Modules and Utilities](#real-world-analogy-for-modules-and-utilities)
   - [6.1 Modules as Hardware Store Sections](#61-modules-as-hardware-store-sections)
   - [6.2 Utilities as Toolbox Essentials](#62-utilities-as-toolbox-essentials)

7. [Practical Examples of Utility and Modules in Common Python Libraries](#practical-examples-of-utility-and-modules-in-common-python-libraries)
   - [7.1 Utility Modules in Python’s Standard Library](#71-utility-modules-in-pythons-standard-library)
   - [7.2 Module vs Utility in Python’s Standard Library](#72-module-vs-utility-in-pythons-standard-library)

8. [Utility Modules in KeyShot Scripting](#utility-modules-in-keyshot-scripting)
   - [8.1 Benefits of Using Utility Modules in KeyShot](#81-benefits-of-using-utility-modules-in-keyshot)
   - [8.2 Using log_utils.py for Consistent Logging](#82-using-log_utilspy-for-consistent-logging)

9. [Magic Methods in Python](#magic-methods-in-python)
   - [9.1 Understanding __magic_methods__ in Python](#91-understanding-magic-methods-in-python)
   - [9.2 The __file__ Magic Method and Its Role](#92-the-file-magic-method-and-its-role)

10. [Functions in Python](#functions-in-python)
    - [10.1 What is a Function?](#101-what-is-a-function)
    - [10.2 Visual Representation of Functions in Python](#102-visual-representation-of-functions-in-python)

11. [How Utility Modules Enhance KeyShot Scripting](#how-utility-modules-enhance-keyshot-scripting)
    - [11.1 Logging in KeyShot Scripts](#111-logging-in-keyshot-scripts)
    - [11.2 Using Utility Functions for Calculations](#112-using-utility-functions-for-calculations)
    - [11.3 Automating Repetitive Tasks](#113-automating-repetitive-tasks)

12. [Conclusion: Modules and Utilities in Python and KeyShot](#conclusion-modules-and-utilities-in-python-and-keyshot)
    - [12.1 Key Takeaways on Modules](#121-key-takeaways-on-modules)
    - [12.2 Key Takeaways on Utility Modules](#122-key-takeaways-on-utility-modules)


The difference between utilities and modules can be subtle in Python, but let’s break it down in the simplest way and relate it back to KeyShot concepts for clarity.

<a name="introduction-to-utilities-and-modules"></a>

## Understanding Utilities vs. Modules in Python

<a name="11-what-is-a-module"></a>

### 1. What is a Module?

A module is simply a Python file (.py) that contains Python code—such as functions, classes, or variables—that you can import and use in other Python scripts.

- Analogy: A module in Python is like a project file in KeyShot.
- Just as a project file in KeyShot contains all the details about a 3D scene (materials, lighting, cameras, etc.), a module contains all the details about a certain functionality in Python.
- For instance, if you save a KeyShot project as lighting_setup.bip, you can import that file into other projects to reuse the lighting settings.
- Similarly, a module is simply a .py file that contains code you might want to reuse, and you can import it into another script.

Example of a Module:

```python
# my_module.py
def greet(name):
return f"Hello, {name}!"

# Another script can import `my_module.py`:
import my_module

print(my_module.greet("KeyShot User")) # Output: Hello, KeyShot User!
```


- Here, my_module.py is a module. It contains one function (greet()), which can be reused by importing my_module in other scripts.

<a name="12-what-is-a-utility"></a>

### 2. What is a Utility?

A utility is a concept rather than a formal structure in Python. In practice, a utility is often a module that provides a collection of helper functions or tools that you can use in multiple different contexts or scripts.

- Analogy: Think of a utility as a toolset within KeyShot.
- Just like you may have a library of materials or a set of HDRIs for different types of scenes, a utility is a collection of reusable pieces of code that can be helpful in many different scenarios.
- A utility is often used to simplify repetitive tasks. For example, if you need a specific lighting setup frequently, you might save it in your library and reuse it in multiple projects—this is what a utility does for Python code.

Example of a Utility Module:

```python
# log_utils.py (A utility module)
import datetime

def log_message(message, status="INFO"):
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
return f"[{status}] {timestamp} - {message}"

# This file contains utility functions that can be reused for logging messages in different scripts.
```


- log_utils.py is a module, but it is also referred to as a utility because it provides helpful, reusable functions.
- The name utility signifies its purpose: to provide tools to help other parts of the program—just like the tools in a toolbox.

<a name="13-difference-between-utilities-and-modules"></a>

## Difference Between a Utility and a Module

- Module:
- A module is just a Python file (.py) that you can import. It can contain anything—functions, classes, variables, etc.
- Example: my_module.py is a module, whether it has one function or many classes.
- Utility:
- A utility is a type of module. It’s a module specifically designed to help other code by providing helper functions or tools. A utility module usually focuses on utility functions (like logging, error handling, calculations, etc.).
- Example: log_utils.py is both a module and a utility because it helps other code with logging functionalities.

To put it simply, all utilities are modules, but not all modules are considered utilities. The term utility implies the intent and content of the module—general-purpose, reusable functions to make coding easier.

## Utility vs. Module in KeyShot Context

<a name="21-keyshot-module-analogy"></a>

- Modules are like any saved KeyShot project that you can import for a specific purpose.
- Think of a module as a general scene file you can open—it might contain lighting, materials, cameras, etc.

<a name="22-keyshot-utility-analogy"></a>

- Utilities are more like a saved set of HDRI images or saved material templates in KeyShot.
- They provide tools that help build a scene, but aren’t a full scene by themselves.
- For example, your log_utils.py utility provides reusable functions like log_message(), which is like having a set of HDRIs to create different moods in a scene.

<a name="examples-of-utility-modules"></a>

## Examples to Demonstrate Usage

Let’s say you’re creating scripts for KeyShot, and you want to:

1. Log Messages to track what your script is doing.
2. Calculate Values like transforming units, working with matrices, etc.

Instead of writing the logging or calculation functions each time, you can create utility modules like:

- log_utils.py: Contains functions for logging actions.
- calc_utils.py: Contains functions to help with math-related operations (like converting units).

<a name="using-utility-modules-in-keyshot-scripts"></a>
<a name="42-visual-example-of-using-utility-modules-in-keyshot-scripts"></a>

## Visual Example: Using Utility Modules in a KeyShot Script

### Utility Modules:

<a name="31-example-of-a-utility-module-for-logging"></a>

- log_utils.py:

```python
# Utility for logging
import datetime

def log_message(log_file, message):
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"[INFO] {timestamp} - {message}"
with open(log_file, "a") as log:
log.write(log_entry + "\n")
print(log_entry)
```



<a name="32-example-of-a-utility-module-for-calculations"></a>

<a name="112-using-utility-functions-for-calculations"></a>

- calc_utils.py:

```python
# Utility for calculations
def convert_meters_to_millimeters(meters):
return meters * 1000

def calculate_area(width, height):
return width * height
```




<a name="41-importing-and-using-utility-modules"></a>

### Your KeyShot Script (my_keyshot_script.py):

```python
import lux
from log_utils import log_message
from calc_utils import convert_meters_to_millimeters, calculate_area

# Set up log file
LOG_FILE = "my_keyshot_script_log.txt"

# Example usage of logging
log_message(LOG_FILE, "Starting KeyShot material operation...")

# Example calculation using a utility function
width_m = 2.0 # Width in meters
height_m = 3.0 # Height in meters

# Convert dimensions and calculate area
width_mm = convert_meters_to_millimeters(width_m)
height_mm = convert_meters_to_millimeters(height_m)
area_mm2 = calculate_area(width_mm, height_mm)

log_message(LOG_FILE, f"Width in mm: {width_mm}, Height in mm: {height_mm}, Area in mm^2: {area_mm2}")

try:
# Example KeyShot operation (replace with real KeyShot code)
log_message(LOG_FILE, "Material operation completed successfully.")
except Exception as e:
log_message(LOG_FILE, f"Error during material operation: {e}")
```


### Visual Representation of Workflow:

1. Your Toolbox (log_utils.py and calc_utils.py):
- You have two utility modules.
- One helps with logging (log_utils), like keeping a detailed record of what happens.
- The other helps with mathematics (calc_utils), like converting units.
2. Using the Tools in Your Project (my_keyshot_script.py):
- You import the utility modules just like opening a toolbox.
- You use the tools (functions) from the utilities to perform specific tasks, like logging and converting units.
3. Result:
- Your KeyShot script (my_keyshot_script.py) now has more power and less redundancy because instead of rewriting the logging and math operations in every script, you can simply import and use them.

## Summary: Utilities vs. Modules

- Module:
- A .py file containing Python code.
- It can be anything—functions, classes, or a combination.
- Utility Module:
- A special kind of module containing helper functions to assist other scripts.
- Provides reusable tools like logging, error handling, or calculations.

In Python:

- Think of modules as any container of code.
- Think of utilities as specific helpers that make your code easier to write, reuse, and understand—much like having a set of standard lighting presets or materials in KeyShot that you use in multiple projects for consistency and ease.

The terms “utilities” and “modules” are often used interchangeably, but there are some subtle differences in what they imply. Let me explain in a way that connects back to how you think about KeyShot and workflows.

### 1. What is a Module?

In Python, a module is simply a file containing Python code. This code can be functions, classes, variables, or even runnable code. A module is a basic building block in Python, designed to organize related code together.

- Visual Example in KeyShot Terms: Imagine a material package. It contains a set of related materials (e.g., all materials related to metals, like steel, aluminum, etc.). A Python module is like that package—it contains related tools (functions, classes, etc.) that work well together.

<a name="51-key-features-of-a-module"></a>

#### Key Characteristics of a Module:

- A module is any Python file ending in .py.
- It can be imported into another Python script using import.
- It can contain any type of Python code: functions, classes, and even code that runs automatically.

Example:

- Suppose you have a Python file named math_operations.py:

```python
# math_operations.py
def add(a, b):
return a + b

def subtract(a, b):
return a - b
```


- This is a module that contains two functions (add() and subtract()).
- You can import this module into another script like this:

```python
import math_operations

result = math_operations.add(5, 3)
print(result) # Output: 8
```




### 2. What is a Utility?

A utility is a type of module that specifically focuses on providing helpful functions or tools that can be reused across many different parts of a project. The term “utility” implies that the module has a specific purpose: to make common tasks easier.

- Visual Example in KeyShot Terms: Imagine a preset library for lighting. You use it over and over again to set up your scenes because it makes things quicker. A Python utility is like that—it provides commonly needed functions (like logging, file operations, etc.) that you use repeatedly to make scripting easier.

<a name="52-key-features-of-a-utility"></a>

#### Key Characteristics of a Utility Module:

- It is a module, but one that is typically filled with reusable, helper functions.
- These functions are usually generic enough that they can be used across different projects or parts of a project.
- Utility modules are meant to save time and effort by reducing redundancy.

Example:

- Consider the log_utils.py file from earlier. This file contains utility functions like log_message(), which can be used across many different scripts to log messages consistently.

Visual Example in Python Terms:

- Imagine you are creating multiple Python scripts that interact with KeyShot:
- Each script may need to log messages, handle errors, or create directories.
- Instead of writing these functions in every script, you put them in a utility module (log_utils.py).
- Now you can import and use these helpful functions whenever needed.

## Difference Between Utilities and Modules

<a name="53-comparison-module-vs-utility"></a>

```text
Feature Module Utility (Utility Module)
Definition Any Python file (.py) that contains code. A type of module with reusable helper functions.
Purpose Organize related Python code, functions, or classes. Provide general-purpose helper functions for repeated use.
Usage Could be anything: a module might define a full system, like how a camera works in KeyShot. Focused on making common tasks easier, like logging, calculating, etc.
Example Content Classes, complex functions, runnable scripts. Logging functions, configuration handlers, small utilities.
Analogy in KeyShot A collection of materials (metals) for a project. A set of lighting presets you use in all your scenes.
```


<a name="real-world-analogy-for-modules-and-utilities"></a>

## 3. Real-World Example

To clarify further, let’s consider a real-world analogy:

<a name="61-modules-as-hardware-store-sections"></a>

- Modules are like different sections in a hardware store:
- You have a section for electrical supplies, a section for plumbing, etc. Each section contains many items that relate to the same purpose.
- A Python module is like one of these sections—it’s a group of code that relates to a specific purpose.

<a name="62-utilities-as-toolbox-essentials"></a>

- Utilities are like the set of most commonly used tools that you always keep in your toolbox:
- Screwdrivers, a measuring tape, pliers, etc. These are tools that you use all the time no matter what kind of work you’re doing.
- A Python utility module is like that toolbox—it contains helper functions that you use frequently, like logging errors or formatting text.

<a name="practical-examples-of-utility-and-modules-in-common-python-libraries"></a>

## Examples from Common Python Libraries

<a name="71-utility-modules-in-pythons-standard-library"></a>

- Utility Modules in Real Life:
- The Python standard library has a module called os for interacting with the operating system, but it also has os.path which is more of a utility for common file path operations like joining paths (os.path.join()) or checking if a file exists (os.path.exists()).

<a name="72-module-vs-utility-in-pythons-standard-library"></a>

- Module vs Utility:
- os module: This handles everything related to interacting with the operating system, from running commands to handling environment variables. It’s a full module.
- os.path utility: This is a specific part of os that focuses only on file path operations, and it helps perform common actions you need often, such as determining if a directory exists.

<a name="utility-modules-in-keyshot-scripting"></a>

## Summary and Why It Matters to You

- A module in Python is just a file that contains Python code—it can contain functions, classes, and even code that executes when the module is imported.
- A utility is a type of module specifically intended to contain helper functions that make common tasks easier. It is essentially a “helper toolkit”.

<a name="81-benefits-of-using-utility-modules-in-keyshot"></a>

For your KeyShot workflow:

- Utility modules (like log_utils.py) help you avoid repetition. Instead of writing logging functions in every script, you import the utility, much like adding a KeyShot library material to different scenes.
- By creating a utility module, you make your code easier to manage and reuse—saving time and reducing the chance for errors.

<a name="113-automating-repetitive-tasks"></a>

## Visual Python Workflow in KeyShot Context

1. Utility Creation:
- Imagine creating a perfect lighting setup in one KeyShot scene. You save it so you can use it again.
- Similarly, you create a utility module (log_utils.py) to store your helper functions.
2. Reusing Utilities:
- In a new scene, instead of setting up the lights from scratch, you import the saved lighting setup.
- In a new Python script, instead of writing the logging code again, you import log_utils.py and call the functions you need.

<a name="conclusion-modules-and-utilities-in-python-and-keyshot"></a>

## Conclusion:

<a name="121-key-takeaways-on-modules"></a>

- Modules help you organize related code. They can contain any functionality you need.

<a name="122-key-takeaways-on-utility-modules"></a>

- Utilities are specialized modules focused on providing general-purpose, reusable helpers.
- Using utility modules in Python scripting for KeyShot is a powerful way to make your work more efficient, consistent, and easier to manage—similar to how reusable settings or material libraries make working in KeyShot easier and more predictable.

<a name="magic-methods-in-python"></a>

## (__magic_ method __)

Python utilities, functions, and what the (__magic_ method __) notation represents. I’ll also relate these concepts back to your experience with KeyShot so you can see how it applies in your workflow.

## Understanding Python Basics Through KeyShot Concepts

### 1. What is a Python Utility Module?

A utility module in Python is like a collection of tools. Think of it as similar to the material library in KeyShot.

- KeyShot Material Library: You have a central place where all your materials are stored, and you can reuse them in different scenes.
- Python Utility Module: It’s a file where you put common functions (small pieces of reusable code) that you can use across different scripts.

For example, you often reuse certain functions like logging messages or displaying summaries. Instead of writing the same code again in every script, you put these functions in a separate file (a utility module), and then you import them wherever needed.

Here’s a visual analogy:

- Utility Module: Imagine having a “toolbox” with many tools (screwdriver, hammer) that you use repeatedly. Instead of creating a new hammer each time, you grab the existing one from your toolbox.
- Python File (log_utils.py): This is the toolbox with all your “tools” (functions) inside it.

<a name="91-understanding-magic-methods-in-python"></a>

### 2. Visual Representation of (__magic_ method __)


In Python, anything that has double underscores (__like_this__) is called a “magic method” or special variable. They are part of Python’s internal workings, used for specific purposes, often to provide some special functionality automatically.

- Example: __file__ is a special variable that holds the path to the current script file. This allows the script to know what its own name is, so it can create a log file with that name.

<a name="92-the-file-magic-method-and-its-role"></a>

#### Think About __file__ Like This:

- Imagine in KeyShot, each scene knows its own name and where it’s saved. Similarly, __file__ lets a Python script know its own name and location.

Here’s a visual breakdown:

```python
# __file__ is like giving the script the ability to "know its own name".
LOG_FILE_NAME = __file__ # Imagine the script is writing "I am my_keyshot_script.py"
```


When you use __file__, the script essentially gets its own filename, which allows us to dynamically generate a log file name based on that.

Visual Example:

- If your script file is named my_keyshot_script.py, then __file__ will be something like "path/to/my_keyshot_script.py".
- We extract "my_keyshot_script" from this to create a log file called "my_keyshot_script_log.txt".

<a name="functions-in-python"></a>
<a name="101-what-is-a-function"></a>

### 3. What is a Function?

A function is like a reusable action. In KeyShot, think of it as a macro or workflow that you run multiple times, such as a lighting setup you use in different scenes.

<a name="102-visual-representation-of-functions-in-python"></a>

- Python Function Example:

```python
def log_message(message):
# This is the action that happens when you call log_message.
print(message)
```


- def is used to define a function.
- log_message is the name of the function.
- Inside the function, you can have any actions, like print(message).

When you call a function by using its name, you execute the actions defined in it. For instance:

- Calling the function: log_message("Hello, KeyShot!")
- What happens? It will print: Hello, KeyShot!

In terms of KeyShot:

- Setting up Lighting Manually: You add each light one by one.
- Function Approach: Imagine you have a button that sets up the lighting perfectly in one click, saving time and effort. This button is like a Python function—it performs multiple steps whenever you call it.

<a name="how-utility-modules-enhance-keyshot-scripting"></a>

### 4. How Does This Help in KeyShot Scripting?

Here’s a visual scenario to help you understand the utility of using functions and logging in KeyShot scripts:

<a name="111-logging-in-keyshot-scripts"></a>

#### Scenario: Debugging a Material Duplication in KeyShot

1. Goal: You want to duplicate a material, but you also want to track what happens step-by-step to ensure everything works as expected.
2. Logging the Steps:
- You create a function called log_message() that writes down each step into a log file.
- This is like keeping a notebook next to you while you’re adjusting materials in KeyShot to record what you’ve done.
3. Putting log_message() in a Utility:
- Instead of writing this logging code in every script, you put it in a file called log_utils.py. This file is your “utility module”.
- Whenever you need to log steps in another script, you just import log_utils.
4. Result:
- When you run your material duplication script (my_keyshot_script.py), it automatically creates a log file with a name based on the script name.
- After the script completes, the log contains all the steps and details, such as “Material duplicated successfully” or “Error: Material not found”.

#### Code Example in Context:

<a name="82-using-log_utilspy-for-consistent-logging"></a>


Here’s how it looks, step-by-step:

- Step 1: Create a utility file (log_utils.py) that contains a logging function.

```python
# log_utils.py (Your Toolbox)
import os
import datetime

def get_log_file_name(script_path):
script_name = os.path.splitext(os.path.basename(script_path))[0]
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
return f"logs/{script_name}_{timestamp}_log.txt"

def log_message(log_file_name, message):
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
detailed_message = f"[INFO] {timestamp} - {message}"
os.makedirs(os.path.dirname(log_file_name), exist_ok=True)
with open(log_file_name, "a") as log_file:
log_file.write(detailed_message + "\n")
print(detailed_message)

```


- Step 2: Create your script (my_keyshot_script.py) that uses this logging utility.

```python
# my_keyshot_script.py (Where You Work)
import lux
from log_utils import get_log_file_name, log_message

# Automatically generate the log file name based on script name
LOG_FILE_NAME = get_log_file_name(__file__)

# Example usage in the script
log_message(LOG_FILE_NAME, "Starting material duplication...")

try:
# Simulated operation (replace with actual KeyShot code)
log_message(LOG_FILE_NAME, "Material duplicated successfully.")
except Exception as e:
log_message(LOG_FILE_NAME, f"Error during material duplication: {str(e)}")


```


#### What Happens Visually:

1. Run the Script (my_keyshot_script.py):
- The script starts and generates a log file called "logs/my_keyshot_script_20231005_141500_log.txt".
- As the script runs, it records messages into the log file like:

```text
[INFO] 2023-10-05 14:15:00 - Starting material duplication...
[INFO] 2023-10-05 14:15:05 - Material duplicated successfully.
```



2. Result:
- At the end of the script, you have a complete log of every major step. This helps you debug and understand exactly what happened during the execution, just like referring back to a notebook after setting up a scene in KeyShot.

## Summary

- Utility Module (log_utils.py): This is your toolbox. It contains reusable functions like log_message().
- Functions: These are like reusable actions or macros. In our case, log_message() logs details into a file.
- __file__: A magic variable that represents the script file’s own name. This helps us create log files with unique names automatically.
- Visual Workflow:
- You import your tools from the toolbox (log_utils.py).
- Run your script.
- Logs are created based on the script name, and they contain all relevant information for debugging.