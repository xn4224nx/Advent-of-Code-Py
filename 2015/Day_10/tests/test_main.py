"""
Tests for functions in the main script.
"""

import main


def test_see_say_ex_01():
    assert main.look_and_say("1") == "11"


def test_see_say_ex_02():
    assert main.look_and_say("11") == "21"


def test_see_say_ex_03():
    assert main.look_and_say("21") == "1211"


def test_see_say_ex_04():
    assert main.look_and_say("1211") == "111221"


def test_see_say_ex_05():
    assert main.look_and_say("111221") == "312211"
