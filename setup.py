from setuptools import setup, find_packages


def find_version():
    with open('pytest_defer.py') as fp:
        for line in fp:
            if '__version__' in line:
                version = line.split('=')[-1].strip()
                return version[1:-1]  # trim ''


with open('README.md') as fp:
    long_desc = fp.read()


setup(
    version=find_version(),
    name='pytest-defer',
    license='MIT',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    author='Miki Tebeka',
    author_email='miki@353solutions.com',
    packges=find_packages(),
    entry_points={
        'pytest11': [
            'defer = pytest_defer',
        ],
    },
    install_requires=[
        'pytest>=6.2',
    ],
)
