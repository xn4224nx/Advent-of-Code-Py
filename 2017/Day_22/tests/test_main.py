"""
Tests for the main script.
"""

from main import Infection


def test_count_on_pixels_exp04():
    test = Infection("./data/example_01.txt")
    assert test.carr_loc == (1, 1)
    assert test.carr_dir == complex(0, 1)
    assert test.infec_nodes == {
        (2, 0),
        (0, 1),
    }


def test_burst_exp01():
    test = Infection("./data/example_01.txt")
    test.burst()
    assert test.carr_loc == (0, 1)
    assert test.carr_dir == complex(-1, 0)
    assert test.infec_nodes == {
        (2, 0),
        (0, 1),
        (1, 1),
    }


def test_burst_exp02():
    test = Infection("./data/example_01.txt")
    test.carr_loc = (0, 1)
    test.carr_dir = complex(-1, 0)
    test.infec_nodes = {
        (2, 0),
        (0, 1),
        (1, 1),
    }
    test.burst()
    assert test.carr_loc == (0, 0)
    assert test.carr_dir == complex(0, 1)
    assert test.infec_nodes == {
        (2, 0),
        (1, 1),
    }


def test_burst_exp03():
    test = Infection("./data/example_01.txt")
    for _ in range(6):
        test.burst()

    assert test.carr_loc == (0, 0)
    assert test.carr_dir == complex(0, 1)
    assert test.infec_nodes == {
        (0, 1),
        (-1, 0),
        (0, 0),
        (-1, 1),
        (1, 1),
        (2, 0),
    }


def test_burst_exp04():
    test = Infection("./data/example_01.txt")
    for _ in range(7):
        test.burst()

    assert test.carr_loc == (1, 0)
    assert test.carr_dir == complex(1, 0)
    assert test.infec_nodes == {(0, 1), (-1, 1), (1, 1), (2, 0), (-1, 0)}


def test_burst_exp05():
    test = Infection("./data/example_01.txt")
    for _ in range(70):
        test.burst()

    assert test.carr_loc == (2, 0)
    assert test.carr_dir == complex(0, 1)
    assert test.infec_nodes == {
        (5, -1),
        (-1, 0),
        (2, 2),
        (4, -2),
        (1, 0),
        (3, 2),
        (4, 1),
        (2, -3),
        (-1, 1),
        (1, 1),
        (3, -3),
        (1, -2),
        (5, 0),
        (0, -1),
    }


def test_num_burst_infected_exp01():
    assert Infection("./data/example_01.txt").num_burst_infected(7) == 5


def test_num_burst_infected_exp02():
    assert Infection("./data/example_01.txt").num_burst_infected(70) == 41


def test_num_burst_infected_exp03():
    assert Infection("./data/example_01.txt").num_burst_infected(10000) == 5587
