"""
Tests for the main script
"""

from main import SpreadSheet


def test_data_import():
    assert SpreadSheet("./data/example_01.txt").data == [
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8],
    ]


def test_checksum():
    assert SpreadSheet("./data/example_01.txt").checksum() == 18
