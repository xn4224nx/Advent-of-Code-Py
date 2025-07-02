"""
Tests for the main script
"""

from main import Polymer


def test_new_polymer_exp01():
    test = Polymer("dabAcCaCBAcCcaDA")
    assert test.units == "dabAcCaCBAcCcaDA"


def test_new_polymer_exp02():
    test = Polymer("abBA")
    assert test.units == "abBA"


def test_new_polymer_exp03():
    test = Polymer("aabAAB")
    assert test.units == "aabAAB"


def test_collapse_exp01():
    test = Polymer("dabAcCaCBAcCcaDA")
    test.collapse()
    assert test.units == "dabAaCBAcaDA"


def test_collapse_exp02():
    test = Polymer("dabAaCBAcaDA")
    test.collapse()
    assert test.units == "dabCBAcaDA"


def test_collapse_exp03():
    test = Polymer("aabAAB")
    test.collapse()
    assert test.units == "aabAAB"


def test_collapse_exp04():
    test = Polymer("abBA")
    test.collapse()
    assert test.units == "aA"


def test_collapse_exp05():
    test = Polymer("aA")
    test.collapse()
    assert test.units == ""


def test_final_len_exp01():
    assert Polymer("dabAcCaCBAcCcaDA").final_len() == 10


def test_final_len_exp02():
    assert Polymer("abBA").final_len() == 0
