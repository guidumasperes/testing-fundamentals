#To execute the tests from a specific file, use the following syntax: "python -m pytest <filename> -v"

def test_greater():
   num = 100
   assert num > 100

def test_greater_equal():
   num = 100
   assert num >= 100

def test_less():
   num = 100
   assert num < 200