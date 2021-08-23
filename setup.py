from setuptools import setup

setup(
    version='0.1.0',
    name='pytest-defer',
    py_modules=['pytest_defer'],
    entry_points={
        'pytest11': [
            'defer = pytest_defer',
        ],
    },
    install_requires=[
        'pytest>=6.2',
    ],
)
