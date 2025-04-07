"""
Tests for the main script
"""

from main import HexGrid


def test_read_path_exp01():
    assert HexGrid("./data/example_01.txt").path == ["ne", "ne", "ne"]


def test_read_path_exp02():
    assert HexGrid("./data/example_02.txt").path == ["ne", "ne", "sw", "sw"]


def test_read_path_exp03():
    assert HexGrid("./data/example_03.txt").path == ["ne", "ne", "s", "s"]


def test_read_path_exp04():
    assert HexGrid("./data/example_04.txt").path == ["se", "sw", "se", "sw", "sw"]


def test_read_path_exp05():
    assert HexGrid("./data/example_05.txt").path == ["se", "se"]


def test_read_path_exp06():
    assert HexGrid("./data/example_06.txt").path == ["s", "s", "sw"]


def test_min_path_len_exp01():
    assert HexGrid("./data/example_01.txt").min_len_path() == 3


def test_min_path_len_exp02():
    assert HexGrid("./data/example_02.txt").min_len_path() == 0


def test_min_path_len_exp03():
    assert HexGrid("./data/example_03.txt").min_len_path() == 2


def test_min_path_len_exp04():
    assert HexGrid("./data/example_04.txt").min_len_path() == 3


def test_min_path_len_exp05():
    assert HexGrid("./data/example_05.txt").min_len_path() == 2


def test_min_path_len_exp06():
    assert HexGrid("./data/example_06.txt").min_len_path() == 3
