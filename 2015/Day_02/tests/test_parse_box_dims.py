"""
Tests for the parse_box_dims() function.
"""

import main


def test_example_01():
    assert main.parse_box_dims("./data/example_01.txt") == [(2, 3, 4)]


def test_example_02():
    assert main.parse_box_dims("./data/example_02.txt") == [(1, 1, 10)]


def test_example_03():
    assert main.parse_box_dims("./data/example_03.txt") == [(2, 3, 4), (1, 1, 10)]
