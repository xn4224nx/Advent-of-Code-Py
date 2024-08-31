"""
Tests for functions in the main script.
"""

import main


def test_find_lowest_house_1():
    assert main.find_lowest_house(120) == 6


def test_find_lowest_house_2():
    assert main.find_lowest_house(150) == 8
