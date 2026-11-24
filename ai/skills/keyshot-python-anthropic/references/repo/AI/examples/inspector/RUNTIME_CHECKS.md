# KeyShot animation runtime probe

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
- Neither exists: the docstring mentions are ahead of the build. Keep them probe-only. Do not ship animation-creation scripts for KeyShot Studio 2026.3 from those names.
