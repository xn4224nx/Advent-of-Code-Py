"""
Tests for the houses_covered() function.
"""

import main


def test_example_01():
    directions = main.read_directions("./data/example_01.txt")
    assert directions == ">"
    assert main.houses_covered(directions) == 2


def test_example_02():
    directions = main.read_directions("./data/example_02.txt")
    assert directions == "^>v<"
    assert main.houses_covered(directions) == 4


def test_example_03():
    directions = main.read_directions("./data/example_03.txt")
    assert directions == "^v^v^v^v^v"
    assert main.houses_covered(directions) == 2


def test_robot_example_02():
    directions = main.read_directions("./data/example_02.txt")
    assert directions == "^>v<"
    assert main.houses_covered(directions, True) == 3


def test_robot_example_03():
    directions = main.read_directions("./data/example_03.txt")
    assert directions == "^v^v^v^v^v"
    assert main.houses_covered(directions, True) == 11


def test_robot_example_04():
    directions = main.read_directions("./data/example_04.txt")
    assert directions == "^v"
    assert main.houses_covered(directions, True) == 3
