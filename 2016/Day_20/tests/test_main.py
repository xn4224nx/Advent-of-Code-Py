"""
Tests for the main script
"""

from main import Firewall


def test_class_initialisation():
    test = Firewall("./data/example_01.txt", (0, 9))
    assert test.rules == [(0, 2), (4, 7), (5, 8)]
    assert test.allowed_rng == (0, 9)


def test_lowest_allowed_address_exp2():
    test = Firewall("./data/example_01.txt", (0, 9))
    assert test.lowest_allowed_address() == 3
