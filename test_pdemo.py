import pytest


def test_add():
    a = 2
    b = 2
    assert a == b

def sub(x):
    return x - 1

def test_answer():

    assert sub(6) == 5


if __name__ == '__main__':
    pytest.main()