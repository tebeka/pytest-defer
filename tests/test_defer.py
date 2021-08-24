from pathlib import Path


code_template = '''
from pathlib import Path
from time import sleep

root_dir = Path({root_dir!r})


def write_to(file_name, data='', extra=''):
    path = root_dir / file_name
    with path.open('w') as out:
        out.write(data)
        out.write(extra)


def test_defer(defer):
    defer.append(lambda: sleep(0.1) or write_to('a'))
    defer.append(lambda: 1/0)  # Make sure exception don't interrupt
    defer.append(lambda: write_to('b'))


def test_args(defer):
    defer.append(write_to, 'c', 'c')
    defer.append(write_to, 'd', 'd', extra='d')
    defer.append(write_to, 'e', extra='e')
'''


def test_files(testdir):
    code = code_template.format(root_dir=str(testdir.tmpdir))
    testdir.makepyfile(code)

    result = testdir.runpytest()
    result.assert_outcomes(passed=2)

    root = Path(testdir.tmpdir)
    file_a, file_b = root / 'a', root / 'b'
    assert file_a.exists()
    assert file_b.exists()
    # Check order
    assert file_a.stat().st_ctime > file_b.stat().st_ctime

    file_c = root / 'c'
    with file_c.open() as fp:
        data = fp.read()
        assert 'c' == data

    file_d = root / 'd'
    with file_d.open() as fp:
        data = fp.read()
        assert 'dd' == data

    file_e = root / 'e'
    with file_e.open() as fp:
        data = fp.read()
        assert 'e' == data
