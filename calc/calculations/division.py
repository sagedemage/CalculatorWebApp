""" This is the division calculation """
# It inherits the value A and value B from the calculation class """
from calc.calculations.calculation import Calculation


class Division(Calculation):
    """The Division class """
    # This class has a get method that calculates the result of division.

    def get_result(self):
        """Get result of division"""
        result = self.value_a
        try:
            for value in self.values:
                # Value needs to be a float to avoid weird rounding issues
                result = round(result / value, 6)
        except ZeroDivisionError:
            result = None
        return result
