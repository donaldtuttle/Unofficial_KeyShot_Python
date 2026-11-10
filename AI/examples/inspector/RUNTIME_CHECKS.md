# KeyShot runtime testing status

Inspector v1.2.0 and v1.2.1 were tested in KeyShot by the author and confirmed working. The Inspector runtime-test item is closed. Offline mock tests are separate evidence, not a substitute for the author's KeyShot testing.

Original checker record: `2c5561339d3f4cc9d6d66c40014c8e200d7d4e5c`

## 1. Inspector 1.2.0 and 1.2.1: confirmed working

The author tested both versions of `AI/examples/inspector/KeyShot_Inspector_1_2.py` in KeyShot and confirmed that both worked. No additional Inspector runtime test is outstanding on the basis of the earlier documentation note.

## 2. Animation probe: separate API investigation

This investigation concerns animation API declarations in the 2026.3 beta capture. It is not a prerequisite for the tested Inspector or a blocker for its public announcement. The Inspector's animation-object helper functions use scene-tree traversal rather than the native animation-object calls below.

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

## Animation probe record

```
Commit:        <commit used for the API investigation>
KeyShot build: <getKeyShotVersion / getKeyShotDisplayVersion output>
Mode:          GUI
Scene:         <file name, animation type used>
Probe output:  <paste>
Follow-up:     none | recapture help() and rebuild index
```
