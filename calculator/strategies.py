from abc import ABC, abstractmethod

class CalculationStrategy(ABC):
    """
    Abstract base class for calculation strategies.
    """
    @abstractmethod
    def calculate(self, a: float, b: float) -> float:
        """
        Perform a calculation on two numbers.
        
        :param a: First number
        :param b: Second number
        :return: Result of the calculation
        """
        pass

class AdditionStrategy(CalculationStrategy):
    """
    Strategy for performing addition.
    """
    def calculate(self, a: float, b: float) -> float:
        """
        Add two numbers.
        
        :param a: First number
        :param b: Second number
        :return: Sum of a and b
        """
        return a + b

class SubtractionStrategy(CalculationStrategy):
    """
    Strategy for performing subtraction.
    """
    def calculate(self, a: float, b: float) -> float:
        """
        Subtract the second number from the first number.
        
        :param a: First number
        :param b: Second number
        :return: Difference of a and b
        """
        return a - b

class MultiplicationStrategy(CalculationStrategy):
    """
    Strategy for performing multiplication.
    """
    def calculate(self, a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        :param a: First number
        :param b: Second number
        :return: Product of a and b
        """
        return a * b

class DivisionStrategy(CalculationStrategy):
    """
    Strategy for performing division.
    """
    def calculate(self, a: float, b: float) -> float:
        """
        Divide the first number by the second number.
        
        :param a: First number
        :param b: Second number
        :return: Quotient of a and b
        :raises ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
