"""
Tests for the main script
"""

from main import Maze


def test_is_wall():
    test = Maze(10)

    assert test.is_wall((0, 0)) == False
    assert test.is_wall((1, 1)) == False

    assert test.is_wall((4, 1)) == False
    assert test.is_wall((4, 2)) == False
    assert test.is_wall((7, 4)) == False
    assert test.is_wall((5, 3)) == False

    assert test.is_wall((7, 3)) == True
    assert test.is_wall((1, 0)) == True
    assert test.is_wall((9, 6)) == True
    assert test.is_wall((2, 3)) == True


def test_poss_moves():
    test = Maze(10)

    assert set(test.poss_moves((1, 1))) == set(
        [
            (1, 2),
            (0, 1),
        ]
    )
    assert set(test.poss_moves((6, 5))) == set(
        [
            (7, 5),
            (5, 5),
            (6, 4),
            (6, 6),
        ]
    )
    assert set(test.poss_moves((0, 4))) == set([(0, 5)])
    assert set(test.poss_moves((7, 0))) == set([(7, 1)])


def test_min_path():
    test = Maze(10)
    assert test.find_min_path_len((7, 4)) == 11
    assert test.find_min_path_len((6, 5)) == 9
