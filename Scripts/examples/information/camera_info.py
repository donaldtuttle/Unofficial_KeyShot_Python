"""KPSA 2026: report active camera state without assuming a camera object.

Evidence: lux.getCamera/getCameraPosition/getCameraDirection/getCameraLookAt/
getCameraLens. Syntax/documentation checks only; KeyShot runtime untested.
"""
import lux

def main():
    getters = (
        ('camera', lux.getCamera),
        ('position', lux.getCameraPosition),
        ('direction', lux.getCameraDirection),
        ('look_at', lux.getCameraLookAt),
        ('lens', lux.getCameraLens),
    )
    for label, getter in getters:
        print(f'{label}: {getter()!r}')

if __name__ == '__main__':
    main()
