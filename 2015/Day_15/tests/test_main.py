"""
Tests for functions in the main script.
"""

import main
import pytest


def test_parse_property_data():
    assert main.parse_property_data("./data/example_01.txt") == {
        "Butterscotch": {
            "capacity": -1,
            "durability": -2,
            "flavor": 6,
            "texture": 3,
            "calories": 8,
        },
        "Cinnamon": {
            "capacity": 2,
            "durability": 3,
            "flavor": -2,
            "texture": -1,
            "calories": 3,
        },
    }


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        main.parse_property_data("./data/UNKNOWN_DATA_FILE")


def test_score_weight_comb():
    assert (
        main.score_weight_comb(
            {
                "Butterscotch": {
                    "capacity": -1,
                    "durability": -2,
                    "flavor": 6,
                    "texture": 3,
                    "calories": 8,
                },
                "Cinnamon": {
                    "capacity": 2,
                    "durability": 3,
                    "flavor": -2,
                    "texture": -1,
                    "calories": 3,
                },
            },
            {"Butterscotch": 44, "Cinnamon": 56},
        )
        == 62842880
    )


def test_weight_combinations_sum():
    for comb in main.weight_combinations(["Butterscotch", "Cinnamon"], 10):
        assert sum(comb.values()) == 10


def test_weight_combinations_contents():
    for comb in main.weight_combinations(["Butterscotch", "Cinnamon"], 10):
        assert sorted(["Butterscotch", "Cinnamon"]) == sorted(list(comb.keys()))


def test_weight_combinations_len():
    assert (
        len([x for x in main.weight_combinations(["Butterscotch", "Cinnamon"], 10)])
        == 12
    )
