"""
Tests for the valid_mine() function.
"""

import main


def test_example_01():
    assert main.valid_mine("abcdef", 609043)


def test_example_02():
    assert main.valid_mine("pqrstuv", 1048970)
