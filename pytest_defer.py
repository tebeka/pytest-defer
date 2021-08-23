import pytest

import logging


@pytest.fixture
def defer():
    defers = []

    yield defers

    for fn in reversed(defers):
        try:
            fn()
        except Exception as err:
            logging.exception('defer: %s: exception: %s', fn.__name__, err)
