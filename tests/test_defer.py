from pathlib import Path


code_template = '''
from pathlib import Path
from time import sleep

root_dir = Path({root_dir!r})

def touch(name):
    path = root_dir / name
    with path.open('w'):
        pass



def test_defer(defer):
    defer.append(lambda: sleep(0.1) or touch('a'))
    defer.append(lambda: 1/0)  # Make sure exception don't interrupt
    defer.append(lambda: touch('b'))
'''


def test_files(testdir):
    code = code_template.format(root_dir=str(testdir.tmpdir))
    testdir.makepyfile(code)

    result = testdir.runpytest()
    result.assert_outcomes(passed=1)

    root = Path(testdir.tmpdir)
    file_a, file_b = root / 'a', root / 'b'
    assert file_a.exists()
    assert file_b.exists()
    # Check order
    assert file_a.stat().st_ctime > file_b.stat().st_ctime
