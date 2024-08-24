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


def test_weight_combinations():
    assert [x for x in main.weight_combinations(["Butterscotch", "Cinnamon"], 10)] == [
        {"Butterscotch": 0, "Cinnamon": 10},
        {"Butterscotch": 1, "Cinnamon": 9},
        {"Butterscotch": 2, "Cinnamon": 8},
        {"Butterscotch": 3, "Cinnamon": 7},
        {"Butterscotch": 4, "Cinnamon": 6},
        {"Butterscotch": 5, "Cinnamon": 5},
        {"Butterscotch": 6, "Cinnamon": 4},
        {"Butterscotch": 7, "Cinnamon": 3},
        {"Butterscotch": 8, "Cinnamon": 2},
        {"Butterscotch": 9, "Cinnamon": 1},
        {"Butterscotch": 10, "Cinnamon": 0},
    ]
