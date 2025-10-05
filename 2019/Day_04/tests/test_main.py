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
