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


def test_find_aunt():
    test_data = main.read_aunt_data("./data/p1_example_aunts.txt")
    aunt_to_find = main.read_aunt_data("./data/p1_aunt.txt")
    assert main.find_matched_aunt(test_data, aunt_to_find) == 5
