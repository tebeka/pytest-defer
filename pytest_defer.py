"""Provide a "defer" fixture to pytest"""

import logging

import pytest

__version__ = '0.1.0'


@pytest.fixture
def defer():
    defers = []

    yield defers

    for fn in reversed(defers):
        try:
            fn()
        except Exception as err:
            logging.exception('defer: %s: exception: %s', fn.__name__, err)
