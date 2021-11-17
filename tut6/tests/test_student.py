# Creating custom pytest fixtures
import pytest
from tut6.myapp.student import Student
from datetime import datetime

# Creating a dummy student fixture
@pytest.fixture(scope="function")
def dummy_student():
    print("making dummy student")
    return Student("Retin", datetime(2000,1,1), "coe")



def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert  dummy_student.get_age() == dummy_student_age

def test_student_add_credits(dummy_student):
    dummy_student.add_credits(5)
    assert dummy_student.get_credits() == 5

def test_student_get_credits(dummy_student):
    assert dummy_student.get_credits() == 0

# By changing the scope of pytest fixture, we can create a
# dummy fixture that can be reused everytime it is needed by a function
# scope = function, class, module, package, session

