import pytest
from calculator.calculator import Calculator
from calculator.strategies import AdditionStrategy, SubtractionStrategy, MultiplicationStrategy, DivisionStrategy

def test_addition():
    """
    Test addition strategy.
    """
    calc = Calculator(AdditionStrategy())
    assert calc.calculate(5, 3) == 8

def test_subtraction():
    """
    Test subtraction strategy.
    """
    calc = Calculator(SubtractionStrategy())
    assert calc.calculate(5, 3) == 2

def test_multiplication():
    """
    Test multiplication strategy.
    """
    calc = Calculator(MultiplicationStrategy())
    assert calc.calculate(5, 3) == 15

def test_division():
    """
    Test division strategy.
    """
    calc = Calculator(DivisionStrategy())
    assert calc.calculate(6, 3) == 2

def test_division_by_zero():
    """
    Test division by zero handling.
    """
    calc = Calculator(DivisionStrategy())
    with pytest.raises(ValueError):
        calc.calculate(5, 0)
