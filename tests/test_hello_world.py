import unittest

import pytest
from modules.hello_world import get_hello_world

#################################################################################
# Class way of testing


class TestHelloWorld(unittest.TestCase):
    def setUp(self):
        self.hello = "Hello world"

    def tearDown(self):
        pass

    def test_get_hello_world(self):
        self.assertEqual(get_hello_world(), self.hello)


#################################################################################
# None class way of testing


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # Setup
    yield
    # Teardown
    pass


def test_something():
    assert True is True
