import pytest
from src.calculator import Calculator

calculator = Calculator()

# Positive case
def test_add_positive():
    assert calculator.add(2, 3) == 5

# Negative case
def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(10, 0)

# Edge case
def test_divide_edge_case():
    assert calculator.divide(5, 2) == 2.5

# Invalid input case
def test_invalid_input():
    with pytest.raises(TypeError):
        calculator.add("a", 2)
