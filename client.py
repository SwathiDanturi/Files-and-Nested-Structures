"""
Practice with classes, files, and netested structures

File: client.py
Developers: COMP 801 instructors
"""

from analysis import Analysis


def main():
    """
    Demo the functionality of the Analysis constructor and __str__() method.
    To run this module, in Terminal, select bash and change directory to h3
    directory. Then, either use the arrow in upper-right corner, or,
    in the Terminal, run: python client.py
    """
    devs_file = "./devops10.csv"
    analysis_obj = Analysis(devs_file)
    print(analysis_obj.devs)


main()
