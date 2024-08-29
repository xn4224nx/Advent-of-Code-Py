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


def test_find_aunt():
    test_data = main.read_aunt_data("./data/p1_example_aunts.txt")
    aunt_to_find = main.read_aunt_data("./data/p1_aunt.txt")
    assert find_matched_aunt(test_data, aunt_to_find) == 5
