"""
Tests for the main script.
"""

from main import valid_password


def test_pass_valid_exp_0():
    assert valid_password(111111) == True


def test_pass_valid_exp_1():
    assert valid_password(223450) == False


def test_pass_valid_exp_2():
    assert valid_password(123789) == False


def test_pass_valid_exp_3():
    assert valid_password(112233, True) == True


def test_pass_valid_exp_4():
    assert valid_password(123444, True) == False


def test_pass_valid_exp_5():
    assert valid_password(111122, True) == True
