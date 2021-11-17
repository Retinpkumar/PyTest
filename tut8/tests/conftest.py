from datetime import datetime
import pytest
from tut8.myapp.student import Student

@pytest.fixture(params=[21, 19] , ids=["eligible", "ineligible"])

def dummy_student(request):
    return Student("Retin", datetime(2000, 1, 1), "coe", request.param)

@pytest.fixture
def make_dummy_student():
    def _make_dummy_student(name, credits):
        return Student(name, datetime(2000,1,1), "coe", credits)
    return _make_dummy_student