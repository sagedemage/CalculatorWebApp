""" contents of calculations.py """

import pandas as pd


class Calculations:
    """Calculator class"""
    history = []
    csv_history = []
    table = {"operations": [], "value1": [], "value2": [], "result": []}

    @staticmethod
    def count_history():
        """Counting the number of items in the history"""
        count = len(Calculations.history)
        return count

    @staticmethod
    def clear_history():
        """Clear the history"""
        Calculations.history.clear()
        return True

    @staticmethod
    def delete_history(index):
        """Delete an item from the history"""
        Calculations.history.pop(index)
        return True

    @staticmethod
    def add_history(class_object):
        """Add an object to the history"""
        Calculations.history.append(class_object)
        return True

    @staticmethod
    def clear_csv_history():
        """ Clear the history in csv history list """
        Calculations.csv_history.clear()

    @staticmethod
    def clear_csv_files():
        """Clear csv file"""
        Calculations.table["operations"].clear()
        Calculations.table["value1"].clear()
        Calculations.table["value2"].clear()
        Calculations.table["result"].clear()
        # Calculations.csv_history.clear()
        Calculations.clear_csv_history()
        Calculations.dataframe = pd.DataFrame(Calculations.table)
        Calculations.dataframe.to_csv("output.csv", index=False)
        return True

    @staticmethod
    def put_history_to_csv(operation, value1, value2, result):
        """Write the history to csv file"""
        Calculations.table["operations"].append(operation)
        Calculations.table["value1"].append(value1)
        Calculations.table["value2"].append(value2)
        Calculations.table["result"].append(result)
        Calculations.dataframe = pd.DataFrame(Calculations.table)
        Calculations.dataframe.to_csv("output.csv", index=False)
        return True

    @staticmethod
    def read_csv_file(): # There is a problem with this function please fix it
        # pylint: disable=consider-using-enumerate
        """Read the history from csv and put it into the history """
        dataframe = pd.read_csv('output.csv')
        operations = dataframe["operations"]
        value1 = dataframe["value1"]
        value2 = dataframe["value2"]
        result = dataframe["result"]
        # Calculations.csv_history.clear()
        Calculations.clear_csv_history()
        for i in range(len(result)):
            item = [operations[i], value1[i], value2[i], result[i]]
            Calculations.csv_history.append(item)
            print(item)
        return True

    @staticmethod
    def get_history():
        """Get Calculation history from CSV file"""
        # Get history after reading the history
        return Calculations.csv_history

    @staticmethod
    def get_first_calculation():
        """Get the first result from the history"""
        return Calculations.history[0].get_result()

    @staticmethod
    def get_last_calculation():
        """Get the last result from the history"""
        return Calculations.history[-1].get_result()
