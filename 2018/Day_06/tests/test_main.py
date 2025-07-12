"""
Tests for the main script
"""

from main import MineField


def test_new_minefield_exp01():
    test = MineField("./data/example_0.txt")
    assert test.mine_coords == [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9),
    ]
    assert test.field_size == (8, 9)


def test_largest_enclosed_space_exp01():
    assert MineField("./data/example_0.txt").largest_enclosed_space() == 17
