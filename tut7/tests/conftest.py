from datetime import datetime

import pytest

from tut7.myapp.student import Student, get_topper



# Creating a dummy student fixture
@pytest.fixture
def dummy_student():
    print("making dummy student")
    return Student("Retin", datetime(2000,1,1), "coe", 20)

#Creating factory
@pytest.fixture
def make_dummy_student():
    def make_dummy_student(name, credits):
        return Student(name, datetime(2000,1,1), "coe", credits)

    return make_dummy_student