from app.calculation import Calculation
import pytest

# test Addition
@pytest.mark.parametrize("a, b, expected", [
    (1, 4, 5), (1, -7, -6), (0, 0, 0)
])
def test_addition(a, b, expected):
    assert Calculation(a, b, "add").result == expected

# test Subtraction
@pytest.mark.parametrize("a, b, expected", [
    (7, 4, 3), (5, -7, 12), (0, 0, 0)
])
def test_subtraction(a, b, expected):
    assert Calculation(a, b, "subtract").result == expected

# test Multiplication
@pytest.mark.parametrize("a, b, expected", [
    (1, 4, 4), (3, -2, -6), (0, 0, 0)
])
def test_multiplication(a, b, expected):
    assert Calculation(a, b, "multiply").result == expected

# test Division
@pytest.mark.parametrize("a, b, expected", [
    (1, 4, .25), (4, -2, -2), (0, 2, 0)
])
def test_division(a, b, expected):
    assert Calculation(a, b, "divide").result == expected

def test_value_error():
    with pytest.raises(ValueError):
        Calculation(1, 0, "divide")

def test_type_error():
    with pytest.raises(TypeError):
        Calculation(6, 'x', "divide")

def test_str():
    c = Calculation(3, 2, "multiply")
    assert str(c) == "multiply 3, 2 = 6"




