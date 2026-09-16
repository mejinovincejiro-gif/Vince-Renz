import pytest 

from calculator import add, subtract, multiply, divide

def test_add() :
  assert add(2, 3) == 5

def test_subtract() :
  assert subtraction(10, 4) == 6

def test_multiply() :
  assert multiply(3, 5) == 15

def test_divide() :
  assert(10, 4) == 2.5

def test_divide_by_zero() :
  with pytest.raises (ValueError) :
      divide(1, 0)
