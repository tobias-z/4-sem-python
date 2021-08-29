from modules.hello_world import get_hello_world
import pytest


#################################################################################
# Class way of testing


class TestHelloWorld:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_get_hello_world(self):
        assert get_hello_world() == "Hello world"


#################################################################################
# None class way of testing


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # Setup
    pass
    yield
    # Teardown
    pass


def test_something():
    assert True is True
