"""
Tests for the main script
"""

from main import Firewall


def test_new_firewall_exp01():
    test = Firewall("./data/example_01.txt")

    assert test.structure == [
        (0, 3),
        (1, 2),
        (4, 4),
        (6, 4),
    ]
    assert test.scanners == [0, 0, 0, 0]
    assert test.packet == 0


def test_cycle_exp1():
    test = Firewall("./data/example_01.txt")
    test.cycle_before_launch(0)
    assert test.scanners == [0, 0, 0, 0]


def test_cycle_exp2():
    test = Firewall("./data/example_01.txt")
    test.cycle_before_launch(1)
    assert test.scanners == [1, 1, 1, 1]


def test_cycle_exp3():
    test = Firewall("./data/example_01.txt")
    test.cycle_before_launch(2)
    assert test.scanners == [2, 0, 2, 2]


def test_cycle_exp4():
    test = Firewall("./data/example_01.txt")
    test.cycle_before_launch(3)
    assert test.scanners == [1, 1, 3, 3]


def test_trip_severity_exp1():
    Firewall("./data/example_01.txt").trip_severity() == 24


def test_traverse_exp1():
    Firewall("./data/example_01.txt").traverse(0) == 24
