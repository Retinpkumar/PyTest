import sys

from tut3.myapp.sample import add
import pytest

def test_add_num():
    assert add(1,2) == 3

def test_add_str():
    assert add("a", "b") == "ab"

# We want to skip a particular test
@pytest.mark.skip(reason="Just wanna skip it")
def test_add_num():
    assert add(1,2) == 3

# Skipping with a condition
@pytest.mark.skipif(sys.version_info > (3,7), reason="Use python 3.7 or less")
def test_add_str():
    assert add("a", "b") == "ab"

# xfail is used for ignoring a unittest exception.
@pytest.mark.xfail(sys.platform == "linux",
                   reason="Don't run on linux")
def test_add_list():
    """
        Here, xfail is used to ignore the exception if the system
        used is a windows machine.
    """
    assert add([1],[2]) == [1,2]
    raise Exception()

# xfail is used for ignoring a unittest exception.
@pytest.mark.xfail(sys.platform == "win32",
                   reason="Don't run on windows")
def test_add_list():
    """
        Here, xfail is used to ignore the exception if the system
        used is a windows machine.
    """
    assert add([1],[2]) == [1,2]
    raise Exception()

