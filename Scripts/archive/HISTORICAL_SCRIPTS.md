# Historical script archive — NOT agent knowledge

**Status:** unreviewed historical collection. Do not treat as current API.

- Source: prior KeyShot Python script notes (mixed 2023–2024 era).
- Heavily duplicated. Many scripts are variants of the same idea.
- Contains calls that are not in the 2026.2 dump. Verify every symbol before reuse.
- API source of truth remains `lux/KeyShot_lux_API.md` (2026.2 `help(lux)`).
- Maintained examples live in `Scripts/examples/`.

Use this only to recover a pattern, then verify every call against the 2026.2 dump before reuse.

---

# Table of Contents

1. [Animation\Animation Batch Rendering Frame Padding.py](#animation-animation-batch-rendering-frame-padding)
2. [Animation\Animation Encode Video with Padding.py](#animation-animation-encode-video-with-padding)
3. [Animation\Animation Frame Padding Agnostic.py](#animation-animation-frame-padding-agnostic)
4. [Animation\Animation Rendered Image Sequence Padding Agnostic.py](#animation-animation-rendered-image-sequence-padding-agnostic)
5. [Automation\Animation Pad Frames.py](#automation-animation-pad-frames)
6. [Automation\Batch Import Queue XR .py](#automation-batch-import-queue-xr-)
7. [Automation\Create Camera Extract xmp Camera Data.py](#automation-create-camera-extract-xmp-camera-data)
8. [Automation\Create Cameras Additional Functions Example.py](#automation-create-cameras-additional-functions-example)
9. [Automation\Create Cameras Template.py](#automation-create-cameras-template)
10. [Automation\Create Configured Cameras Template.py](#automation-create-configured-cameras-template)
11. [Automation\Create Custom Cameras From XMP.py](#automation-create-custom-cameras-from-xmp)
12. [Automation\Create Standard Scene Example.py](#automation-create-standard-scene-example)
13. [Automation\Create Standard Views and Perspective Beauty Camera.py](#automation-create-standard-views-and-perspective-beauty-camera)
14. [Automation\Create Standard Views and Perspective Camera with ModelSets.py](#automation-create-standard-views-and-perspective-camera-with-modelsets)
15. [Automation\Create Standard Views and Perspective Camera.py](#automation-create-standard-views-and-perspective-camera)
16. [Automation\Create Standard Views and Perspective Cameras.py](#automation-create-standard-views-and-perspective-cameras)
17. [Automation\Create Standard Views and Perspective Cameras_Distance_50Units.py](#automation-create-standard-views-and-perspective-cameras_distance_50units)
18. [Automation\Create Standard Views and Perspective Cameras_Distance_5Units.py](#automation-create-standard-views-and-perspective-cameras_distance_5units)
19. [Automation\Create a Perspective Camera.py](#automation-create-a-perspective-camera)
20. [Automation\Create and Configure Studios.py](#automation-create-and-configure-studios)
21. [Automation\Creates Model Set.py](#automation-creates-model-set)
22. [Automation\Delete Unused Nodes.py](#automation-delete-unused-nodes)
23. [GUI\CustomInputDialog_PC.py](#gui-custominputdialog_pc)
24. [GUI\GUI Script Example Doc.py](#gui-gui-script-example-doc)
25. [GUI\Get InputDialog GUI Example.py](#gui-get-inputdialog-gui-example)
26. [ImportExport\Batch Import CAD Model Assign Material Template Name Model Set.py](#importexport-batch-import-cad-model-assign-material-template-name-model-set)
27. [ImportExport\Batch Import CAD Model Assign Material Template.py](#importexport-batch-import-cad-model-assign-material-template)
28. [ImportExport\Batch Import CAD.py](#importexport-batch-import-cad)
29. [ImportExport\Batch Import Multiple CAD File Types.py](#importexport-batch-import-multiple-cad-file-types)
30. [ImportExport\Import CAD.py](#importexport-import-cad)
31. [ImportExport\Import CAD_Prompt.py](#importexport-import-cad_prompt)
32. [ImportExport\Import Scene Template cm into a New Scene.py](#importexport-import-scene-template-cm-into-a-new-scene)
33. [ImportExport\Import Scene Template cm into an Existing Scene.py](#importexport-import-scene-template-cm-into-an-existing-scene)
34. [ImportExport\Import Scene Template cm.py](#importexport-import-scene-template-cm)
35. [ImportExport\Import Scene Template mm.py](#importexport-import-scene-template-mm)
36. [ImportExport\Import Template meters.py](#importexport-import-template-meters)
37. [ImportExport\Import Template mm.py](#importexport-import-template-mm)
38. [ImportExport\Import_GLB_TranslateRotateScale.py](#importexport-import_glb_translaterotatescale)
39. [ImportExport\Import_OBJ_TranslateRotateScale.py](#importexport-import_obj_translaterotatescale)
40. [Information\Get Camera Distance.py](#information-get-camera-distance)
41. [Information\Get MaterialGraph Parameters.py](#information-get-materialgraph-parameters)
42. [Information\Get Metadata.py](#information-get-metadata)
43. [Information\Get Model Sets.py](#information-get-model-sets)
44. [Information\Get Node Type.py](#information-get-node-type)
45. [Information\Get Render Info.py](#information-get-render-info)
46. [Information\Get Resource Library Models 2024.py](#information-get-resource-library-models-2024)
47. [Information\Get Resource Library Path 2024.py](#information-get-resource-library-path-2024)
48. [Information\Get Resource Library Path 2024_v2.py](#information-get-resource-library-path-2024_v2)
49. [Information\Get Resource Library Path.py](#information-get-resource-library-path)
50. [Information\Get Scene Info.py](#information-get-scene-info)
51. [Information\Get Scene Information.py](#information-get-scene-information)
52. [Information\Get Scene Materials.py](#information-get-scene-materials)
53. [Information\Get SceneTree Nodes.py](#information-get-scenetree-nodes)
54. [Information\Get SceneTree.py](#information-get-scenetree)
55. [Information\Get Scenes Material Parameters and Save to File.py](#information-get-scenes-material-parameters-and-save-to-file)
56. [Information\Get_Camera_Info.py](#information-get_camera_info)
57. [Load\Load Enviorment From Library and Apply Settings.py](#load-load-enviorment-from-library-and-apply-settings)
58. [Load\Load Enviorment From Library.py](#load-load-enviorment-from-library)
59. [Load\Load Ground Plane 2024.py](#load-load-ground-plane-2024)
60. [Load\Load Ground Plane.py](#load-load-ground-plane)
61. [Load\Load Library Texture Assign to Diffuse Material Bump Add 2024.py](#load-load-library-texture-assign-to-diffuse-material-bump-add-2024)
62. [Material\Adjust Texture Scale Scene Units 1cm.py](#material-adjust-texture-scale-scene-units-1cm)
63. [Material\Apply 2 Library Textures to Diffuse Material Bump Add.py](#material-apply-2-library-textures-to-diffuse-material-bump-add)
64. [Material\Apply Library Color by Name to Diffuse Material Color.py](#material-apply-library-color-by-name-to-diffuse-material-color)
65. [Material\Apply Library Texture to Diffuse Material Bump Add 2024.py](#material-apply-library-texture-to-diffuse-material-bump-add-2024)
66. [Material\Apply Library Texture to Diffuse Material Bump Add.py](#material-apply-library-texture-to-diffuse-material-bump-add)
67. [Material\Apply Library Texture to Diffuse Material Bump.py](#material-apply-library-texture-to-diffuse-material-bump)
68. [Material\Apply Library Texture to Diffuse Material Color.py](#material-apply-library-texture-to-diffuse-material-color)
69. [Material\Batch Multi-Material Diffuse Sub-Material Assign Texture Default Units m.py](#material-batch-multi-material-diffuse-sub-material-assign-texture-default-units-m)
70. [Material\Batch Multi-Material Diffuse Sub-Material Assign Texture Scale Units cm.py](#material-batch-multi-material-diffuse-sub-material-assign-texture-scale-units-cm)
71. [Material\Batch Save All Scene Materials to KS2024 Material Library Agnostic.py](#material-batch-save-all-scene-materials-to-ks2024-material-library-agnostic)
72. [Material\Batch Save All Scene Materials to Library Agnostic 2024.py](#material-batch-save-all-scene-materials-to-library-agnostic-2024)
73. [Material\Batch Save All Scene Materials to Material Library Agnostic.py](#material-batch-save-all-scene-materials-to-material-library-agnostic)
74. [Material\Batch Save All Scene Materials to Material Library.py](#material-batch-save-all-scene-materials-to-material-library)
75. [Material\Batch Save Multi-Material Sub-Materials to KS2024 Material Library Agnostic.py](#material-batch-save-multi-material-sub-materials-to-ks2024-material-library-agnostic)
76. [Material\Batch Save Multi-Material Sub-Materials to Material Library Agnostic.py](#material-batch-save-multi-material-sub-materials-to-material-library-agnostic)
77. [Material\Change IES Light Color and File Agnostic.py](#material-change-ies-light-color-and-file-agnostic)
78. [Material\Color Gradient ShaderEdge Cube Material Color Connect.py](#material-color-gradient-shaderedge-cube-material-color-connect)
79. [Material\Color Gradient ShaderEdge Diffuse Material Color Connect.py](#material-color-gradient-shaderedge-diffuse-material-color-connect)
80. [Material\Create Python Material Output Script.py](#material-create-python-material-output-script)
81. [Material\Delete Unused Nodes in Material Graph.py](#material-delete-unused-nodes-in-material-graph)
82. [Material\Delete Unused Shader Nodes.py](#material-delete-unused-shader-nodes)
83. [Material\Delete Unused Shader and Material Graph Nodes.py](#material-delete-unused-shader-and-material-graph-nodes)
84. [Material\Material Diffuse Color Apply Texture Example Agnostic.py](#material-material-diffuse-color-apply-texture-example-agnostic)
85. [Material\Material Diffuse Color Apply Texture Example.py](#material-material-diffuse-color-apply-texture-example)
86. [Material\Material Diffuse Color Change Example.py](#material-material-diffuse-color-change-example)
87. [Material\Material Diffuse Color Texture Example.py](#material-material-diffuse-color-texture-example)
88. [Material\Material IES Light Color and File Change 2024.py](#material-material-ies-light-color-and-file-change-2024)
89. [Material\Material IES Light Color and File Change.py](#material-material-ies-light-color-and-file-change)
90. [Material\Material Color Gradient ShaderEdge Diffuse Material Color Connect.py](#material-color-gradient-shaderedge-diffuse-material-color-connect)
91. [Material\Material Gradient View Direction.py](#material-color-gradient-view-direction)
92. [Material\Material Physical Light Color Change.py](#material-material-physical-light-color-change)
93. [Material\Saves All Materials to the Library.py](#material-saves-all-materials-to-the-library)
94. [Material\ShaderEdge Connect.py](#material-shaderedge-connect)
95. [Material\Batch Create Multi-Material Sub-Materials with Custom Advanced Shader Parameters.py](#material-batch-create-multi-material-sub-materials-with-custom-advanced-shader-parameters)
96. [Model\Delete Model Set by Name.py](#model-delete-model-set-by-name)
97. [Model\Hide All Model Set Children.py](#model-hide-all-model-set-children)
98. [Model\Hide All Model Sets Children.py](#model-hide-all-model-sets-children)
99. [Model\Hide All Model Sets and Children.py](#model-hide-all-model-sets-and-children)
100. [Model\Hide and Show Model Sets.py](#model-hide-and-show-model-sets)
101. [Model\Hides Node by Name.py](#model-hides-node-by-name)
102. [Model\Model Set Remove Default .py](#model-model-set-remove-default-)
103. [Model\Model Set Renamer.py](#model-model-set-renamer)
104. [Model\Model Translate and Rotate Example.py](#model-model-translate-and-rotate-example)
105. [Model\New Model Set Template.py](#model-new-model-set-template)
106. [Model\Product Model Sets.py](#model-product-model-sets)
107. [Model\Show All Model Sets Children.py](#model-show-all-model-sets-children)
108. [Model\Show All Model Sets.py](#model-show-all-model-sets)
109. [Model\Show Model Set.py](#model-show-model-set)
110. [Model\Transform Model Sets.py](#model-transform-model-sets)
111. [Naming\Batch Rename Find Replace GUI.py](#naming-batch-rename-find-replace-gui)
112. [Naming\Batch Rename Material Clashing Node Names.py](#naming-batch-rename-material-clashing-node-names)
113. [Naming\Batch Rename Model Sets.py](#naming-batch-rename-model-sets)
114. [Naming\Batch Rename Rhino CAD.py](#naming-batch-rename-rhino-cad)
115. [Naming\Batch Rename Rhino Clashing Node Names Remove Underscores Colons.py](#naming-batch-rename-rhino-clashing-node-names-remove-underscores-colons)
116. [Naming\Rename Clashing Node Names.py](#naming-rename-clashing-node-names)
117. [Naming\Rename Model Sets per Imported CAD.py](#naming-rename-model-sets-per-imported-cad)
118. [Naming\Rename ModelSets Manual.py](#naming-rename-modelsets-manual)
119. [Naming\Renames Nodes Parenthesis.py](#naming-renames-nodes-parenthesis)
120. [Render\Add To Queue.py](#render-add-to-queue)
121. [Render\Batch Render Incrmental Screenshots.py](#render-batch-render-incrmental-screenshots)
122. [Render\Queue Render And Name Per Image Style.py](#render-queue-render-and-name-per-image-style)
123. [Render\Queue Render SwapToggle Aspect Ratio.py](#render-queue-render-swaptoggle-aspect-ratio)
124. [Render\Render Images Commented.py](#render-render-images-commented)
125. [Render\Render Optimal Ambient Occlusion Pass.py](#render-render-optimal-ambient-occlusion-pass)
126. [Render\Render SwapToggle Aspect Ratio.py](#render-render-swaptoggle-aspect-ratio)
127. [Render\Screenshot.py](#render-screenshot)
128. [Scripts_Lux\Create Standard Views.py](#scripts_lux-create-standard-views)
129. [Scripts_Lux\Encode Video.py](#scripts_lux-encode-video)
130. [Scripts_Lux\Random Scattering.py](#scripts_lux-random-scattering)
131. [Scripts_Lux\Render Ambient Occlusion.py](#scripts_lux-render-ambient-occlusion)
132. [Scripts_Lux\Render Animation Passes.py](#scripts_lux-render-animation-passes)
133. [Scripts_Lux\Render Images.py](#scripts_lux-render-images)
134. [Scripts_Lux\Render Panoramic Frames.py](#scripts_lux-render-panoramic-frames)
135. [Settings\Lighting Settings.py](#settings-lighting-settings)
136. [Settings\Set Scene Unit.py](#settings-set-scene-unit)
137. [Settings\Set Scene Unit_CM.py](#settings-set-scene-unit_cm)
138. [Transform\Apply Ground Transformations.py](#transform-apply-ground-transformations)
139. [Transform\Select Group by Name and Translate Rotate Scale.py](#transform-select-group-by-name-and-translate-rotate-scale)
140. [Transform\Select Model by Name and Translate Rotate Scale.py](#transform-select-model-by-name-and-translate-rotate-scale)
141. [Transform\Select by Name and Translate and Rotate.py](#transform-select-by-name-and-translate-and-rotate)
142. [Transform\Transform Model and Export.py](#transform-transform-model-and-export)
143. [Transform\Translate Part By Name.py](#transform-translate-part-by-name)
144. [Transform\Translate and Rotate a Part.py](#transform-translate-and-rotate-a-part)

# Color Gradient View Direction.py
<a name="color-gradient-view-direction"></a>

# Animation\Animation Batch Rendering Frame Padding.py
<a name="animation-animation-batch-rendering-frame-padding"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Adds Animation Frame Padding to current scene and renders.
``` python
import lux
import os

def render_padded_frames(start_frame, end_frame, padding_frames, output_folder, file_name, width, height):
    """
    Render frames with specific frames padded (duplicated), saving them in the specified directory.
    """
    for frame in range(start_frame, end_frame + 1):

        # Define the output file path
        output_file_path = os.path.join(output_folder, f"{file_name}_{frame:04d}.png")

        # Check if the current frame is in the padding list
        if frame in padding_frames:
            # Render the frame multiple times based on the padding count
            for _ in range(padding_frames[frame]):
                lux.setAnimationFrame(frame)
                if not lux.renderImage(output_file_path, width, height):
                    print("Rendering cancelled.")
                    return
        else:
            # Render the frame normally
            lux.setAnimationFrame(frame)
            if not lux.renderImage(output_file_path, width, height):
                print("Rendering cancelled.")
                return

def get_user_input():
    """
    Display a GUI to get frame range, resolution, file name, and output folder from the user.
    """
    dialog_fields = [
        ("start_frame", lux.DIALOG_INTEGER, "Start Frame:", 1, (1, 10000)),
        ("end_frame", lux.DIALOG_INTEGER, "End Frame:", 30, (1, 10000)),
        ("width", lux.DIALOG_INTEGER, "Render Width:", 1920, (1, 10000)),
        ("height", lux.DIALOG_INTEGER, "Render Height:", 1080, (1, 10000)),
        ("file_name", lux.DIALOG_TEXT, "File Name Prefix:", "frame"),
        ("output_folder", lux.DIALOG_FOLDER, "Output Folder:", None)
    ]
    user_input = lux.getInputDialog(title="Frame Range and Resolution", 
                                    desc="Enter the start and end frames for rendering, desired resolution, file name prefix, and output folder:",
                                    values=dialog_fields,
                                    id="frame_range_resolution_file_output")
    if user_input:
        return (user_input["start_frame"], user_input["end_frame"],
                user_input["width"], user_input["height"],
                user_input["file_name"], user_input["output_folder"])
    else:
        return None, None, None, None, None, None

def main():
    # Get user input for frame range, resolution, file name, and output folder
    start_frame, end_frame, width, height, file_name, output_folder = get_user_input()
    if start_frame is None or end_frame is None:
        return  # Cancel if no input

    # Example padding frames
    padding_frames = {5: 3, 10: 2}

    render_padded_frames(start_frame, end_frame, padding_frames, output_folder, file_name, width, height)

if __name__ == "__main__":
    main()
```

# End of Animation\Animation Batch Rendering Frame Padding.py

# Animation\Animation Encode Video with Padding.py
<a name="animation-animation-encode-video-with-padding"></a>


# AUTHOR LUX DT ChatGPT
# VERSION 0.4.1
# HEADLESS COMPLIANT
# Encodes video from separate frame range, now supporting padded frame numbers.
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

def main():
    opts = {}
    if not lux.isHeadless():
        values = [("folder", lux.DIALOG_FOLDER, "Folder with frames:", None),
                  ("fmt", lux.DIALOG_TEXT, "Frame file format with padding (e.g., frame.%04d.jpg):", "frame.%04d.jpg"),
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
        opts["fmt"] = inputText("Frame file format with padding (e.g., frame.%04d.jpg):", "frame.%04d.jpg")
        opts["start"] = inputInt("Start frame:", 1, (1, 4096))
        opts["end"] = inputInt("End frame:", 10, (1, 4096))
        opts["fps"] = inputInt("FPS:", 10, (1, 1024))
        opts["name"] = inputText("Video name:", "video.mp4")
    if not opts: return

    # Validate and prepare inputs
    if opts["folder"] is None or len(opts["folder"]) == 0:
        raise Exception("Folder cannot be empty!")
    fld = opts["folder"]

    files = opts["fmt"]
    if len(files) == 0 or "%d" not in files:
        raise Exception("Frame format must contain a digit placeholder like '%04d' for padding!")
    # Modify the regex to accommodate padded numbers based on the user's input format
    reDigits = re.compile(re.escape(files).replace("\\%04d", r"(0\d+|\d+)").replace("\\%d", r"(\d+)"))

    found = False
    for f in os.listdir(fld):
        if reDigits.match(f):
            found = True
            break
    if not found:
        raise Exception(f"Could not find any frames matching the frame format \"{files}\" in \"{fld}\"!")

    start, end, fps = opts["start"], opts["end"], opts["fps"]
    if start > end:
        raise Exception("Start frame cannot be larger than end frame!")

    if len(opts["name"]) == 0:
        raise Exception("Video name cannot be empty!")
    path = os.path.join(fld, opts["name"])
    print(f"Encoding video {path}")
    res = lux.encodeVideo(folder=fld, frameFiles=files, videoName=opts["name"],
                          fps=fps, firstFrame=start, lastFrame=end)
    if not res:
        raise Exception("Failed to encode video!")

main()
```

# End of Animation\Animation Encode Video with Padding.py

# Animation\Animation Frame Padding Agnostic.py
<a name="animation-animation-frame-padding-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to add padding to animation frames in KeyShot and render them.
``` python
import lux  # Import the KeyShot built-in module 'lux'.
import os  # Import the os module for file path operations.

# Function to render frames with padding.
def render_padded_frames(start_frame, end_frame, padding_frames, output_folder, file_name, width, height):
    """
    Render frames with specific frames padded (duplicated), saving them in the specified directory.

    :param start_frame: The starting frame of the animation.
    :param end_frame: The ending frame of the animation.
    :param padding_frames: Dictionary containing frames to be padded and the number of times to pad.
    :param output_folder: Directory to save the rendered frames.
    :param file_name: Prefix for the output file names.
    :param width: Width of the rendered image.
    :param height: Height of the rendered image.
    """
    for frame in range(start_frame, end_frame + 1):
        output_file_path = os.path.join(output_folder, f"{file_name}_{frame:04d}.png")  # Format the output file path.

        # Check if the current frame is in the list of frames to be padded.
        if frame in padding_frames:
            # Render the frame multiple times based on the padding count.
            for _ in range(padding_frames[frame]):
                lux.setAnimationFrame(frame)  # Set the animation frame.
                if not lux.renderImage(output_file_path, width, height):  # Render the frame.
                    print("Rendering cancelled.")
                    return
        else:
            # Render the frame normally if it's not in the padding list.
            lux.setAnimationFrame(frame)
            if not lux.renderImage(output_file_path, width, height):
                print("Rendering cancelled.")
                return

# Function to display a GUI for user input.
def get_user_input():
    """
    Display a GUI to get frame range, resolution, file name, and output folder from the user.
    """
    # Define the fields for the input dialog.
    dialog_fields = [
        ("start_frame", lux.DIALOG_INTEGER, "Start Frame:", 1, (1, 10000)),
        ("end_frame", lux.DIALOG_INTEGER, "End Frame:", 30, (1, 10000)),
        ("width", lux.DIALOG_INTEGER, "Render Width:", 1920, (1, 10000)),
        ("height", lux.DIALOG_INTEGER, "Render Height:", 1080, (1, 10000)),
        ("file_name", lux.DIALOG_TEXT, "File Name Prefix:", "frame"),
        ("output_folder", lux.DIALOG_FOLDER, "Output Folder:", None)
    ]
    # Display the dialog and get the user input.
    user_input = lux.getInputDialog(title="Frame Range and Resolution",
                                    desc="Enter the start and end frames for rendering, desired resolution, file name prefix, and output folder:",
                                    values=dialog_fields,
                                    id="frame_range_resolution_file_output")
    if user_input:
        return user_input["start_frame"], user_input["end_frame"], user_input["width"], user_input["height"], user_input["file_name"], user_input["output_folder"]
    else:
        return None, None, None, None, None, None  # Return None for each field if the user cancels or inputs are invalid.

# Main function where the script execution begins.
def main():
    # Get user input for frame range, resolution, file name, and output folder.
    start_frame, end_frame, width, height, file_name, output_folder = get_user_input()
    if start_frame is None or end_frame is None:
        return  # Exit if no input is provided.

    # Example padding frames: Frame 5 padded 3 times, frame 10 padded 2 times.
    padding_frames = {5: 3, 10: 2}

    # Render the frames with specified padding.
    render_padded_frames(start_frame, end_frame, padding_frames, output_folder, file_name, width, height)

# Check if the script is being run directly (not imported).
if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly.
```

# End of Animation\Animation Frame Padding Agnostic.py

# Animation\Animation Rendered Image Sequence Padding Agnostic.py
<a name="animation-animation-rendered-image-sequence-padding-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script for adding frame padding to individual frame files in a specified folder.
``` python
import os
import re  # Import the regular expressions module for pattern matching.
import lux  # Import the KeyShot built-in module 'lux'.

# Define the input dialog fields for user inputs.
values = [
    ("folder", lux.DIALOG_FOLDER, "Folder with frames:", None),
    ("fmt", lux.DIALOG_TEXT, "Current frame file format (e.g., frame%d.png):", "frame%d.png"),
    ("start", lux.DIALOG_INTEGER, "Start frame:", 1, (1, 4096)),
    ("end", lux.DIALOG_INTEGER, "End frame:", 10, (1, 4096)),
    ("padding", lux.DIALOG_INTEGER, "New frame padding (number of digits):", 5, (1, 10))
]

# Display the input dialog to get options from the user.
opts = lux.getInputDialog(
    title = "Rename Animation Frames",
    desc = "Rename frame files with specified padding.",
    values = values,
    id = "unique_id_for_frame_renaming"  # Unique ID to remember dialog state.
)

# Check if user has provided the inputs.
if opts:
    folder = opts['folder']  # Directory containing frame files.
    fmt = opts['fmt']  # Format of the frame files.
    start_frame = opts['start']  # Starting frame number for renaming.
    end_frame = opts['end']  # Ending frame number for renaming.
    padding = opts['padding']  # Padding to be added to frame numbers.

    # Compile a regular expression pattern to match frame filenames.
    frame_pattern = re.compile(re.escape(fmt).replace("%d", "(\\d+)"))

    # Iterate over files in the specified folder.
    for filename in os.listdir(folder):
        match = frame_pattern.match(filename)
        if match:
            frame_number = int(match.group(1))
            # Rename files within the specified frame range.
            if start_frame <= frame_number <= end_frame:
                new_frame_number = f"{frame_number:0{padding}d}"
                new_filename = frame_pattern.sub(fmt.replace("%d", new_frame_number), filename)
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
                print(f"Renamed {filename} to {new_filename}")
else:
    print("Operation cancelled or invalid input.")  # Notify if operation is cancelled or inputs are invalid.
```

# End of Animation\Animation Rendered Image Sequence Padding Agnostic.py

# Automation\Animation Pad Frames.py
<a name="automation-animation-pad-frames"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# This script will open a GUI which will allow you to add frame padding to individual frames.
``` python
import os
import re
import lux

# Define the values for the input dialog
values = [
    ("folder", lux.DIALOG_FOLDER, "Folder with frames:", None),
    ("fmt", lux.DIALOG_TEXT, "Current frame file format (e.g., frame%d.png):", "frame%d.png"),
    ("start", lux.DIALOG_INTEGER, "Start frame:", 1, (1, 4096)),
    ("end", lux.DIALOG_INTEGER, "End frame:", 10, (1, 4096)),
    ("padding", lux.DIALOG_INTEGER, "New frame padding (number of digits):", 5, (1, 10))
]

# Show the input dialog and get options
opts = lux.getInputDialog(
    title = "Rename Animation Frames",
    desc = "Rename frame files with specified padding.",
    values = values,
    id = "unique_id_for_frame_renaming"
)

# Check if user provided the inputs
if opts:
    folder = opts['folder']
    fmt = opts['fmt']
    start_frame = opts['start']
    end_frame = opts['end']
    padding = opts['padding']

    frame_pattern = re.compile(re.escape(fmt).replace("%d", "(\\d+)"))

    for filename in os.listdir(folder):
        match = frame_pattern.match(filename)
        if match:
            frame_number = int(match.group(1))
            if start_frame <= frame_number <= end_frame:
                new_frame_number = f"{frame_number:0{padding}d}"
                new_filename = frame_pattern.sub(fmt.replace("%d", new_frame_number), filename)
                os.rename(os.path.join(folder, filename), os.path.join(folder, new_filename))
                print(f"Renamed {filename} to {new_filename}")
else:
    print("Operation cancelled or invalid input.")
```

# End of Automation\Animation Pad Frames.py

# Automation\Batch Import Queue XR .py
<a name="automation-batch-import-queue-xr-"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Batch Import KSP files and queue for XR.
``` python
import os
import lux

def main():
    # GUI to select the directory containing KSP files
    opts = lux.getInputDialog(title="Select Directory",
                              desc="Select the directory that contains the KSP files",
                              values=[("folder", lux.DIALOG_FOLDER, "Folder path:", None)],
                              id="select_ksp_folder")

    if opts is None or "folder" not in opts or not opts["folder"]:
        print("No folder selected or dialog cancelled.")
        return

    folder_path = opts["folder"]
    ksp_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.ksp')]

    # Import each KSP file and queue for rendering using XR renderer
    for ksp_file in ksp_files:
        print(f"Importing {ksp_file}")
        lux.importFile(ksp_file)

        # Create Front View Camera
        lux.newCamera("FrontView")
        lux.setStandardView(lux.VIEW_FRONT)
        lux.saveCamera()

        # Set up XR render options
        render_options = lux.getRenderOptions()
        render_options.setAdvancedRendering(16)  # Set samples count, adjust as needed
        #render_options.setMaxTimeRendering(600)   # Max time in seconds, adjust as needed
        render_options.setRayBounces(16)          # Number of ray bounces, adjust as needed
        render_options.setAddToQueue(True)        # Add to the internal KeyShot queue

        # Set up XR render
        print(f"Setting up XR rendering for {ksp_file}")
        lux.renderXR(folder="/path/to/output", name=os.path.splitext(os.path.basename(ksp_file))[0],
                     type=lux.XR_TYPE_SPHERICAL, width=800, height=800, opts=render_options)

    # Process the render queue
    #lux.processQueue()

if __name__ == "__main__":
    main()
```


# End of Automation\Batch Import Queue XR .py

# Automation\Create Camera Extract xmp Camera Data.py
<a name="automation-create-camera-extract-xmp-camera-data"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Recreate Cameras via XMP File
``` python
import lux
import os
import re

def select_xmp_file():
    values = [("file_path", lux.DIALOG_FILE, "Select XMP file:", "*.xmp", "XMP files (*.xmp)")]
    opts = lux.getInputDialog(title="Select Metadata File", desc="Select an XMP metadata file.", values=values)
    return opts["file_path"] if opts and "file_path" in opts else None

def parse_xmp_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    camera_settings = {
        'azimuth': float(re.search(r'<keyshot:Azimuth>([\d.-]+)</keyshot:Azimuth>', content).group(1)),
        'distance': float(re.search(r'<keyshot:Distance>([\d.-]+)</keyshot:Distance>', content).group(1)),
        'inclination': float(re.search(r'<keyshot:Inclination>([\d.-]+)</keyshot:Inclination>', content).group(1)),
        'look_at': (
            float(re.search(r'<keyshot:x>([\d.-]+)</keyshot:x>', content).group(1)),
            float(re.search(r'<keyshot:y>([\d.-]+)</keyshot:y>', content).group(1)),
            float(re.search(r'<keyshot:z>([\d.-]+)</keyshot:z>', content).group(1))
        ),
        'camera_type': re.search(r'<keyshot:Type>([^<]+)</keyshot:Type>', content).group(1),
    }
    return camera_settings

def apply_camera_settings(settings, camera_name):
    lux.newCamera(camera_name)
    lux.setCamera(camera_name)  # Ensure it's the active camera
    set_camera_type(settings['camera_type'])
    lux.setSphericalCamera(azimuth=settings['azimuth'], incl=settings['inclination'], twist=0)
    lux.setCameraLookAt(pt=settings['look_at'])
    if settings['camera_type'] != "Shift Camera":
        lux.setCameraDistance(dist=settings['distance'])
    lux.saveCamera()

def set_camera_type(camera_type):
    if camera_type == "Perspective Camera":
        lux.setCameraPerspective()
    elif camera_type == "Orthographic Camera":
        lux.setCameraOrthographic()
    elif camera_type == "Shift Camera":
        lux.setCameraShift()  # Set default shift values; adjust if necessary

def main():
    file_path = select_xmp_file()
    if file_path:
        camera_name = os.path.splitext(os.path.basename(file_path))[0]
        settings = parse_xmp_file(file_path)
        if settings:
            apply_camera_settings(settings, camera_name)
            print(f"Camera '{camera_name}' created and configured based on XMP data.")
        else:
            print("Failed to extract camera settings from the XMP file.")
    else:
        print("No XMP file selected.")

main()
```

# End of Automation\Create Camera Extract xmp Camera Data.py

# Automation\Create Cameras Additional Functions Example.py
<a name="automation-create-cameras-additional-functions-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Template creates cameras with specific parameters.
``` python
import lux

def create_and_setup_camera(name, azimuth, distance, inclination):
    """
    Creates a new camera in KeyShot or updates an existing one, and sets it up with the given parameters.
    Assumes the distance is already in centimeters.
    """
    # Get the list of existing camera names
    existing_cameras = [cam for cam in lux.getCameras()]

    # Check if camera already exists
    if name in existing_cameras:
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)

    # Set spherical camera settings (azimuth, inclination, twist)
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)

    # Convert distance to float and set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))

    # Save the camera settings
    lux.saveCamera()

    # Additional camera settings can be set here using other lux functions
    # ...

def set_camera_field_of_view(fov):
    """
    Sets the field of view for the active camera.
    :param fov: Field of view in degrees.
    """
    lux.setCameraFieldOfView(fov)

def set_camera_focal_length(focal_length):
    """
    Sets the focal length for the active camera.
    :param focal_length: Focal length in millimeters.
    """
    lux.setCameraFocalLength(focal_length)

# Camera data with specified field of view and focal lengths
camera_settings = {
    "RearFacing": {"fov": 10.286, "focal_length": 200},
    "FrontFacing": {"fov": 10.286, "focal_length": 200},
    "FrontRightFacing": {"fov": 24, "focal_length": 84.683},
    "RearRightFacing": {"fov": 24, "focal_length": 84.683}
}

# Camera data with azimuth and distance values
camera_data = [
    {"name": "FrontFacing", "azimuth": -90.000, "distance": 885.390, "inclination": -0.000},
    {"name": "FrontRightFacing", "azimuth": -45.000, "distance": 375.466, "inclination": -10.000},
    {"name": "RearFacing", "azimuth": 90.000, "distance": 909.570, "inclination": -0.000},
    {"name": "RearRightFacing", "azimuth": 135.000, "distance": 375.467, "inclination": -10.000}
]

# Creating and setting up cameras in KeyShot
for cam in camera_data:
    create_and_setup_camera(cam["name"], cam["azimuth"], cam["distance"], cam["inclination"])

    # Set the field of view and focal length for each camera
    settings = camera_settings.get(cam["name"], {})
    if settings:
        set_camera_field_of_view(settings["fov"])
        set_camera_focal_length(settings["focal_length"])
        lux.saveCamera()

# If KeyShot requires manual saving of the scene, add the save function here
# lux.saveScene()  # Example, replace with actual function if required
```


# End of Automation\Create Cameras Additional Functions Example.py

# Automation\Create Cameras Template.py
<a name="automation-create-cameras-template"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script for creating and setting up cameras with specific parameters in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

# Function to create a new camera or update an existing one with specified settings.
def create_and_setup_camera(name, azimuth, distance, inclination):
    """
    Creates a new camera in KeyShot or updates an existing one, and sets it up with the given parameters.
    Assumes the distance is already in centimeters.

    :param name: Name of the camera.
    :param azimuth: Azimuth angle in degrees.
    :param distance: Distance from camera to pivot/look-at point in centimeters.
    :param inclination: Inclination angle in degrees.
    """
    existing_cameras = [cam for cam in lux.getCameras()]  # Get the list of existing camera names.

    if name in existing_cameras:
        lux.setCamera(name)  # Activate the existing camera.
    else:
        lux.newCamera(name)  # Create a new camera if it does not exist.

    # Set spherical camera settings: azimuth, inclination, and twist angle.
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)
    lux.setCameraDistance(dist=float(distance))  # Set the camera distance.
    lux.saveCamera()  # Save the camera settings.

    # Additional camera settings can be added here if required.

# Functions to set camera field of view and focal length.
def set_camera_field_of_view(fov):
    """
    Sets the field of view for the active camera.

    :param fov: Field of view in degrees.
    """
    lux.setCameraFieldOfView(fov)  # Set the field of view.

def set_camera_focal_length(focal_length):
    """
    Sets the focal length for the active camera.

    :param focal_length: Focal length in millimeters.
    """
    lux.setCameraFocalLength(focal_length)  # Set the focal length.

# Define settings for different cameras.
camera_settings = {
    "RearFacing": {"fov": 10.286, "focal_length": 200},
    "FrontFacing": {"fov": 10.286, "focal_length": 200},
    "FrontRightFacing": {"fov": 24, "focal_length": 84.683},
    "RearRightFacing": {"fov": 24, "focal_length": 84.683}
}

# Data for camera creation, including azimuth, distance, and inclination.
camera_data = [
    {"name": "FrontFacing", "azimuth": -90.000, "distance": 885.390, "inclination": -0.000},
    {"name": "FrontRightFacing", "azimuth": -45.000, "distance": 375.466, "inclination": -10.000},
    {"name": "RearFacing", "azimuth": 90.000, "distance": 909.570, "inclination": -0.000},
    {"name": "RearRightFacing", "azimuth": 135.000, "distance": 375.467, "inclination": -10.000}
]

# Loop to create and configure each camera based on the data provided.
for cam in camera_data:
    create_and_setup_camera(cam["name"], cam["azimuth"], cam["distance"], cam["inclination"])

    settings = camera_settings.get(cam["name"], {})
    if settings:
        set_camera_field_of_view(settings["fov"])  # Set field of view.
        set_camera_focal_length(settings["focal_length"])  # Set focal length.
        lux.saveCamera()  # Save camera settings.

# Save the KeyShot scene if required.
# lux.saveScene()  # Uncomment and modify if necessary to save the scene.
```

# End of Automation\Create Cameras Template.py

# Automation\Create Configured Cameras Template.py
<a name="automation-create-configured-cameras-template"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Template creates cameras with specific parameters.
``` python
import lux

def create_and_setup_camera(name, azimuth, distance, inclination):
    """
    Creates a new camera in KeyShot or updates an existing one, and sets it up with the given parameters.
    Assumes the distance is already in centimeters.
    """
    # Get the list of existing camera names
    existing_cameras = [cam for cam in lux.getCameras()]

    # Check if camera already exists
    if name in existing_cameras:
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)

    # Set spherical camera settings (azimuth, inclination, twist)
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)

    # Convert distance to float and set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))

    # Save the camera settings
    lux.saveCamera()

    # Additional camera settings can be set here using other lux functions
    # ...

def set_camera_field_of_view(fov):
    """
    Sets the field of view for the active camera.
    :param fov: Field of view in degrees.
    """
    lux.setCameraFieldOfView(fov)

def set_camera_focal_length(focal_length):
    """
    Sets the focal length for the active camera.
    :param focal_length: Focal length in millimeters.
    """
    lux.setCameraFocalLength(focal_length)

# Camera data with specified field of view and focal lengths
camera_settings = {
    "RearFacing": {"fov": 10.286, "focal_length": 200},
    "FrontFacing": {"fov": 10.286, "focal_length": 200},
    "FrontRightFacing": {"fov": 24, "focal_length": 84.683},
    "RearRightFacing": {"fov": 24, "focal_length": 84.683}
}

# Camera data with azimuth and distance values
camera_data = [
    {"name": "FrontFacing", "azimuth": -90.000, "distance": 4, "inclination": -0.000},
    {"name": "FrontRightFacing", "azimuth": -45.000, "distance": 4, "inclination": -10.000},
    {"name": "RearFacing", "azimuth": 90.000, "distance": 4, "inclination": -0.000},
    {"name": "RearRightFacing", "azimuth": 135.000, "distance": 4, "inclination": -10.000}
]

# Creating and setting up cameras in KeyShot
for cam in camera_data:
    create_and_setup_camera(cam["name"], cam["azimuth"], cam["distance"], cam["inclination"])

    # Set the field of view and focal length for each camera
    settings = camera_settings.get(cam["name"], {})
    if settings:
        set_camera_field_of_view(settings["fov"])
        set_camera_focal_length(settings["focal_length"])
        lux.saveCamera()

# If KeyShot requires manual saving of the scene, add the save function here
# lux.saveScene()  # Example, replace with actual function if required
```

# End of Automation\Create Configured Cameras Template.py

# Automation\Create Custom Cameras From XMP.py
<a name="automation-create-custom-cameras-from-xmp"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script uses camera metadata from obtained from an .xmp file to recreate the cameras.
``` python
import lux

def create_and_setup_camera(name, azimuth, distance, inclination):
    """
    Creates a new camera in KeyShot or updates an existing one, and sets it up with the given parameters.
    Assumes the distance is already in centimeters.
    """
    # Get the list of existing camera names
    existing_cameras = [cam for cam in lux.getCameras()]

    # Check if camera already exists
    if name in existing_cameras:
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)

    # Set spherical camera settings (azimuth, inclination, twist)
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)

    # Convert distance to float and set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))

    # Save the camera settings
    lux.saveCamera()

    # Additional camera settings can be set here using other lux functions
    # ...

def set_camera_field_of_view(fov):
    """
    Sets the field of view for the active camera.
    :param fov: Field of view in degrees.
    """
    lux.setCameraFieldOfView(fov)

def set_camera_focal_length(focal_length):
    """
    Sets the focal length for the active camera.
    :param focal_length: Focal length in millimeters.
    """
    lux.setCameraFocalLength(focal_length)

# Camera data with specified field of view and focal lengths
camera_settings = {
    "RearFacing": {"fov": 10.286, "focal_length": 200},
    "FrontFacing": {"fov": 10.286, "focal_length": 200},
    "FrontRightFacing": {"fov": 24, "focal_length": 84.683},
    "RearRightFacing": {"fov": 24, "focal_length": 84.683}
}

# Camera data with azimuth and distance values
camera_data = [
    {"name": "FrontFacing", "azimuth": -90.000, "distance": 885.390, "inclination": -0.000},
    {"name": "FrontRightFacing", "azimuth": -45.000, "distance": 375.466, "inclination": -10.000},
    {"name": "RearFacing", "azimuth": 90.000, "distance": 909.570, "inclination": -0.000},
    {"name": "RearRightFacing", "azimuth": 135.000, "distance": 375.467, "inclination": -10.000}
]

# Creating and setting up cameras in KeyShot
for cam in camera_data:
    create_and_setup_camera(cam["name"], cam["azimuth"], cam["distance"], cam["inclination"])

    # Set the field of view and focal length for each camera
    settings = camera_settings.get(cam["name"], {})
    if settings:
        set_camera_field_of_view(settings["fov"])
        set_camera_focal_length(settings["focal_length"])
        lux.saveCamera()

# If KeyShot requires manual saving of the scene, add the save function here
# lux.saveScene()  # Example, replace with actual function if required
```


# End of Automation\Create Custom Cameras From XMP.py

# Automation\Create Standard Scene Example.py
<a name="automation-create-standard-scene-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script template for creating a standard scene in KeyShot with predefined model sets and cameras.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

# Function to create a new model set in the scene.
def create_model_set(name):
    """
    Create a new model set in the KeyShot scene.

    :param name: The name of the model set to be created.
    """
    model_set = lux.newModelSet(name)  # Create a model set with the given name.
    root_node = lux.getSceneTree()  # Retrieve the root node of the scene tree.
    # Additional functionality for manipulating model sets can be added here.

# Function to create a new camera in the scene.
def create_camera(name, position, target):
    """
    Create a new camera in the KeyShot scene.

    :param name: The name of the camera.
    :param position: The position of the camera (not used in current API).
    :param target: The target point of the camera (not used in current API).
    """
    if not lux.newCamera(name):  # Attempt to create the camera with the given name.
        print(f"Failed to create camera: {name}")
    # Note: Positioning and targeting of the camera is not included due to API limitations.

# Main function where the script execution begins.
def main():
    # Create predefined model sets.
    create_model_set('Ground Plane')
    create_model_set('AO')
    create_model_set('AO Shadow')

    # Define camera positions and targets.
    camera_definitions = [
        ('FRONT', (0, 0, 100), (0, 0, 0)),
        ('FRONTRIGHT', (100, 0, 0), (0, 0, 0)),
        ('FRONTLEFT', (-100, 0, 0), (0, 0, 0)),
        ('BACK', (0, 0, -100), (0, 0, 0)),
        # Additional cameras can be added here.
    ]
    
    # Create and configure cameras based on the definitions.
    for name, position, target in camera_definitions:
        create_camera(name, position, target)

# Check if the script is being run directly (not imported).
if __name__ == '__main__':
    main()  # Execute the main function if the script is run directly.
```


# End of Automation\Create Standard Scene Example.py

# Automation\Create Standard Views and Perspective Beauty Camera.py
<a name="automation-create-standard-views-and-perspective-beauty-camera"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.8
# Template creates cameras with specific parameters for standard views and a perspective beauty camera.
``` python
import lux

def create_standard_view_camera(view_constant, name):
    """
    Creates or updates a camera for a standard view.
    """
    # Check if the camera already exists
    existing_cameras = lux.getCameras()
    if name in existing_cameras:
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)
    # Set the view to the predefined standard view
    lux.setStandardView(view=view_constant)
    # Save the camera settings
    lux.saveCamera()
    print("{} camera: {}".format("Updated" if name in existing_cameras else "Created", name))

def create_perspective_beauty_camera(name, azimuth, distance, inclination, fov):
    """
    Creates or updates a perspective beauty camera with spherical settings.
    """
    # Check if the camera already exists
    existing_cameras = lux.getCameras()
    if name in existing_cameras:
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)
    # Set spherical camera settings
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)
    # Set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))
    # Set the field of view
    lux.setCameraFieldOfView(fov)
    # Save the camera settings
    lux.saveCamera()
    print("{} camera: {}".format("Updated" if name in existing_cameras else "Created", name))

# Define the standard views with view constants
standard_views = [
    {"name": "Front", "view_constant": lux.VIEW_FRONT},
    {"name": "Back", "view_constant": lux.VIEW_BACK},
    {"name": "Left", "view_constant": lux.VIEW_LEFT},
    {"name": "Right", "view_constant": lux.VIEW_RIGHT},
    {"name": "Top", "view_constant": lux.VIEW_TOP},
    {"name": "Bottom", "view_constant": lux.VIEW_BOTTOM},
    {"name": "Isometric", "view_constant": lux.VIEW_ISOMETRIC}
]

# Define the camera data for the perspective beauty camera
perspective_beauty_camera = {
    "name": "Perspective Beauty",
    "azimuth": 0.0,
    "distance": 100.0,
    "inclination": 0.0,
    "fov": 35.0
}

# Create and set up standard view cameras
for cam in standard_views:
    create_standard_view_camera(cam["view_constant"], cam["name"])

# Create and set up the perspective beauty camera with spherical settings
create_perspective_beauty_camera(
    perspective_beauty_camera["name"],
    azimuth=perspective_beauty_camera["azimuth"],
    distance=perspective_beauty_camera["distance"],
    inclination=perspective_beauty_camera["inclination"],
    fov=perspective_beauty_camera["fov"]
)

print("Cameras created successfully.")
```

# End of Automation\Create Standard Views and Perspective Beauty Camera.py

# Automation\Create Standard Views and Perspective Camera with ModelSets.py
<a name="automation-create-standard-views-and-perspective-camera-with-modelsets"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.8
# Template creates cameras with specific parameters for standard views and a perspective beauty camera.
``` python
import lux

def create_standard_view_camera(view_constant, name):
    """
    Creates or updates a camera for a standard view.
    """
    # Check if the camera already exists
    existing_cameras = lux.getCameras()
    if name in existing_cameras:
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)
    # Set the view to the predefined standard view
    lux.setStandardView(view=view_constant)
    # Save the camera settings
    lux.saveCamera()
    print("{} camera: {}".format("Updated" if name in existing_cameras else "Created", name))

def create_perspective_beauty_camera(name, azimuth, distance, inclination, fov):
    """
    Creates or updates a perspective beauty camera with spherical settings.
    """
    # Check if the camera already exists
    existing_cameras = lux.getCameras()
    if name in existing_cameras:
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)
    # Set spherical camera settings
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)
    # Set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))
    # Set the field of view
    lux.setCameraFieldOfView(fov)
    # Save the camera settings
    lux.saveCamera()
    print("{} camera: {}".format("Updated" if name in existing_cameras else "Created", name))

# Define the standard views with view constants
standard_views = [
    {"name": "Front", "view_constant": lux.VIEW_FRONT},
    {"name": "Back", "view_constant": lux.VIEW_BACK},
    {"name": "Left", "view_constant": lux.VIEW_LEFT},
    {"name": "Right", "view_constant": lux.VIEW_RIGHT},
    {"name": "Top", "view_constant": lux.VIEW_TOP},
    {"name": "Bottom", "view_constant": lux.VIEW_BOTTOM},
    {"name": "Isometric", "view_constant": lux.VIEW_ISOMETRIC}
]

# Define the camera data for the perspective beauty camera
perspective_beauty_camera = {
    "name": "Perspective Beauty",
    "azimuth": 0.0,
    "distance": 100.0,
    "inclination": 0.0,
    "fov": 35.0
}

# Create model sets
model_set_names = ["product", "ground", "AO"]
for name in model_set_names:
    lux.newModelSet(name=name)

# Create and set up standard view cameras
for cam in standard_views:
    create_standard_view_camera(cam["view_constant"], cam["name"])

# Create and set up the perspective beauty camera with spherical settings
create_perspective_beauty_camera(
    perspective_beauty_camera["name"],
    azimuth=perspective_beauty_camera["azimuth"],
    distance=perspective_beauty_camera["distance"],
    inclination=perspective_beauty_camera["inclination"],
    fov=perspective_beauty_camera["fov"]
)

print("Model sets and cameras created successfully.")


# End of Automation\Create Standard Views and Perspective Camera with ModelSets.py

# Automation\Create Standard Views and Perspective Camera.py
<a name="automation-create-standard-views-and-perspective-camera"></a>
import lux
import luxmath

def create_standard_views_and_perspective_camera():
    # Function to create standard views
    def create_standard_view_camera(view_name, view_constant):
        camera_name = f"{view_name} View"
        if camera_name not in lux.getCameras():
            lux.newCamera(camera_name)
        lux.setCamera(camera_name)
        lux.setStandardView(view=view_constant)
        lux.saveCamera()

    # Creating standard view cameras
    standard_views = {
        "Front": lux.VIEW_FRONT,
        "Back": lux.VIEW_BACK,
        "Left": lux.VIEW_LEFT,
        "Right": lux.VIEW_RIGHT,
        "Top": lux.VIEW_TOP,
        "Bottom": lux.VIEW_BOTTOM,
        "Isometric": lux.VIEW_ISOMETRIC
    }
    
    for view_name, view_constant in standard_views.items():
        create_standard_view_camera(view_name, view_constant)
    
    # Function to create a perspective camera
    def create_perspective_camera(camera_name="Perspective Camera", azimuth=30, inclination=30, distance=100, fov=35):
        if camera_name not in lux.getCameras():
            lux.newCamera(camera_name)
        lux.setCamera(camera_name)
        lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)
        lux.setCameraDistance(dist=distance)
        lux.setCameraFieldOfView(fov)
        lux.saveCamera()

    # Creating perspective camera
    create_perspective_camera()

# Execute the function to create standard views and perspective camera
create_standard_views_and_perspective_camera()
```

# End of Automation\Create Standard Views and Perspective Camera.py

# Automation\Create Standard Views and Perspective Cameras.py
<a name="automation-create-standard-views-and-perspective-cameras"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Creates Cameras for standard views and perspectives.
``` python
import lux

# Function to create and set up camera
def create_and_setup_camera(name, azimuth, distance, inclination):
    # Check if camera already exists
    if name in lux.getCameras():
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)

    # Set spherical camera settings (azimuth, inclination, twist)
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)

    # Set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))

    # Save the camera settings
    lux.saveCamera()

# Define all standard views and additional 3/4 views
camera_data = [
    {"name": "Front", "azimuth": 0.000, "distance": 100.000, "inclination": 0.000},
    {"name": "Back", "azimuth": 180.000, "distance": 100.000, "inclination": 0.000},
    {"name": "Left", "azimuth": 90.000, "distance": 100.000, "inclination": 0.000},
    {"name": "Right", "azimuth": -90.000, "distance": 100.000, "inclination": 0.000},
    {"name": "Top", "azimuth": 0.000, "distance": 100.000, "inclination": -90.000},
    {"name": "Bottom", "azimuth": 0.000, "distance": 100.000, "inclination": 90.000},
    {"name": "FrontRight3/4", "azimuth": -45.0, "distance": 100.0, "inclination": 0.0},
    {"name": "FrontLeft3/4", "azimuth": 45.0, "distance": 100.0, "inclination": 0.0},
    {"name": "BackRight3/4", "azimuth": 135.0, "distance": 100.0, "inclination": 0.0},
    {"name": "BackLeft3/4", "azimuth": -135.0, "distance": 100.0, "inclination": 0.0}
]

# Creating and setting up cameras in KeyShot
for cam in camera_data:
    create_and_setup_camera(cam["name"], cam["azimuth"], cam["distance"], cam["inclination"])

print("All cameras have been created and set up.")
```


# End of Automation\Create Standard Views and Perspective Cameras.py

# Automation\Create Standard Views and Perspective Cameras_Distance_50Units.py
<a name="automation-create-standard-views-and-perspective-cameras_distance_50units"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Creates Cameras for standard views and perspectives.
``` python
import lux

# Function to create and set up camera
def create_and_setup_camera(name, azimuth, distance, inclination):
    # Check if camera already exists
    if name in lux.getCameras():
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)

    # Set spherical camera settings (azimuth, inclination, twist)
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)

    # Set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))

    # Save the camera settings
    lux.saveCamera()

# Define all standard views and additional 3/4 views
camera_data = [
    {"name": "Front", "azimuth": 0.000, "distance": 50.000, "inclination": 0.000},
    {"name": "Back", "azimuth": 180.000, "distance": 50.000, "inclination": 0.000},
    {"name": "Left", "azimuth": 90.000, "distance": 50.000, "inclination": 0.000},
    {"name": "Right", "azimuth": -90.000, "distance": 50.000, "inclination": 0.000},
    {"name": "Top", "azimuth": 0.000, "distance": 50.000, "inclination": -90.000},
    {"name": "Bottom", "azimuth": 0.000, "distance": 50.000, "inclination": 90.000},
    {"name": "FrontRight3/4", "azimuth": -45.0, "distance": 50.0, "inclination": 0.0},
    {"name": "FrontLeft3/4", "azimuth": 45.0, "distance": 50.0, "inclination": 0.0},
    {"name": "BackRight3/4", "azimuth": 135.0, "distance": 50.0, "inclination": 0.0},
    {"name": "BackLeft3/4", "azimuth": -135.0, "distance": 50.0, "inclination": 0.0}
]

# Creating and setting up cameras in KeyShot
for cam in camera_data:
    create_and_setup_camera(cam["name"], cam["azimuth"], cam["distance"], cam["inclination"])

print("All cameras have been created and set up.")
```


# End of Automation\Create Standard Views and Perspective Cameras_Distance_50Units.py

# Automation\Create Standard Views and Perspective Cameras_Distance_5Units.py
<a name="automation-create-standard-views-and-perspective-cameras_distance_5units"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Creates Cameras for standard views and perspectives.
``` python
import lux

# Function to create and set up camera
def create_and_setup_camera(name, azimuth, distance, inclination):
    # Check if camera already exists
    if name in lux.getCameras():
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)

    # Set spherical camera settings (azimuth, inclination, twist)
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)

    # Set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))

    # Save the camera settings
    lux.saveCamera()

# Define all standard views and additional 3/4 views
camera_data = [
    {"name": "Front", "azimuth": 0.000, "distance": 5.000, "inclination": 0.000},
    {"name": "Back", "azimuth": 180.000, "distance": 5.000, "inclination": 0.000},
    {"name": "Left", "azimuth": 90.000, "distance": 5.000, "inclination": 0.000},
    {"name": "Right", "azimuth": -90.000, "distance": 5.000, "inclination": 0.000},
    {"name": "Top", "azimuth": 0.000, "distance": 5.000, "inclination": -90.000},
    {"name": "Bottom", "azimuth": 0.000, "distance": 5.000, "inclination": 90.000},
    {"name": "FrontRight3/4", "azimuth": -45.0, "distance": 5.0, "inclination": 0.0},
    {"name": "FrontLeft3/4", "azimuth": 45.0, "distance": 5.0, "inclination": 0.0},
    {"name": "BackRight3/4", "azimuth": 135.0, "distance": 5.0, "inclination": 0.0},
    {"name": "BackLeft3/4", "azimuth": -135.0, "distance": 5.0, "inclination": 0.0}
]

# Creating and setting up cameras in KeyShot
for cam in camera_data:
    create_and_setup_camera(cam["name"], cam["azimuth"], cam["distance"], cam["inclination"])

print("All cameras have been created and set up.")
```


# End of Automation\Create Standard Views and Perspective Cameras_Distance_5Units.py

# Automation\Create a Perspective Camera.py
<a name="automation-create-a-perspective-camera"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Template creates a perspective camera.
``` python
import lux

# Function to create and set up a camera
def create_camera(name, azimuth, inclination, distance):
    # Check if camera already exists
    if name in lux.getCameras():
        # Set the existing camera as active
        lux.setCamera(name)
    else:
        # Create a new camera
        lux.newCamera(name)

    # Set spherical camera settings (azimuth, inclination, twist)
    lux.setSphericalCamera(azimuth=azimuth, incl=inclination, twist=0)

    # Set distance from camera to pivot/look-at point
    lux.setCameraDistance(dist=float(distance))

    # Save the camera settings
    lux.saveCamera()

# Example usage
camera_name = "MyCamera"
azimuth_angle = 45.0
inclination_angle = 20.0
camera_distance = 100.0

create_camera(camera_name, azimuth_angle, inclination_angle, camera_distance)

print("Camera created and set up successfully.")
```

# End of Automation\Create a Perspective Camera.py

# Automation\Create and Configure Studios.py
<a name="automation-create-and-configure-studios"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.3
# Script that creates specified model sets and configures studios.
``` python
import lux

def ensure_visibility(item, item_type):
    """
    Ensure that the specified item is visible in the scene.
    :param item: The name of the item (camera, environment, etc.)
    :param item_type: The type of item (camera, environment, model_set, image_style)
    """
    if item_type == 'camera':
        if item in lux.getCameras():
            lux.setCamera(item)
    elif item_type == 'environment':
        if item in lux.getEnvironments():
            lux.setActiveEnvironment(item)
    elif item_type == 'model_set':
        if item in lux.getModelSets():
            lux.setModelSets([item])
    elif item_type == 'image_style':
        if item in lux.getImageStyles():
            lux.setActiveImageStyle(item)

def set_active_model_sets(model_sets):
    """
    Ensure all specified model sets are active.
    :param model_sets: List of model set names to activate.
    """
    # Retrieve all model sets (active and inactive)
    root_node = lux.getSceneTree()
    all_model_sets = [node for node in root_node.getChildren() if node.isModelSet()]

    # Collect the names of all model sets
    all_model_set_names = [model_set.getName() for model_set in all_model_sets]

    # Check if the specified model sets exist in the list and activate them
    active_model_sets = []
    for model_set_name in model_sets:
        if model_set_name in all_model_set_names:
            active_model_sets.append(model_set_name)
        else:
            print(f"Model set '{model_set_name}' not found.")
    
    if active_model_sets:
        success = lux.setModelSets(active_model_sets)
        if not success:
            print(f"Some model sets in {active_model_sets} could not be activated.")

def print_model_sets():
    """Print the names of all model sets."""
    model_sets = lux.getModelSets()
    for model_set in model_sets:
        print(model_set)

def create_and_configure_studios():
    """Create and configure studios based on predefined settings."""
    studios = [
        {
            "name": "Product",
            "camera": "Front",
            "environment": "Front",
            "model_sets": ["Product", "Default"],
            "image_style": "Default"
        },
        {
            "name": "ProductPro",
            "camera": "Front",
            "environment": "Front",
            "model_sets": ["ProductPro", "Default"],
            "image_style": "Default"
        },
        {
            "name": "Accessory",
            "camera": "Front",
            "environment": "Front",
            "model_sets": ["Accessory", "Default"],
            "image_style": "Default"
        },
        {
            "name": "ProductAccessory",
            "camera": "Front",
            "environment": "Front",
            "model_sets": ["ProductAccessory", "Default"],
            "image_style": "Default"
        },
        {
            "name": "ProductProAccessory",
            "camera": "Front",
            "environment": "Front",
            "model_sets": ["ProductProAccessory", "Default"],
            "image_style": "Default"
        },
        {
            "name": "ProductAccessoryExploded",
            "camera": "Front",
            "environment": "Front",
            "model_sets": ["ProductAccessoryExploded", "Default"],
            "image_style": "Default"
        }
    ]

    for studio in studios:
        try:
            # Ensure visibility of necessary elements
            ensure_visibility(studio["camera"], 'camera')
            ensure_visibility(studio["environment"], 'environment')
            set_active_model_sets(studio["model_sets"])
            ensure_visibility(studio["image_style"], 'image_style')

            # Check and print available model sets
            print_model_sets()

            # Create a new studio
            studio_obj = lux.newStudio(name=str(studio["name"]))
            lux.setActiveStudio(studio_obj.getName())

            # Set the camera
            studio_obj.setCamera(str(studio["camera"]))

            # Set the environment
            studio_obj.setEnvironment(str(studio["environment"]))

            # Set the model sets specifically for the studio
            if not studio_obj.setModelSets([str(ms) for ms in studio["model_sets"]]):
                print(f"Some model sets in {studio['model_sets']} not found for studio '{studio['name']}'.")

            # Set the image style
            studio_obj.setImageStyle(str(studio["image_style"]))

            print(f"Studio '{studio['name']}' has been created and configured.")
        except Exception as e:
            print(f"An error occurred while creating the studio '{studio['name']}': {e}")

def create_model_sets():
    """Create the necessary model sets for the studios."""
    model_sets = ["Product", "ProductPro", "Accessory", "ProductAccessory", "ProductProAccessory", "ProductAccessoryExploded"]
    for model_set in model_sets:
        lux.newModelSet(model_set)
    print("Model sets created.")

def main():
    # Create the necessary model sets
    create_model_sets()

    # Create and configure studios
    create_and_configure_studios()

if __name__ == "__main__":
    main()
```

# End of Automation\Create and Configure Studios.py

# Automation\Creates Model Set.py
<a name="automation-creates-model-set"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# HEADLESS COMPLIANT
# Creates a model set.
``` python
import lux

# Specify the name of the new model set
model_set_name = "NewModelSet"

# Create the new model set
lux.newModelSet(name=model_set_name)

print(f"Model set '{model_set_name}' created successfully.")
```


# End of Automation\Creates Model Set.py

# Automation\Delete Unused Nodes.py
<a name="automation-delete-unused-nodes"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# HEADLESS COMPLIANT
# Deletes unused nodes.
``` python
def has_material_connections(node):
    """Check if a material node has connections."""
    input_edges = node.getInputEdges()
    output_edges = node.getOutputEdges()
    return bool(input_edges or output_edges)

def cleanup_unused_material_nodes(material_graph):
    """Clean up unconnected nodes within a material graph."""
    try:
        nodes = material_graph.getNodes()
        for node in nodes:
            if not has_material_connections(node):
                material_graph.removeNode(node)
                print(f"Removed node: {node.getName()} from material: {material_graph.getMaterialName()}")
    except Exception as e:
        print(f"Exception encountered while processing material graph: {e}")

def is_node_in_use(node):
    """Check if a scene node is in use."""
    # Placeholder for actual implementation. Adjust this based on your specific requirements.
    # For example, checking if the node is visible or part of the render list.
    return True  # Assume nodes are in use. Replace with actual logic as necessary.

def cleanup_unused_scene_nodes(node):
    """Recursively clean up unconnected scene nodes."""
    # Check if the node is in use
    if not is_node_in_use(node):
        node.delete()
        print(f"Removed unconnected node: {node.getName()}")
        return

    # Recursively check and clean child nodes if the node is a group or model set
    if node.isGroup() or node.isModelSet():
        if hasattr(node, 'getChildren'):
            children = node.getChildren()
            for child in children:
                cleanup_unused_scene_nodes(child)

def cleanup_scene():
    """Main function to clean up the scene."""
    # Cleanup material nodes
    material_names = lux.getSceneMaterials()
    for material_name in material_names:
        try:
            material_graph = lux.getMaterialGraph(material_name)
            if material_graph:
                cleanup_unused_material_nodes(material_graph)
        except Exception as e:
            print(f"Exception encountered while processing material {material_name}: {e}")
    
    # Cleanup scene nodes
    root_node = lux.getSceneTree()
    cleanup_unused_scene_nodes(root_node)

    lux.getMessageBox("Scene cleanup of unconnected nodes completed.", "Cleanup Complete", lux.MESSAGE_BOX_INFO)

cleanup_scene()
```

# End of Automation\Delete Unused Nodes.py

# GUI\CustomInputDialog_PC.py
<a name="gui-custominputdialog_pc"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Example of lux.getInputDialog GUI
``` python
import lux

# Define the input fields
values = [
    ("file_path", lux.DIALOG_FILE, "Select a file:", None),
    ("frame_rate", lux.DIALOG_INTEGER, "Frame Rate:", 24, (1, 60)),
    ("project_name", lux.DIALOG_TEXT, "Project Name:", "MyProject")
]

# Show the dialog
opts = lux.getInputDialog(title="Project Settings", desc="Enter your project settings:", values=values)

# Print the results
if opts:
    print(f"File Path: {opts['file_path']}")
    print(f"Frame Rate: {opts['frame_rate']}")
    print(f"Project Name: {opts['project_name']}")
else:
    print("Dialog was cancelled or closed.")
```

# End of GUI\CustomInputDialog_PC.py

# GUI\GUI Script Example Doc.py
<a name="gui-gui-script-example-doc"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Example of lux.getInputDialog GUI
``` python
import lux

def create_input_dialog():
    # Define the input fields for the dialog
    values = [
        ("name", lux.DIALOG_TEXT, "Enter your name:", "John Doe"),  # Provide a non-empty default value
        ("age", lux.DIALOG_INTEGER, "Enter your age:", 30, (1, 100)),  # The last tuple defines the range (min, max)
        ("file", lux.DIALOG_FILE, "Select a file:", None),
        ("folder", lux.DIALOG_FOLDER, "Select a folder:", None)
    ]
    
    # Show the dialog and get the user's input
    opts = lux.getInputDialog(
        title="User Information",
        desc="Please fill in the information below:",
        values=values,
        id="user_info_dialog"  # Unique identifier to remember the last values entered
    )
    
    # Check if the user clicked OK and opts is not None
    if opts:
        print("User's Input:")
        for key, value in opts.items():
            print(f"{key}: {value}")
    else:
        print("User cancelled the dialog.")

# Call the function to show the dialog
create_input_dialog()
```

# End of GUI\GUI Script Example Doc.py

# GUI\Get InputDialog GUI Example.py
<a name="gui-get-inputdialog-gui-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Example of lux.getInputDialog GUI
``` python
import lux

def create_input_dialog():
    # Define the input fields for the dialog
    values = [
        ("name", lux.DIALOG_TEXT, "Enter your name:", "John Doe"),  # Provide a non-empty default value
        ("age", lux.DIALOG_INTEGER, "Enter your age:", 30, (1, 100)),  # The last tuple defines the range (min, max)
        ("file", lux.DIALOG_FILE, "Select a file:", None),
        ("folder", lux.DIALOG_FOLDER, "Select a folder:", None)
    ]
    
    # Show the dialog and get the user's input
    opts = lux.getInputDialog(
        title="User Information",
        desc="Please fill in the information below:",
        values=values,
        id="user_info_dialog"  # Unique identifier to remember the last values entered
    )
    
    # Check if the user clicked OK and opts is not None
    if opts:
        print("User's Input:")
        for key, value in opts.items():
            print(f"{key}: {value}")
    else:
        print("User cancelled the dialog.")

# Call the function to show the dialog
create_input_dialog()
```

# End of GUI\Get InputDialog GUI Example.py

# ImportExport\Batch Import CAD Model Assign Material Template Name Model Set.py
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

# ImportExport\Batch Import CAD Model Assign Material Template.py
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

# ImportExport\Batch Import CAD.py
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

# ImportExport\Batch Import Multiple CAD File Types.py
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

# ImportExport\Import CAD.py
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

# ImportExport\Import CAD_Prompt.py
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

# ImportExport\Import Scene Template cm into a New Scene.py
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

# ImportExport\Import Scene Template cm into an Existing Scene.py
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

# ImportExport\Import Scene Template cm.py
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

# ImportExport\Import Scene Template mm.py
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

# ImportExport\Import Template meters.py
<a name="importexport-import-template-meters"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Imports a Baron Ring template Scene into a new scene.
``` python
import os
import lux

# Determine the operating system and set the library path accordingly
if os.name == 'nt':  # Windows
    file_path = "C:\\Users\\Public\\Documents\\KeyShot 12\\Templates\\Layout_Master_Scene_05.bip"
else:  # macOS and Unix/Linux
    file_path = "/Library/Application Support/KeyShot 12/Templates/Layout_Master_Scene_05.bip"

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

# ImportExport\Import Template mm.py
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

# ImportExport\Import_GLB_TranslateRotateScale.py
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

# ImportExport\Import_OBJ_TranslateRotateScale.py
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

# Information\Get Camera Distance.py
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

# Information\Get MaterialGraph Parameters.py
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

# Information\Get Metadata.py
<a name="information-get-metadata"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Get Metadata
``` python
import lux

# Print the entire scene info to understand its structure
scene_metadata = lux.getMetaData
print(scene_metadata)


# End of Information\Get Metadata.py

# Information\Get Model Sets.py
<a name="information-get-model-sets"></a>
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

# Information\Get Node Type.py
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

# Information\Get Render Info.py
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

# Information\Get Resource Library Models 2024.py
<a name="information-get-resource-library-models-2024"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script that lists models in the KeyShot Resources/Models directory and its subdirectories.
# Compatible with KeyShot 2024 and higher.
``` python
import os
import lux

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system.
    """
    # Determine the library path based on the operating system
    library_path = os.path.join(os.environ.get('PUBLIC', ''), "Documents", "KeyShot")
    if not os.path.exists(library_path):  # If not Windows, try Unix-like path
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot")
    
    return library_path

def list_models_in_library():
    """
    Lists all model files in the KeyShot Resources/Models directory and its subdirectories.
    """
    library_path = get_library_path()
    models_path = os.path.join(library_path, "Models")
    
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

# End of Information\Get Resource Library Models 2024.py

# Information\Get Resource Library Path 2024.py
<a name="information-get-resource-library-path-2024"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script that gets the KeyShot Resources Library Path.  
# Compatible with KeyShot 2024 and higher.
``` python
import os
import lux

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system and displays the path in a message box.
    """
    # Determine the library path based on the operating system
    library_path = os.path.join(os.environ.get('PUBLIC', ''), "Documents", "KeyShot",)
    if not os.path.exists(library_path):  # If not Windows, try Unix-like path
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot",)
    
    # Display the library path in a message box
    lux.getMessageBox(f"Your KeyShot Resources Library path is:\n{library_path}", "Library Path", lux.MESSAGE_BOX_INFO)
    
    return library_path

# Example usage
library_path = get_library_path()
print(f"Library path: {library_path}")
```

# End of Information\Get Resource Library Path 2024.py

# Information\Get Resource Library Path 2024_v2.py
<a name="information-get-resource-library-path-2024_v2"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Determines the KeyShot 2024 and higher "Resources Library" path based on the operating system and displays the path in a message box.
``` python
import os
import lux

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system and displays the path in a message box.
    """
    # Determine the library path based on the operating system
    if os.name == 'nt':  # Windows
        library_path = os.path.join(os.environ.get('USERPROFILE', ''), "Documents", "KeyShot",)
    else:  # macOS or Unix-like
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot")
    
    # Check if the path exists and if not, try an alternative common path
    if not os.path.exists(library_path):
        if os.name == 'nt':  # Windows alternative
            library_path = os.path.join(os.environ.get('PUBLIC', ''), "Documents", "KeyShot")
        else:  # macOS alternative
            library_path = os.path.join(os.path.expanduser('~'), "Documents", "KeyShot")
    
    # Display the library path in a message box
    lux.getMessageBox(f"Your KeyShot Resources Library path is:\n{library_path}", "Library Path", lux.MESSAGE_BOX_INFO)
    
    return library_path

# Example usage
library_path = get_library_path()
print(f"Library path: {library_path}")
```

# End of Information\Get Resource Library Path 2024_v2.py

# Information\Get Resource Library Path.py
<a name="information-get-resource-library-path"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script that gets the KeyShot Resources Library Path.  
# Compatible with KeyShot 2024 and higher.
``` python
import os
import lux

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system and displays the path in a message box.
    """
    # Determine the library path based on the operating system
    library_path = os.path.join(os.environ.get('PUBLIC', ''), "Documents", "KeyShot",)
    if not os.path.exists(library_path):  # If not Windows, try Unix-like path
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot",)
    
    # Display the library path in a message box
    lux.getMessageBox(f"Your KeyShot Resources Library path is:\n{library_path}", "Library Path", lux.MESSAGE_BOX_INFO)
    
    return library_path

# Example usage
library_path = get_library_path()
print(f"Library path: {library_path}")
```

# End of Information\Get Resource Library Path.py

# Information\Get Scene Info.py
<a name="information-get-scene-info"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Get Scene Info.
``` python
import lux

# Print the entire scene info to understand its structure
scene_info = lux.getSceneInfo()
print(scene_info)


# End of Information\Get Scene Info.py

# Information\Get Scene Information.py
<a name="information-get-scene-information"></a>
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

# Information\Get Scene Materials.py
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

# Information\Get SceneTree Nodes.py
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

# Information\Get SceneTree.py
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

# Information\Get Scenes Material Parameters and Save to File.py
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

# Information\Get_Camera_Info.py
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

# Load\Load Enviorment From Library and Apply Settings.py
<a name="load-load-enviorment-from-library-and-apply-settings"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Script Applies Enviorment from library.  Uses the "ENV" class.
``` python
import lux
import os

# Function to load environments
def load_environment_from_library(env_filename):
    library_envs = lux.getLibraryEnvironments()
    full_env_path = None
    for lib_env_path in library_envs:
        if env_filename.lower() in os.path.basename(lib_env_path).lower():
            full_env_path = lib_env_path
            break
    
    if full_env_path is not None:
        try:
            env_name = os.path.splitext(env_filename)[0].replace(" ", "_")
            new_env = lux.newEnvironment(name=env_name, activate=True)
            if new_env.setLightingEnvironment(full_env_path):
                print(f"Environment '{env_filename}' has been successfully loaded and set.")
                return new_env
            else:
                print(f"Failed to apply environment '{env_filename}'.")
        except Exception as e:
            print(f"An error occurred while setting the environment '{env_filename}': {e}")
    else:
        print(f"The environment '{env_filename}' could not be found in the KeyShot library.")
    return None

# Function to set environment parameters
def set_environment_parameters(env, brightness, size, height, rotation):
    try:
        if env:
            env.setBrightness(brightness)
            env.setSize(size)
            env.setHeight(height)
            env.setRotation(rotation)
            env.setBackgroundColor((255, 255, 255))
            env.setGroundSize(0.01)
            env.setGroundShadows(False)
            env.setOcclusionGroundShadows(False)
            env.setGroundReflections(False)
            env.setFlattenGround(False)
            lux.setActiveEnvironment(env.getName())
            lux.getActiveEnvironment().setBackgroundColor((255, 255, 255))
            print(f"Parameters for environment '{env.getName()}' have been successfully set.")
        else:
            print("Environment not found.")
    except Exception as e:
        print(f"An error occurred while setting parameters for environment '{env.getName()}': {e}")

# Combined function to configure the "3 Panel 4K" environment
def configure_environment():
    env_filename = "3 Panels Straight 4K.klf"
    brightness = 1.0
    size = 1.0
    height = 0.0
    rotation = 0.0
    
    environment = load_environment_from_library(env_filename)
    if environment:
        set_environment_parameters(environment, brightness, size, height, rotation)

# Run the configuration
configure_environment()
```
# End of Load\Load Enviorment From Library and Apply Settings.py

# Load\Load Enviorment From Library.py
<a name="load-load-enviorment-from-library"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Script Applies Enviorment from library.  Uses the "ENV" class.
``` python
import lux
import os

def load_environment_from_library(env_filename):
    # Define the KeyShot library path. This may need to be adapted for your specific system or KeyShot version.
    keyshot_lib_path = "C:/Users/Public/Documents/KeyShot/Environments"
    
    # Normalize the KeyShot library path
    keyshot_lib_path = os.path.normpath(keyshot_lib_path)
    
    # Retrieve the list of environments from KeyShot's library
    library_envs = lux.getLibraryEnvironments()
    
    # Attempt to find the full path of the desired environment file in the library
    full_env_path = None
    for lib_env_path in library_envs:
        if env_filename.lower() in os.path.basename(lib_env_path).lower():
            full_env_path = lib_env_path
            break
    
    # Check if the desired environment file was found
    if full_env_path is not None:
        try:
            # Create and activate a new environment in the scene with the found environment file
            new_env = lux.newEnvironment(name=os.path.splitext(env_filename)[0], activate=True)
            if new_env.setLightingEnvironment(full_env_path):
                print(f"Environment '{env_filename}' has been successfully loaded and set.")
            else:
                print(f"Failed to apply environment '{env_filename}'.")
        except Exception as e:
            print(f"An error occurred while setting the environment '{env_filename}': {e}")
    else:
        print(f"The environment '{env_filename}' could not be found in the KeyShot library.")

# Example usage
env_filename = "3 Panels Straight 4K.klf"  # Update this with the exact filename of the environment you wish to load
load_environment_from_library(env_filename)
```
# End of Load\Load Enviorment From Library.py

# Load\Load Ground Plane 2024.py
<a name="load-load-ground-plane-2024"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script that loads a ground plane from the keyshot resources library.  Must have Ground Plane Model. 
# Compatible with KeyShot 2024 and higher.
``` python
import lux
import os

def get_library_path():
    if os.name == 'nt':
        library_path = os.path.join(os.environ['PUBLIC'], "Documents", "KeyShot", "Models", "Ground")
    else:
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot", "Models", "Ground")
    return library_path

def add_ground_plane_to_default_model_set():
    default_model_set_name = "Default"

    # Ensure the default model set exists
    lux.newModelSet(name=default_model_set_name)
    lux.setModelSets([default_model_set_name])
    print(f"Activated or created model set: {default_model_set_name}")
    
    library_path = get_library_path()
    ground_plane_model = "Ground.bip"
    ground_plane_path = os.path.join(library_path, ground_plane_model)
    
    if not os.path.exists(ground_plane_path):
        print(f"Ground plane model '{ground_plane_model}' not found in the KeyShot Resources Library.")
        return
    
    print(f"Importing ground plane model from: {ground_plane_path}")
    import_options = {
        'import_type': 0,
        'snap_to_ground': True,
        'center_geometry': False,
        'merge_objects': False
    }
    lux.importFile(ground_plane_path, opts=import_options)
    print("Ground plane model imported and assigned to the default model set.")

def main():
    add_ground_plane_to_default_model_set()

if __name__ == "__main__":
    main()
```

# End of Load\Load Ground Plane 2024.py

# Load\Load Ground Plane.py
<a name="load-load-ground-plane"></a>
# AUTHOR LUX DT ChatGPT4
# VERSION 0.1.5
# Import Ground Plane Model from Resources Library and assign to Default Model Set.
``` python
import lux
import os

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system.
    """
    if os.name == 'nt':  # Windows
        library_path = os.path.join(os.environ['PUBLIC'], "Documents", "KeyShot", "Models", "Ground Plane")
    else:  # macOS and Unix/Linux
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot", "Models", "Ground Plane")
    return library_path

def add_ground_plane_to_default_model_set():
    """
    Imports the ground plane model from the KeyShot Resources Model Library and assigns it to the default model set.
    """
    default_model_set_name = "Default"
    
    # Check if the default model set exists and set it as active
    model_sets = lux.getModelSets()
    if default_model_set_name in model_sets:
        lux.setModelSets([default_model_set_name])
        print(f"Activated model set: {default_model_set_name}")
    else:
        print(f"Model set '{default_model_set_name}' not found. Creating a new one.")
        lux.newModelSet(name=default_model_set_name)
        lux.setModelSets([default_model_set_name])
    
    # Determine the path to the ground plane model
    library_path = get_library_path()
    ground_plane_model = "Ground Plane.bip"  # Example ground plane model filename
    ground_plane_path = os.path.join(library_path, ground_plane_model)
    
    if not os.path.exists(ground_plane_path):
        print(f"Ground plane model '{ground_plane_model}' not found in the KeyShot Resources Library.")
        return
    
    # Import the ground plane model without clearing the scene
    print(f"Importing ground plane model from: {ground_plane_path}")
    import_options = {
        'import_type': 0,  # Add to scene
        'snap_to_ground': True,
        'center_geometry': False,
        'merge_objects': False
    }
    lux.importFile(ground_plane_path, opts=import_options)
    print("Ground plane model imported and assigned to the default model set.")

def main():
    add_ground_plane_to_default_model_set()

if __name__ == "__main__":
    main()
```

# End of Load\Load Ground Plane.py

# Load\Load Library Texture Assign to Diffuse Material Bump Add 2024.py
<a name="load-load-library-texture-assign-to-diffuse-material-bump-add-2024"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.5
# Script to apply a texture to the bump map of a diffuse material in KeyShot.
``` python
import lux

def create_texture_node(graph, texture_file_path):
    """
    Creates a texture node and sets the texture file path.
    """
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node:
        try:
            file_param = texture_node.getParameter("texture")
            file_param.setValue(texture_file_path)
            return texture_node
        except Exception as e:
            print(f"Error setting texture file path: {e}")
    return None

def connect_textures_to_bump(material_name, texture_file_paths):
    """
    Connects multiple textures to the bump parameters of a given material.
    """
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    texture_nodes = [create_texture_node(graph, path) for path in texture_file_paths]
    if any(node is None for node in texture_nodes):
        print("Failed to create all texture nodes.")
        return

    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    try:
        for idx, node in enumerate(texture_nodes):
            graph.newEdge(source=node, target=bump_add_node, param=f"bump_{idx + 1}")
            print(f"Successfully created edge from texture node to bump add node (bump_{idx + 1}).")
    except Exception as e:
        print(f"Failed to create edge from texture node to bump add node: {e}")
        return

    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump textures successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
material_name = "Cube Material"
texture_file_paths = [
    "C:/Users/Public/Documents/KeyShot/Textures/ash.jpg",
    "C:/Users/Public/Documents/KeyShot/Textures/Color Maps/asphalt.jpg"
]

connect_textures_to_bump(material_name, texture_file_paths)
```

# End of Load\Load Library Texture Assign to Diffuse Material Bump Add 2024.py

# Material\Adjust Texture Scale Scene Units 1cm.py
<a name="material-adjust-texture-scale-scene-units-1cm"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Resets the texture Scale Width and Height to 1cm.  KeyShot imports in Meters.
``` python
import lux

# Replace with your material name
material_name = "Cube Material"

# Access the Material Graph
graph = lux.getMaterialGraph(material_name)

# Create an Image Texture Node
texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)

# Set the texture file
texture_file_parameter_name = "texture"
texture_path = "C:/Users/Public/Documents/KeyShot 12/Textures/Color Maps/asphalt.jpg"
texture_node.getParameter(texture_file_parameter_name).setValue(texture_path)

# Adjust the UV scale to 1 cm (assuming scene units are in meters)
texture_node.getParameter("uv_scale_u").setValue(0.01)  # Adjusting U scale to 1 cm
texture_node.getParameter("uv_scale_v").setValue(0.01)  # Adjusting V scale to 1 cm

# Access the Material's Root Node
root_node = graph.getRoot()

# Get the shader node connected to the surface parameter of the root node
surface_shader_edge = root_node.getInputEdge("surface")
if not surface_shader_edge:
    print("No shader connected to the surface parameter.")
    exit()

surface_shader_node = surface_shader_edge.getSourceNode()

# Find the diffuse color parameter and connect the texture node
for parameter in surface_shader_node.getParameters():
    if parameter.getType() in [lux.PARAMETER_TYPE_COLOR, lux.PARAMETER_TYPE_COLORALPHA]:
        try:
            graph.newEdge(texture_node, surface_shader_node, parameter.getName())
            print(f"Texture applied to '{parameter.getName()}' parameter of surface shader in '{material_name}'.")
            exit()
        except Exception as e:
            print(f"Error applying texture to '{parameter.getName()}': {e}")

print("No suitable color parameter found in the surface shader node.")
```

# End of Material\Adjust Texture Scale Scene Units 1cm.py

# Material\Apply 2 Library Textures to Diffuse Material Bump Add.py
<a name="material-apply-2-library-textures-to-diffuse-material-bump-add"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.6
# Script to apply two textures to the bump map of a diffuse material in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edges_to_bump(material_name, texture_file_path_1, texture_file_path_2):
    """
    Connects two texture files to the bump parameters of a given material.

    :param material_name: The name of the material to apply the bump textures to.
    :param texture_file_path_1: The file path of the first bump texture to apply.
    :param texture_file_path_2: The file path of the second bump texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node for the first texture.
    texture_node_1 = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node_1 is None:
        print("Failed to create first texture node.")
        return

    # Set the first texture file path using the correct parameter name.
    try:
        file_param_1 = texture_node_1.getParameter("texture")
        file_param_1.setValue(texture_file_path_1)  # Set the file path of the first texture.
    except Exception as e:
        print(f"Error setting first texture file path: {e}")
        return

    # Create a new texture node for the second texture.
    texture_node_2 = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node_2 is None:
        print("Failed to create second texture node.")
        return

    # Set the second texture file path using the correct parameter name.
    try:
        file_param_2 = texture_node_2.getParameter("texture")
        file_param_2.setValue(texture_file_path_2)  # Set the file path of the second texture.
    except Exception as e:
        print(f"Error setting second texture file path: {e}")
        return

    # Create a bump add node in the material graph.
    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    # Debugging: Print IDs and parameter names
    print(f"Texture Node 1 ID: {texture_node_1.getID()}, Texture Node 2 ID: {texture_node_2.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
    print(f"Connecting texture node 1's 'texture' parameter to bump add node's 'bump_1' parameter")
    print(f"Connecting texture node 2's 'texture' parameter to bump add node's 'bump_2' parameter")

    # Connect the first texture node to the bump add node.
    try:
        graph.newEdge(source=texture_node_1, target=bump_add_node, param="bump_1")
        print("Successfully created edge from first texture node to bump add node.")
    except Exception as e:
        print(f"Failed to create edge from first texture node to bump add node: {e}")
        return

    # Connect the second texture node to the bump add node.
    try:
        graph.newEdge(source=texture_node_2, target=bump_add_node, param="bump_2")
        print("Successfully created edge from second texture node to bump add node.")
    except Exception as e:
        print(f"Failed to create edge from second texture node to bump add node: {e}")
        return

    # Connect the bump add node to the diffuse material's bumpmap parameter.
    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            print(f"Diffuse Node ID: {shader_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump textures successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
# Define the material name and texture file paths.
material_name = "Cube Material"
texture_file_path_1 = "C:/Users/Public/Documents/KeyShot 12/Textures/ash.jpg"
texture_file_path_2 = "C:/Users/Public/Documents/KeyShot 12/Textures/Color Maps/asphalt.jpg"

# Apply the bump textures to the specified material.
connect_shader_edges_to_bump(material_name, texture_file_path_1, texture_file_path_2)
```

# End of Material\Apply 2 Library Textures to Diffuse Material Bump Add.py

# Material\Apply Library Color by Name to Diffuse Material Color.py
<a name="material-apply-library-color-by-name-to-diffuse-material-color"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example Script Applies Color from library to a material.
``` python
import lux

def assign_library_color_to_material_by_name(material_name, color_name):
    # Retrieve the material graph for the specified material
    material_graph = lux.getMaterialGraph(material_name)
    if not material_graph:
        print(f"Material '{material_name}' not found in the current scene.")
        return

    # Correct approach to iterate through nodes and find the 'diffuse' parameter
    success = False
    for shader_node in material_graph.getNodes():
        # Iterate through parameters to find 'diffuse'
        for parameter in shader_node.getParameters():
            if parameter.getName() == 'diffuse' and parameter.getType() == 14:  # Type 14 for color
                try:
                    # Set the diffuse color by name, assuming it exists in KeyShot's color library
                    parameter.setValue(color_name)
                    print(f"Color '{color_name}' successfully assigned to material '{material_name}'.")
                    success = True
                    break  # Exit after successfully setting the color
                except Exception as e:
                    print(f"Failed to assign color '{color_name}' to material '{material_name}': {e}")
        if success:
            break

    if not success:
        print(f"Failed to find a 'diffuse' parameter for material '{material_name}' or apply color '{color_name}'.")

# Example usage
assign_library_color_to_material_by_name("Cube Material", "PANTONE 186 C")
```

# End of Material\Apply Library Color by Name to Diffuse Material Color.py

# Material\Apply Library Texture to Diffuse Material Bump Add 2024.py
<a name="material-apply-library-texture-to-diffuse-material-bump-add-2024"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.5
# Script to apply a texture to the bump map of a diffuse material in KeyShot.
``` python
import lux

def create_texture_node(graph, texture_file_path):
    """
    Creates a texture node and sets the texture file path.
    """
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node:
        try:
            file_param = texture_node.getParameter("texture")
            file_param.setValue(texture_file_path)
            return texture_node
        except Exception as e:
            print(f"Error setting texture file path: {e}")
    return None

def connect_textures_to_bump(material_name, texture_file_paths):
    """
    Connects multiple textures to the bump parameters of a given material.
    """
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    texture_nodes = [create_texture_node(graph, path) for path in texture_file_paths]
    if any(node is None for node in texture_nodes):
        print("Failed to create all texture nodes.")
        return

    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    try:
        for idx, node in enumerate(texture_nodes):
            graph.newEdge(source=node, target=bump_add_node, param=f"bump_{idx + 1}")
            print(f"Successfully created edge from texture node to bump add node (bump_{idx + 1}).")
    except Exception as e:
        print(f"Failed to create edge from texture node to bump add node: {e}")
        return

    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump textures successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
material_name = "Cube Material"
texture_file_paths = [
    "C:/Users/Public/Documents/KeyShot/Textures/ash.jpg",
    "C:/Users/Public/Documents/KeyShot/Textures/Color Maps/asphalt.jpg"
]

connect_textures_to_bump(material_name, texture_file_paths)
```

# End of Material\Apply Library Texture to Diffuse Material Bump Add 2024.py

# Material\Apply Library Texture to Diffuse Material Bump Add.py
<a name="material-apply-library-texture-to-diffuse-material-bump-add"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.5
# Script to apply a texture to the bump map of a diffuse material in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edge_to_bump(material_name, texture_file_path):
    """
    Connects a texture file to the bump parameter of a given material.

    :param material_name: The name of the material to apply the bump texture to.
    :param texture_file_path: The file path of the bump texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Set the texture file path using the correct parameter name.
    try:
        file_param = texture_node.getParameter("texture")
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    except Exception as e:
        print(f"Error setting texture file path: {e}")
        return

    # Create a bump add node in the material graph.
    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    # Debugging: Print IDs and parameter names
    print(f"Texture Node ID: {texture_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
    print(f"Connecting texture node's 'texture' parameter to bump add node's 'bump_1' parameter")

    # Connect the texture node to the bump add node.
    try:
        texture_to_bump_edge = graph.newEdge(source=texture_node, target=bump_add_node, param="bump_1")
        print("Successfully created edge from texture node to bump add node.")
    except Exception as e:
        print(f"Failed to create edge from texture node to bump add node: {e}")
        return

    # Connect the bump add node to the diffuse material's bumpmap parameter.
    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            print(f"Diffuse Node ID: {shader_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump texture successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
# Define the material name and texture file path.
material_name = "Cube Material"
texture_file_path = "C:/Users/Public/Documents/KeyShot 12/Textures/Color Maps/asphalt.jpg"

# Apply the bump texture to the specified material.
connect_shader_edge_to_bump(material_name, texture_file_path)
```

# End of Material\Apply Library Texture to Diffuse Material Bump Add.py

# Material\Apply Library Texture to Diffuse Material Bump.py
<a name="material-apply-library-texture-to-diffuse-material-bump"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.5
# Script to apply a texture to the bump map of a diffuse material in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edge_to_bump(material_name, texture_file_path):
    """
    Connects a texture file to the bump parameter of a given material.

    :param material_name: The name of the material to apply the bump texture to.
    :param texture_file_path: The file path of the bump texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Set the texture file path using the correct parameter name.
    try:
        file_param = texture_node.getParameter("texture")
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    except Exception as e:
        print(f"Error setting texture file path: {e}")
        return

    # Create a bump add node in the material graph.
    bump_add_node = graph.newNode(lux.SHADER_TYPE_BUMP_ADD)
    if bump_add_node is None:
        print("Failed to create bump add node.")
        return

    # Debugging: Print IDs and parameter names
    print(f"Texture Node ID: {texture_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
    print(f"Connecting texture node's 'texture' parameter to bump add node's 'bump_1' parameter")

    # Connect the texture node to the bump add node.
    try:
        texture_to_bump_edge = graph.newEdge(source=texture_node, target=bump_add_node, param="bump_1")
        print("Successfully created edge from texture node to bump add node.")
    except Exception as e:
        print(f"Failed to create edge from texture node to bump add node: {e}")
        return

    # Connect the bump add node to the diffuse material's bumpmap parameter.
    connected = False
    for shader_node in graph.getNodesFromType(lux.SHADER_TYPE_DIFFUSE):
        bump_param = shader_node.getParameter("bumpmap")
        if bump_param:
            print(f"Diffuse Node ID: {shader_node.getID()}, Bump Add Node ID: {bump_add_node.getID()}")
            try:
                graph.newEdge(source=bump_add_node, target=shader_node, param="bumpmap")
                print("Bump texture successfully connected to the diffuse material's bumpmap parameter.")
                connected = True
                break
            except Exception as e:
                print(f"Failed to create edge from bump add node to diffuse node: {e}")

    if not connected:
        print("Suitable shader node for bumpmap parameter not found in material graph.")

# Example usage
# Define the material name and texture file path.
material_name = "Cube Material"
texture_file_path = "C:/Users/Public/Documents/KeyShot 12/Textures/Color Maps/asphalt.jpg"

# Apply the bump texture to the specified material.
connect_shader_edge_to_bump(material_name, texture_file_path)
```

# End of Material\Apply Library Texture to Diffuse Material Bump.py

# Material\Apply Library Texture to Diffuse Material Color.py
<a name="material-apply-library-texture-to-diffuse-material-color"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Assign Texture from Library to the Color of a Diffuse Material.
``` python
import lux

def connect_texture_to_diffuse_color(material_name, texture_file_path):
    """
    Connects a texture file to the diffuse color parameter of a given material.

    Parameters:
    material_name (str): The name of the material to apply the texture to.
    texture_file_path (str): The file path of the texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Retrieve the texture parameter from the texture node.
    file_param = texture_node.getParameter("texture")  # Assuming 'texture' is the correct parameter.
    if file_param:
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    else:
        print("Texture parameter not found.")
        return

    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    connected = False
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the texture node to the diffuse parameter of the shader node.
            graph.newEdge(source=texture_node, target=shader_node, param="diffuse")
            print(f"Texture '{texture_file_path}' connected to the diffuse color of '{material_name}'.")
            connected = True
            break

    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
material_name = "Cube Material"
texture_file_path = "C:/Users/Public/Documents/KeyShot 12/Textures/Color Maps/asphalt.jpg"
connect_texture_to_diffuse_color(material_name, texture_file_path)
```

# End of Material\Apply Library Texture to Diffuse Material Color.py

# Material\Batch Multi-Material Diffuse Sub-Material Assign Texture Default Units m.py
<a name="material-batch-multi-material-diffuse-sub-material-assign-texture-default-units-m"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script for automating multi-material creation and Sub-Material (Diffuse) texture application in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.
import os  # Import the os module for file path operations.

def display_material_selection_and_directory():
    """
    Display a dialog for the user to select materials and a directory for textures.
    """
    scene_materials = lux.getSceneMaterials()  # Get all materials in the current scene.
    if not scene_materials:
        lux.getMessageBox("No materials found in the scene.", "Error", lux.MESSAGE_BOX_CRITICAL)
        return None, None

    # Create a list of tuples for each material for the dialog.
    material_values = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    directory_values = [("directory", lux.DIALOG_FOLDER, "Bitmap directory:", None)]
    # Display a dialog to get user's selection of materials and directory.
    opts = lux.getInputDialog(title="Select Material and Directory", values=material_values + directory_values)
    if not opts:
        return None, None  # Return None if the user does not make a selection.

    selected_materials = [mat for mat, selected in opts.items() if selected and mat in scene_materials]
    directory = opts['directory']
    return selected_materials, directory

def create_and_apply_texture(material_name, texture_path):
    """
    Create a new material node and apply a texture to it.

    :param material_name: Name of the material to apply the texture to.
    :param texture_path: Path of the texture file.
    """
    material_graph = lux.getMaterialGraph(material_name)  # Get the material graph.
    texture_node = material_graph.newNode('__texture')  # Create a new texture node.
    texture_node.getParameter('texture').setValue(texture_path)  # Set the texture file.

    # Connect the texture node to the color parameter of the material.
    for node in material_graph.getNodes():
        for param in node.getParameters():
            if param.getType() in [lux.PARAMETER_TYPE_COLOR, lux.PARAMETER_TYPE_COLORALPHA]:
                material_graph.newEdge(texture_node, node, param.getName())
                return

def process_material(material_name, directory):
    """
    Process each material to create sub-materials with textures from the directory.

    :param material_name: Name of the material to process.
    :param directory: Directory containing texture files.
    """
    bitmap_files = [f for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in ['.png', '.jpg', '.jpeg']]
    if not bitmap_files:
        print(f"No bitmap files found in directory: {directory}")
        return

    # Convert to MultiMaterial if necessary.
    multi_material = lux.getMultiMaterial(material_name)
    if not multi_material:
        lux.createMultiMaterial(material_name)
        multi_material = lux.getMultiMaterial(material_name)

    # Create a new sub-material for each texture file and apply the texture.
    for file in bitmap_files:
        texture_path = os.path.join(directory, file)
        new_material_name = f"{material_name}_{os.path.splitext(file)[0]}"
        lux.createSceneMaterial(new_material_name)  # Create a new material.
        create_and_apply_texture(new_material_name, texture_path)  # Apply texture.

        # Update the multi-material with the new sub-material.
        sub_materials = multi_material.getSubMaterials()
        sub_materials.append(new_material_name)
        multi_material.setSubMaterials(sub_materials)

        print(f"Added sub-material '{new_material_name}' with texture '{file}' to '{material_name}'.")

def main():
    """
    Main function to execute the script.
    """
    selected_materials, directory = display_material_selection_and_directory()
    if not selected_materials or not directory:
        print("Operation cancelled or invalid input.")
        return

    # Process each selected material.
    for material_name in selected_materials:
        process_material(material_name, directory)

# Execute the main function.
main()
```

# End of Material\Batch Multi-Material Diffuse Sub-Material Assign Texture Default Units m.py

# Material\Batch Multi-Material Diffuse Sub-Material Assign Texture Scale Units cm.py
<a name="material-batch-multi-material-diffuse-sub-material-assign-texture-scale-units-cm"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.0
# Script for automating the creation of sub-materials and applying textures with UV scale adjustment in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.
import os  # Import the os module for file path operations.

def display_material_selection_and_directory():
    """
    Display a dialog for the user to select materials and a directory for textures.
    """
    scene_materials = lux.getSceneMaterials()  # Get all materials in the current scene.
    if not scene_materials:
        lux.getMessageBox("No materials found in the scene.", "Error", lux.MESSAGE_BOX_CRITICAL)
        return None, None

    # Create dialog fields for material selection and directory.
    material_values = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    directory_values = [("directory", lux.DIALOG_FOLDER, "Bitmap directory:", None)]
    opts = lux.getInputDialog(title="Select Material and Directory", values=material_values + directory_values)
    if not opts:
        return None, None  # Return None if the user does not make a selection.

    selected_materials = [mat for mat, selected in opts.items() if selected and mat in scene_materials]
    directory = opts['directory']
    return selected_materials, directory

def create_and_apply_texture(material_name, texture_path):
    """
    Create a new material node, apply a texture, and set UV scale.

    :param material_name: Name of the material to apply the texture to.
    :param texture_path: Path of the texture file.
    """
    material_graph = lux.getMaterialGraph(material_name)  # Get the material graph.
    texture_node = material_graph.newNode('__texture')  # Create a new texture node.
    texture_node.getParameter('texture').setValue(texture_path)  # Set the texture file.

    # Set the UV scale for the texture.
    texture_node.getParameter("uv_scale_u").setValue(0.01)  # Set scale for U coordinate.
    texture_node.getParameter("uv_scale_v").setValue(0.01)  # Set scale for V coordinate.

    # Connect the texture node to the color parameter of the material.
    for node in material_graph.getNodes():
        for param in node.getParameters():
            if param.getType() in [lux.PARAMETER_TYPE_COLOR, lux.PARAMETER_TYPE_COLORALPHA]:
                material_graph.newEdge(texture_node, node, param.getName())
                return

def process_material(material_name, directory):
    """
    Process each material to create sub-materials with textures from the directory.

    :param material_name: Name of the material to process.
    :param directory: Directory containing texture files.
    """
    bitmap_files = [f for f in os.listdir(directory) if os.path.splitext(f)[1].lower() in ['.png', '.jpg', '.jpeg']]
    if not bitmap_files:
        print(f"No bitmap files found in directory: {directory}")
        return

    # Convert to MultiMaterial if necessary.
    multi_material = lux.getMultiMaterial(material_name)
    if not multi_material:
        lux.createMultiMaterial(material_name)
        multi_material = lux.getMultiMaterial(material_name)

    # Create a new sub-material for each texture file and apply the texture with UV scaling.
    for file in bitmap_files:
        texture_path = os.path.join(directory, file)
        new_material_name = f"{material_name}_{os.path.splitext(file)[0]}"
        lux.createSceneMaterial(new_material_name)  # Create a new material.
        create_and_apply_texture(new_material_name, texture_path)  # Apply texture.

        # Update the multi-material with the new sub-material.
        sub_materials = multi_material.getSubMaterials()
        sub_materials.append(new_material_name)
        multi_material.setSubMaterials(sub_materials)

        print(f"Added sub-material '{new_material_name}' with texture '{file}' to '{material_name}'.")

def main():
    """
    Main function to execute the script.
    """
    selected_materials, directory = display_material_selection_and_directory()
    if not selected_materials or not directory:
        print("Operation cancelled or invalid input.")
        return

    # Process each selected material.
    for material_name in selected_materials:
        process_material(material_name, directory)

# Execute the main function.
main()
```

# End of Material\Batch Multi-Material Diffuse Sub-Material Assign Texture Scale Units cm.py

# Material\Batch Save All Scene Materials to KS2024 Material Library Agnostic.py
<a name="material-batch-save-all-scene-materials-to-ks2024-material-library-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to save the scene's materials and multi-material sub-materials to the material library in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system.
    """
    if os.name == 'nt':  # Windows
        library_path = os.path.join(os.environ['PUBLIC'], "Documents", "KeyShot")
    else:  # macOS and Unix/Linux
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot")
    return library_path

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The parent node from which children are to be gathered.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def save_sub_materials_to_library(multi_material_name, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: Name of the multi-material.
    :param saved_materials: Set of already saved material names to avoid duplication.
    """
    library_path = get_library_path()  # Get the library path based on the OS.
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Retrieve sub-materials of the multi-material.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        # Check if the sub-material has not been saved already.
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene():
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Iterate through all nodes in the scene and process their materials.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name:
            save_sub_materials_to_library(material_name, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    # Process the currently open KeyShot scene.
    process_current_scene()

# Execute the main function.
main()
```

# End of Material\Batch Save All Scene Materials to KS2024 Material Library Agnostic.py

# Material\Batch Save All Scene Materials to Library Agnostic 2024.py
<a name="material-batch-save-all-scene-materials-to-library-agnostic-2024"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.1
# Script to save all scene materials to the material libray.
# Compatible with KeyShot 2024 and higher.
``` python
import os
import lux

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system.
    """
    library_path = os.path.join(os.environ.get('PUBLIC', ''), "Documents", "KeyShot")
    if not os.path.exists(library_path):
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot")
    return library_path

def get_all_children(node):
    """
    Recursively get all children of a node.
    """
    all_children = []
    try:
        children = node.getChildren()
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))
    except Exception:
        pass
    return all_children

def save_material(material_name, saved_materials, library_path):
    """
    Saves a material to the library if it hasn't been saved yet.
    """
    if material_name not in saved_materials:
        lux.saveMaterial(name=material_name, folder=library_path)
        print(f"Saved material '{material_name}' to library at '{library_path}'.")
        saved_materials.add(material_name)

def save_sub_materials_to_library(multi_material_name, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.
    """
    library_path = get_library_path()
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        save_material(sub_material.getName(), saved_materials, library_path)

def process_current_scene():
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name:
            save_sub_materials_to_library(material_name, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    process_current_scene()

main()
```

# End of Material\Batch Save All Scene Materials to Library Agnostic 2024.py

# Material\Batch Save All Scene Materials to Material Library Agnostic.py
<a name="material-batch-save-all-scene-materials-to-material-library-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to save the scene's materials and multi-material sub-materials to the material library in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system.
    """
    if os.name == 'nt':  # Windows
        library_path = os.path.join(os.environ['PUBLIC'], "Documents", "KeyShot 12")
    else:  # macOS and Unix/Linux
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot 12")
    return library_path

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The parent node from which children are to be gathered.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def save_sub_materials_to_library(multi_material_name, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: Name of the multi-material.
    :param saved_materials: Set of already saved material names to avoid duplication.
    """
    library_path = get_library_path()  # Get the library path based on the OS.
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Retrieve sub-materials of the multi-material.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        # Check if the sub-material has not been saved already.
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene():
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Iterate through all nodes in the scene and process their materials.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name:
            save_sub_materials_to_library(material_name, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    # Process the currently open KeyShot scene.
    process_current_scene()

# Execute the main function.
main()
```

# End of Material\Batch Save All Scene Materials to Material Library Agnostic.py

# Material\Batch Save All Scene Materials to Material Library.py
<a name="material-batch-save-all-scene-materials-to-material-library"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.1
# Script to save the scene's materials and multi-material sub-materials to the material library in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The parent node from which children are to be gathered.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def save_sub_materials_to_library(multi_material_name, library_path, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: Name of the multi-material.
    :param library_path: Path to the material library where materials will be saved.
    :param saved_materials: Set of already saved material names to avoid duplication.
    """
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Retrieve sub-materials of the multi-material.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        # Check if the sub-material has not been saved already.
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene(library_path):
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.

    :param library_path: Path to the material library where materials will be saved.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Iterate through all nodes in the scene and process their materials.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name:
            save_sub_materials_to_library(material_name, library_path, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    # Define the library path based on the operating system.
    library_path = "C:\\Users\\Public\\Documents\\KeyShot 12\\Materials"

    # Process the currently open KeyShot scene.
    process_current_scene(library_path)

# Execute the main function.
main()
```

# End of Material\Batch Save All Scene Materials to Material Library.py

# Material\Batch Save Multi-Material Sub-Materials to KS2024 Material Library Agnostic.py
<a name="material-batch-save-multi-material-sub-materials-to-ks2024-material-library-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Script to save multi-material sub-materials to the material library in KeyShot, compatible with PC and Apple systems.
``` python
import os
import platform  # Module to detect the operating system.
import lux  # Import the KeyShot built-in module 'lux'.

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The node from which to start the recursion.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def is_multi_material(material_name):
    """
    Check if the given material is a multi-material.

    :param material_name: The name of the material to check.
    :return: True if the material is a multi-material, False otherwise.
    """
    material_graph = lux.getMaterialGraph(name=material_name)
    return material_graph and len(material_graph.getMaterialNodes()) > 1  # True if more than one sub-material.

def save_sub_materials_to_library(multi_material_name, library_path, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: The name of the multi-material.
    :param library_path: The library path where the materials will be saved.
    :param saved_materials: A set to keep track of already saved materials.
    """
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Save each sub-material to the library, avoiding duplicates.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene(library_path):
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.

    :param library_path: The library path where the materials will be saved.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Process each node in the scene.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name and is_multi_material(material_name):
            save_sub_materials_to_library(material_name, library_path, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    # Determine the library path based on the operating system.
    if platform.system() == "Windows":
        library_path = "C:/Users/Public/Documents/KeyShot/Materials"
    else:  # macOS and other Unix-like systems
        library_path = "/Library/Application Support/KeyShot/Materials"

    # Process the currently open KeyShot scene.
    process_current_scene(library_path)

# Execute the main function.
main()
```

# End of Material\Batch Save Multi-Material Sub-Materials to KS2024 Material Library Agnostic.py

# Material\Batch Save Multi-Material Sub-Materials to Material Library Agnostic.py
<a name="material-batch-save-multi-material-sub-materials-to-material-library-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.2
# Script to save multi-material sub-materials to the material library in KeyShot, compatible with PC and Apple systems.
``` python
import os
import platform  # Module to detect the operating system.
import lux  # Import the KeyShot built-in module 'lux'.

def get_all_children(node):
    """
    Recursively get all children of a node.

    :param node: The node from which to start the recursion.
    :return: A list of all child nodes.
    """
    all_children = []
    try:
        children = node.getChildren()  # Retrieve direct children of the node.
        all_children.extend(children)
        for child in children:
            all_children.extend(get_all_children(child))  # Recursive call for children of each child.
    except Exception:
        pass  # Ignore any errors during the process.
    return all_children

def is_multi_material(material_name):
    """
    Check if the given material is a multi-material.

    :param material_name: The name of the material to check.
    :return: True if the material is a multi-material, False otherwise.
    """
    material_graph = lux.getMaterialGraph(name=material_name)
    return material_graph and len(material_graph.getMaterialNodes()) > 1  # True if more than one sub-material.

def save_sub_materials_to_library(multi_material_name, library_path, saved_materials):
    """
    Save all sub-materials of a multi-material while avoiding duplicates.

    :param multi_material_name: The name of the multi-material.
    :param library_path: The library path where the materials will be saved.
    :param saved_materials: A set to keep track of already saved materials.
    """
    material_graph = lux.getMaterialGraph(name=multi_material_name)
    if not material_graph:
        print(f"Multi-material '{multi_material_name}' not found.")
        return

    # Save each sub-material to the library, avoiding duplicates.
    sub_materials = material_graph.getMaterialNodes()
    for sub_material in sub_materials:
        sub_material_name = sub_material.getName()
        if sub_material_name not in saved_materials:
            lux.saveMaterial(name=sub_material_name, folder=library_path)
            print(f"Saved sub-material '{sub_material_name}' to library at '{library_path}'.")
            saved_materials.add(sub_material_name)

def process_current_scene(library_path):
    """
    Process the currently open KeyShot file and avoid saving duplicate materials.

    :param library_path: The library path where the materials will be saved.
    """
    saved_materials = set()
    root_node = lux.getSceneTree()
    all_nodes = get_all_children(root_node)

    # Process each node in the scene.
    for node in all_nodes:
        material_name = node.getMaterial()
        if material_name and is_multi_material(material_name):
            save_sub_materials_to_library(material_name, library_path, saved_materials)

def main():
    """
    Main function to execute the script.
    """
    # Determine the library path based on the operating system.
    if platform.system() == "Windows":
        library_path = "C:/Users/Public/Documents/KeyShot 12/Materials"
    else:  # macOS and other Unix-like systems
        library_path = "/Library/Application Support/KeyShot 12/Materials"

    # Process the currently open KeyShot scene.
    process_current_scene(library_path)

# Execute the main function.
main()
```

# End of Material\Batch Save Multi-Material Sub-Materials to Material Library Agnostic.py

# Material\Change IES Light Color and File Agnostic.py
<a name="material-change-ies-light-color-and-file-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Change IES Light Color and File
``` python
import os
import lux

def get_ies_library_path():
    """
    Determines the path to the IES Profiles based on the operating system.
    """
    if os.name == 'nt':  # Windows
        library_path = os.path.join(os.environ['PUBLIC'], "Documents", "KeyShot 12", "Textures", "IES Profiles")
    else:  # macOS and Unix/Linux
        library_path = os.path.join(os.path.expanduser('~'), "Library", "Application Support", "KeyShot 12", "Textures", "IES Profiles")
    return library_path

def display_material_selection():
    scene_materials = lux.getSceneMaterials()
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def change_ies_light_properties(material_name, new_color, ies_file_name):
    ies_library_path = get_ies_library_path()  # Get the IES library path based on the OS.
    new_ies_file = os.path.join(ies_library_path, ies_file_name)  # Full path to the IES file.

    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    color_changed, file_changed = False, False
    for shader_node in material_graph.getNodes():
        try:
            if not color_changed:
                color_param = shader_node.getParameter('color')
                if color_param and color_param.getType() == lux.PARAMETER_TYPE_COLOR:
                    color_param.setValue(new_color)
                    print(f"IES light color in '{material_name}' changed to {new_color}.")
                    color_changed = True

            if not file_changed:
                file_param = shader_node.getParameter('file')
                if file_param and file_param.getType() == lux.PARAMETER_TYPE_STRING:
                    file_param.setValue(new_ies_file)
                    print(f"IES file in '{material_name}' changed to {new_ies_file}.")
                    file_changed = True

            if color_changed and file_changed:
                return

        except Exception as e:
            print(f"Error setting IES light properties in shader node: {e}")

def main():
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_color = (1.0, 1.0, 1.0)  # Example: White color in RGB format
    ies_file_name = "IES Spot Light/keyshot_spot_45.ies"  # Relative path from the IES Profiles directory

    for material_name in selected_materials:
        change_ies_light_properties(material_name, new_color, ies_file_name)

main()
```

# End of Material\Change IES Light Color and File Agnostic.py

# Material\Color Gradient ShaderEdge Cube Material Color Connect.py
<a name="material-color-gradient-shaderedge-cube-material-color-connect"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example of graphing a Color Gradient shader edge node.

import lux  # Import the KeyShot built-in module 'lux'.

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return

    # Set up the Color Gradient node if necessary.
    # This step is customizable based on specific gradient requirements.

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "Cube Material"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)


# End of Material\Color Gradient ShaderEdge Cube Material Color Connect.py

# Material\Color Gradient ShaderEdge Diffuse Material Color Connect.py
<a name="material-color-gradient-shaderedge-diffuse-material-color-connect"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example of graphing a Color Gradient shader edge node.

import lux  # Import the KeyShot built-in module 'lux'.

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return

    # Set up the Color Gradient node if necessary.
    # This step is customizable based on specific gradient requirements.

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "ColorGradient Rainbow"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)
```

# End of Material\Color Gradient ShaderEdge Diffuse Material Color Connect.py

# Material\Create Python Material Output Script.py
<a name="material-create-python-material-output-script"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Create KeyShot Material
``` python
def save_keyshot_material_creation_script():
    # Define the name of the output Python script file
    output_script_name = "C:/Users/Public/Documents/KeyShot/Scripts/create_keyshot_material.py"

    # Script content to create a KeyShot material
    script_content = """
import lux

def create_material_with_metadata():
    # Ensure we have an active scene
    scene = lux.getSceneTree()

    # Create a new material graph for a multi-material
    material_name = "Custom Multi-Material"
    material_graph = lux.newMaterial(material_name, multi_material=True)
    
    # Example: Adding a Diffuse material node
    diffuse_node = material_graph.newNode(lux.SHADER_TYPE_DIFFUSE)
    diffuse_node.setParameter('diffuse', (0.3025, 0.3025, 0.3025, 1.0))
    diffuse_node.setParameter('roughness', 0.0)
    material_graph.connect(material_graph.getRoot(), diffuse_node, 'surface')

    # Example: Adding a Glass material node
    glass_node = material_graph.newNode(lux.SHADER_TYPE_GLASS)
    glass_node.setParameter('ior', 1.5)
    glass_node.setParameter('transmission', (0.3, 0.3, 0.3))
    glass_node.setParameter('two sided', True)
    material_graph.connect(material_graph.getRoot(), glass_node, 'surface')

    # Apply the material to an object, replace 'YourObjectNameHere' with the actual object name
    object_name = "YourObjectNameHere"
    obj = scene.find(object_name)
    if obj:
        obj.applyMaterial(material_name)
    else:
        print(f"Object '{object_name}' not found in the scene.")

create_material_with_metadata()
    """

    # Write the script content to the output file
    with open(output_script_name, 'w') as file:
        file.write(script_content)

    return output_script_name

# Save the KeyShot material creation script
script_file_path = save_keyshot_material_creation_script()
print(f"KeyShot material creation script saved as: {script_file_path}")
```

# End of Material\Create Python Material Output Script.py

# Material\Delete Unused Nodes in Material Graph.py
<a name="material-delete-unused-nodes-in-material-graph"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Delete unused nodes from the material graph.  May need to be run multiple times.
``` python
import lux

MAX_ITERATIONS = 10  # Maximum number of cleanup iterations

def has_material_connections(node):
    """Check if a material node has connections."""
    input_edges = node.getInputEdges()
    output_edges = node.getOutputEdges()
    return bool(input_edges or output_edges)

def cleanup_unused_material_nodes(material_graph):
    """Clean up unconnected nodes within a material graph."""
    nodes_to_remove = []
    try:
        nodes = material_graph.getNodes()
        for node in nodes:
            if not has_material_connections(node):
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            material_graph.removeNode(node)
            print(f"Removed node: {node.getName()} from material: {material_graph.getMaterialName()}")
    except Exception as e:
        print(f"Exception encountered while processing material graph: {e}")
    return bool(nodes_to_remove)

def cleanup_scene():
    """Main function to clean up the scene."""
    any_changes = True
    iteration_count = 0

    while any_changes and iteration_count < MAX_ITERATIONS:
        any_changes = False
        iteration_count += 1

        # Cleanup material nodes
        material_names = lux.getSceneMaterials()
        for material_name in material_names:
            try:
                material_graph = lux.getMaterialGraph(name=material_name)
                if material_graph:
                    if cleanup_unused_material_nodes(material_graph):
                        any_changes = True
            except Exception as e:
                print(f"Exception encountered while processing material {material_name}: {e}")

    if iteration_count >= MAX_ITERATIONS:
        lux.getMessageBox("Scene cleanup stopped after reaching the maximum number of iterations.", "Cleanup Stopped", lux.MESSAGE_BOX_WARNING)
    else:
        lux.getMessageBox("Scene cleanup of unconnected nodes completed.", "Cleanup Complete", lux.MESSAGE_BOX_INFO)

cleanup_scene()
```

# End of Material\Delete Unused Nodes in Material Graph.py

# Material\Delete Unused Shader Nodes.py
<a name="material-delete-unused-shader-nodes"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 1.1.0
# Script that deletes unused shader nodes.  May need to be run multiple times.  Use lux.getSceneMaterials() to locate unused material shaders.
``` python
import lux

MAX_ITERATIONS = 10  # Maximum number of cleanup iterations

def has_material_connections(node):
    """Check if a material node has connections."""
    input_edges = node.getInputEdges()
    output_edges = node.getOutputEdges()
    return bool(input_edges or output_edges)

def cleanup_unused_material_nodes(material_graph):
    """Clean up unconnected nodes within a material graph."""
    nodes_to_remove = []
    try:
        nodes = material_graph.getNodes()
        for node in nodes:
            if not has_material_connections(node):
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            material_graph.removeNode(node)
            print(f"Removed node: {node.getName()} from material: {material_graph.getMaterialName()}")
    except Exception as e:
        print(f"Exception encountered while processing material graph: {e}")
    return bool(nodes_to_remove)

def cleanup_scene():
    """Main function to clean up the scene."""
    any_changes = True
    iteration_count = 0

    while any_changes and iteration_count < MAX_ITERATIONS:
        any_changes = False
        iteration_count += 1

        # Cleanup material nodes
        material_names = lux.getSceneMaterials()
        for material_name in material_names:
            try:
                material_graph = lux.getMaterialGraph(material_name)
                if material_graph:
                    if cleanup_unused_material_nodes(material_graph):
                        any_changes = True
            except Exception as e:
                print(f"Exception encountered while processing material {material_name}: {e}")

    if iteration_count >= MAX_ITERATIONS:
        lux.getMessageBox("Scene cleanup stopped after reaching the maximum number of iterations.", "Cleanup Stopped", lux.MESSAGE_BOX_WARNING)
    else:
        lux.getMessageBox("Scene cleanup of unconnected nodes completed.", "Cleanup Complete", lux.MESSAGE_BOX_INFO)

cleanup_scene()
```

# End of Material\Delete Unused Shader Nodes.py

# Material\Delete Unused Shader and Material Graph Nodes.py
<a name="material-delete-unused-shader-and-material-graph-nodes"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 1.1.0
# Script that deletes unused material shader and material graph nodes. May need to be run multiple times. Uses lux.getSceneMaterials() to locate unused material shaders.
``` python
import lux

MAX_ITERATIONS = 10  # Maximum number of cleanup iterations

def has_material_connections(node):
    """Check if a material node has connections."""
    input_edges = node.getInputEdges()
    output_edges = node.getOutputEdges()
    return bool(input_edges or output_edges)

def cleanup_unused_material_nodes(material_graph):
    """Clean up unconnected nodes within a material graph."""
    nodes_to_remove = []
    try:
        nodes = material_graph.getNodes()
        for node in nodes:
            if not has_material_connections(node):
                nodes_to_remove.append(node)
        for node in nodes_to_remove:
            material_graph.removeNode(node)
            print(f"Removed node: {node.getName()} from material: {material_graph.getMaterialName()}")
    except Exception as e:
        print(f"Exception encountered while processing material graph: {e}")
    return bool(nodes_to_remove)

def cleanup_scene():
    """Main function to clean up the scene."""
    any_changes = True
    iteration_count = 0

    while any_changes and iteration_count < MAX_ITERATIONS:
        any_changes = False
        iteration_count += 1

        # Cleanup material nodes
        material_names = lux.getSceneMaterials()
        for material_name in material_names:
            try:
                material_graph = lux.getMaterialGraph(name=material_name)
                if material_graph:
                    if cleanup_unused_material_nodes(material_graph):
                        any_changes = True
            except Exception as e:
                print(f"Exception encountered while processing material {material_name}: {e}")

    if iteration_count >= MAX_ITERATIONS:
        lux.getMessageBox("Scene cleanup stopped after reaching the maximum number of iterations.", "Cleanup Stopped", lux.MESSAGE_BOX_WARNING)
    else:
        lux.getMessageBox("Scene cleanup of unconnected nodes completed.", "Cleanup Complete", lux.MESSAGE_BOX_INFO)

cleanup_scene()
```

# End of Material\Delete Unused Shader and Material Graph Nodes.py

# Material\Material Diffuse Color Apply Texture Example Agnostic.py
<a name="material-material-diffuse-color-apply-texture-example-agnostic"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to apply a texture from the library to the diffuse color of a material in KeyShot.
``` python
import os
import lux  # Import the KeyShot built-in module 'lux'.

def get_library_path():
    """
    Determines the KeyShot "Resources Library" path based on the operating system.
    """
    if os.name == 'nt':  # Windows
        library_path = os.path.join(os.environ['PUBLIC'], "Documents", "KeyShot 12")
    else:  # macOS and Unix/Linux
        library_path = "/Library/Application Support/KeyShot12"
    return library_path

def connect_shader_edge_to_diffuse_color(material_name, texture_relative_path):
    """
    Connects a texture file to the diffuse color parameter of a given material.

    :param material_name: The name of the material to apply the texture to.
    :param texture_relative_path: The relative path of the texture from the KeyShot "Resources Library" directory.
    """
    library_path = get_library_path()  # Get the library path based on the OS.
    texture_file_path = os.path.join(library_path, texture_relative_path)  # Full path to the texture file.

    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Retrieve the texture parameter from the texture node.
    file_param = texture_node.getParameter("texture")  # Assuming 'texture' is the correct parameter.
    if file_param:
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    else:
        print("Texture parameter not found.")
        return

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        if shader_node.getParameter("diffuse"):
            # Connect the texture node to the diffuse parameter of the shader node.
            graph.newEdge(source=texture_node, target=shader_node, param="diffuse")
            print("Shader edge successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name and relative path to the texture file.
material_name = "Cube Material"
texture_relative_path = "Textures/Color Maps/asphalt.jpg"

# Apply the texture to the diffuse color of the specified material.
connect_shader_edge_to_diffuse_color(material_name, texture_relative_path)
```

# End of Material\Material Diffuse Color Apply Texture Example Agnostic.py

# Material\Material Diffuse Color Apply Texture Example.py
<a name="material-material-diffuse-color-apply-texture-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to apply a texture to the diffuse color of a material in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edge_to_diffuse_color(material_name, texture_file_path):
    """
    Connects a texture file to the diffuse color parameter of a given material.

    :param material_name: The name of the material to apply the texture to.
    :param texture_file_path: The file path of the texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Retrieve the texture parameter from the texture node.
    file_param = texture_node.getParameter("texture")  # Assuming 'texture' is the correct parameter.
    if file_param:
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    else:
        print("Texture parameter not found.")
        return

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        if shader_node.getParameter("diffuse"):
            # Connect the texture node to the diffuse parameter of the shader node.
            graph.newEdge(source=texture_node, target=shader_node, param="diffuse")
            print("Shader edge successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name and texture file path.
material_name = "Cube Material"
texture_file_path = "C:/Users/Public/Documents/KeyShot 12/Textures/Color Maps/asphalt.jpg"

# Apply the texture to the diffuse color of the specified material.
connect_shader_edge_to_diffuse_color(material_name, texture_file_path)
```

# End of Material\Material Diffuse Color Apply Texture Example.py

# Material\Material Diffuse Color Change Example.py
<a name="material-material-diffuse-color-change-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example Change Diffuse Material Color
``` python
import lux

def display_material_selection():
    scene_materials = lux.getSceneMaterials()
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def change_diffuse_color(material_name, new_color):
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    for shader_node in material_graph.getNodesFromType('lux_diffuse'):
        try:
            diffuse_param = shader_node.getParameter('diffuse')
            if diffuse_param and diffuse_param.getType() == lux.PARAMETER_TYPE_COLORALPHA:
                diffuse_param.setValue(new_color)
                print(f"Diffuse color of '{material_name}' changed to {new_color}.")
                return
        except Exception as e:
            print(f"Error setting diffuse color in shader node: {e}")

def main():
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_color = (1.0, 0.0, 0.0, 1.0)  # Example: Red color with full opacity in RGBA format

    for material_name in selected_materials:
        change_diffuse_color(material_name, new_color)

main()
```

# End of Material\Material Diffuse Color Change Example.py

# Material\Material Diffuse Color Texture Example.py
<a name="material-material-diffuse-color-texture-example"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to apply a texture to the diffuse color of a material in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_shader_edge_to_diffuse_color(material_name, texture_file_path):
    """
    Connects a texture file to the diffuse color parameter of a given material.

    :param material_name: The name of the material to apply the texture to.
    :param texture_file_path: The file path of the texture to apply.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new texture node in the material graph.
    texture_node = graph.newNode(lux.SHADER_TYPE_TEXTURE_MAP)
    if texture_node is None:
        print("Failed to create texture node.")
        return

    # Retrieve the texture parameter from the texture node.
    file_param = texture_node.getParameter("texture")  # Assuming 'texture' is the correct parameter.
    if file_param:
        file_param.setValue(texture_file_path)  # Set the file path of the texture.
    else:
        print("Texture parameter not found.")
        return

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        if shader_node.getParameter("diffuse"):
            # Connect the texture node to the diffuse parameter of the shader node.
            graph.newEdge(source=texture_node, target=shader_node, param="diffuse")
            print("Shader edge successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name and texture file path.
material_name = "Cube Material"
texture_file_path = "C:/Users/Public/Documents/KeyShot 12/Textures/Color Maps/asphalt.jpg"

# Apply the texture to the diffuse color of the specified material.
connect_shader_edge_to_diffuse_color(material_name, texture_file_path)
```

# End of Material\Material Diffuse Color Texture Example.py

# Material\Material IES Light Color and File Change 2024.py
<a name="material-material-ies-light-color-and-file-change-2024"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.6
``` python
import lux

def display_material_selection():
    """
    Display a dialog for the user to select materials from the current scene.
    """
    scene_materials = lux.getSceneMaterials()
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def change_ies_light_properties(material_name, new_properties):
    """
    Changes the color and file of IES lights in the specified material.
    """
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    changes_applied = {key: False for key in new_properties}
    for shader_node in material_graph.getNodes():
        try:
            for param_name, param_value in new_properties.items():
                param = shader_node.getParameter(param_name)
                if param and param.getType() == lux.PARAMETER_TYPE_COLOR if param_name == 'color' else lux.PARAMETER_TYPE_STRING:
                    param.setValue(param_value)
                    changes_applied[param_name] = True
                    print(f"IES light {param_name} in '{material_name}' changed to {param_value}.")

            if all(changes_applied.values()):
                return

        except Exception as e:
            print(f"Error setting IES light properties in shader node: {e}")

def main():
    """
    Main function to execute the script.
    """
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_properties = {
        'color': (1.0, 1.0, 1.0),
        'file': "C:/Users/Public/Documents/KeyShot/Textures/IES Profiles/IES Spot Light/keyshot_spot_45.ies"
    }

    for material_name in selected_materials:
        change_ies_light_properties(material_name, new_properties)

main()
```

# End of Material\Material IES Light Color and File Change 2024.py

# Material\Material IES Light Color and File Change.py
<a name="material-material-ies-light-color-and-file-change"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Change IES Light Color and File
``` python
import lux

def display_material_selection():
    scene_materials = lux.getSceneMaterials()
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def change_ies_light_properties(material_name, new_color, new_ies_file):
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    color_changed, file_changed = False, False
    for shader_node in material_graph.getNodes():
        try:
            if not color_changed:
                color_param = shader_node.getParameter('color')
                if color_param and color_param.getType() == lux.PARAMETER_TYPE_COLOR:
                    color_param.setValue(new_color)
                    print(f"IES light color in '{material_name}' changed to {new_color}.")
                    color_changed = True

            if not file_changed:
                file_param = shader_node.getParameter('file')
                if file_param and file_param.getType() == lux.PARAMETER_TYPE_STRING:
                    file_param.setValue(new_ies_file)
                    print(f"IES file in '{material_name}' changed to {new_ies_file}.")
                    file_changed = True

            if color_changed and file_changed:
                return

        except Exception as e:
            print(f"Error setting IES light properties in shader node: {e}")

def main():
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_color = (1.0, 1.0, 1.0)  # Example: White color in RGB format
    new_ies_file = "C:/Users/Public/Documents/KeyShot 12/Textures/IES Profiles/IES Spot Light/keyshot_spot_45.ies"  # Replace with the path to your texture file

    for material_name in selected_materials:
        change_ies_light_properties(material_name, new_color, new_ies_file)

main()
```

# End of Material\Material IES Light Color and File Change.py

# Material\Material Physical Light Color Change.py
<a name="material-material-physical-light-color-change"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Script to change the color of light materials in KeyShot.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def display_material_selection():
    """
    Display a dialog for the user to select materials from the scene.
    """
    scene_materials = lux.getSceneMaterials()  # Get all materials in the current scene.
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    # Create a list of tuples for each material for the dialog.
    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    # Display a dialog to the user to select materials.
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None  # Return None if the user does not make a selection.
    # Return a list of materials selected by the user.
    return [mat for mat, selected in user_selection.items() if selected]

def change_spotlight_color(material_name, new_color):
    """
    Change the color parameter of a spotlight material.

    :param material_name: Name of the material to change.
    :param new_color: New color as an RGB tuple.
    """
    # Get the material graph of the specified material.
    material_graph = lux.getMaterialGraph(name=material_name)
    if not material_graph:
        print(f"Material graph not found for material: {material_name}")
        return

    # Iterate through each shader node in the material graph.
    for shader_node in material_graph.getNodes():
        try:
            # Get the color parameter of the shader node.
            color_param = shader_node.getParameter('color')
            # Check if the color parameter exists and is of type color.
            if color_param and color_param.getType() == lux.PARAMETER_TYPE_COLOR:
                color_param.setValue(new_color)  # Set the new color.
                print(f"Spotlight color of '{material_name}' changed to {new_color}.")
                return
        except Exception as e:
            print(f"Error setting spotlight color in shader node: {e}")

def main():
    """
    Main function to execute the script.
    """
    # Get the user's selection of materials.
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    new_color = (1.0, 1.0, 1.0)  # Define the new color (white in this case).

    # Change the spotlight color for each selected material.
    for material_name in selected_materials:
        change_spotlight_color(material_name, new_color)

# Execute the main function.
main()
```

# End of Material\Material Physical Light Color Change.py

# Material\Saves All Materials to the Library.py
<a name="material-saves-all-materials-to-the-library"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.2.1
# Script to save all scene materials to the material libray.
# Compatible with KeyShot 2024 and higher.
``` python
import lux
import os

def load_environment_from_library(env_filename):
    """
    Loads an environment from the KeyShot library and sets it as the active environment.
    """
    library_envs = lux.getLibraryEnvironments()
    full_env_path = None
    for lib_env_path in library_envs:
        if env_filename.lower() in os.path.basename(lib_env_path).lower():
            full_env_path = lib_env_path
            break
    
    if full_env_path is not None:
        try:
            env_name = os.path.splitext(env_filename)[0].replace(" ", "_")
            new_env = lux.newEnvironment(name=env_name, activate=True)
            if new_env.setLightingEnvironment(full_env_path):
                print(f"Environment '{env_filename}' has been successfully loaded and set.")
                return new_env
            else:
                print(f"Failed to apply environment '{env_filename}'.")
        except Exception as e:
            print(f"An error occurred while setting the environment '{env_filename}': {e}")
    else:
        print(f"The environment '{env_filename}' could not be found in the KeyShot library.")
    return None

def set_environment_parameters(env, parameters):
    """
    Sets various parameters for the specified environment.
    """
    try:
        if env:
            for param, value in parameters.items():
                if isinstance(value, tuple):
                    getattr(env, f"set{param}")(*value)
                else:
                    getattr(env, f"set{param}")(value)
            lux.setActiveEnvironment(env.getName())
            print(f"Parameters for environment '{env.getName()}' have been successfully set.")
        else:
            print("Environment not found.")
    except Exception as e:
        print(f"An error occurred while setting parameters for environment '{env.getName()}': {e}")

def configure_environment():
    """
    Configures the "3 Panels Straight 4K" environment with specific parameters.
    """
    env_filename = "3 Panels Straight 4K.klf"
    parameters = {
        'Brightness': 1.0,
        'Size': 300.0,
        'Height': 0.0,
        'Rotation': 0.0,
        'BackgroundColor': ((255, 255, 255),),  # Needs to be a tuple of a tuple for colors
        'GroundSize': 0.01,
        'GroundShadows': False,
        'OcclusionGroundShadows': False,
        'GroundReflections': False,
        'FlattenGround': False
    }
    
    environment = load_environment_from_library(env_filename)
    if environment:
        set_environment_parameters(environment, parameters)

configure_environment()
```

# End of Material\Saves All Materials to the Library.py

# Material\ShaderEdge Connect.py
<a name="material-shaderedge-connect"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example of graphing a Color Gradient shader edge node.
``` python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return

    # Set up the Color Gradient node if necessary.
    # This step is customizable based on specific gradient requirements.

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "ColorGradient Rainbow"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)
```

# End of Material\ShaderEdge Connect.py

# Model\Delete Model Set by Name.py
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

# Model\Hide All Model Set Children.py
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

# Model\Hide All Model Sets Children.py
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

# Model\Hide All Model Sets and Children.py
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

# Model\Hide and Show Model Sets.py
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

# Model\Hides Node by Name.py
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

# Model\Model Set Remove Default .py
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

# Model\Model Set Renamer.py
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

# Model\Model Translate and Rotate Example.py
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

# Model\New Model Set Template.py
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

# Model\Product Model Sets.py
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

# Model\Show All Model Sets Children.py
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

# Model\Show All Model Sets.py
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

# Model\Show Model Set.py
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

# Model\Transform Model Sets.py
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

# Naming\Batch Rename Find Replace GUI.py
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

# Naming\Batch Rename Material Clashing Node Names.py
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

# Naming\Batch Rename Model Sets.py
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

# Naming\Batch Rename Rhino CAD.py
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

# Naming\Batch Rename Rhino Clashing Node Names Remove Underscores Colons.py
<a name="naming-batch-rename-rhino-clashing-node-names-remove-underscores-colons"></a>
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

# Naming\Rename Clashing Node Names.py
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

# Naming\Rename Model Sets per Imported CAD.py
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

# Naming\Rename ModelSets Manual.py
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

# Naming\Renames Nodes Parenthesis.py
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

# Render\Add To Queue.py
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


# End of Render\Add To Queue.py

# Render\Batch Render Incrmental Screenshots.py
<a name="render-batch-render-incrmental-screenshots"></a>
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

# Render\Queue Render And Name Per Image Style.py
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

# Render\Queue Render SwapToggle Aspect Ratio.py
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

# Render\Render Images Commented.py
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

# Render\Render Optimal Ambient Occlusion Pass.py
<a name="render-render-optimal-ambient-occlusion-pass"></a>
# -*- coding: utf-8 -*-
# AUTHOR LUX DT ChatGPT
# VERSION 1.18.2
# DESCRIPTION: This script sets up a scene in KeyShot 2024 and higher for ambient occlusion rendering.
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

# Render\Render SwapToggle Aspect Ratio.py
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

# Render\Screenshot.py
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


# End of Render\Screenshot.py

# Scripts_Lux\Create Standard Views.py
<a name="scripts_lux-create-standard-views"></a>
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


# End of Scripts_Lux\Create Standard Views.py

# Scripts_Lux\Encode Video.py
<a name="scripts_lux-encode-video"></a>
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

# Scripts_Lux\Random Scattering.py
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

# Scripts_Lux\Render Ambient Occlusion.py
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

# Scripts_Lux\Render Animation Passes.py
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

# Scripts_Lux\Render Images.py
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

# Scripts_Lux\Render Panoramic Frames.py
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

# Settings\Lighting Settings.py
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


# End of Settings\Lighting Settings.py

# Settings\Set Scene Unit.py
<a name="settings-set-scene-unit"></a>
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

# Settings\Set Scene Unit_CM.py
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

# Transform\Apply Ground Transformations.py
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

# Transform\Select Group by Name and Translate Rotate Scale.py
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

# Transform\Select Model by Name and Translate Rotate Scale.py
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

# Transform\Select by Name and Translate and Rotate.py
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

# Transform\Transform Model and Export.py
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

# Transform\Translate Part By Name.py
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

# Transform\Translate and Rotate a Part.py
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

# Batch Create Multi-Material Sub-Materials with Custom Advanced Shader Parameters.py
<a name="batch-create-multi-material-sub-materials-with-custom-advanced-shader-parameters"></a>
# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Batch Create Multi-Material Sub-Materials with Custom Advanced Shader Parameters.
```python
import lux  # Import the KeyShot built-in module 'lux'
import re  # Import the regular expression module for renaming

# Constants for Shader Types
SHADER_TYPE_ADVANCED = 'lux_advanced'

# Constants for Parameter Types
PARAMETER_TYPE_COLOR = 13
PARAMETER_TYPE_COLORALPHA = 14
PARAMETER_TYPE_FLOAT = 4
PARAMETER_TYPE_BOOLEAN = 1
PARAMETER_TYPE_INTEGER = 2
PARAMETER_TYPE_TEXTURE = 14
PARAMETER_TYPE_BUMP = 65539

# Parameters for the Advanced Shader
PARAMETERS = [
    ("alpha", PARAMETER_TYPE_FLOAT, 1.0),
    ("ambient", PARAMETER_TYPE_COLOR, (0, 0, 0)),
    ("apply_bump_to_labels", PARAMETER_TYPE_BOOLEAN, False),
    ("bumpmap", PARAMETER_TYPE_BUMP, None),
    ("diffuse", PARAMETER_TYPE_COLORALPHA, (0, 0, 0, 1.0)),
    ("diffuse_transmission", PARAMETER_TYPE_COLOR, (0, 0, 0)),
    ("fresnel", PARAMETER_TYPE_BOOLEAN, True),
    ("glossy", PARAMETER_TYPE_BOOLEAN, True),
    ("glossy_samples", PARAMETER_TYPE_INTEGER, 9),
    ("ior", PARAMETER_TYPE_FLOAT, 1.5),
    ("opacity_mode", PARAMETER_TYPE_INTEGER, 0),
    ("opacitymap", PARAMETER_TYPE_TEXTURE, None),
    ("opacitymap_mode", PARAMETER_TYPE_INTEGER, 0),
    ("roughness", PARAMETER_TYPE_FLOAT, 0.0),
    ("roughness_transmission", PARAMETER_TYPE_FLOAT, 0.0),
    ("specular", PARAMETER_TYPE_COLOR, (1.0, 1.0, 1.0)),
    ("specular_transmission", PARAMETER_TYPE_COLOR, (0, 0, 0)),
    ("use_diffuse_map_alpha", PARAMETER_TYPE_BOOLEAN, False)
]

def display_material_selection():
    scene_materials = lux.getSceneMaterials()  # Retrieve all materials from the current scene
    if not scene_materials:
        print("No materials found in the scene.")
        return None

    material_selection_elements = [(mat, lux.DIALOG_CHECK, mat, False) for mat in scene_materials]
    user_selection = lux.getInputDialog(title="Select Materials", values=material_selection_elements)
    if not user_selection:
        return None
    return [mat for mat, selected in user_selection.items() if selected]

def display_color_selection():
    colors = {
        "Red": (1.0, 0.0, 0.0, 1.0),
        "Green": (0.0, 1.0, 0.0, 1.0),
        "Blue": (0.0, 0.0, 1.0, 1.0)
    }
    color_selection_elements = [(name, lux.DIALOG_CHECK, name, False) for name in colors.keys()]
    user_selection = lux.getInputDialog(title="Select Colors", values=color_selection_elements)
    if not user_selection:
        return None

    selected_colors = [name for name, selected in user_selection.items() if selected]
    if not selected_colors:
        return None

    return [(name, colors[name]) for name in selected_colors]

def create_sub_material(material_name, color_name, color_value):
    new_material_name = f"{material_name}_{color_name}"
    lux.createSceneMaterial(new_material_name)  # Create a new material
    material_graph = lux.getMaterialGraph(new_material_name)  # Get the material graph

    if material_graph is None:
        print(f"Failed to create material graph for '{new_material_name}'.")
        return None

    advanced_shader = material_graph.newNode(SHADER_TYPE_ADVANCED)
    for param_name, param_type, default_value in PARAMETERS:
        param = advanced_shader.getParameter(param_name)
        if param and not param.isPure():
            param.setValue(default_value)

    diffuse_param = advanced_shader.getParameter('diffuse')
    if diffuse_param and diffuse_param.getType() == PARAMETER_TYPE_COLORALPHA:
        diffuse_param.setValue(color_value)
        print(f"Diffuse color of '{color_name}' sub-material set to {color_value}.")

    material_graph.newEdge(advanced_shader, material_graph.getRoot(), 'surface')
    print(f"Created sub-material '{new_material_name}' with diffuse color {color_value}.")
    return new_material_name

def create_multi_material_with_sub_materials(material_name, colors):
    sub_material_names = []
    for color_name, color_value in colors:
        sub_material_name = create_sub_material(material_name, color_name, color_value)
        if sub_material_name:
            sub_material_names.append(sub_material_name)

    material_graph = lux.getMaterialGraph(material_name)
    if material_graph is None:
        print(f"Material graph for {material_name} not found.")
        return

    material_graph.setMultiMaterial(enable=True)
    multi_material = lux.getMultiMaterial(material_name)

    multi_material.setSubMaterials(sub_material_names)
    print(f"Multi-Material '{material_name}' now contains sub-materials: {sub_material_names}")

def rename_multi_material(material_name, name_count):
    """Rename multi-material and its sub-materials by sanitizing their names."""
    try:
        multi_material = lux.getMultiMaterial(material_name)
        if multi_material:
            old_name = multi_material.getName()
            new_name = sanitize_material_name(old_name, name_count)
            if new_name != old_name:
                multi_material.setName(new_name)
                if multi_material.getName() == new_name:
                    print(f"Renamed multi-material from '{old_name}' to '{new_name}'")
                else:
                    print(f"Failed to rename multi-material from '{old_name}' to '{new_name}'")

            sub_materials = multi_material.getSubMaterials()
            for sub_material in sub_materials:
                old_sub_name = sub_material.getName()
                new_sub_name = sanitize_material_name(old_sub_name, name_count)
                if new_sub_name != old_sub_name:
                    sub_material.setName(new_sub_name)
                    if sub_material.getName() == new_sub_name:
                        print(f"Renamed sub-material from '{old_sub_name}' to '{new_sub_name}'")
                    else:
                        print(f"Failed to rename sub-material from '{old_sub_name}' to '{new_sub_name}'")
    except Exception as e:
        print(f"Error with multi-material '{material_name}': {e}")

def sanitize_material_name(name, name_count):
    new_name = re.sub(r'#\d+', '', name).strip() + "_MM"
    if new_name in name_count:
        name_count[new_name] += 1
        new_name = f"{new_name}_{name_count[new_name]}"
    else:
        name_count[new_name] = 1
    return new_name

def main():
    selected_materials = display_material_selection()
    if not selected_materials:
        print("No materials selected or operation cancelled.")
        return

    selected_colors = display_color_selection()
    if not selected_colors:
        print("No colors selected or operation cancelled.")
        return

    for material_name in selected_materials:
        create_multi_material_with_sub_materials(material_name, selected_colors)
        rename_multi_material(material_name, {})  # Ensure renaming after converting to multi-material

main()
```

# End of Batch Create Multi-Material Sub-Materials with Custom Advanced Shader Parameters.py
<a name="end-material-batch-create-multi-material-sub-materials-with-custom-advanced-shader-parameters"></a>

## Color Gradient ShaderEdge Diffuse Material Color Connect.py
<a name="color-gradient-shaderedge-diffuse-material-color-connect"></a>

# AUTHOR LUX DT ChatGPT
# VERSION 0.1.0
# Example of graphing a Color Gradient shader edge node.
## Example: Connecting a Color Gradient to Diffuse Color
#This script demonstrates how to connect a Color Gradient shader to the diffuse color parameter of a given material in KeyShot.
```python
import lux  # Import the KeyShot built-in module 'lux'.

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return

    # Set up the Color Gradient node if necessary.
    # This step is customizable based on specific gradient requirements.

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "Center"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)

## End of Color Gradient ShaderEdge Diffuse Material Color Connect.py
<a name="color-gradient-shaderedge-diffuse-material-color-connect"></a>
```

## Color Gradient View Direction.py
<a name="color-gradient-view-direction"></a>

# AUTHOR LUX DT ChatGPT
# VERSION 0.2.6
# Example of graphing a Color Gradient shader edge node with manual parameter setting.
```python
import lux  # Import the KeyShot built-in module 'lux'.

def create_rainbow_gradient_node(graph):
    """
    Creates a simplified Color Gradient shader node and adds it to the provided material graph.
    
    :param graph: The material graph where the Color Gradient node will be added.
    :return: The created Color Gradient node.
    """
    # Create a new Color Gradient node in the material graph.
    gradient_node = graph.newNode("lux_color_gradient")
    if gradient_node is None:
        print("Failed to create Color Gradient node.")
        return None

    # Print available parameters for debugging
    parameters = gradient_node.getParameters()
    print("Available parameters for 'lux_color_gradient' node:")
    for param in parameters:
        print(f"Parameter Name: {param.getName()}")

    # Set other gradient properties
    try:
        gradient_node.getParameter("gradient_type").setValue(9)  # View-dependent gradient
        gradient_node.getParameter("blend").setValue(True)
        gradient_node.getParameter("invert").setValue(False)
        gradient_node.getParameter("scale").setValue(1.0)
        gradient_node.getParameter("shift").setValue(0.0)
        gradient_node.getParameter("angle").setValue(0.0)
        gradient_node.getParameter("repeat").setValue(False)
        print("Other gradient properties set successfully.")
    except Exception as e:
        print(f"Error setting gradient properties: {e}")

    return gradient_node

def connect_color_gradient_to_diffuse_color(material_name):
    """
    Connects a Color Gradient shader to the diffuse color parameter of a given material.

    :param material_name: The name of the material to modify.
    """
    # Get the material graph of the specified material.
    graph = lux.getMaterialGraph(material_name)
    if graph is None:
        print(f"Material '{material_name}' not found.")
        return

    # Create the Color Gradient node and configure it
    gradient_node = create_rainbow_gradient_node(graph)
    if gradient_node is None:
        return

    # Flag to check if the connection is made.
    connected = False
    # Loop through all nodes of type 'lux_diffuse' in the material graph.
    for shader_node in graph.getNodesFromType('lux_diffuse'):
        # Check if the node has a diffuse parameter.
        diffuse_param = shader_node.getParameter("diffuse")
        if diffuse_param:
            # Connect the Color Gradient node to the diffuse parameter of the shader node.
            graph.newEdge(source=gradient_node, target=shader_node, param="diffuse")
            print("Color Gradient shader successfully connected to lux_diffuse node.")
            connected = True
            break  # Break the loop after making the connection.

    # Notify if no suitable shader node is found for the diffuse color.
    if not connected:
        print("Suitable shader node for diffuse color not found in material graph.")

# Example usage
# Define the material name.
material_name = "Rainbow Gradient Material"

# Apply the Color Gradient to the diffuse color of the specified material.
connect_color_gradient_to_diffuse_color(material_name)
```

## End of Color Gradient View Direction.py
<a name="color-gradient-view-direction"></a>
