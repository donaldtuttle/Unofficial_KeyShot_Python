"""KPSA 2026: GUI dialog with range, item-pair and cancel handling.

Read-only apart from normal dialog UI. Evidence: getInputDialog/isHeadless.
Syntax/documentation checks only; GUI runtime untested.
"""
import lux

def main():
    if lux.isHeadless():
        raise RuntimeError('Run this example in the KeyShot GUI.')
    values = [
        ('count', lux.DIALOG_INTEGER, 'Count:', 4, (1, 20)),
        ('choice', lux.DIALOG_ITEM, 'Choose a number:', 2, [1, 2, 3]),
        (lux.DIALOG_LABEL, 'This example only reports the chosen values.'),
    ]
    result = lux.getInputDialog(title='KPSA input example', values=values)
    if result is None:
        print('Cancelled.')
        return
    if not isinstance(result, dict):
        raise TypeError('Unexpected dialog return representation.')
    choice = result['choice']
    if not isinstance(choice, (tuple, list)) or len(choice) != 2:
        raise TypeError(f'Expected an item selection pair, got {choice!r}.')
    print(f"Count: {result['count']!r}; index: {choice[0]!r}; displayed item: {choice[1]!r}")

if __name__ == '__main__':
    main()
