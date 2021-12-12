""" This is the multiplication calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


class Multiplication(Calculation):
    """The Multiplication class """
    # This class has a get method that calculates the result of multiplication.

    def get_result(self):
        """Get result of multiplication"""
        result = self.value_a
        for value in self.values:
            result = result * value
        return result
