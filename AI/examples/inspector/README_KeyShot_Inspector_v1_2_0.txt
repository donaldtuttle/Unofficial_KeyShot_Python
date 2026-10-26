KEYSHOT INFORMATION INSPECTOR 1.2.0 — COMMUNITY RELEASE
=======================================================
Unofficial Python diagnostic tool for KeyShot 2026.x GUI.
Primary script: KeyShot_Inspector_1_2.py

QUICK START
-----------
1. Save a copy of your KeyShot scene before using advanced inventories.
2. Run KeyShot_Inspector_1_2.py from KeyShot's Scripts interface.
3. Select "Save TXT only" and an existing writable folder.
4. Check "Individual Gets mode" and choose one category.
5. Choose one operation; start with getSceneInfo() - Scene summary.
6. Review TXT output and KeyShot_Inspector_v1_2_0_Trace.txt.

ABOUT THE GUIDE
---------------
Read KeyShot_Information_Inspector_v1_2_0_User_Guide.txt for:
* What every one of the 74 selectable operations retrieves and why it is useful.
* The difference between category mode and Individual Gets mode.
* The optional all-saved-camera, environment and image-style inventories.
* Output limits, large-scene performance, and optional Exhaustive mode.
* Safe library and file scanning, material CMF metadata and native scene export.
* Trace troubleshooting and guidance for sharing diagnostic reports.

IMPORTANT SAFETY INFORMATION
----------------------------
* Normal inspection does not modify KeyShot scene content or timeline state.
* FULL saved-camera/environment/image-style inspection requires explicit
  "Inspect ALL cameras/environments/styles via switching/restoring" opt-in.
* This temporarily changes the active selection and tries to restore it.
* If KeyShot crashes at native level, restoration may not happen.
* Restoring the selected item may not reverse all transient side effects.
* All-camera scan refuses when the current camera has unsaved changes, or
  when its unsaved status cannot be checked. Use a saved scene copy.
  reported KeyShot crashes. Availability inventory is not execution.
* "Allow slow scans" is independently required for library inventories,
  Resource Models scan, full tree dump and library CMF lookup.
* "Exhaustive output" lifts most scene/material/shader/section limits and
  can create very large reports. It does not bypass any safety opt-in.
* Resource Models disk scans retain a fixed 150-directory/300-match cap.
* Native metadata export creates two extra files (.metadata and .xmp)
  based on the current scene; it does not inspect every saved camera.
* TXT/trace files can contain sensitive file paths, scene/material names,
  machine details and license data. Review and redact before posting.

OUTPUT
------
KeyShot_Information_Report.txt (or a non-overwriting timestamped name)
KeyShot_Inspector_v1_2_0_Trace.txt (overwritten at each new diagnostic run)
Optional <report_name>.metadata and <report_name>.xmp (non-overwriting).

REPORT COVERAGE
---------------
12 categories, 74 selectable report operations.
2026 reference contains 59 non-dialog top-level information get* methods;
the two native animation-object get calls are intentionally hard blocked.

VERIFICATION
------------
Documentation and category labels cross-checked against the bundled
KeyShot_Inspector_1_2.py source.
Offline regression tests exist, but native KeyShot crashes cannot be
simulated or ruled out. The user should validate on their own 2026.x build.

Files included in this GitHub folder:
- KeyShot_Inspector_1_2.py (Python script)
- KeyShot_Information_Inspector_v1_2_0_User_Guide.txt (full guide)
- README_KeyShot_Inspector_v1_2_0.txt (quick start)
- test_KeyShot_Information_Inspector_v1_2_0.py (offline tests)
