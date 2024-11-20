"""
Test lang_histogram function of analysis.py

File: test_lang_histogram.py
Developer: Swathi Danturi
Date: 11/11/2024
"""

import pytest
from analysis import Analysis


def test_lang_histogram_for_devops1csv():
    """
    Test lang_histogram function of analysis.py for devops1.csv
    """
    test_lang_histo = Analysis("./devops1.csv")
    actual = test_lang_histo.lang_histogram()
    expected = {1: ["Assembly", "C#", "C++", "SQL"]}
    assert actual == expected


def test_lang_histogram_for_devops5csv():
    """
    Test lang_histogram function of analysis.py for devops5.csv
    """
    test_lang_histo = Analysis("./devops5.csv")
    actual = test_lang_histo.lang_histogram()
    expected = {
        3: ["C#", "SQL"],
        2: ["C++", "Bash/Shell (all shells)"],
        1: [
            "HTML/CSS",
            "Java",
            "JavaScript",
            "Python",
            "Go",
            "Assembly",
            "C",
            "MATLAB",
            "PowerShell",
        ],
    }
    assert actual == expected


def test_lang_histogram_for_devops10csv():
    """
    Test lang_histogram function of analysis.py for devops10.csv
    """
    test_lang_histo = Analysis("./devops10.csv")
    actual = test_lang_histo.lang_histogram()
    expected = {
        2: ["Bash/Shell (all shells)", "Lua"],
        1: ["Go", "C#", "PowerShell", "SQL", "C++", "Swift", "R"],
        5: ["HTML/CSS", "JavaScript"],
        3: ["Java"],
        4: ["Python", "TypeScript"],
    }
    assert actual == expected


pytest.main()
