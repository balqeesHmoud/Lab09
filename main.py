from calculator.calculator import Calculator
from calculator.strategies import AdditionStrategy, SubtractionStrategy, MultiplicationStrategy, DivisionStrategy

if __name__ == "__main__":
    """
    Main application entry point.
    """
    calc = Calculator(AdditionStrategy())
    print("Addition:", calc.calculate(5, 3))

    calc.set_strategy(SubtractionStrategy())
    print("Subtraction:", calc.calculate(5, 3))

    calc.set_strategy(MultiplicationStrategy())
    print("Multiplication:", calc.calculate(5, 3))

    calc.set_strategy(DivisionStrategy())
    print("Division:", calc.calculate(5, 3))
