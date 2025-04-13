"""
Tests for the main script
"""

from main import Firewall


def test_new_firewall_exp01():
    assert Firewall("./data/example_01.txt").sc_info == {
        0: 3,
        1: 2,
        4: 4,
        6: 4,
    }


def test_scanner_position_exp01():
    assert Firewall("./data/example_01.txt").scanner_position(0, 2) == 2


def test_scanner_position_exp02():
    assert Firewall("./data/example_01.txt").scanner_position(1, 2) == 0


def test_scanner_position_exp03():
    assert Firewall("./data/example_01.txt").scanner_position(4, 2) == 2


def test_scanner_position_exp04():
    assert Firewall("./data/example_01.txt").scanner_position(6, 2) == 2


def test_scanner_position_exp05():
    assert Firewall("./data/example_01.txt").scanner_position(0, 6) == 2


def test_scanner_position_exp06():
    assert Firewall("./data/example_01.txt").scanner_position(1, 6) == 0


def test_scanner_position_exp07():
    assert Firewall("./data/example_01.txt").scanner_position(4, 6) == 0


def test_scanner_position_exp08():
    assert Firewall("./data/example_01.txt").scanner_position(6, 6) == 0


def test_trip_severity_exp1():
    assert Firewall("./data/example_01.txt").trip_severity() == 24


def test_find_clear_path_exp1():
    assert Firewall("./data/example_01.txt").find_clear_path() == 10
