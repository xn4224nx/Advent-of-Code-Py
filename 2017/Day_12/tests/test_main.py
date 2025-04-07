"""
Tests for the main script
"""

from main import ProgramNetwork


def test_read_path_exp01():
    assert ProgramNetwork("./data/example_01.txt").conns == {
        0: {2},
        1: set(),
        2: {0, 2, 3, 4},
        3: {2, 4},
        4: {2, 3, 6},
        5: {6},
        6: {4, 5},
    }


def test_group_size_exp1():
    assert ProgramNetwork("./data/example_01.txt").group_size(0) == 6


def test_group_size_exp2():
    assert ProgramNetwork("./data/example_01.txt").group_size(2) == 6


def test_group_size_exp3():
    assert ProgramNetwork("./data/example_01.txt").group_size(3) == 6


def test_group_size_exp4():
    assert ProgramNetwork("./data/example_01.txt").group_size(4) == 6


def test_group_size_exp5():
    assert ProgramNetwork("./data/example_01.txt").group_size(5) == 6


def test_group_size_exp6():
    assert ProgramNetwork("./data/example_01.txt").group_size(6) == 6


def test_group_size_exp7():
    assert ProgramNetwork("./data/example_01.txt").group_size(1) == 1
