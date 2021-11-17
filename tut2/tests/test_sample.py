# Asserting if the test is raising exceptions

from tut2.myapp.sample import validate_age
import pytest

def test_validate_age_valid_age():
    validate_age(10)

def test_validate_age_invalid_age():
    validate_age(-1)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError):
        validate_age(-1)

def test_validate_age_invalid_age():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    print(str(exc_info.value))

def test_validate_age_invalid_age():
    with pytest.raises(ValueError) as exc_info:
        validate_age(-1)
    assert str(exc_info.value) == "Age cannot be less than 0"

def test_validate_age_invalid_age():
    with pytest.raises(ValueError, match="Age cannot be less than 0"):
        validate_age(-1)

