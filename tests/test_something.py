import pytest


@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    # Setup
    yield
    # Teardown
