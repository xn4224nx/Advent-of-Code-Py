"""
Tests for the calc_area() function.
"""

import main


def test_example_01():
    assert main.calc_area(2, 3, 4) == 58


def test_example_02():
    assert main.calc_area(1, 1, 10) == 43
