"""
Tests for functions in the main script.
"""

import main
import pytest


def test_parse_aunt_data():
    assert main.read_aunt_data("./data/p1_aunt.txt") == [
        {
            "children": 3,
            "cats": 7,
            "samoyeds": 2,
            "pomeranians": 3,
            "akitas": 0,
            "vizslas": 0,
            "goldfish": 5,
            "trees": 3,
            "cars": 2,
            "perfumes": 1,
        }
    ]


def test_parse_aunt_data_2():
    assert main.read_aunt_data("./data/p1_example_aunts.txt") == [
        {"children": 1, "cars": 8, "vizslas": 7},
        {"akitas": 10, "perfumes": 10, "children": 5},
        {"cars": 5, "pomeranians": 4, "vizslas": 1},
        {"goldfish": 5, "children": 8, "perfumes": 3},
        {"vizslas": 0, "akitas": 0, "perfumes": 1},
        {"vizslas": 0, "akitas": 1, "perfumes": 2},
        {"perfumes": 8, "cars": 4, "goldfish": 10},
        {"perfumes": 7, "children": 2, "cats": 1},
        {"pomeranians": 3, "goldfish": 10, "trees": 10},
        {"akitas": 7, "trees": 8, "pomeranians": 4},
    ]


def test_is_same_aunt_ex_1():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"children": 1, "cars": 8, "vizslas": 7}) == False
    )


def test_is_same_aunt_ex_2():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"akitas": 10, "perfumes": 10, "children": 5})
        == False
    )


def test_is_same_aunt_ex_3():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"cars": 5, "pomeranians": 4, "vizslas": 1})
        == False
    )


def test_is_same_aunt_ex_4():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"goldfish": 5, "children": 8, "perfumes": 3})
        == False
    )


def test_is_same_aunt_ex_5():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"vizslas": 0, "akitas": 0, "perfumes": 1}) == True
    )


def test_is_same_aunt_ex_6():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"vizslas": 0, "akitas": 1, "perfumes": 2})
        == False
    )


def test_is_same_aunt_ex_7():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"perfumes": 8, "cars": 4, "goldfish": 10})
        == False
    )


def test_is_same_aunt_ex_8():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"perfumes": 7, "children": 2, "cats": 1}) == False
    )


def test_is_same_aunt_ex_9():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"pomeranians": 3, "goldfish": 10, "trees": 10})
        == False
    )


def test_is_same_aunt_ex_10():
    true_aunt = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert (
        main.is_same_aunt(true_aunt, {"akitas": 7, "trees": 8, "pomeranians": 4})
        == False
    )


def test_find_aunt():
    test_data = main.read_aunt_data("./data/p1_example_aunts.txt")
    aunt_to_find = main.read_aunt_data("./data/p1_aunt.txt")[0]
    assert main.find_matched_aunt(test_data, aunt_to_find) == 5
