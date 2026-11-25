# Scripting Examples: Lux Scripts, Settings, and Transforms

[Scripting Examples TOC](../Scripting_Examples.md)

## Create Standard Views.py
<a name="scripts_lux-create-standard-views"></a>
```python
# -*- coding: utf-8 -*-
# AUTHOR Luxion
# VERSION 0.1.3
# HEADLESS COMPLIANT
# Creates a new camera for each of the 7 standard views. If the cameras exist
# already then they will be updated.

views = {lux.VIEW_FRONT: "Front",
         lux.VIEW_BACK: "Back",
         lux.VIEW_LEFT: "Left",
         lux.VIEW_RIGHT: "Right",
         lux.VIEW_TOP: "Top",
         lux.VIEW_BOTTOM: "Bottom",
         lux.VIEW_ISOMETRIC: "Isometric"}

for view in views:
    name = "View_" + views[view]
    has = False
    if name in lux.getCameras():
        has = True
        lux.setCamera(name)
    else:
        lux.newCamera(name)
    lux.setStandardView(view)
    lux.saveCamera()
    print("{} camera: {}".format("Updated" if has else "Created", name))


```
# End of Scripts_Lux\Create Standard Views.py

## Encode Video.py
<a name="scripts_lux-encode-video"></a>
```python
# -*- coding: utf-8 -*-
# AUTHOR Luxion
# VERSION 0.4.0
# HEADLESS COMPLIANT
# Encodes video from separate frame range.
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
            sys.stdout.write("\n")  # Yield a new line so next input isn't on same line.
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

def main():
    opts = {}
    if not lux.isHeadless():
        values = [("folder", lux.DIALOG_FOLDER, "Folder with frames:", None),
                  ("fmt", lux.DIALOG_TEXT, "Frame file format:", "frame.%d.jpg"),
                  ("start", lux.DIALOG_INTEGER, "Start frame:", 1, (1, 4096)),
                  ("end", lux.DIALOG_INTEGER, "End frame:", 10, (1, 4096)),
                  ("fps", lux.DIALOG_INTEGER, "FPS:", 10, (1, 1024)),
                  ("name", lux.DIALOG_TEXT, "Video name:", "video.mp4")]
        opts = lux.getInputDialog(title = "Encode Video",
                                  desc = "Encode video from separate frames of a specified range.",
                                  values = values,
                                  id = "encodevideo.py.luxion")
    else:
        opts["folder"] = inputFolder("Folder with frames:")
        opts["fmt"] = inputText("Frame file format:", "frame.%d.jpg")
        opts["start"] = inputInt("Start frame:", 1, (1, 4096))
        opts["end"] = inputInt("End frame:", 10, (1, 4096))
        opts["fps"] = inputInt("FPS:", 10, (1, 1024))
        opts["name"] = inputText("Video name:", "video.mp4")
    if not opts: return

    if opts["folder"] is None or len(opts["folder"]) == 0:
        raise Exception("Folder cannot be empty!")
    fld = opts["folder"]

    files = opts["fmt"]
    if len(files) == 0:
        raise Exception("Frame format cannot be empty!")
    if files.find("%d") == -1:
        raise Exception("Frame format must contain '%d'!")
    reDigits = re.compile(files.replace("%d", "\d+"))
    found = False
    for f in os.listdir(fld):
        if reDigits.match(f):
            found = True
            break
    if not found:
        raise Exception("Could not find any frames matching the frame format \"{}\" in \"{}\"!"
                        .format(files, fld))

    start = opts["start"]
    end = opts["end"]
    if start > end:
        raise Exception("Start frame cannot be larger than end frame!")

    fps = opts["fps"]

    if len(opts["name"]) == 0:
        raise Exception("Video name cannot be empty!")
    name = opts["name"]

    path = os.path.join(fld, name)
    print("Encoding video {}".format(path))
    res = lux.encodeVideo(folder = fld, frameFiles = files, videoName = name,
                          fps = fps, firstFrame = start, lastFrame = end)
    if not res: raise Exception("Failed to encode video!")

main()
```

# End of Scripts_Lux\Encode Video.py

## Random Scattering.py
<a name="scripts_lux-random-scattering"></a>
# -*- coding: utf-8 -*-
# AUTHOR Luxion
# VERSION 0.2.0
# HEADLESS COMPLIANT
# Duplicates and randomly scatters an object.
```python
import os, sys
from random import uniform, randint, choice

def randbool():
    return randint(0, 1) == 1

def randaxis():
    return luxmath.Vector(choice([(1, 0, 0), (0, 1, 0), (0, 0, 1)]))

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
            sys.stdout.write("\n")  # Yield a new line so next input isn't on same line.
            continue
        except KeyboardInterrupt:
            sys.exit()

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

def main():
    # Find objects to choose from.
    objTxt = []
    objRef = []
    root = lux.getSceneTree()
    types = (lux.NODE_TYPE_GROUP, lux.NODE_TYPE_OBJECT, lux.NODE_TYPE_MODEL)
    for n in root.find("", types = types, depth = 3):
        if n != root:
            objTxt.append("{} ({})".format(str(n.getPath(text = True)[1:]),
                                           n.getMaterial()))
            objRef.append(n)

    if len(objTxt) == 0:
        raise Exception("No objects in the scene!")

    opts = {}
    if not lux.isHeadless():
        values = [("object", lux.DIALOG_ITEM, "Object:", objTxt[0], objTxt),
                  ("dups", lux.DIALOG_INTEGER, "#Duplicates:", 4, (1, 4096)),
                  ("tx", lux.DIALOG_CHECK, "Translate by X axis", True),
                  ("ty", lux.DIALOG_CHECK, "Translate by Y axis", True),
                  ("tz", lux.DIALOG_CHECK, "Translate by Z axis", True),
                  ("rot", lux.DIALOG_CHECK, "Rotate", True)]
        opts = lux.getInputDialog(title = "Random Scattering",
                                  desc = "Duplicates and randomly scatters an object.",
                                  values = values,
                                  id = "randomscattering.py.luxion")
    else:
        opts["object"] = inputItem("Object:", 0, objTxt)
        opts["dups"] = inputInt("#Duplicates:", 4, (1, 4096))
        opts["tx"] = inputBool("Translate by X axis:", True)
        opts["ty"] = inputBool("Translate by Y axis:", True)
        opts["tz"] = inputBool("Translate by Z axis:", True)
        opts["rot"] = inputBool("Rotate:", True)
    if not opts: return

    obj = objRef[opts["object"][0]]
    amount = opts["dups"]
    tx = opts["tx"]
    ty = opts["ty"]
    tz = opts["tz"]
    rot = opts["rot"]

    dups = obj.duplicate(amount = amount)
    if len(dups) == 0:
        raise Exception("No duplicates could be created!")

    # Randomly scatter the duplicates.
    gbbMin, gbbMax = root.getBoundingBox(world = True)
    for dup in dups:
        bbMin, bbMax = dup.getBoundingBox(world = True)

        cx = 0
        if tx:
            cx = (bbMax.x - bbMin.x) / 2
            if randbool():
                cx = uniform(gbbMin.x, cx) - cx
            else:
                cx = uniform(cx, gbbMax.x) - cx

        cy = 0
        if ty:
            cy = (bbMax.y - bbMin.y) / 2
            if randbool():
                cy = uniform(gbbMin.y, cy) - cy
            else:
                cy = uniform(cy, gbbMax.y) - cy

        cz = 0
        if tz:
            cz = (bbMax.z - bbMin.z) / 2
            if randbool():
                cz = uniform(gbbMin.z, cz) - cz
            else:
                cz = uniform(cz, gbbMax.z) - cz

        mat = luxmath.Matrix().makeIdentity().translate(luxmath.Vector((cx, cy, cz)))
        if rot:
            mat = mat.rotateAroundAxis(randaxis(), uniform(0, 360))
        dup.applyTransform(mat)

main()
```

# End of Scripts_Lux\Random Scattering.py

## Render Ambient Occlusion.py
<a name="scripts_lux-render-ambient-occlusion"></a>
# -*- coding: utf-8 -*-
# AUTHOR Luxion
# VERSION 0.2.6
# Render ambient occlusion of current scene.
```python
import os

def main():
    info = lux.getSceneInfo()
    values = [("folder", lux.DIALOG_FOLDER, "Output folder:", None),
              ("name", lux.DIALOG_TEXT, "Image name:", "occlusion.png"),
              ("width", lux.DIALOG_INTEGER, "Output width:", info["width"]),
              ("height", lux.DIALOG_INTEGER, "Output height:", info["height"]),
              ("time", lux.DIALOG_INTEGER, "Render max time (s):", 10, (1, 86400)),
              (lux.DIALOG_LABEL, "--"),
              ("queue", lux.DIALOG_CHECK, "Add to queue", True),
              ("process", lux.DIALOG_CHECK, "Process queue after running script", False)]
    opts = lux.getInputDialog(title = "Render Ambient Occlusion",
                              desc = "Render ambient occlusion of current scene.",
                              values = values,
                              id = "renderambientocclusion.py.luxion")
    if not opts: return

    if len(opts["folder"]) == 0:
        raise Exception("Folder cannot be empty!")

    if len(opts["name"]) == 0:
        raise Exception("Image name cannot be empty!")

    env = lux.getActiveEnvironment()
    oldLightEnv = env.getLightingEnvironment()
    mmap = lux.getMaterialMapping()

    env.setLightingEnvironment("All White 4k")
    for node in lux.getSceneTree().find(""):
        node.setMaterial("Matte White")

    path = os.path.join(opts["folder"], opts["name"])
    width = opts["width"]
    height = opts["height"]
    time = opts["time"]
    queue = opts["queue"]
    process = opts["process"]

    ropts = lux.getRenderOptions()

    # Maximum time rendering does not work on NR so disable sending to it if set, otherwise it
    # yields an exception about mixing the two settings.
    ropts.setSendToNetwork(False)
    ropts.setMaxTimeRendering(time)

    ropts.setAddToQueue(queue)

    lux.renderImage(path = path, width = width, height = height, opts = ropts)

    env.setLightingEnvironment(oldLightEnv)
    lux.applyMaterialMapping(mmap)

    if process:
        print("Processing queue")
        lux.processQueue()

main()
```

# End of Scripts_Lux\Render Ambient Occlusion.py

## Render Animation Passes.py
<a name="scripts_lux-render-animation-passes"></a>
# -*- coding: utf-8 -*-
# AUTHOR Luxion
# VERSION 0.3.6
# Renders animation frames with optional passes.
```python
import os

def ambOcclusionPass():
    lux.getActiveEnvironment().setLightingEnvironment("All White 4k")
    for node in lux.getSceneTree().find(""):
        node.setMaterial("Matte White")

def toonShaderPass():
    for node in lux.getSceneTree().find(""):
        node.setMaterial("Toon Outline Black")

def render(folder, fmt, frame, pass_, width, height, env, mmap, opts):
    fmt = fmt.replace("%d", str(frame)).replace("%s", pass_)
    path = os.path.join(folder, fmt)
    lux.renderImage(path = path, width = width, height = height, opts = opts)
    lux.getActiveEnvironment().setLightingEnvironment(env)
    lux.applyMaterialMapping(mmap)

def main():
    frames = lux.getAnimationInfo()["frames"]
    if frames == 0:
        raise Exception("No animation in scene! Please create one and try again.")

    info = lux.getSceneInfo()
    values = [("folder", lux.DIALOG_FOLDER, "Output folder:", None),
              ("fmt", lux.DIALOG_TEXT, "Output file format:", "frame.%d.%s.jpg"),
              ("width", lux.DIALOG_INTEGER, "Output width:", info["width"]),
              ("height", lux.DIALOG_INTEGER, "Output height:", info["height"]),
              ("start", lux.DIALOG_INTEGER, "Start frame:", 1, (1, frames)),
              ("end", lux.DIALOG_INTEGER, "End frame:", 10, (1, frames)),
              (lux.DIALOG_LABEL, "---"),
              (lux.DIALOG_LABEL, "Passes:"),
              ("occl", lux.DIALOG_CHECK, "Ambient occlusion", True),
              ("toon", lux.DIALOG_CHECK, "Toon outline shading", True),
              (lux.DIALOG_LABEL, "--"),
              (lux.DIALOG_LABEL, "Options:"),
              ("queue", lux.DIALOG_CHECK, "Add to queue", True),
              ("process", lux.DIALOG_CHECK, "Process queue after running script", False)]
    opts = lux.getInputDialog(title = "Render Animation Passes",
                              desc = "Render animation frames with optional passes.",
                              values = values,
                              id = "renderanimationpasses.py.luxion")
    if not opts: return

    if len(opts["folder"]) == 0:
        raise Exception("Folder cannot be empty!")
    fld = opts["folder"]

    fmt = opts["fmt"]
    if len(fmt) == 0:
        raise Exception("Output format cannot be empty!")
    if fmt.find("%d") == -1:
        raise Exception("Output format must contain '%d' to express the frame number!")
    if fmt.find("%s") == -1:
        raise Exception("Output format must contain '%s' to express the pass!")

    width = opts["width"]
    height = opts["height"]

    start = opts["start"]
    end = opts["end"]
    if start > end:
        raise Exception("Start frame cannot be larger than end frame!")

    if not opts["occl"] and not opts["toon"]:
        raise Exception("You must select at least one pass!")

    queue = opts["queue"]
    process = opts["process"]

    lightEnv = lux.getActiveEnvironment().getLightingEnvironment()
    mmap = lux.getMaterialMapping()

    ropts = lux.getRenderOptions()
    ropts.setAddToQueue(queue)

    for frame in range(start, end+1):
        lux.setAnimationFrame(frame)

        # Passes to apply.
        if opts["occl"]:
            ambOcclusionPass()
            render(fld, fmt, frame, "occl", width, height, lightEnv, mmap, ropts)

        if opts["toon"]:
            toonShaderPass()
            render(fld, fmt, frame, "toon", width, height, lightEnv, mmap, ropts)

    if process:
        print("Processing queue")
        lux.processQueue()

main()
```

# End of Scripts_Lux\Render Animation Passes.py

## Render Images.py
<a name="scripts_lux-render-images"></a>
# -*- coding: utf-8 -*-
# AUTHOR Luxion
# VERSION 0.7.1
# HEADLESS COMPLIANT
# Renders all models with a chosen extension to images.
```python
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
            sys.stdout.write("\n")  # Yield a new line so next input isn't on same line.
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
                  ("oext", lux.DIALOG_TEXT, "Output image format:", "png"),
                  ("width", lux.DIALOG_INTEGER, "Output width:", info["width"]),
                  ("height", lux.DIALOG_INTEGER, "Output height:", info["height"]),
                  (lux.DIALOG_LABEL, "--"),
                  ("template", lux.DIALOG_ITEM, "Apply material template on each import (optional):",
                   tmpls[0], tmpls),
                  (lux.DIALOG_LABEL, "--"),
                  ("queue", lux.DIALOG_CHECK, "Add to queue", True),
                  ("process", lux.DIALOG_CHECK, "Process queue after running script", False)]
        desc = "Rendes all models with a chosen input extension to images of chosen output extension."
        opts = lux.getInputDialog(title = "Render Images",
                                  desc = desc,
                                  values = values,
                                  id = "renderimages.py.luxion")
    else:
        opts["folder"] = inputFolder("Folder to import from:")
        opts["iext"] = inputText("Input file format to read:", "bip")
        opts["oext"] =  inputText("Output image format:", "png")
        opts["width"] =  inputInt("Output width:", info["width"])
        opts["height"] =  inputInt("Output height:", info["height"])
        opts["template"] = inputItem("Apply material template on each import (optional):", 0, tmpls)
        opts["queue"] = inputBool("Add to queue", True)
        opts["process"] = inputBool("Process queue after running script", False)
    if not opts: return

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

    width = opts["width"]
    height = opts["height"]
    template = opts["template"]
    queue = opts["queue"]
    process = opts["process"]

    # Only set template if one was chosen.
    if template[0] == 0:
        template = None
    else:
        template = template[1]

    opts = lux.getRenderOptions()
    opts.setAddToQueue(queue)

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

    if process:
        print("Processing queue")
        lux.processQueue()

main()
```

# End of Scripts_Lux\Render Images.py

## Render Panoramic Frames.py
<a name="scripts_lux-render-panoramic-frames"></a>
# -*- coding: utf-8 -*-
# AUTHOR Luxion
# VERSION 0.5.1
# HEADLESS COMPLIANT
# Renders frames similar to a panoramic VR.
```python
import os, sys
from math import cos, sin, pi

def rotateY(vec, angle, clockwise):
    if clockwise: angle *= -1
    return (vec[0] * cos(angle) + vec[2] * sin(angle),
            vec[1],
            -vec[0] * sin(angle) + vec[2] * cos(angle))

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
            sys.stdout.write("\n")  # Yield a new line so next input isn't on same line.
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

def main():
    cams = lux.getCameras()
    if len(cams) == 0:
      raise Exception("No cameras found! Save a camera and try again. Free camera won't be used!")

    info = lux.getSceneInfo()

    opts = {}
    if not lux.isHeadless():
        values = [("cam", lux.DIALOG_ITEM, "Camera to use:", lux.getCamera(), cams),
                  ("frames", lux.DIALOG_INTEGER, "#Frames:", 6, (1, 360)),
                  ("fmt", lux.DIALOG_TEXT, "Output file format:", "frame.%d.png"),
                  ("folder", lux.DIALOG_FOLDER, "Output folder:", None),
                  ("width", lux.DIALOG_INTEGER, "Output width:", info["width"]),
                  ("height", lux.DIALOG_INTEGER, "Output height:", info["height"]),
                  (lux.DIALOG_LABEL, "--"),
                  ("queue", lux.DIALOG_CHECK, "Add to queue", True),
                  ("process", lux.DIALOG_CHECK, "Process queue after running script", False),
                  ("clockwise", lux.DIALOG_CHECK, "Rotate clockwise", True)]
        opts = lux.getInputDialog(title = "Render Panoramic Frames",
                                  desc = "Renders frames similar to a panoramic VR. This script assumes the camera is already positioned correctly.",
                                  values = values,
                                  id = "renderpanframes.py.luxion")
    else:
        try:
            camIdx = cams.index(lux.getCamera())
        except:
            camIdx = 0
        opts["cam"] = inputItem("Camera to use:", camIdx, cams)
        opts["frames"] = inputInt("#Frames:", 6, (1, 360))
        opts["fmt"] = inputText("Output file format:", "frame.%d.png")
        opts["folder"] = inputFolder("Output folder:")
        opts["width"] = inputInt("Width:", info["width"])
        opts["height"] = inputInt("height:", info["height"])
        opts["clockwise"] = inputBool("Rotate clockwise:", True)
        opts["queue"] = inputBool("Add to queue", True)
        opts["process"] = inputBool("Process queue after running script", False)
    if not opts: return

    cam = opts["cam"][1]
    frames = opts["frames"]

    fmt = opts["fmt"]
    if len(fmt) == 0:
        raise Exception("Output format cannot be empty!")
    if fmt.find("%d") == -1:
        raise Exception("Output format must contain '%d'!")

    folder = opts["folder"]
    if len(folder) == 0:
        raise Exception("Folder cannot be empty!")

    width = opts["width"]
    height = opts["height"]
    clockwise = opts["clockwise"]
    queue = opts["queue"]
    process = opts["process"]

    oldcam = lux.getCamera()
    angle = (360 / frames) * pi / 180 # radians

    cancelled = False
    lux.setCamera(cam)
    for i in range(frames):
        # Rotate around Y-axis by angle.
        lux.setCameraDirection(rotateY(lux.getCameraDirection(), angle, clockwise))
        lux.setCameraUp(rotateY(lux.getCameraUp(), angle, clockwise))

        path = os.path.join(folder, fmt.replace("%d", str(i)))
        print("Rendering {} of {} frames: {}".format(i+1, frames, path))
        opts = lux.getRenderOptions()
        opts.setAddToQueue(queue)
        if not lux.renderImage(path = path, width = width, height = height, opts = opts):
            print("Cancelled script!")
            cancelled = True
            break

    # Reset to old camera.
    lux.setCamera(oldcam)

    if process and not cancelled:
        print("Processing queue")
        lux.processQueue()

main()
```

# End of Scripts_Lux\Render Panoramic Frames.py

## Lighting Settings.py
<a name="settings-lighting-settings"></a>
# AUTHOR LUX DT ChatGPT4
# VERSION 0.1.0
# Script that cinfigures the scene lighting settings
```python
import lux

def configure_lighting_settings():
    """Configure global lighting settings."""
    lighting_presets = lux.getLightingPresets()
    preset_name = "Product"
    if preset_name in lighting_presets:
        lux.setLightingPreset(preset_name)
        print(f"Lighting settings configured using preset: {preset_name}")
    else:
        print(f"Lighting preset '{preset_name}' not found.")

if __name__ == "__main__":
    configure_lighting_settings()


```
# End of Settings\Lighting Settings.py

## Set Scene Unit.py
<a name="settings-set-scene-unit"></a>
```python
# AUTHOR LUX  DT ChatGPT4
# VERSION 0.0.0
# Set Scene Unit Template

import lux

class UnitSetter:
    def __init__(self):
        self.unit_map = {
            "MM": lux.UNIT_MM,
            "CM": lux.UNIT_CM,
            "IN": lux.UNIT_IN,
            "FT": lux.UNIT_FT,
            "M": lux.UNIT_M
        }

    def set_units(self, unit_name, rescale=True):
        unit = self.unit_map.get(unit_name.upper())
        if unit is None:
            print(f"Invalid unit name: {unit_name}. Please use one of {list(self.unit_map.keys())}.")
            return False
        
        try:
            print(f"Setting units to: {unit_name.upper()}, Rescale: {rescale}")
            result = lux.setSceneUnit(unit, rescale)
            if result:
                print(f"Units successfully set to {unit_name.upper()}. Rescale: {'Yes' if rescale else 'No'}.")
            else:
                print(f"Failed to set units to {unit_name.upper()}. The function returned False.")
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

# Example usage
if __name__ == "__main__":
    unit_setter = UnitSetter()
    
    # Setting units to millimeters and rescale the scene
    unit_setter.set_units("MM", rescale=True)

    # You can also try setting other units
    # unit_setter.set_units("CM", rescale=True)
    # unit_setter.set_units("IN", rescale=True)
    # unit_setter.set_units("FT", rescale=True)
    # unit_setter.set_units("M", rescale=True)
```

# End of Settings\Set Scene Unit.py

## Set Scene Unit_CM.py
<a name="settings-set-scene-unit_cm"></a>
# AUTHOR LUX DT ChatGPT4
# VERSION 0.1.0
# Script that setSceneUnit (lux.UNIT_CM)
```python
import lux

def set_scene_units():
    """Set global scene units to centimeters."""
    lux.setSceneUnit(lux.UNIT_CM)
    print("Scene units set to centimeters.")

if __name__ == "__main__":
    set_scene_units()
```

# End of Settings\Set Scene Unit_CM.py

## Apply Ground Transformations.py
<a name="transform-apply-ground-transformations"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to Translate ground.
```python
import lux
import luxmath

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
            # Create translation and rotation matrices
            translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)
            rotation_matrix = luxmath.Matrix.makeRotate(luxmath.Vector(0, 0, 0), rotation_degrees)
            
            # Combine translation and rotation matrices
            transform_matrix = translation_matrix.mul(rotation_matrix)
            
            # Apply the combined transformation to the part
            part_node.applyTransform(transform_matrix, absolute=False)
            print(f"Transformation applied to {part_node.getName()}.")
        except AttributeError:
            print(f"{part_node.getName()} cannot be transformed.")

def position_case_model():
    """
    Position the "Case" model with a hardcoded translation and rotation.
    """
    part_name = "Ground"  # Replace with the actual name of your part
    translation_vector = luxmath.Vector(-30, 30.5, 78)
    rotation_degrees = 0  # Rotate 0 degrees

    position_part(part_name, translation_vector, rotation_degrees)

def main():
    position_case_model()

if __name__ == "__main__":
    main()
```

# End of Transform\Apply Ground Transformations.py

## Select Group by Name and Translate Rotate Scale.py
<a name="transform-select-group-by-name-and-translate-rotate-scale"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Example: Select Group by Name, Translate, Rotate Z -90, Scale by a factor of 2, and apply on a Model
```python
import lux
import luxmath

def get_user_input():
    """
    Display a dialog for the user to input the name of the group.
    """
    default_group_name = "Enter group name here"
    values = [("group_name", lux.DIALOG_TEXT, "Enter the group name:", default_group_name)]
    opts = lux.getInputDialog(title="Input Group Name", desc="Enter the name of the group to position", values=values)
    return opts

def move_rotate_scale_group(group_name, distance, scale_factor):
    """
    Move the group down along the Y-axis by a specified distance, rotate it -90 degrees along the Z-axis, and scale by a given factor.
    """
    scene_root = lux.getSceneTree()
    group_nodes = scene_root.find(group_name, types=[lux.NODE_TYPE_GROUP])

    if not group_nodes:
        print(f"Group {group_name} not found.")
        return

    for group_node in group_nodes:
        print(f"Found group node: {group_node.getName()}")

        # Translation
        translation_vector = luxmath.Vector(0, -distance, 0)
        translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)

        # Rotation
        rotation_axis = luxmath.Vector(0, 0, 1)  # Z-axis
        rotation_angle = -90  # Angle in degrees
        rotation_matrix = luxmath.Matrix().makeIdentity().rotateAroundAxis(rotation_axis, rotation_angle)

        # Scaling
        scale_matrix = luxmath.Matrix().makeIdentity().scale(luxmath.Vector(scale_factor, scale_factor, scale_factor))

        # Combining transformations
        combined_transform = translation_matrix.mul(rotation_matrix).mul(scale_matrix)

        group_node.applyTransform(combined_transform, absolute=False)

# Main script
user_input = get_user_input()
if user_input and "group_name" in user_input and user_input["group_name"] != "Enter group name here":
    selected_group = user_input["group_name"]
    print(f"Moving, rotating, and scaling group '{selected_group}' down by 2 units along the Y-axis, rotating -90 degrees along the Z-axis, and scaling by a factor of 2.")
    move_rotate_scale_group(selected_group, 2, 2)
else:
    print("Operation cancelled or invalid input.")
```

# End of Transform\Select Group by Name and Translate Rotate Scale.py

## Select Model by Name and Translate Rotate Scale.py
<a name="transform-select-model-by-name-and-translate-rotate-scale"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Example: Select Model by Name, Translate, Rotate Z -90, Scale by a factor of 2, and apply on a Model
```python
import lux
import luxmath

def get_user_input():
    """
    Display a dialog for the user to input the name of the model.
    """
    default_model_name = "Enter model name here"
    values = [("model_name", lux.DIALOG_TEXT, "Enter the model name:", default_model_name)]
    opts = lux.getInputDialog(title="Input Model Name", desc="Enter the name of the model to position", values=values)
    return opts

def move_rotate_scale_model(model_name, distance, scale_factor):
    """
    Move the model down along the Y-axis by a specified distance, rotate it -90 degrees along the Z-axis, and scale by a given factor.
    """
    scene_root = lux.getSceneTree()
    model_nodes = scene_root.find(model_name, types=[lux.NODE_TYPE_OBJECT])

    if not model_nodes:
        print(f"Model {model_name} not found.")
        return

    for model_node in model_nodes:
        print(f"Found model node: {model_node.getName()}")

        # Translation
        translation_vector = luxmath.Vector(0, -distance, 0)
        translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)

        # Rotation
        rotation_axis = luxmath.Vector(0, 0, 1)  # Z-axis
        rotation_angle = -90  # Angle in degrees
        rotation_matrix = luxmath.Matrix().makeIdentity().rotateAroundAxis(rotation_axis, rotation_angle)

        # Scaling
        scale_matrix = luxmath.Matrix().makeIdentity().scale(luxmath.Vector(scale_factor, scale_factor, scale_factor))

        # Combining transformations
        combined_transform = translation_matrix.mul(rotation_matrix).mul(scale_matrix)

        model_node.applyTransform(combined_transform, absolute=False)

# Main script
user_input = get_user_input()
if user_input and "model_name" in user_input and user_input["model_name"] != "Enter model name here":
    selected_model = user_input["model_name"]
    print(f"Moving, rotating, and scaling model '{selected_model}' down by 2 units along the Y-axis, rotating -90 degrees along the Z-axis, and scaling by a factor of 2.")
    move_rotate_scale_model(selected_model, 2, 2)
else:
    print("Operation cancelled or invalid input.")
```

# End of Transform\Select Model by Name and Translate Rotate Scale.py

## Select by Name and Translate and Rotate.py
<a name="transform-select-by-name-and-translate-and-rotate"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example: Select by Name and Translate and Rotate Z -90
```python
import lux
import luxmath

def get_user_input():
    """
    Display a dialog for the user to input the name of the group.
    """
    default_group_name = "Enter group name here"
    values = [("group_name", lux.DIALOG_TEXT, "Enter the group name:", default_group_name)]
    opts = lux.getInputDialog(title="Input Group Name", desc="Enter the name of the group to position", values=values)
    return opts

def move_and_rotate_group(group_name, distance):
    """
    Move the group down along the Y-axis by a specified distance and rotate it -90 degrees along the Z-axis.
    """
    scene_root = lux.getSceneTree()
    group_nodes = scene_root.find(group_name, types=[lux.NODE_TYPE_GROUP])

    if not group_nodes:
        print(f"Group {group_name} not found.")
        return

    for group_node in group_nodes:
        print(f"Found group node: {group_node.getName()}")

        # Translation
        translation_vector = luxmath.Vector(0, -distance, 0)
        translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)

        # Rotation
        rotation_axis = luxmath.Vector(0, 0, 1)  # Z-axis
        rotation_angle = -90  # Angle in degrees

        # Correct usage of rotateAroundAxis method
        rotation_matrix = luxmath.Matrix().makeIdentity().rotateAroundAxis(rotation_axis, rotation_angle)

        # Correctly combine translation and rotation
        combined_transform = translation_matrix.mul(rotation_matrix)

        group_node.applyTransform(combined_transform, absolute=False)

# Main script
user_input = get_user_input()
if user_input and "group_name" in user_input and user_input["group_name"] != "Enter group name here":
    selected_group = user_input["group_name"]
    print(f"Moving and rotating group '{selected_group}' down by 2 units along the Y-axis and rotating -90 degrees along the Z-axis.")
    move_and_rotate_group(selected_group, 2)
else:
    print("Operation cancelled or invalid input.")
```

# End of Transform\Select by Name and Translate and Rotate.py

## Transform Model and Export.py
<a name="transform-transform-model-and-export"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script that transforms model before exporting it in 2 file formats OBJ and GLB. 
```python
import lux
import luxmath
import os

def apply_transformations_to_all_models(distance, scale_factor):
    """
    Apply translation, rotation, and scaling transformations to all models in the scene.
    """
    scene_root = lux.getSceneTree()
    model_nodes = scene_root.find("", types=[lux.NODE_TYPE_MODEL])

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

def export_transformed_models(directory, formats=['.obj', '.glb']):
    """
    Export all transformed models in the scene to specified formats.
    """
    scene_root = lux.getSceneTree()
    model_nodes = scene_root.find("", types=[lux.NODE_TYPE_MODEL])

    for model_node in model_nodes:
        for export_format in formats:
            export_path = os.path.join(directory, model_node.getName() + export_format)
            print(f"Exporting model node: {model_node.getName()} to {export_path}")
            lux.exportFile(export_path, format=lux.EXPORT_OBJ if export_format == '.obj' else lux.EXPORT_GLTF)

# Specify the directory where to export the transformed models
directory = r"C:/GLB_OBJ"

# Apply transformations to all models in the scene
apply_transformations_to_all_models(2, 2)

# Export transformed models to OBJ and GLB formats
export_transformed_models(directory)

print("Transforming and exporting complete.")
```

# End of Transform\Transform Model and Export.py

## Translate Part By Name.py
<a name="transform-translate-part-by-name"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Translate Part By Name
```python
import lux
import luxmath

def get_user_input():
    """
    Display a dialog for the user to input the name of the group.
    """
    default_group_name = "Enter group name here"
    values = [("group_name", lux.DIALOG_TEXT, "Enter the group name:", default_group_name)]
    opts = lux.getInputDialog(title="Input Group Name", desc="Enter the name of the group to position", values=values)
    return opts

def move_group_down_y(group_name, distance):
    """
    Move the group down along the Y-axis by a specified distance.
    """
    scene_root = lux.getSceneTree()
    group_nodes = scene_root.find(group_name, types=[lux.NODE_TYPE_GROUP])

    if not group_nodes:
        print(f"Group {group_name} not found.")
        return

    for group_node in group_nodes:
        print(f"Found group node: {group_node.getName()}")
        translation_vector = luxmath.Vector(0, -distance, 0)
        translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)
        group_node.applyTransform(translation_matrix, absolute=False)

# Main script
user_input = get_user_input()

if user_input and "group_name" in user_input and user_input["group_name"] != "Enter group name here":
    selected_group = user_input["group_name"]
    print(f"Moving group '{selected_group}' down by 2 units along the Y-axis.")
    move_group_down_y(selected_group, 2)
else:
    print("Operation cancelled or invalid input.")
```

# End of Transform\Translate Part By Name.py

## Translate and Rotate a Part.py
<a name="transform-translate-and-rotate-a-part"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to Translate and Rotate a Product.
```python
import lux
import luxmath

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
            # Create translation and rotation matrices
            translation_matrix = luxmath.Matrix.makeTranslate(translation_vector)
            rotation_matrix = luxmath.Matrix.makeRotate(luxmath.Vector(0, 0, 0), rotation_degrees)
            
            # Combine translation and rotation matrices
            transform_matrix = translation_matrix.mul(rotation_matrix)
            
            # Apply the combined transformation to the part
            part_node.applyTransform(transform_matrix, absolute=False)
            print(f"Transformation applied to {part_node.getName()}.")
        except AttributeError:
            print(f"{part_node.getName()} cannot be transformed.")

def position_case_model():
    """
    Position the "Product" model with a hardcoded translation and rotation.
    """
    part_name = "Product"  # Replace with the actual name of your part
    translation_vector = luxmath.Vector(0, 100, 0)
    rotation_degrees = 0  # Rotate 0 degrees

    position_part(part_name, translation_vector, rotation_degrees)

def main():
    position_case_model()

if __name__ == "__main__":
    main()
```

# End of Transform\Translate and Rotate a Part.py

