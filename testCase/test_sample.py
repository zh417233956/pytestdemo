import pytest

# 当前目录执行：pytest

def func(x):
    return x + 1
def test_answer():
    assert func(3) == 4
def test_error():
    assert func(3) == 5