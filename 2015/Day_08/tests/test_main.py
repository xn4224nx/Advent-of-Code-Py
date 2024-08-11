"""
Tests for functions in the main script.
"""

import main


def test_read_nn_list():
    assert main.read_nn_list("./data/example_01.txt") == [
        '""',
        '"abc"',
        '"aaa\\"aaa"',
        '"\\x27"',
    ]


def test_count_raw_char():
    assert [
        main.count_raw_char(x) for x in main.read_nn_list("./data/example_01.txt")
    ] == [2, 5, 10, 6]


def test_count_literal_char():
    assert [
        main.count_literal_char(x) for x in main.read_nn_list("./data/example_01.txt")
    ] == [0, 3, 7, 1]


def test_char_deficit():
    assert main.char_deficit("./data/example_01.txt") == 12
