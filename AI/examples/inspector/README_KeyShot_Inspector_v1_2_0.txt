KEYSHOT INFORMATION INSPECTOR 1.2.1 — COMMUNITY RELEASE
=======================================================
Unofficial Python diagnostic tool for KeyShot 2026.x GUI.
Primary script: KeyShot_Inspector_1_2.py

RELEASE STATUS
--------------
Current version: 1.2.1 (repair of 1.2.0)
Change in 1.2.1: animation-name teaching removed.
Offline mock tests: 28 passed (ordinary Python, mocked lux).
KeyShot GUI runtime testing: the author tested v1.2.0 and v1.2.1 and confirmed both working.
Animation API probe: separate API investigation; not an Inspector release requirement.
See RUNTIME_CHECKS.md for testing status and the separate animation API investigation.
Companion files retain 1.2.0 filenames; they cover this 1.2.1 repair.
Some dialog titles and report labels also retain 1.2.0 in the current source.

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
* What every one of the 72 selectable operations retrieves and why it is useful.
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
12 categories, 72 selectable report operations in the v1.2.1 registry.
The API availability report checks the names in GETTERS_2026 without
executing them; it is not an exhaustive inventory of every API getter.
Native animation-object enumeration is not a selectable report in v1.2.1.
Advanced animation reports use scene-tree traversal instead.

VERIFICATION
------------
Documentation and category labels cross-checked against the bundled
KeyShot_Inspector_1_2.py source.
The author tested v1.2.0 and v1.2.1 in KeyShot and confirmed both working.
Offline regression tests are separate from that KeyShot runtime testing.
Native KeyShot crashes cannot be simulated or ruled out by offline tests.
The user should validate on their own 2026.x build.

Files included in this GitHub folder:
- KeyShot_Inspector_1_2.py (Python script, version 1.2.1)
- KeyShot_Information_Inspector_v1_2_0_User_Guide.txt (full guide)
- README_KeyShot_Inspector_v1_2_0.txt (quick start)
- test_KeyShot_Information_Inspector_v1_2_0.py (offline tests)
- RUNTIME_CHECKS.md (testing status and separate animation API investigation)
