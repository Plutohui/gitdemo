import pytest


def test_add():
    a = 2
    b = 2
    assert a == b

def sub(x):
    return x - 1

def test_answer():

    assert sub(6) == 5

def test_add_2():
    a = 5
    b = 5
    assert a * b <= 50


if __name__ == '__main__':
    pytest.main(['-v','--html=report/test_pdemo.html', '--junitxml=report/test_pdemo.xml'])