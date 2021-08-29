from modules.hello_world import get_hello_world

class TestHelloWorld():

    def test_get_hello_world(self):
        assert get_hello_world() == "Hello world"


