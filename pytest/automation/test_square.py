#Pytest requires the test function names to start with test.
#To run go to the directory where test files reside and type "python -m pytest" to run all tests
#You can yse "python -m pytest -v" to run in verbose mode

import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def test_square():
   num = 7
   assert 7*7 == 49

def test_equality():
   assert 10 == 10
