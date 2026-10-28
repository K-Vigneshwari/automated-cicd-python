from app import greet


def test_greet():
    assert greet() == "Hello! Welcome to my CI/CD project."