import pytest
from operations import Operations

def test_sum():
	ops = Operations(4, 3)
	assert ops.sum() == 4+3

def test_sub():
	ops = Operations(4, 3)
	assert ops.sub() == 4-3

def test_mul():
	ops = Operations(4, 3)
	assert ops.mul() == 4*3

def test_div():
	ops = Operations(4, 3)
	assert ops.div() == 4/3