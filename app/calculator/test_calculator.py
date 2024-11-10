from app.calculator import Calculator
import pytest

def test_perform_operation():
    calculator = Calculator()
    assert calculator.perform_operation("subtract", 3, 2) == 1