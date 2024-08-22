"""
Tests for functions in the main script.
"""

import main


def test_increment_string_01():
    test = "aaaaaaaa"
    for _ in range(1):
        test = main.increment_string(test)

    assert test == "aaaaaaab"


def test_increment_string_02():
    test = "aaaaaaaa"
    for _ in range(1000):
        test = main.increment_string(test)

    assert test == "aaaaabmm"


def test_valid_str_01():
    assert main.valid_password("hijklmmn") == False


def test_valid_str_02():
    assert main.valid_password("abbceffg") == False


def test_valid_str_03():
    assert main.valid_password("abbcegjk") == False


def test_valid_str_04():
    assert main.valid_password("abcdffaa") == True


def test_valid_str_05():
    assert main.valid_password("ghjaabcc") == True


def test_find_next_01():
    assert main.find_next_pass("abcdefgh") == "abcdffaa"


def test_find_next_02():
    assert main.find_next_pass("ghijklmn") == "ghjaabcc"
