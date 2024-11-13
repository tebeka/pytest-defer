# Tested code, ignored by main test

from pathlib import Path
from time import sleep

root_dir = Path(__file__).parent.absolute()


def write_to(file_name, data='', extra=''):
    path = root_dir / file_name
    with path.open('w') as out:
        out.write(data)
        out.write(extra)


def test_defer(defer):
    defer.append(lambda: sleep(0.1) or write_to('a'))
    defer.append(lambda: 1 / 0)  # Make sure exception don't interrupt
    defer.append(lambda: write_to('b'))


def test_args(defer):
    defer.append(write_to, 'c', 'c')
    defer.append(write_to, 'd', 'd', extra='d')
    defer.append(write_to, 'e', extra='e')
