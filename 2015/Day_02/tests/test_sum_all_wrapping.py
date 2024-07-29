"""
Tests for the sum_all_wrapping() function.
"""

import main


def test_example_03():

    box_dims = main.parse_box_dims("./data/example_03.txt")

    assert main.parse_box_dims("./data/example_03.txt") == [(2, 3, 4), (1, 1, 10)]
    assert main.sum_all_wrapping(box_dims) == 101
