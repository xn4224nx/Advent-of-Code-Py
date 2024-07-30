"""
Tests for the read_directions() function.
"""

import main


def test_example_01():
    assert main.read_directions("./data/example_01.txt") == ">"


def test_example_02():
    assert main.read_directions("./data/example_02.txt") == "^>v<"


def test_example_03():
    assert main.read_directions("./data/example_03.txt") == "^v^v^v^v^v"
