"""
Tests for the houses_covered() function.
"""

import main


def test_example_01():
    directions = main.read_directions("./data/example_01.txt")
    assert directions == ">"
    assert len(main.houses_covered(directions)) == 2


def test_example_02():
    directions = main.read_directions("./data/example_02.txt")
    assert directions == "^>v<"
    assert len(main.houses_covered(directions)) == 4


def test_example_03():
    directions = main.read_directions("./data/example_03.txt")
    assert directions == "^v^v^v^v^v"
    assert len(main.houses_covered(directions)) == 2
