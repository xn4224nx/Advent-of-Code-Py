"""
Tests for the main script
"""

from main import decompress_data


def test_decompress_exp1():
    decompress_data("./data/example_01.txt") == "ADVENT"


def test_decompress_exp2():
    decompress_data("./data/example_02.txt") == "ABBBBBC"


def test_decompress_exp3():
    decompress_data("./data/example_03.txt") == "XYZXYZXYZ"


def test_decompress_exp4():
    decompress_data("./data/example_04.txt") == "ABCBCDEFEFG"


def test_decompress_exp5():
    decompress_data("./data/example_05.txt") == "(1x3)A"


def test_decompress_exp6():
    decompress_data("./data/example_06.txt") == "X(3x3)ABC(3x3)ABCY"
