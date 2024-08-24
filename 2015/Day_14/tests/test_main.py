"""
Tests for functions in the main script.
"""

import main


def test_parse_data():
    assert main.parse_data("./data/example_01.txt") == {
        "Comet": {"fly_speed": 14, "fly_time": 10, "rest_time": 127},
        "Dancer": {"fly_speed": 16, "fly_time": 11, "rest_time": 162},
    }


def test_distance_comet():
    assert [
        x
        for x in main.dist_trav(
            {"fly_speed": 14, "fly_time": 10, "rest_time": 127}, 1000
        )
    ][-1] == 1120


def test_distance_dancer():
    assert [
        x
        for x in main.dist_trav(
            {"fly_speed": 16, "fly_time": 11, "rest_time": 162}, 1000
        )
    ][-1] == 1056
