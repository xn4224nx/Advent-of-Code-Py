"""
Tests for the main script
"""

from main import Warehouse


def test_read_exp01():
    assert Warehouse("./data/example_01.txt").boxes == [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab",
    ]


def test_box_check_exp01():
    assert Warehouse("./data/example_01.txt").box_check("abcdef") == (False, False)


def test_box_check_exp02():
    assert Warehouse("./data/example_01.txt").box_check("bababc") == (True, True)


def test_box_check_exp03():
    assert Warehouse("./data/example_01.txt").box_check("abbcde") == (True, False)


def test_box_check_exp04():
    assert Warehouse("./data/example_01.txt").box_check("abcccd") == (False, True)


def test_box_check_exp05():
    assert Warehouse("./data/example_01.txt").box_check("aabcdd") == (True, False)


def test_box_check_exp06():
    assert Warehouse("./data/example_01.txt").box_check("abcdee") == (True, False)


def test_box_check_exp07():
    assert Warehouse("./data/example_01.txt").box_check("ababab") == (False, True)


def test_checksum_exp01():
    assert Warehouse("./data/example_01.txt").checksum() == 12
