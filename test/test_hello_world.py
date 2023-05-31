from index import hello_world


def test_hello_world() -> bool:
    assert hello_world() == "Hello World"
