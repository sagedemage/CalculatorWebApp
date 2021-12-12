"""Testing Addition"""

from tests import read_csv
from calc.calculations.division import Division


def test_division_two_values():
    """Testing division method for two values"""
    path = "tests/test_data/division/division_2_values.csv"
    # read_two_columns function
    columns = read_csv.read_two_columns(path)

    for i in range(columns[2].size):
        # columns: value1, value2 and result
        # Arrange
        division = Division(columns[0][i], (columns[1][i],))
        # Act and Assert
        assert division.get_result() == columns[2][i]


def test_division_three_values():
    """Testing multiplication method for three values"""
    path = "tests/test_data/division/division_3_values.csv"
    # read_three_columns function
    columns = read_csv.read_three_columns(path)

    for i in range(columns[3].size):
        # columns: value1, value2, value3 and result
        # Arrange
        division = Division(columns[0][i], (columns[1][i], columns[2][i]))
        # Act and Assert
        assert division.get_result() == columns[3][i]


def test_division_by_zero():
    """Testing division by zero"""
    # Arrange
    division1 = Division(5, (0,))
    division2 = Division(5, (0, 0))
    # Act and Assert
    assert division1.get_result() is None
    assert division2.get_result() is None
