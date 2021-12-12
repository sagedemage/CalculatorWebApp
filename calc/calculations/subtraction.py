""" This is the subtraction calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


class Subtraction(Calculation):
    """The Subtraction class """
    # This class has a get method that calculates the result of subtraction.

    def get_result(self):
        """Get result of subtraction"""
        result = self.value_a
        for value in self.values:
            result = result - value
        return result
