# Scripting Examples: Import, Export, and Information

[Scripting Examples TOC](../Scripting_Examples.md)

## Batch Import CAD Model Assign Material Template Name Model Set.py
<a name="importexport-batch-import-cad-model-assign-material-template-name-model-set"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.1
# HEADLESS COMPLIANT
# Batch Import CAD Model, Name Model Set pr CAD, and assign material template.
``` python
import os, re, sys
import os.path

def genericInput(msg, default=None, check=lambda x: len(x) > 0):
    if default is not None:
        msg += " [{}] ".format(default)
    if not msg.endswith(" "):
        msg += " "
    while True:
        try:
            value = input(msg)
            if check(value):
                return value
            elif len(value) == 0 and default is not None:
                return default
        except EOFError:
            sys.stdout.write("\n")
            continue
        except KeyboardInterrupt:
            sys.exit()

def inputFolder(msg):
    return genericInput(msg, check=lambda x: os.path.isdir(x))

def inputText(msg, default):
    return genericInput(msg, default=default)

def intInRange(value, valueRange=None):
    try:
        n = int(value)
        if valueRange is not None:
            return n >= valueRange[0] and n <= valueRange[1]
        else:
            return True
    except ValueError:
        return False

def inputInt(msg, default, valueRange=None):
    return int(genericInput(msg, default=default, check=lambda x: intInRange(x, valueRange)))

def inputItem(msg, defaultIndex, items):
    pre = ""
    for i in range(len(items)):
        pre += "[{}] {}\n".format(i + 1, items[i])
    idx = inputInt(pre + msg, defaultIndex + 1, (1, len(items))) - 1
    return (idx, items[idx])

def inputBool(msg, default=False):
    return str(genericInput(msg, default=default)).lower() in ["y", "yes", "true", "1"]

def cleanExt(ext):
    while ext.startswith("."):
        ext = ext[1:]
    return ext.lower()

def main():
    tmpls = ["-- None --"] + lux.getMaterialTemplates()
    info = lux.getSceneInfo()
    opts = {}
    if not lux.isHeadless():
        values = [("folder", lux.DIALOG_FOLDER, "Folder to import from:", None),
                  ("iext", lux.DIALOG_TEXT, "Input file format to read:", "bip"),
                  (lux.DIALOG_LABEL, "--"),
                  ("template", lux.DIALOG_ITEM, "Apply material template on each import (optional):", tmpls[0], tmpls)]
        desc = "Batch import models and assign a selected material template if specified."
        opts = lux.getInputDialog(title = "Batch Import and Assign Material Template",
                                  desc = desc,
                                  values = values,
                                  id = "batchimport_assignmaterial.py.luxion")
    else:
        opts["folder"] = inputFolder("Folder to import from:")
        opts["iext"] = inputText("Input file format to read:", "bip")
        opts["template"] = inputItem("Apply material template on each import (optional):", 0, tmpls)[1]
    if not opts: return

    fld = opts["folder"]
    iext = cleanExt(opts["iext"])
    reFiles = re.compile(".*\." + iext + "$", re.IGNORECASE)

    if not any(reFiles.match(f) for f in os.listdir(fld)):
        raise Exception("Could not find any input files matching the extension '{}'' in '{}'!".format(iext, fld))

    for f in [f for f in os.listdir(fld) if f.lower().endswith(iext)]:
        path = fld + os.path.sep + f

        print("Importing {}".format(path))
        lux.importFile(path)

        if opts["template"][0] != 0:  # Check if a template is selected other than "-- None --"
            template = tmpls[opts["template"][0]]
            print("Setting material template {}".format(template))
            lux.setMaterialTemplate(template)

    # Renaming model sets based on the first child.
    root_node = lux.getSceneTree()
    for model_set in root_node.getChildren():
        if model_set.isModelSet():
            children = model_set.getChildren()
            if children:
                # Assuming the first child's name is the desired new name for the model set.
                new_name = children[0].getName()
                model_set.setName(new_name)
                print(f"Model set renamed to: {new_name}")

main()
```

# End of ImportExport\Batch Import CAD Model Assign Material Template Name Model Set.py

## Batch Import CAD Model Assign Material Template.py
<a name="importexport-batch-import-cad-model-assign-material-template"></a>
# -*- coding: utf-8 -*-
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# HEADLESS COMPLIANT
# Batch Import and assign material template.
``` python
import os, re, sys
import os.path

def genericInput(msg, default=None, check=lambda x: len(x) > 0):
    if default is not None:
        msg += " [{}] ".format(default)
    if not msg.endswith(" "):
        msg += " "
    while True:
        try:
            value = input(msg)
            if check(value):
                return value
            elif len(value) == 0 and default is not None:
                return default
        except EOFError:
            sys.stdout.write("\n")
            continue
        except KeyboardInterrupt:
            sys.exit()

def inputFolder(msg):
    return genericInput(msg, check=lambda x: os.path.isdir(x))

def inputText(msg, default):
    return genericInput(msg, default=default)

def intInRange(value, valueRange=None):
    try:
        n = int(value)
        if valueRange is not None:
            return n >= valueRange[0] and n <= valueRange[1]
        else:
            return True
    except ValueError:
        return False

def inputInt(msg, default, valueRange=None):
    return int(genericInput(msg, default=default, check=lambda x: intInRange(x, valueRange)))

def inputItem(msg, defaultIndex, items):
    pre = ""
    for i in range(len(items)):
        pre += "[{}] {}\n".format(i + 1, items[i])
    idx = inputInt(pre + msg, defaultIndex + 1, (1, len(items))) - 1
    return (idx, items[idx])

def inputBool(msg, default=False):
    return str(genericInput(msg, default=default)).lower() in ["y", "yes", "true", "1"]

def cleanExt(ext):
    while ext.startswith("."):
        ext = ext[1:]
    return ext.lower()

def main():
    tmpls = ["-- None --"] + lux.getMaterialTemplates()
    info = lux.getSceneInfo()
    opts = {}
    if not lux.isHeadless():
        values = [("folder", lux.DIALOG_FOLDER, "Folder to import from:", None),
                  ("iext", lux.DIALOG_TEXT, "Input file format to read:", "bip"),
                  (lux.DIALOG_LABEL, "--"),
                  ("template", lux.DIALOG_ITEM, "Apply material template on each import (optional):", tmpls[0], tmpls)]
        desc = "Batch import models and assign a selected material template if specified."
        opts = lux.getInputDialog(title = "Batch Import and Assign Material Template",
                                  desc = desc,
                                  values = values,
                                  id = "batchimport_assignmaterial.py.luxion")
    else:
        opts["folder"] = inputFolder("Folder to import from:")
        opts["iext"] = inputText("Input file format to read:", "bip")
        opts["template"] = inputItem("Apply material template on each import (optional):", 0, tmpls)[1]
    if not opts: return

    fld = opts["folder"]
    iext = cleanExt(opts["iext"])
    reFiles = re.compile(".*\." + iext + "$", re.IGNORECASE)

    if not any(reFiles.match(f) for f in os.listdir(fld)):
        raise Exception("Could not find any input files matching the extension '{}'' in '{}'!".format(iext, fld))

    for f in [f for f in os.listdir(fld) if f.lower().endswith(iext)]:
        path = fld + os.path.sep + f

        print("Importing {}".format(path))
        lux.importFile(path)

        if opts["template"][0] != 0:  # Check if a template is selected other than "-- None --"
            template = tmpls[opts["template"][0]]
            print("Setting material template {}".format(template))
            lux.setMaterialTemplate(template)

main()
```

# End of ImportExport\Batch Import CAD Model Assign Material Template.py

## Batch Import CAD.py
<a name="importexport-batch-import-cad"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.3.0
# Extended script to batch import CAD files for multiple model sets without snapping to ground and merging parts with the same material.
``` python
import os
import lux

def genericInput(msg, default=None, check=lambda x: len(x) > 0):
    if default is not None:
        msg += " [{}] ".format(default)
    if not msg.endswith(" "):
        msg += " "
    while True:
        try:
            value = input(msg)
            if check(value):
                return value
            elif len(value) == 0 and default is not None:
                return default
        except EOFError:
            sys.stdout.write("\n")
            continue
        except KeyboardInterrupt:
            sys.exit()

def inputFile(msg):
    return genericInput(msg, check=lambda x: os.path.isfile(x))

def inputText(msg, default):
    return genericInput(msg, default=default)

def intInRange(value, valueRange=None):
    try:
        n = int(value)
        if valueRange is not None:
            return n >= valueRange[0] and n <= valueRange[1]
        else:
            return True
    except ValueError:
        return False

def inputInt(msg, default, valueRange=None):
    return int(genericInput(msg, default=default, check=lambda x: intInRange(x, valueRange)))

def inputItem(msg, defaultIndex, items):
    pre = ""
    for i in range(len(items)):
        pre += "[{}] {}\n".format(i + 1, items[i])
    idx = inputInt(pre + msg, defaultIndex + 1, (1, len(items))) - 1
    return (idx, items[idx])

def cleanExt(ext):
    while ext.startswith("."):
        ext = ext[1:]
    return ext.lower()

def import_cad_for_model_set(model_set_name):
    tmpls = ["-- None --"] + lux.getMaterialTemplates()

    opts = {}
    if not lux.isHeadless():
        values = [
            ("file", lux.DIALOG_FILE, f"File to import for {model_set_name}:", None),
            ("template", lux.DIALOG_ITEM, "Apply material template (optional):", tmpls[0], tmpls)
        ]
        desc = f"Import a model for {model_set_name}, optionally apply a material template, and assign to the model set."
        opts = lux.getInputDialog(
            title=f"Import CAD for {model_set_name}",
            desc=desc,
            values=values,
            id=f"import_assignmaterial_{model_set_name}.py.luxion"
        )
    else:
        opts["file"] = inputFile(f"File to import for {model_set_name}:")
        opts["template"] = inputItem("Apply material template (optional):", 0, tmpls)[1]

    if not opts:
        return

    file_path = opts["file"]
    template = opts["template"][1]  # Extract the template name

    print(f"File Path: {file_path}, Template: {template}, Model Set: {model_set_name}")

    # Import the file
    print(f"Importing {file_path} for model set {model_set_name}")
    import_options = lux.getImportOptions()
    import_options["model_set_import_to"] = 3  # Import to new model set
    import_options["snap_to_ground"] = False  # Do not snap to ground
    import_options["center_geometry"] = False  # Do not center geometry
    import_options["merge_objects"] = True  # Merge parts with the same material

    # Import the file with the new model set active
    lux.importFile(file_path, opts=import_options)

    # Apply the material template if specified
    if template != "-- None --":
        print(f"Setting material template {template}")
        lux.setMaterialTemplate(template)

    # Rename the new model set
    root_node = lux.getSceneTree()
    for model_set in root_node.getChildren():
        if model_set.isModelSet() and model_set.getName() == "New Model Set":
            model_set.setName(model_set_name)
            print(f"Model set renamed to: {model_set_name}")

def main():
    model_sets = [
        "Case",
        "Case Pro",
        "Device",
        "Device Pro",
        "SP",
        "SP Pro",
        "Device Explode",
        "Device Pro Explode",
    ]

    for model_set in model_sets:
        import_cad_for_model_set(model_set)

if __name__ == "__main__":
    main()
```

# End of ImportExport\Batch Import CAD.py

## Batch Import Multiple CAD File Types.py
<a name="importexport-batch-import-multiple-cad-file-types"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.3.2
# HEADLESS COMPLIANT
# Batch Import multiple CAD file types, Name Model Set per CAD, and assign material template.
# MUST be an empty scene.  You must set the import preferences per file type for consistency.
``` python
import os, re, sys
import os.path

def genericInput(msg, default=None, check=lambda x: len(x) > 0):
    if default is not None:
        msg += " [{}] ".format(default)
    if not msg.endswith(" "):
        msg += " "
    while True:
        try:
            value = input(msg)
            if check(value):
                return value
            elif len(value) == 0 and default is not None:
                return default
        except EOFError:
            sys.stdout.write("\n")
            continue
        except KeyboardInterrupt:
            sys.exit()

def inputFolder(msg):
    return genericInput(msg, check=lambda x: os.path.isdir(x))

def inputText(msg, default):
    return genericInput(msg, default=default)

def intInRange(value, valueRange=None):
    try:
        n = int(value)
        if valueRange is not None:
            return n >= valueRange[0] and n <= valueRange[1]
        else:
            return True
    except ValueError:
        return False

def inputInt(msg, default, valueRange=None):
    return int(genericInput(msg, default=default, check=lambda x: intInRange(x, valueRange)))

def inputItem(msg, defaultIndex, items):
    pre = ""
    for i in range(len(items)):
        pre += "[{}] {}\n".format(i + 1, items[i])
    idx = inputInt(pre + msg, defaultIndex + 1, (1, len(items))) - 1
    return (idx, items[idx])

def inputBool(msg, default=False):
    return str(genericInput(msg, default=default)).lower() in ["y", "yes", "true", "1"]

def cleanExt(ext):
    return [e.strip().lower() for e in ext.split(",")]

def main():
    tmpls = ["-- None --"] + lux.getMaterialTemplates()
    info = lux.getSceneInfo()
    opts = {}
    if not lux.isHeadless():
        values = [("folder", lux.DIALOG_FOLDER, "Folder to import from:", None),
                  ("iext", lux.DIALOG_TEXT, "Input file formats to read (comma-separated):", "bip,obj,fbx"),
                  (lux.DIALOG_LABEL, "--"),
                  ("template", lux.DIALOG_ITEM, "Apply material template on each import (optional):", tmpls[0], tmpls)]
        desc = "Batch import models with multiple formats and assign a selected material template if specified."
        opts = lux.getInputDialog(title = "Batch Import and Assign Material Template",
                                  desc = desc,
                                  values = values,
                                  id = "batchimport_assignmaterial_multiformat.py.luxion")
    else:
        opts["folder"] = inputFolder("Folder to import from:")
        opts["iext"] = inputText("Input file formats to read (comma-separated):", "bip,obj,fbx")
        opts["template"] = inputItem("Apply material template on each import (optional):", 0, tmpls)[1]
    if not opts: return

    fld = opts["folder"]
    iexts = cleanExt(opts["iext"])
    reFiles = re.compile(".*\.({})$".format("|".join(iexts)), re.IGNORECASE)

    if not any(reFiles.match(f) for f in os.listdir(fld)):
        raise Exception("Could not find any input files matching the extensions '{}' in '{}'!".format(", ".join(iexts), fld))

    for f in [f for f in os.listdir(fld) if reFiles.match(f)]:
        path = fld + os.path.sep + f

        print("Importing {}".format(path))
        lux.importFile(path)

        if opts["template"][0] != 0:  # Check if a template is selected other than "-- None --"
            template = tmpls[opts["template"][0]]
            print("Setting material template {}".format(template))
            lux.setMaterialTemplate(template)

    # Renaming model sets based on the first child.
    root_node = lux.getSceneTree()
    for model_set in root_node.getChildren():
        if model_set.isModelSet():
            children = model_set.getChildren()
            if children:
                # Assuming the first child's name is the desired new name for the model set.
                new_name = children[0].getName()
                model_set.setName(new_name)
                print(f"Model set renamed to: {new_name}")

main()
```

# End of ImportExport\Batch Import Multiple CAD File Types.py

## Import CAD.py
<a name="importexport-import-cad"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Script to Import CAD
``` python
import os
import lux

def genericInput(msg, default=None, check=lambda x: len(x) > 0):
    if default is not None:
        msg += " [{}] ".format(default)
    if not msg.endswith(" "):
        msg += " "
    while True:
        try:
            value = input(msg)
            if check(value):
                return value
            elif len(value) == 0 and default is not None:
                return default
        except EOFError:
            sys.stdout.write("\n")
            continue
        except KeyboardInterrupt:
            sys.exit()

def inputFile(msg):
    return genericInput(msg, check=lambda x: os.path.isfile(x))

def inputText(msg, default):
    return genericInput(msg, default=default)

def intInRange(value, valueRange=None):
    try:
        n = int(value)
        if valueRange is not None:
            return n >= valueRange[0] and n <= valueRange[1]
        else:
            return True
    except ValueError:
        return False

def inputInt(msg, default, valueRange=None):
    return int(genericInput(msg, default=default, check=lambda x: intInRange(x, valueRange)))

def inputItem(msg, defaultIndex, items):
    pre = ""
    for i in range(len(items)):
        pre += "[{}] {}\n".format(i + 1, items[i])
    idx = inputInt(pre + msg, defaultIndex + 1, (1, len(items))) - 1
    return (idx, items[idx])

def cleanExt(ext):
    while ext.startswith("."):
        ext = ext[1:]
    return ext.lower()

def main():
    tmpls = ["-- None --"] + lux.getMaterialTemplates()
    model_sets = ["Case", "Case Pro", "SP", "Device Exploded", "Default", "Device", "Device Pro", "Device Pro Exploded", "SP Pro"]
    opts = {}
    if not lux.isHeadless():
        values = [
            ("file", lux.DIALOG_FILE, "File to import:", None),
            ("template", lux.DIALOG_ITEM, "Apply material template (optional):", tmpls[0], tmpls),
            ("model_set", lux.DIALOG_ITEM, "Select model set to assign:", model_sets[0], model_sets)
        ]
        desc = "Import a model and optionally apply a material template and assign to a model set."
        opts = lux.getInputDialog(
            title="Import and Assign Material Template",
            desc=desc,
            values=values,
            id="import_assignmaterial.py.luxion"
        )
    else:
        opts["file"] = inputFile("File to import:")
        opts["template"] = inputItem("Apply material template (optional):", 0, tmpls)[1]
        opts["model_set"] = inputItem("Select model set to assign:", 0, model_sets)[1]

    if not opts:
        return

    file_path = opts["file"]
    template = opts["template"][1]  # Extract the template name
    selected_model_set = opts["model_set"][1]  # Extract the model set name

    print(f"File Path: {file_path}, Template: {template}, Model Set: {selected_model_set}")

    # Import the file
    print("Importing {}".format(file_path))
    import_options = lux.getImportOptions()
    import_options["model_set_import_to"] = 3  # Import to new model set

    # Import the file with the new model set active
    lux.importFile(file_path, opts=import_options)

    # Apply the material template if specified
    if template != "-- None --":
        print(f"Setting material template {template}")
        lux.setMaterialTemplate(template)

    # Rename the new model set
    root_node = lux.getSceneTree()
    for model_set in root_node.getChildren():
        if model_set.isModelSet() and model_set.getName() == "New Model Set":
            model_set.setName(selected_model_set)
            print(f"Model set renamed to: {selected_model_set}")

main()
```

# End of ImportExport\Import CAD.py

## Import CAD_Prompt.py
<a name="importexport-import-cad_prompt"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.0.1
# HEADLESS COMPLIANT
# Import CAD via GUI, apply material template, and assign to model sets.
``` python
import os
import lux

def genericInput(msg, default=None, check=lambda x: len(x) > 0):
    if default is not None:
        msg += " [{}] ".format(default)
    if not msg.endswith(" "):
        msg += " "
    while True:
        try:
            value = input(msg)
            if check(value):
                return value
            elif len(value) == 0 and default is not None:
                return default
        except EOFError:
            sys.stdout.write("\n")
            continue
        except KeyboardInterrupt:
            sys.exit()

def inputFile(msg):
    return genericInput(msg, check=lambda x: os.path.isfile(x))

def inputText(msg, default):
    return genericInput(msg, default=default)

def intInRange(value, valueRange=None):
    try:
        n = int(value)
        if valueRange is not None:
            return n >= valueRange[0] and n <= valueRange[1]
        else:
            return True
    except ValueError:
        return False

def inputInt(msg, default, valueRange=None):
    return int(genericInput(msg, default=default, check=lambda x: intInRange(x, valueRange)))

def inputItem(msg, defaultIndex, items):
    pre = ""
    for i in range(len(items)):
        pre += "[{}] {}\n".format(i + 1, items[i])
    idx = inputInt(pre + msg, defaultIndex + 1, (1, len(items))) - 1
    return (idx, items[idx])

def cleanExt(ext):
    while ext.startswith("."):
        ext = ext[1:]
    return ext.lower()

def main():
    tmpls = ["-- None --"] + lux.getMaterialTemplates()
    model_sets = ["Product", "ProductPro", "ProductAccessory", "ProductAccessoryExploded", "Default", "Accessory", "ProductProAccessory"]
    opts = {}
    if not lux.isHeadless():
        values = [
            ("file", lux.DIALOG_FILE, "File to import:", None),
            ("template", lux.DIALOG_ITEM, "Apply material template (optional):", tmpls[0], tmpls),
            ("model_set", lux.DIALOG_ITEM, "Select model set to assign:", model_sets[0], model_sets)
        ]
        desc = "Import a model and optionally apply a material template and assign to a model set."
        opts = lux.getInputDialog(
            title="Import and Assign Material Template",
            desc=desc,
            values=values,
            id="import_assignmaterial.py.luxion"
        )
    else:
        opts["file"] = inputFile("File to import:")
        opts["template"] = inputItem("Apply material template (optional):", 0, tmpls)[1]
        opts["model_set"] = inputItem("Select model set to assign:", 0, model_sets)[1]

    if not opts:
        return

    file_path = opts["file"]
    template = opts["template"][1]  # Extract the template name
    selected_model_set = opts["model_set"][1]  # Extract the model set name

    print(f"File Path: {file_path}, Template: {template}, Model Set: {selected_model_set}")

    # Import the file
    print("Importing {}".format(file_path))
    import_options = lux.getImportOptions()
    import_options["model_set_import_to"] = 3  # Import to new model set

    # Import the file with the new model set active
    lux.importFile(file_path, opts=import_options)

    # Apply the material template if specified
    if template != "-- None --":
        print(f"Setting material template {template}")
        lux.setMaterialTemplate(template)

    # Rename the new model set
    root_node = lux.getSceneTree()
    for model_set in root_node.getChildren():
        if model_set.isModelSet() and model_set.getName() == "New Model Set":
            model_set.setName(selected_model_set)
            print(f"Model set renamed to: {selected_model_set}")

main()
```

# End of ImportExport\Import CAD_Prompt.py

## Import Scene Template cm into a New Scene.py
<a name="importexport-import-scene-template-cm-into-a-new-scene"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.3
# Imports a template Scene into a new scene with units in centimeters.
``` python
import os
import lux

def import_scene_template_cm():
    # Determine the operating system and set the library path accordingly
    if os.name == 'nt':  # Windows
        file_path = "C:\\Users\\Public\\Documents\\KeyShot\\Templates\\Template Test.bip"
    else:  # macOS and Unix/Linux
        file_path = "/Library/Application Support/KeyShot/Templates/Template Test.bip"

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Scene template file '{file_path}' does not exist.")
        return

    # Get the default import options
    opts = lux.getImportOptions(getDefaults=True)

    # Configure the import options based on specified requirements
    opts['import_type'] = 2  # Clear and import to new scene
    opts['model_set_import_to'] = 3  # Add to New Model Set
    opts['geometry_units'] = 100  # Assuming the file uses cm, KeyShot uses meters by default
    opts['inclusion_options'] = 31  # Import Geometry, Cameras, Environments, Image Styles, Studios
    opts['center_geometry'] = False  # Keep Relative to native origin
    opts['adjust_camera_look_at'] = False  # Do not adjust camera look at
    opts['adjust_environment'] = False  # Do not adjust environment
    opts['snap_to_ground'] = False  # Do not snap to ground

    # Import the file with the specified options
    lux.importFile(path=file_path, opts=opts)
    print(f"Scene template '{file_path}' imported with units in centimeters.")

def main():
    import_scene_template_cm()

# Run the main function
main()
```

# End of ImportExport\Import Scene Template cm into a New Scene.py

## Import Scene Template cm into an Existing Scene.py
<a name="importexport-import-scene-template-cm-into-an-existing-scene"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.7
# Imports a template Scene into the existing scene with units in centimeters and adds to a new model set each time.
``` python
import os
import lux
from datetime import datetime

def import_scene_template_cm():
    # Determine the operating system and set the library path accordingly
    if os.name == 'nt':  # Windows
        file_path = "C:\\Users\\Public\\Documents\\KeyShot\\Templates\\Template Test.bip"
    else:  # macOS and Unix/Linux
        file_path = "/Library/Application Support/KeyShot/Templates/Template Test.bip"

    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"Scene template file '{file_path}' does not exist.")
        return

    # Generate a unique model set name based on the current time to avoid name conflicts
    model_set_name = "ModelSet_" + datetime.now().strftime("%Y%m%d_%H%M%S")

    # Get the default import options
    opts = lux.getImportOptions(getDefaults=True)

    # Configure the import options based on specified requirements
    opts['import_type'] = 1  # Add to current scene
    opts['model_set_import_to'] = 3  # Add to New Model Set
    opts['geometry_units'] = 100  # Assuming the file uses cm, KeyShot uses meters by default
    opts['inclusion_options'] = 31  # Import Geometry, Cameras, Environments, Image Styles, Studios
    opts['center_geometry'] = False  # Keep Relative to native origin
    opts['adjust_camera_look_at'] = False  # Do not adjust camera look at
    opts['adjust_environment'] = False  # Do not adjust environment
    opts['snap_to_ground'] = False  # Do not snap to ground

    # Create a new model set with a temporary name
    temporary_model_set_name = "TemporaryModelSet_" + datetime.now().strftime("%Y%m%d_%H%M%S")
    lux.newModelSet(name=temporary_model_set_name)
    print(f"Created new model set '{temporary_model_set_name}'.")

    # Import the file with the specified options
    lux.importFile(path=file_path, opts=opts)
    print(f"Scene template '{file_path}' imported with units in centimeters into new model set.")

    # Rename the new model set to the unique name
    root_node = lux.getSceneTree()
    for model_set in root_node.getChildren():
        if model_set.isModelSet() and model_set.getName() == temporary_model_set_name:
            model_set.setName(model_set_name)
            print(f"Model set renamed to: {model_set_name}")

def main():
    import_scene_template_cm()

# Run the main function
main()
```

# End of ImportExport\Import Scene Template cm into an Existing Scene.py

## Import Scene Template cm.py
<a name="importexport-import-scene-template-cm"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Imports a template Scene into a new scene.
``` python
import os
import lux

# Determine the operating system and set the library path accordingly
if os.name == 'nt':  # Windows
    file_path = "C:\\Users\\Public\\Documents\\KeyShot\\Templates\\Template Test.bip"
else:  # macOS and Unix/Linux
    file_path = "/Library/Application Support/KeyShot/Templates/Template Test.bip"

# Get the default import options
opts = lux.getImportOptions(getDefaults=True)

# Configure the import options based on specified requirements
opts['import_type'] = 2  # Clear and import to new scene
opts['model_set_import_to'] = 3  # Add to New Model Set
opts['geometry_units'] = 100  # Assuming the file uses cm, KeyShot uses meters by default
opts['inclusion_options'] = 31  # Import Geometry, Cameras, Environments, Image Styles, Studios
opts['center_geometry'] = False  # Keep Relative to native origin
opts['adjust_camera_look_at'] = False  # Do not adjust camera look at
opts['adjust_environment'] = False  # Do not adjust environment
opts['snap_to_ground'] = False  # Do not snap to ground

# Import the file with the specified options
lux.importFile(path=file_path, opts=opts)

# After importing the file, delete the "Default" model set if it's empty
#model_sets = lux.getModelSets()
#if "Default" in model_sets:
#    lux.removeModelSet(name="Default")
```

# End of ImportExport\Import Scene Template cm.py

## Import Scene Template mm.py
<a name="importexport-import-scene-template-mm"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Imports a template Scene into a new scene.
``` python
import os
import lux

# Determine the operating system and set the library path accordingly. Change Your Scene Name.bip to your file name and extension.
if os.name == 'nt':  # Windows
    file_path = "C:\\Users\\Public\\Documents\\KeyShot\\Templates\\Your Scene Name.bip"
else:  # macOS and Unix/Linux
    file_path = "/Library/Application Support/KeyShot/Templates/Your Scene Name.bip"

# Get the default import options
opts = lux.getImportOptions(getDefaults=True)

# Configure the import options based on specified requirements
# opts['import_type'] = 2  # Clear and import to new scene
opts['model_set_import_to'] = 3  # Add to New Model Set
opts['geometry_units'] = 1000  # Assuming the file uses mm, KeyShot uses meters by default
opts['inclusion_options'] = 31  # Import Geometry, Cameras, Environments, Image Styles, Studios
opts['center_geometry'] = False  # Keep Relative to native origin
opts['adjust_camera_look_at'] = False  # Do not adjust camera look at
opts['adjust_environment'] = False  # Do not adjust environment
opts['snap_to_ground'] = False  # Do not snap to ground

# Import the file with the specified options
lux.importFile(path=file_path, opts=opts)
```

# End of ImportExport\Import Scene Template mm.py

## Import Template meters.py
<a name="importexport-import-template-meters"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Imports a Baron Ring template Scene into a new scene.
``` python
import os
import lux

file_path = os.path.join(lux.getKeyShotFolder(type=lux.FOLDER_RESOURCE_ROOT), "Templates", "Layout_Master_Scene_05.bip")

# Get the default import options
opts = lux.getImportOptions(getDefaults=True)

# Configure the import options based on specified requirements
opts['import_type'] = 2  # Clear and import to new scene
opts['model_set_import_to'] = 3  # Add to New Model Set
opts['geometry_units'] = 1  # Assuming the file uses meters, KeyShot uses meters by default
opts['inclusion_options'] = 31  # Import Geometry, Cameras, Environments, Image Styles, Studios
opts['center_geometry'] = False  # Keep Relative to native origin
opts['adjust_camera_look_at'] = False  # Do not adjust camera look at
opts['adjust_environment'] = False  # Do not adjust environment
opts['snap_to_ground'] = False  # Do not snap to ground

# Import the file with the specified options
lux.importFile(path=file_path, opts=opts)

# After importing the file, check and delete the "Default" model set if it exists
#model_sets = lux.getModelSets()
#if "Default" in model_sets:
#    lux.removeModelSet(name="Default")
```

# End of ImportExport\Import Template meters.py

## Import Template mm.py
<a name="importexport-import-template-mm"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Imports a template Scene into a new scene.
``` python
import os
import lux

# Determine the operating system and set the library path accordingly
if os.name == 'nt':  # Windows
    file_path = "C:\\Users\\Public\\Documents\\KeyShot\\Templates\\Template Test.bip"
else:  # macOS and Unix/Linux
    file_path = "/Library/Application Support/KeyShot/Templates/Template Test.bip"

# Get the default import options
opts = lux.getImportOptions(getDefaults=True)

# Configure the import options based on specified requirements
opts['import_type'] = 2  # Clear and import to new scene
opts['model_set_import_to'] = 3  # Add to New Model Set
opts['geometry_units'] = 1000  # Assuming the file uses mm, KeyShot uses meters by default
opts['inclusion_options'] = 31  # Import Geometry, Cameras, Environments, Image Styles, Studios
opts['center_geometry'] = False  # Keep Relative to native origin
opts['adjust_camera_look_at'] = False  # Do not adjust camera look at
opts['adjust_environment'] = False  # Do not adjust environment
opts['snap_to_ground'] = False  # Do not snap to ground

# Import the file with the specified options
lux.importFile(path=file_path, opts=opts)

# After importing the file, check and delete the "Default" model set if it exists
#model_sets = lux.getModelSets()
#if "Default" in model_sets:
#    lux.removeModelSet(name="Default")
```

# End of ImportExport\Import Template mm.py

## Import_GLB_TranslateRotateScale.py
<a name="importexport-import_glb_translaterotatescale"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.1
# Headless Example: Import GLB files from a directory and apply transformations
``` python
import lux
import luxmath
import os

def import_glb_files_from_directory(directory):
    """
    Import GLB files from the specified directory into KeyShot.
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith('.glb'):
            file_path = os.path.join(directory, filename)
            print(f"Importing GLB file: {file_path}")
            lux.importFile(file_path, showOpts=False)

def apply_transformations_to_all_models(distance, scale_factor):
    """
    Apply translation, rotation, and scaling transformations to all models in the scene.
    """
    scene_root = lux.getSceneTree()
    model_nodes = scene_root.find("", types=[lux.NODE_TYPE_OBJECT])

    for model_node in model_nodes:
        print(f"Transforming model node: {model_node.getName()}")

        # Translation
        translation_vector = luxmath.Vector(0, -distance, 0)
        translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)

        # Rotation
        rotation_axis = luxmath.Vector(0, 0, 1)
        rotation_angle = -90
        rotation_matrix = luxmath.Matrix().makeIdentity().rotateAroundAxis(rotation_axis, rotation_angle)

        # Scaling
        scale_matrix = luxmath.Matrix().makeIdentity().scale(luxmath.Vector(scale_factor, scale_factor, scale_factor))

        # Combining transformations
        combined_transform = translation_matrix.mul(rotation_matrix).mul(scale_matrix)

        model_node.applyTransform(combined_transform, absolute=False)

# Specify the directory containing GLB files
directory = r"C:\GLB_OBJ"

# Import GLB files from the directory
import_glb_files_from_directory(directory)

# Apply transformations to all imported models
apply_transformations_to_all_models(2, 2)

print("Importing and transformations of GLB files complete.")
```

# End of ImportExport\Import_GLB_TranslateRotateScale.py

## Import_OBJ_TranslateRotateScale.py
<a name="importexport-import_obj_translaterotatescale"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.2
# Headless Example: Import OBJ files from a directory and apply transformations
``` python
import lux
import luxmath
import os

def import_obj_files_from_directory(directory):
    """
    Import OBJ files from the specified directory into KeyShot.
    """
    for filename in os.listdir(directory):
        if filename.lower().endswith('.obj'):
            file_path = os.path.join(directory, filename)
            print(f"Importing OBJ file: {file_path}")
            lux.importFile(file_path, showOpts=False)

def apply_transformations_to_all_models(distance, scale_factor):
    """
    Apply translation, rotation, and scaling transformations to all models in the scene.
    """
    scene_root = lux.getSceneTree()
    model_nodes = scene_root.find("", types=[lux.NODE_TYPE_OBJECT])

    for model_node in model_nodes:
        print(f"Transforming model node: {model_node.getName()}")

        # Translation
        translation_vector = luxmath.Vector(0, -distance, 0)
        translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)

        # Rotation
        rotation_axis = luxmath.Vector(0, 0, 1)
        rotation_angle = -90
        rotation_matrix = luxmath.Matrix().makeIdentity().rotateAroundAxis(rotation_axis, rotation_angle)

        # Scaling
        scale_matrix = luxmath.Matrix().makeIdentity().scale(luxmath.Vector(scale_factor, scale_factor, scale_factor))

        # Combining transformations
        combined_transform = translation_matrix.mul(rotation_matrix).mul(scale_matrix)

        model_node.applyTransform(combined_transform, absolute=False)

# Specify the directory containing OBJ files
directory = r"C:\GLB_OBJ"

# Import OBJ files from the directory
import_obj_files_from_directory(directory)

# Apply transformations to all imported models
apply_transformations_to_all_models(2, 2)

print("Importing and transformations of OBJ files complete.")
```

# End of ImportExport\Import_OBJ_TranslateRotateScale.py

## Get Camera Distance.py
<a name="information-get-camera-distance"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Display the camera distance in a custom input dialog. Select Reset to see the camera distance to target.
``` python
import lux

def main():
    # Retrieve the active camera
    camera = lux.getCamera()

    # Get camera position and look-at point
    camera_position = lux.getCameraPosition()
    look_at_point = lux.getCameraLookAt()

    # Calculate the distance between camera position and look-at point
    camera_distance = calculate_distance(camera_position, look_at_point)

    # Prepare the dialog values
    values = [("camera_distance", lux.DIALOG_TEXT, "Camera Distance:", str(camera_distance))]

    # Display the dialog
    opts = lux.getInputDialog(title = "Display Camera Distance", 
                              desc = "The distance from the camera to the look-at point is:", 
                              values = values, 
                              id = "display_camera_distance")

    # The opts dictionary will contain the values entered by the user
    print(opts)

def calculate_distance(point1, point2):
    # Assuming point1 and point2 are tuples (x, y, z)
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2) ** 0.5

main()
```

# End of Information\Get Camera Distance.py

## Get MaterialGraph Parameters.py
<a name="information-get-materialgraph-parameters"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script for retrieving and displaying material parameters in KeyShot for scripting purposes.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

# Function to display a dialog for material selection from the scene.
def display_material_selection():
    scene_materials = lux.getSceneMaterials()  # Retrieve all materials from the current scene.
    if not scene_materials:
        print("No materials found in the scene.")  # Print a message if no materials are found.
        return None

    # Create a list of tuples for each material to be used in the dialog.
    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    # Display a dialog to the user to select materials. It returns a dictionary of user selections.
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None  # Return None if the user does not make a selection.
    # Return a list of materials selected by the user.
    return [mat for mat, selected in user_selection.items() if selected]

# Function to print the parameters of shader nodes for a given material.
def print_shader_node_parameters(material_name):
    # Get the material graph of the specified material.
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")  # Notify if material graph is not found.
        return

    # Iterate through each shader node in the material graph.
    for shader_node in material_graph.getNodes():
        print(f"Parameters for shader node in material '{material_name}':")
        # Print each parameter's name and type for the shader node.
        for parameter in shader_node.getParameters():
            print(f"- {parameter.getName()} (Type: {parameter.getType()})")

# Main function to run the script.
def main():
    selected_materials = display_material_selection()  # Get the user's selection of materials.
    if not selected_materials:
        print("No materials selected or operation cancelled.")  # Inform if no materials are selected.
        return

    # For each selected material, print its shader node parameters.
    for material_name in selected_materials:
        print_shader_node_parameters(material_name)

main()  # Execute the main function.
```

# End of Information\Get MaterialGraph Parameters.py

## Get Metadata.py
<a name="information-get-metadata"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Get Metadata
``` python
import lux

# Print the entire scene info to understand its structure
scene_metadata = lux.getMetaData
print(scene_metadata)


```
# End of Information\Get Metadata.py

## Get Model Sets.py
<a name="information-get-model-sets"></a>
```python
# AUTHOR LUX DT ChatGPT
# VERSION 0.0.0
# Script that prints out the names of all model sets.

import lux

def print_model_sets():
    # Retrieve a list of all active model sets
    model_sets = lux.getModelSets()
    
    # Print the names of all model sets
    for model_set in model_sets:
        print(model_set)

# Execute the function
print_model_sets()
```

# End of Information\Get Model Sets.py

## Get Node Type.py
<a name="information-get-node-type"></a>
# AUTHOR LUX DT
# VERSION 0.1.1
# HEADLESS COMPLIANT
# Print (Get) Node Type
``` python
import lux

def print_part_properties():
    # Get the root of the scene tree
    root_node = lux.getSceneTree()

    # Recursive function to process each node
    def process_node(node):
        print(f"Node Name: {node.getName()}")
        print(f"Node Type: {node.getKind()}")  # Outputs the type of node, e.g., object, group, etc.

        # Process all children nodes
        for child in node.getChildren():
            process_node(child)

    # Start processing from the root
    process_node(root_node)

# Execute the function
print_part_properties()
```


# End of Information\Get Node Type.py

## Get Render Info.py
<a name="information-get-render-info"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Print / Get Scene Render Options from Dictionary.
``` python
import lux
import json

def print_render_options_prettily():
    # Get the current render options
    render_options = lux.getRenderOptions()
    
    # Use getDict() method to get all render options as a dictionary
    render_options_dict = render_options.getDict()

    # Pretty print the dictionary using json.dumps for better readability
    pretty_render_options = json.dumps(render_options_dict, indent=4)
    print("Render Options:")
    print(pretty_render_options)

# Execute the function to show render settings in a pretty format
print_render_options_prettily()
```
# End of Information\Get Render Info.py

## Get Resource Library Models.py
<a name="information-get-resource-library-models"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script that lists models in the KeyShot Resources/Models directory and its subdirectories.
``` python
import os
import lux


def list_models_in_library():
    """
    Lists all model files in the KeyShot Resources/Models directory and its subdirectories.
    """
    models_path = lux.getKeyShotFolder(type=lux.FOLDER_MODELS)
    
    # Check if the models directory exists
    if not os.path.exists(models_path):
        lux.getMessageBox(f"Models directory not found at:\n{models_path}", "Models Directory", lux.MESSAGE_BOX_WARNING)
        return
    
    # Recursively list all model files in the directory and subdirectories
    model_files = []
    for root, dirs, files in os.walk(models_path):
        for file in files:
            if file.endswith(('.bip', '.ksp')):
                model_files.append(os.path.relpath(os.path.join(root, file), models_path))
    
    if not model_files:
        message = "No model files found in the Resources/Models directory."
    else:
        message = "Models found in the Resources/Models directory:\n" + "\n".join(model_files)
    
    # Display the model files in a message box
    lux.getMessageBox(message, "Models List", lux.MESSAGE_BOX_INFO)

# Example usage
list_models_in_library()
```

# End of Information\Get Resource Library Models.py

## Get Configured Resource Library Path.py
<a name="information-get-configured-resource-library-path"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script that gets the KeyShot Resources Library Path.  
``` python
import lux

def get_library_path():
    """Display the configured KeyShot resource folder."""
    library_path = lux.getKeyShotFolder(type=lux.FOLDER_RESOURCE_ROOT)

    # Display the library path in a message box
    lux.getMessageBox(f"Your KeyShot Resources Library path is:\n{library_path}", "Library Path", lux.MESSAGE_BOX_INFO)
    
    return library_path

# Example usage
library_path = get_library_path()
print(f"Library path: {library_path}")
```

# End of Information\Get Configured Resource Library Path.py

## Display Resource Library Path.py
<a name="information-display-resource-library-path"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Displays the configured KeyShot resource folder in a message box.
``` python
import lux

def get_library_path():
    """Display the configured KeyShot resource folder."""
    library_path = lux.getKeyShotFolder(type=lux.FOLDER_RESOURCE_ROOT)

    # Display the library path in a message box
    lux.getMessageBox(f"Your KeyShot Resources Library path is:\n{library_path}", "Library Path", lux.MESSAGE_BOX_INFO)
    
    return library_path

# Example usage
library_path = get_library_path()
print(f"Library path: {library_path}")
```

# End of Information\Display Resource Library Path.py

## Get Resource Library Path.py
<a name="information-get-resource-library-path"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script that gets the KeyShot Resources Library Path.  
``` python
import lux

def get_library_path():
    """Display the configured KeyShot resource folder."""
    library_path = lux.getKeyShotFolder(type=lux.FOLDER_RESOURCE_ROOT)

    # Display the library path in a message box
    lux.getMessageBox(f"Your KeyShot Resources Library path is:\n{library_path}", "Library Path", lux.MESSAGE_BOX_INFO)
    
    return library_path

# Example usage
library_path = get_library_path()
print(f"Library path: {library_path}")
```

# End of Information\Get Resource Library Path.py

## Get Scene Info.py
<a name="information-get-scene-info"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Get Scene Info.
``` python
import lux

# Print the entire scene info to understand its structure
scene_info = lux.getSceneInfo()
print(scene_info)


```
# End of Information\Get Scene Info.py

## Get Scene Information.py
<a name="information-get-scene-information"></a>
```python
# AUTHOR LUX DT CHATGPT
# VERSION 0.1.1
# HEADLESS COMPLIANT
# Print (Get) Scene Information 

import lux

def print_scene_info():
    # Retrieve overall scene information
    scene_info = lux.getSceneInfo()
    
    # Print all available information from the scene info
    print("Scene Information:")
    for key, value in scene_info.items():
        print(f"{key}: {value}")

# Execute the function
print_scene_info()
```
# End of Information\Get Scene Information.py

## Get Scene Materials.py
<a name="information-get-scene-materials"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to get and print the names of all materials in a KeyShot scene.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def test_script():
    """
    Print the names of all materials currently used in the scene.
    """
    # Retrieve the list of all materials in the current scene.
    scene_materials = lux.getSceneMaterials()

    # Iterate through each material and print its name.
    for material_name in scene_materials:
        print(f"Material: {material_name}")

# Execute the test script to list materials.
test_script()
```

# End of Information\Get Scene Materials.py

## Get SceneTree Nodes.py
<a name="information-get-scenetree-nodes"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example script that retrieves Scene Nodes; Group, Model, ModelSet, Object, Camera, Animation, and Unknown.
``` python
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

# End of Information\Get SceneTree Nodes.py

## Get SceneTree.py
<a name="information-get-scenetree"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example script that retrieves the root node of the current scene using lux.getSceneTree(),
# and then prints out a summary of the scene structure by recursively listing all nodes and their types.
# This script is a basic demonstration of how to interact with the scene tree in KeyShot via scripting.
``` python
import lux

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
    return all_children # Main process starts here.
# Get the root node of the scene.
root_node = lux.getSceneTree()

# Get all nodes in the scene.
all_nodes = get_all_children(root_node)

if __name__ == "__main__":
    main()
```

# End of Information\Get SceneTree.py

## Get Scenes Material Parameters and Save to File.py
<a name="information-get-scenes-material-parameters-and-save-to-file"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Get scene material parameters and saves them to a .txt.
``` python
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
```

# End of Information\Get Scenes Material Parameters and Save to File.py

## Get_Camera_Info.py
<a name="information-get_camera_info"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.3
# Script to view camera details in a window in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def get_camera_info(camera_name):
    """
    Retrieve and format information for a specified camera.

    :param camera_name: Name of the camera to get information about.
    :return: Formatted string containing camera details.
    """
    # Set the selected camera as active.
    lux.setCamera(camera_name)

    # Retrieve various camera details.
    lens_info = lux.getCameraLens()
    fov = round(lux.getCameraFieldOfView(), 2)  # Field of view.
    focal_length = round(lux.getCameraFocalLength(), 2)  # Focal length.
    lens_type = lens_info.get('type') if isinstance(lens_info, dict) else 'Unknown'
    direction = lux.getCameraDirection()  # Camera direction.
    distance = round(lux.getCameraDistance(), 2)  # Distance from pivot.
    position = lux.getCameraPosition()  # Camera position.
    up_vector = lux.getCameraUp()  # Up vector.

    # Format the camera information for display.
    camera_info = (f"Lens Info: {lens_info}\nFOV: {fov}\nFocal Length: {focal_length} mm\n"
                   f"Lens Type: {lens_type}\nDirection: {direction}\nDistance: {distance}\n"
                   f"Position: {position}\nUp Vector: {up_vector}")
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
```
# End of Information\Get_Camera_Info.py

