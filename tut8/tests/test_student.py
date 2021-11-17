from datetime import datetime

import pytest


def test_student_get_age(dummy_student):
    dummy_student_age = (datetime.now() - dummy_student.dob).days // 365
    assert dummy_student.get_age() == dummy_student_age

# def test_student_get_credits(dummy_student):
#     assert dummy_student.get_credits() == 20

def test_student_is_eligible_for_degree_true(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam", 19)) is False

def test_student_is_eligible_for_degree_false(make_dummy_student):
    assert is_eligible_for_degree(make_dummy_student("sam", 19)) is False

@pytest.mark.parametrize("credits, expected", [(19, False), (21, True)])
def test_student_is_eligible_for_degree_false(make_dummy_student, credits, expected):
    assert is_eligible_for_degree(make_dummy_student("sam", credits)) is expected
