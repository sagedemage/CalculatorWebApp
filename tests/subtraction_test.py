"""Testing Subtraction"""

from tests import read_csv
from calc.calculations.subtraction import Subtraction


def test_subtraction_two_values():
    """Testing subtraction method for two values"""
    path = "tests/test_data/subtraction/subtraction_2_values.csv"
    # read_two_columns function
    columns = read_csv.read_two_columns(path)

    for i in range(columns[2].size):
        # columns: value1, value2 and result
        # Arrange
        subtraction = Subtraction(columns[0][i], (columns[1][i],))
        # Act and Assert
        assert subtraction.get_result() == columns[2][i]


def test_subtraction_three_values():
    """Testing subtraction method for three values"""
    path = "tests/test_data/subtraction/subtraction_3_values.csv"
    # read_three_columns function
    columns = read_csv.read_three_columns(path)

    for i in range(columns[3].size):
        # columns: value1, value2, value3 and result
        # Arrange
        subtraction = Subtraction(columns[0][i], (columns[1][i], columns[2][i]))
        # Act and Assert
        assert subtraction.get_result() == columns[3][i]
