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
    assert test.wire_dists == [
        {
            (1, 0): 1,
            (2, 0): 2,
            (3, 0): 3,
            (4, 0): 4,
            (5, 0): 5,
            (6, 0): 6,
            (7, 0): 7,
            (8, 0): 8,
            (8, 1): 9,
            (8, 2): 10,
            (8, 3): 11,
            (8, 4): 12,
            (8, 5): 13,
            (7, 5): 14,
            (6, 5): 15,
            (5, 5): 16,
            (4, 5): 17,
            (3, 5): 18,
            (3, 4): 19,
            (3, 3): 20,
            (3, 2): 21,
        },
        {
            (0, 1): 1,
            (0, 2): 2,
            (0, 3): 3,
            (0, 4): 4,
            (0, 5): 5,
            (0, 6): 6,
            (0, 7): 7,
            (1, 7): 8,
            (2, 7): 9,
            (3, 7): 10,
            (4, 7): 11,
            (5, 7): 12,
            (6, 7): 13,
            (6, 6): 14,
            (6, 5): 15,
            (6, 4): 16,
            (6, 3): 17,
            (5, 3): 18,
            (4, 3): 19,
            (3, 3): 20,
            (2, 3): 21,
        },
    ]


def test_crossing_dist_exp_0():
    assert TwoWires("./data/example_0.txt").crossing_dist() == 6


def test_crossing_dist_exp_1():
    assert TwoWires("./data/example_1.txt").crossing_dist() == 159


def test_crossing_dist_exp_2():
    assert TwoWires("./data/example_2.txt").crossing_dist() == 135


def test_crossing_dist_exp_3():
    assert TwoWires("./data/example_0.txt").crossing_dist(True) == 30


def test_crossing_dist_exp_4():
    assert TwoWires("./data/example_1.txt").crossing_dist(True) == 610


def test_crossing_dist_exp_5():
    assert TwoWires("./data/example_2.txt").crossing_dist(True) == 410
