def test_greater():
   num = 100
   assert num > 100

def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200

# Run the test using pytest -v and observe the result.

# Run: pytest test_compare.py -v

# Run: pytest -k great -v
