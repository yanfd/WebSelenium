import pytest

def add(x):
    return x + 2

class Test_Class_Add():
    def test_add1(self):
        assert add(2) == 4

    def test_add2(self):
        assert add(22) == 24

    def test_add3(self):
        assert add(100) == 102

class Test_Class_In():
    def test_in(self):
        a = "Hello World！"
        b = "Hi"
        c = "World"
        assert c in a
        assert b not in a

    def test_notin(self):
        a = "Hello World！"
        b = "Hi"
        c = "World"
        assert b in a
        assert c not in a