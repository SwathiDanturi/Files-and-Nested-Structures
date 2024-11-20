"""
Test write_lang_popularity function of analysis.py

File: test_write_lang_popularity.py
Developer: Swathi Danturi
Date: 11/11/2024
"""

import pytest
from analysis import Analysis


def test_write_lang_popularity_for_devops1csv():
    """
    Test write_lang_popularity function of analysis.py for devops1.csv
    """
    test_write_lang_popularity = Analysis("./devops1.csv")
    test_write_lang_popularity.write_lang_popularity()
    # using constructor to read the file instead of reading the file again
    test_write_lang_popularity_for_file1csv = Analysis("./devopswrite.csv")
    actual = test_write_lang_popularity_for_file1csv.devs
    expected = [{"Frequency": "1", "Languages": "Assembly;C#;C++;SQL"}]
    assert actual == expected


def test_write_lang_popularity_for_devops5csv():
    """
    Test write_lang_popularity function of analysis.py for devops5.csv
    """
    test_write_lang_popularity = Analysis("./devops5.csv")
    test_write_lang_popularity.write_lang_popularity()
    # using constructor to read the file instead of reading the file again
    test_write_lang_popularity_for_file1csv = Analysis("./devopswrite.csv")
    actual = test_write_lang_popularity_for_file1csv.devs
    expected = [
        {"Frequency": "3", "Languages": "C#;SQL"},
        {"Frequency": "2", "Languages": "C++;Bash/Shell (all shells)"},
        {
            "Frequency": "1",
            "Languages": "HTML/CSS;Java;JavaScript;Python;Go;Assembly;C;MATLAB;"
            "PowerShell",
        },
    ]
    assert actual == expected


def test_write_lang_popularity_for_devops10csv():
    """
    Test write_lang_popularity function of analysis.py for devops10.csv
    """
    test_write_lang_popularity = Analysis("./devops10.csv")
    test_write_lang_popularity.write_lang_popularity()
    # using constructor to read the file instead of reading the file again
    test_write_lang_popularity_for_file1csv = Analysis("./devopswrite.csv")
    actual = test_write_lang_popularity_for_file1csv.devs
    expected = [
        {"Frequency": "2", "Languages": "Bash/Shell (all shells);Lua"},
        {"Frequency": "1", "Languages": "Go;C#;PowerShell;SQL;C++;Swift;R"},
        {"Frequency": "5", "Languages": "HTML/CSS;JavaScript"},
        {"Frequency": "3", "Languages": "Java"},
        {"Frequency": "4", "Languages": "Python;TypeScript"},
    ]
    assert actual == expected


pytest.main()
