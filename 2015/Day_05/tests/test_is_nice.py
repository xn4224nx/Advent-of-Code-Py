"""
Tests for the valid_mine() function.
"""

import main


def test_is_nice_exp_1():
    assert main.is_nice("ugknbfddgicrmopn")


def test_is_nice_exp_2():
    assert main.is_nice("aaa")


def test_is_nice_exp_3():
    assert not main.is_nice("jchzalrnumimnmhp")


def test_is_nice_exp_4():
    assert not main.is_nice("haegwjzuvuyypxyu")


def test_is_nice_exp_5():
    assert not main.is_nice("dvszwmarrgswjxmb")
