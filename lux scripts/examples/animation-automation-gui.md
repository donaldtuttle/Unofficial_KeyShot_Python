# Scripting Examples: Animation, Automation, and GUI

[Scripting Examples TOC](../Scripting_Examples.md)

## Animation Batch Rendering Frame Padding.py
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

## Animation Encode Video with Padding.py
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

## Animation Frame Padding Agnostic.py
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

## Animation Rendered Image Sequence Padding Agnostic.py
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

## Animation Pad Frames.py
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

## Batch Import Queue XR .py
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

## Create Camera Extract xmp Camera Data.py
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

## Create Cameras Additional Functions Example.py
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

## Create Cameras Template.py
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

## Create Configured Cameras Template.py
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

## Create Custom Cameras From XMP.py
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

## Create Standard Scene Example.py
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

## Create Standard Views and Perspective Beauty Camera.py
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

## Create Standard Views and Perspective Camera with ModelSets.py
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


```
# End of Automation\Create Standard Views and Perspective Camera with ModelSets.py

## Create Standard Views and Perspective Camera.py
<a name="automation-create-standard-views-and-perspective-camera"></a>
```python
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

## Create Standard Views and Perspective Cameras.py
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

## Create Standard Views and Perspective Cameras_Distance_50Units.py
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

## Create Standard Views and Perspective Cameras_Distance_5Units.py
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

## Create a Perspective Camera.py
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

## Create and Configure Studios.py
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

## Creates Model Set.py
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

## Delete Unused Nodes.py
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

## CustomInputDialog_PC.py
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

## GUI Script Example Doc.py
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

## Get InputDialog GUI Example.py
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

