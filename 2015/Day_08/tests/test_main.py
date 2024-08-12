"""
Tests for functions in the main script.
"""

import main

file_p = "./data/example_01.txt"


def test_read_nn_list():
    assert main.read_nn_list(file_p) == [
        '""',
        '"abc"',
        '"aaa\\"aaa"',
        '"\\x27"',
    ]


def test_count_raw_char():
    assert [main.count_raw_char(x) for x in main.read_nn_list(file_p)] == [2, 5, 10, 6]


def test_count_literal_char():
    assert [main.count_literal_char(x) for x in main.read_nn_list(file_p)] == [
        0,
        3,
        7,
        1,
    ]


def test_count_encoded_char():
    assert [main.count_encoded_char(x) for x in main.read_nn_list(file_p)] == [
        6,
        9,
        16,
        11,
    ]


def test_char_deficit_1():
    assert main.char_deficit(file_p, True) == 12


def test_char_deficit_2():
    assert main.char_deficit(file_p, False) == 19
