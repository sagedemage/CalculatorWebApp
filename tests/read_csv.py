"""Reading in the cvs file"""
import pandas as pd


def read_two_columns(path):
    """Reading two columns of a table"""
    # Read in the csv file
    dataframe = pd.read_csv(path)

    # Read each column of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    result = dataframe["result"]

    # return tuple of values
    return value1, value2, result


def read_three_columns(path):
    """Reading three columns of a table"""
    # Read in the csv file
    dataframe = pd.read_csv(path)

    # Read each column of the table
    value1 = dataframe["value_1"]
    value2 = dataframe["value_2"]
    value3 = dataframe["value_3"]
    result = dataframe["result"]

    # return a tuple of values
    return value1, value2, value3, result
