from .strategies import CalculationStrategy

class Calculator:
    """
    Calculator that uses different calculation strategies.
    """
    def __init__(self, strategy: CalculationStrategy):
        """
        Initialize the calculator with a specific strategy.
        
        :param strategy: The calculation strategy to use
        """
        self._strategy = strategy

    def set_strategy(self, strategy: CalculationStrategy):
        """
        Set a new calculation strategy.
        
        :param strategy: The new calculation strategy to use
        """
        self._strategy = strategy

    def calculate(self, a: float, b: float) -> float:
        """
        Perform a calculation using the current strategy.
        
        :param a: First number
        :param b: Second number
        :return: Result of the calculation
        """
        return self._strategy.calculate(a, b)
