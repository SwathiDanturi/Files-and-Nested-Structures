"""
Test freq_of_lang function of analysis.py

File: test_freq_of_lang.py
Developer: Swathi Danturi
Date: 11/11/2024
"""

import pytest
from analysis import Analysis


def test_freq_of_lang_for_devops1csv():
    """
    Test freq_of_lang function of analysis.py for devops1.csv
    """
    test_lang_freq = Analysis("./devops1.csv")
    actual = test_lang_freq.freq_of_lang()
    expected = {"Assembly": 1, "C#": 1, "C++": 1, "SQL": 1}
    assert actual == expected


def test_freq_of_lang_for_devops5csv():
    """
    Test freq_of_lang function of analysis.py for devops5.csv
    """
    test_lang_freq = Analysis("./devops5.csv")
    actual = test_lang_freq.freq_of_lang()
    expected = {
        "C#": 3,
        "C++": 2,
        "HTML/CSS": 1,
        "Java": 1,
        "JavaScript": 1,
        "Python": 1,
        "Bash/Shell (all shells)": 2,
        "Go": 1,
        "SQL": 3,
        "Assembly": 1,
        "C": 1,
        "MATLAB": 1,
        "PowerShell": 1,
    }
    assert actual == expected


def test_freq_of_lang_for_devops10csv():
    """
    Test freq_of_lang function of analysis.py for devops10.csv
    """
    test_lang_freq = Analysis("./devops10.csv")
    actual = test_lang_freq.freq_of_lang()
    expected = {
        "Bash/Shell (all shells)": 2,
        "Go": 1,
        "HTML/CSS": 5,
        "Java": 3,
        "JavaScript": 5,
        "Python": 4,
        "TypeScript": 4,
        "C#": 1,
        "PowerShell": 1,
        "SQL": 1,
        "C++": 1,
        "Lua": 2,
        "Swift": 1,
        "R": 1,
    }
    assert actual == expected


pytest.main()
