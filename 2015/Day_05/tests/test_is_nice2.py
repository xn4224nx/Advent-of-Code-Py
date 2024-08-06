"""
Tests for the valid_mine() function.
"""

import main


def test_is_nice_2_exp_1():
    assert main.is_nice_2("qjhvhtzxzqqjkmpb")


def test_is_nice_2_exp_2():
    assert not main.is_nice_2("aaa")


def test_is_nice_2_exp_3():
    assert main.is_nice_2("xxyxx")


def test_is_nice_2_exp_4():
    assert not main.is_nice_2("uurcxstgmygtbstg")


def test_is_nice_2_exp_5():
    assert not main.is_nice_2("ieodomkazucvgmuy")


def test_is_nice_2_exp_6():
    assert main.is_nice_2("xyxy")


def test_is_nice_2_exp_7():
    assert main.is_nice_2("aaaa")


def test_is_nice_2_exp_8():
    assert not main.is_nice_2("a")
