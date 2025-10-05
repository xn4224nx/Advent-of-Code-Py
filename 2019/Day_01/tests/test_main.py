"""
Tests for the main script.
"""

from main import module_fuel_req


def test_example_01():
    assert module_fuel_req(12) == 2


def test_example_02():
    assert module_fuel_req(14) == 2


def test_example_03():
    assert module_fuel_req(1969) == 654


def test_example_04():
    assert module_fuel_req(100756) == 33583


def test_example_05():
    assert module_fuel_req(14, True) == 2


def test_example_06():
    assert module_fuel_req(1969, True) == 966


def test_example_07():
    assert module_fuel_req(100756, True) == 50346
