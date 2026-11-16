"""KPSA 2026: add one file using format-specific documented import options.

Set INPUT_PATH. Does not select clear/update import_type. Additive imports still
change the scene and can affect format-dependent state; use a test scene first.
Evidence: getImportOptions, importFile. Runtime untested.
"""
from pathlib import Path
import lux

INPUT_PATH = ''
DRY_RUN = True

def import_additive(input_path, *, dry_run=True):
    if not input_path:
        raise ValueError('Provide an explicit input file.')
    path = Path(input_path).expanduser().resolve()
    if not path.is_file() or not path.suffix:
        raise ValueError('Input must be an existing file with an extension.')
    print(f'Add file: {path}; dry_run={dry_run}')
    if dry_run:
        return
    options = lux.getImportOptions(ext=path.suffix.lstrip('.'), getDefaults=True)
    if not isinstance(options, dict):
        raise TypeError('getImportOptions did not return the documented dictionary.')
    if 'import_type' not in options:
        raise ValueError('No import_type option returned for this format; inspect before import.')
    options['import_type'] = 0
    lux.importFile(path=str(path), showOpts=False, dontAsk=True, opts=options)

if __name__ == '__main__':
    import_additive(INPUT_PATH, dry_run=DRY_RUN)
