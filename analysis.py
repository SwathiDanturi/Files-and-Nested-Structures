"""
Practice with classes, files, and nested structures.

File: analysis.py
Initial developers: COMP 801 instructors
Data source: https://insights.stackoverflow.com/survey
Developer: Swathi Danturi
"""

import csv


class Analysis:
    """
    Analyze developer data from the Stack Overflow 2024 survey.
    """

    def __init__(self, file_path):
        """
        Initialize instance variable `self.devs` list with dictionary objects.
        A dictionary object has:
            keys: strings from the fields in the 1st row of the CSV file
            values: strings with information corresponding to the keys

        :param file_path: str, path of CSV file, relative to `analysis.py`
            module. The file has a heading 1st row, followed by rows that have
            data about developers collected by 2024 Stach Overflow survey
            hhttps://survey.stackoverflow.co/2024:
                one respondent per row and one column per answer.
        :return: Analysis object
        """
        self.devs = []
        try:
            with open(file_path, mode="r", encoding="utf-8") as csv_file:
                csv_reader = csv.DictReader(
                    csv_file, delimiter=",", quotechar='"'
                    )
                self.devs = list(csv_reader)
        except IOError as err:
            print(err)

    def __str__(self):
        """
        Returns string representation of the list `self.devs`. The elements
        of the list are dictionaries. Each dictionary corresponds to a row
        in the text file located at `file_path`.
        """
        return self.devs
