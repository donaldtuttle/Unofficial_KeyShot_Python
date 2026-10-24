"""KPSA 2026: render the open scene to a new PNG path after preflight.

Set OUTPUT_PATH; a missing parent or existing destination is rejected. Dry-run
does not call the renderer. Path checks do not provide atomic reservation.
Evidence: getRenderOptions, RenderOptions.setMaxSamplesRendering, renderImage.
Syntax/documentation checks only; KeyShot runtime untested.
"""
from pathlib import Path
import lux

OUTPUT_PATH = ''
WIDTH = 1280
HEIGHT = 720
SAMPLES = 64
DRY_RUN = True

def render(output_path, width, height, samples, *, dry_run=True):
    if not output_path:
        raise ValueError('Set an explicit new output path.')
    path = Path(output_path).expanduser().resolve()
    if path.suffix.lower() != '.png':
        raise ValueError('This example supports a PNG destination only.')
    if not path.parent.is_dir() or path.exists():
        raise ValueError('Parent folder must exist and destination must be new.')
    if any(type(v) is not int or v <= 0 for v in (width, height, samples)):
        raise ValueError('Width, height and samples must be positive integers.')
    print(f'Render {width}x{height}, samples={samples}, path={path}, dry_run={dry_run}')
    if dry_run:
        return
    options = lux.getRenderOptions(defaults=True)
    options.setMaxSamplesRendering(samples)
    lux.renderImage(path=str(path), width=width, height=height, opts=options)
    if not path.is_file() or path.stat().st_size == 0:
        raise RuntimeError('Renderer returned without a nonempty output file; inspect KeyShot.')
    return str(path)

if __name__ == '__main__':
    render(OUTPUT_PATH, WIDTH, HEIGHT, SAMPLES, dry_run=DRY_RUN)
