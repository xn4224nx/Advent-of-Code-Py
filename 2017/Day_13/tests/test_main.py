"""
Tests for the main script
"""

from main import Firewall


def test_new_firewall_exp01():
    test = Firewall("./data/example_01.txt")

    assert test.sc_info == [
        (0, 3),
        (1, 2),
        (4, 4),
        (6, 4),
    ]
    assert test.sc_level == [0, 0, 0, 0]
    assert test.sc_desc == [True, True, True, True]
    assert test.packet_loc == 0


def test_increment_scanners_exp1():
    test = Firewall("./data/example_01.txt")
    test.increment_scanners()
    assert test.sc_level == [1, 1, 1, 1]
    assert test.sc_desc == [
        True,
        False,
        True,
        True,
    ]


def test_increment_scanners_exp2():
    test = Firewall("./data/example_01.txt")
    for _ in range(2):
        test.increment_scanners()
    assert test.sc_level == [2, 0, 2, 2]
    assert test.sc_desc == [
        False,
        True,
        True,
        True,
    ]


def test_increment_scanners_exp3():
    test = Firewall("./data/example_01.txt")
    for _ in range(3):
        test.increment_scanners()
    assert test.sc_level == [1, 1, 3, 3]
    assert test.sc_desc == [
        False,
        False,
        False,
        False,
    ]


def test_increment_scanners_exp4():
    test = Firewall("./data/example_01.txt")
    for _ in range(4):
        test.increment_scanners()
    assert test.sc_level == [0, 0, 2, 2]
    assert test.sc_desc == [
        True,
        True,
        False,
        False,
    ]


def test_increment_scanners_exp5():
    test = Firewall("./data/example_01.txt")
    for _ in range(5):
        test.increment_scanners()
    assert test.sc_level == [1, 1, 1, 1]
    assert test.sc_desc == [
        True,
        False,
        False,
        False,
    ]


def test_increment_scanners_exp6():
    test = Firewall("./data/example_01.txt")
    for _ in range(6):
        test.increment_scanners()
    assert test.sc_level == [2, 0, 0, 0]
    assert test.sc_desc == [
        False,
        True,
        True,
        True,
    ]


def test_increment_scanners_exp7():
    test = Firewall("./data/example_01.txt")
    for _ in range(7):
        test.increment_scanners()
    assert test.sc_level == [1, 1, 1, 1]
    assert test.sc_desc == [
        False,
        False,
        True,
        True,
    ]


def test_trip_severity_exp1():
    assert Firewall("./data/example_01.txt").trip_severity() == 24


def test_traverse_exp1():
    assert Firewall("./data/example_01.txt").traverse(0) == 24


def test_traverse_eq_trip_severity_exp1():
    assert (
        Firewall("./data/example_01.txt").traverse(0)
        == Firewall("./data/example_01.txt").trip_severity()
    )
