from modules.hello_world import get_hello_world


def test_hello_world():
    assert get_hello_world() == "Hello world"
