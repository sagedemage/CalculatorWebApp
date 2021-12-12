"""Testing Addition"""

from tests import read_csv
from calc.calculations.multiplication import Multiplication


def test_multiplication_two_values():
    """Testing multiplication method for two values"""
    path = "tests/test_data/multiplication/multiplication_2_values.csv"
    # read_two_columns function
    columns = read_csv.read_two_columns(path)

    for i in range(columns[2].size):
        # columns: value1, value2 and result
        # Arrange
        multiplication = Multiplication(columns[0][i], (columns[1][i],))
        # Act and Assert
        assert multiplication.get_result() == columns[2][i]


def test_multiplication_three_values():
    """Testing multiplication method for three values"""
    path = "tests/test_data/multiplication/multiplication_3_values.csv"
    # read_three_columns function
    columns = read_csv.read_three_columns(path)

    for i in range(columns[3].size):
        # columns: value1, value2, value3 and result
        # Arrange
        multiplication = Multiplication(columns[0][i], (columns[1][i], columns[2][i]))
        # Act and Assert
        assert multiplication.get_result() == columns[3][i]
