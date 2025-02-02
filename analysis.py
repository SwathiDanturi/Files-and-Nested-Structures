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
                csv_reader = csv.DictReader(csv_file, delimiter=",", quotechar='"')
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

    def freq_of_lang(self):
        """
        Returns a dictionary with the number of times each language appears
        in the `self.devs` list, where language is a key and the frequency
        of the language is the value.
        """
        lang_freq = {}
        for dev_data in self.devs:
            languages_admired = dev_data["LanguageAdmired"].split(";")
            for language in languages_admired:
                if language != "NA":
                    if language not in lang_freq:
                        lang_freq[language] = 0
                    lang_freq[language] += 1
        return lang_freq

    def lang_histogram(self):
        """
        Returns a dictionary with the number of developers who know a
        certain number of languages, where the number of languages is a key
        and the list of languages known by that number of developers is the
        value.
        """
        lang_histo = {}
        lang_freq = self.freq_of_lang()
        for lang, freq in lang_freq.items():
            if freq not in lang_histo:
                lang_histo[freq] = []
            lang_histo[freq].append(lang)
        return lang_histo

    def write_lang_popularity(self):
        """
        Writes the popularity of languages into a new CSV file.
        """
        lang_histogram = self.lang_histogram()
        try:
            with open(
                "devopswrite.csv", mode="w", encoding="utf-8", newline=""
            ) as new_csv_file:
                csv_write = csv.writer(new_csv_file)
                csv_write.writerow(["Frequency", "Languages"])
                for freq, langs in lang_histogram.items():
                    langs = ";".join(langs)
                    csv_write.writerow([freq, langs])
            new_csv_file.close()
        except IOError as err:
            print(err)
