"""
Tests for the main script.
"""

from main import TwoWires


def test_new_two_wires_exp_0():
    test = TwoWires("./data/example_0.txt")
    assert test.wire_pnts == [
        {
            (4, 0),
            (3, 4),
            (8, 0),
            (8, 3),
            (1, 0),
            (6, 5),
            (3, 0),
            (4, 5),
            (3, 3),
            (5, 0),
            (8, 2),
            (8, 5),
            (7, 0),
            (3, 2),
            (3, 5),
            (5, 5),
            (8, 4),
            (8, 1),
            (2, 0),
            (6, 0),
            (7, 5),
        },
        {
            (4, 3),
            (3, 7),
            (5, 7),
            (0, 2),
            (0, 5),
            (6, 5),
            (3, 3),
            (5, 3),
            (0, 1),
            (0, 7),
            (0, 4),
            (2, 7),
            (6, 4),
            (6, 7),
            (4, 7),
            (0, 3),
            (0, 6),
            (2, 3),
            (1, 7),
            (6, 6),
            (6, 3),
        },
    ]


def test_crossing_dist_exp_0():
    assert TwoWires("./data/example_0.txt").crossing_dist() == 6


def test_crossing_dist_exp_1():
    assert TwoWires("./data/example_1.txt").crossing_dist() == 159


def test_crossing_dist_exp_2():
    assert TwoWires("./data/example_2.txt").crossing_dist() == 135
