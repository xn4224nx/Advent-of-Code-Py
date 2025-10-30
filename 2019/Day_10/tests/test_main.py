"""
Tests for the main script.
"""

from main import AsteroidField


def test_read_field_exp0():
    assert AsteroidField("./data/example_0.txt").locs == [
        (1, 0),
        (4, 0),
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (4, 2),
        (4, 3),
        (3, 4),
        (4, 4),
    ]


def test_num_los_exp0():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(0) == 7


def test_num_los_exp1():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(1) == 7


def test_num_los_exp2():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(2) == 6


def test_num_los_exp3():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(3) == 7


def test_num_los_exp4():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(4) == 7


def test_num_los_exp5():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(5) == 7


def test_num_los_exp6():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(6) == 5


def test_num_los_exp7():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(7) == 7


def test_num_los_exp8():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(8) == 8


def test_num_los_exp9():
    assert AsteroidField("./data/example_0.txt").line_of_sight_num(9) == 7


def test_find_max_los_exp0():
    assert AsteroidField("./data/example_0.txt").find_max_los() == 8


def test_find_max_los_exp1():
    assert AsteroidField("./data/example_1.txt").find_max_los() == 33


def test_find_max_los_exp2():
    assert AsteroidField("./data/example_2.txt").find_max_los() == 35


def test_find_max_los_exp3():
    assert AsteroidField("./data/example_3.txt").find_max_los() == 41


def test_find_max_los_exp4():
    assert AsteroidField("./data/example_4.txt").find_max_los() == 210
