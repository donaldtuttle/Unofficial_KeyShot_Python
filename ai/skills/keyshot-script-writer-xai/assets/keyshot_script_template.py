#!/usr/bin/env python3
"""
KeyShot Python Script Template
==============================
Copy this file into your KeyShot Scripts folder or paste into the Scripting Console.
Customize the USER SETTINGS section, then run.

Targets KeyShot Studio 2026.3 (embedded Python).
All lux / luxmath calls verified against the 2026.3 help() dumps.
Static verification only — not runtime-tested in KeyShot.
"""

import lux
import luxmath
import os
import sys

# =============================================================================
# USER SETTINGS - EDIT THESE
# =============================================================================
PROJECT_NAME = "MyProject"
OUTPUT_DIR = r"C:\Renders\MyProject"
HDRI_PATH = r"C:\HDRI\neutral.exr"

# Camera
CAMERA_POS = (150.0, -220.0, 110.0)
LOOK_AT = (0.0, 0.0, 45.0)
FOV_DEG = 26.0

# Render
WIDTH = 1920
HEIGHT = 1080
SAMPLES = 64
ENGINE = lux.RENDER_ENGINE_PRODUCT   # or RENDER_ENGINE_PRODUCT_GPU / INTERIOR_*
GI_QUALITY = 3                       # 0–5 (0 disables GI). Separate from engine.

# Output
OUTPUT_FORMAT = lux.RENDER_OUTPUT_JPEG
OUTPUT_EXT = ".jpg"

# Animation / XR (uncomment as needed)
# DO_ANIMATION = True
# FRAMES = 36
# FPS = 30

# =============================================================================
# SCRIPT LOGIC
# =============================================================================

def main():
    print(f"=== KeyShot Script: {PROJECT_NAME} ===")
    
    # Ensure output dir
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Basic scene check
    if not lux.hasContents():
        print("ERROR: No geometry in scene. Open or import a model first.")
        return
    
    print("Scene has content. Proceeding...")
    
    # === ENVIRONMENT ===
    try:
        env = lux.getActiveEnvironment()
        if os.path.exists(HDRI_PATH):
            env.setLightingEnvironment(HDRI_PATH)
            print(f"HDRI loaded: {HDRI_PATH}")
        env.setBrightness(1.0)
        env.setRotation(0)
        env.setGroundShadows(True)
    except Exception as e:
        print(f"Environment setup warning: {e}")
    
    # === CAMERA ===
    try:
        lux.setCameraPosition(CAMERA_POS)
        lux.setCameraLookAt(LOOK_AT)
        lux.setCameraFieldOfView(FOV_DEG)
        print("Camera positioned.")
    except Exception as e:
        print(f"Camera setup warning: {e}")
    
    # === RENDER OPTIONS ===
    lux.setRenderEngine(ENGINE)
    opts = lux.getRenderOptions()
    opts.setMaxSamplesRendering(SAMPLES)
    opts.setGlobalIllumination(GI_QUALITY)
    opts.setSharperTextureFiltering(True)
    opts.setOutputAlphaChannel(True)
    # Add more passes if needed:
    # opts.setOutputDepthPass(True)
    # opts.setOutputNormalsPass(True)
    
    # === EXECUTE RENDER ===
    output_path = os.path.join(OUTPUT_DIR, f"{PROJECT_NAME}_render{OUTPUT_EXT}")
    
    print(f"Starting render to: {output_path}")
    try:
        lux.renderImage(output_path, WIDTH, HEIGHT, opts, OUTPUT_FORMAT)
        print("Render complete!")
    except Exception as e:
        print(f"Render failed: {e}")
        return
    
    print("=== Script finished successfully ===")


if __name__ == "__main__":
    # When run as standalone .py inside KeyShot, __main__ works
    main()
