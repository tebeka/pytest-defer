"""Provide a "defer" fixture to pytest"""

import logging

import pytest

__version__ = '0.2.0'


class Defers(list):
    def append(self, fn, *args, **kw):
        return super().append((fn, args, kw))


@pytest.fixture
def defer():
    defers = Defers()

    yield defers

    for fn, args, kw in reversed(defers):
        try:
            fn(*args, **kw)
        except Exception as err:
            logging.exception(
                'defer: %s: exception: %s', fn.__name__, err)
