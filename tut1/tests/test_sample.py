# Importing "add" function from sample.py
from tut1.myapp.sample import add

# defining pytest function with test_ prefix to add 2 int
def test_add_num():
    assert add(1,2) == 3

# defining pytest function with test_ prefix to add 2 char
def test_add_str():
    assert add("a", "b") == "ab"

# defining a pytest class encompassing above 2 functions
class TestSample:
    def test_add_num(self):
        assert add(1, 2) == 3

    def test_add_str(self):
        assert add("a", "b") == "ab"