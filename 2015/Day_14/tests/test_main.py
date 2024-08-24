"""
Tests for functions in the main script.
"""

import main


def test_parse_data():
    assert main.parse_data("./data/example_01.txt") == [
        {"fly_speed": 14, "fly_time": 10, "rest_time": 127},
        {"fly_speed": 16, "fly_time": 11, "rest_time": 162},
    ]


def test_distance_comet():
    assert (
        main.dist_trav({"fly_speed": 14, "fly_time": 10, "rest_time": 127}, 1000)
        == 1120
    )


def test_distance_dancer():
    assert (
        main.dist_trav({"fly_speed": 16, "fly_time": 11, "rest_time": 162}, 1000)
        == 1056
    )


def test_race_dist():
    rein_data = main.parse_data("./data/example_01.txt")
    assert main.race_winner_dist(rein_data, 1000)[0] == 1120


def test_race_score():
    rein_data = main.parse_data("./data/example_01.txt")
    assert main.race_winner_dist(rein_data, 1000)[1] == 689
