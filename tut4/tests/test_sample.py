# Parametrize
# Helps in running multiple tests using a single function
import pytest

from tut4.myapp.sample import add

def test_add_num():
    assert add(1,2) == 3

def test_add_str():
    assert add("a","b") == "ab"

def test_add_list():
    assert add([1,2], [3,4]) == [1,2,3,4]

# Parametrizing all the above tests

@pytest.mark.parametrize("a,b,c",
                         [(1,2,3),
                          ("a","b","ab"),
                          ([1,2],[3,4],[1,2,3,4])],
                         ids=["num","str","list"])
def test_add(a,b,c):
    assert add(a,b) == c