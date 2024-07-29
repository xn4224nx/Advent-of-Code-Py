"""
Tests for the calc_ribbon() function.
"""

import main


def test_example_01():
    assert main.calc_ribbon(2, 3, 4) == 34


def test_example_02():
    assert main.calc_ribbon(1, 1, 10) == 14
