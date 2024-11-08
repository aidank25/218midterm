import pytest
from app.operations import (
    Addition,
    Subtraction,
    Multiplication,
    Division,
)

# test Addition
@pytest.mark.parametrize("a, b, expected", [
    (1, 4, 5), (1, -7, -6), (0, 0, 0)
])
def test_addition(a, b, expected):
    assert Addition().execute(a, b) == expected

# test Subtraction
@pytest.mark.parametrize("a, b, expected", [
    (7, 4, 3), (5, -7, 12), (0, 0, 0)
])
def test_subtraction(a, b, expected):
    assert Subtraction().execute(a, b) == expected

# test Multiplication
@pytest.mark.parametrize("a, b, expected", [
    (1, 4, 4), (3, -2, -6), (0, 0, 0)
])
def test_multiplication(a, b, expected):
    assert Multiplication().execute(a, b) == expected

# test Division
@pytest.mark.parametrize("a, b, expected", [
    (1, 4, .25), (4, -2, -2), (0, 2, 0)
])
def test_division(a, b, expected):
    assert Division().execute(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Division().execute(1,0)

def test_str():
    assert str(Addition()) == "Addition"

