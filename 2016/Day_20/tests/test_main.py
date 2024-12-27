"""
Tests for the main script
"""

from main import Firewall


def test_class_initialisation():
    test = Firewall("./data/example_01.txt", (0, 9))
    assert test.rules == [(5, 8), (0, 2), (4, 7)]
    assert test.allowed_rng == [(0, 9)]


def test_blacklist_range_exp1():
    test = Firewall("", (0, 9))
    test.blacklist_range((5, 8))
    assert test.allowed_rng == [(0, 4), (9, 9)]


def test_blacklist_range_exp2():
    test = Firewall("", (0, 9))
    test.blacklist_range((0, 2))
    assert test.allowed_rng == [(3, 9)]


def test_blacklist_range_exp3():
    test = Firewall("", (0, 9))
    test.blacklist_range((4, 7))
    assert test.allowed_rng == [(0, 3), (8, 9)]


def test_blacklist_range_exp4():
    test = Firewall("", (0, 9))

    test.blacklist_range((5, 8))
    assert test.allowed_rng == [(0, 4), (9, 9)]

    test.blacklist_range((0, 2))
    assert test.allowed_rng == [(3, 4), (9, 9)]

    test.blacklist_range((4, 7))
    assert test.allowed_rng == [(3, 3), (9, 9)]


def test_blacklist_all_ranges_exp1():
    test = Firewall("", (0, 9))
    test.blacklist_all_ranges()
    assert test.allowed_rng == [(3, 3), (9, 9)]


def test_lowest_allowed_address_exp1():
    test = Firewall("", (0, 9))
    assert test.lowest_allowed_address() == 0


def test_lowest_allowed_address_exp2():
    test = Firewall("./data/example_01.txt", (0, 9))
    test.blacklist_all_ranges()
    assert test.lowest_allowed_address() == 3
