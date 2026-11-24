# KeyShot runtime checks still open

Checker side is closed. These two need a KeyShot session. Record the commit SHA, the KeyShot build, the scene, and the output.

Commit when this note was written: `2c5561339d3f4cc9d6d66c40014c8e200d7d4e5c`

## 1. Inspector 1.2.1

Run `AI/examples/inspector/KeyShot_Inspector_1_2.py` once in KeyShot GUI.

Note the scene and the result. The 1.2.0 author test does not cover these bytes.

## 2. Animation probe

Open a scene that has at least one animation, such as a turntable.

Paste into the scripting console:

```python
import lux
print("KeyShot", lux.getKeyShotVersion(), lux.getKeyShotDisplayVersion(),
      "headless" if lux.isHeadless() else "GUI")
print("ANIMATION_TYPE_*:", [n for n in dir(lux) if n.startswith("ANIMATION_TYPE")])
print("lux.Animation:", hasattr(lux, "Animation"))
anims = lux.getAnimations() or []
print("animations in scene:", len(anims))
if anims:
    a = anims[0]
    print(type(a), [m for m in dir(a) if not m.startswith("_")])
```

What the result means:

- The constants or the class exist: capture `help()` for them, for example `help(type(a))`, add that to the dump, and rebuild the index.
- Neither exists: the docstring mentions are ahead of the build. Keep them probe-only. Do not ship animation-creation scripts for 2026.3 beta from those names.

## Record

```
Commit:        2c5561339d3f4cc9d6d66c40014c8e200d7d4e5c
KeyShot build: <getKeyShotVersion / getKeyShotDisplayVersion output>
Mode:          GUI
Scene:         <file name, animation type used>
Inspector:     pass | fail - <notes>
Probe output:  <paste>
Follow-up:     none | recapture help() and rebuild index
```
