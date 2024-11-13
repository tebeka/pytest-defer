from subprocess import run
from sys import executable
from pathlib import Path
from shutil import copyfile
from io import StringIO

test_dir = Path(__file__).parent


def test_defer(tmp_path):
    tmp_path = Path('/tmp/ff')
    venv = tmp_path / '.venv'
    run([executable, '-m', 'venv', str(venv)], check=True)
    venv_py = str(venv / 'bin' / 'python')
    run([venv_py, '-m', 'pip', 'install', '-e', '.'], check=True)

    for file in test_dir.glob('_*.py'):
        dest = tmp_path / file.name[1:]  # trim leading _
        copyfile(file, dest)

    out = run(
        # -rfp shows summary of failed and passed
        [venv_py, '-m', 'pytest', '-rfp'],
        cwd=str(tmp_path),
        check=True,
        capture_output=True,
        text=True,
    )

    # PASSED test_files.py::test_a
    passed = 0
    for line in StringIO(out.stdout):
        if line.startswith('PASSED'):
            passed += 1

    assert passed == 2

    file_a, file_b = tmp_path / 'a', tmp_path / 'b'
    assert file_a.exists()
    assert file_b.exists()
    # Check order
    assert file_a.stat().st_ctime > file_b.stat().st_ctime

    file_c = tmp_path / 'c'
    with file_c.open() as fp:
        data = fp.read()
        assert 'c' == data

    file_d = tmp_path / 'd'
    with file_d.open() as fp:
        data = fp.read()
        assert 'dd' == data

    file_e = tmp_path / 'e'
    with file_e.open() as fp:
        data = fp.read()
        assert 'e' == data
