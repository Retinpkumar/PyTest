import math

# This function will pass the test
def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

# This function will fail the test
def testsquare():
   num = 7
   assert 7*7 == 40

# This function will not be tested at all.
def tesequality():
   assert 10 == 11

# Run the test using: pytest -v