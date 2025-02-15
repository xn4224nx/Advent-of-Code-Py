"""
Tests for the main script
"""

from main import SpreadSheet


def test_data_import_exp1():
    assert SpreadSheet("./data/example_01.txt").data == [
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8],
    ]


def test_data_import_exp2():
    assert SpreadSheet("./data/example_02.txt").data == [
        [5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5],
    ]


def test_checksum():
    assert SpreadSheet("./data/example_01.txt").checksum() == 18


def test_checksum():
    assert SpreadSheet("./data/example_02.txt").even_divisible_sum() == 9
