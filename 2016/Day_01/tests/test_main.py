"""
Tests for the main script
"""

from main import read_direction_data, directions_dist


def test_read_example_01():
    assert read_direction_data("./data/example_01.txt") == [["R", 2], ["L", 3]]


def test_read_example_02():
    assert read_direction_data("./data/example_02.txt") == [
        ["R", 2],
        ["R", 2],
        ["R", 2],
    ]


def test_read_example_03():
    assert read_direction_data("./data/example_03.txt") == [
        ["R", 5],
        ["L", 5],
        ["R", 5],
        ["R", 3],
    ]


def test_directions_dist_exp_1():
    data = read_direction_data("./data/example_01.txt")
    assert directions_dist(data) == 5


def test_directions_dist_exp_2():
    data = read_direction_data("./data/example_02.txt")
    assert directions_dist(data) == 2


def test_directions_dist_exp_3():
    data = read_direction_data("./data/example_03.txt")
    assert directions_dist(data) == 12
