"""
Tests for the main script
"""

from main import ProgramNetwork


def test_read_path_exp01():
    assert ProgramNetwork("./data/example_01.txt").conns == {
        0: {2},
        1: set(),
        2: {0, 3, 4},
        3: {2, 4},
        4: {2, 3, 6},
        5: {6},
        6: {4, 5},
    }


def test_group_size_exp1():
    assert len(ProgramNetwork("./data/example_01.txt").group_contents(0)) == 6


def test_group_size_exp2():
    assert len(ProgramNetwork("./data/example_01.txt").group_contents(2)) == 6


def test_group_size_exp3():
    assert len(ProgramNetwork("./data/example_01.txt").group_contents(3)) == 6


def test_group_size_exp4():
    assert len(ProgramNetwork("./data/example_01.txt").group_contents(4)) == 6


def test_group_size_exp5():
    assert len(ProgramNetwork("./data/example_01.txt").group_contents(5)) == 6


def test_group_size_exp6():
    assert len(ProgramNetwork("./data/example_01.txt").group_contents(6)) == 6


def test_group_size_exp7():
    assert len(ProgramNetwork("./data/example_01.txt").group_contents(1)) == 1


def test_group_count_exp1():
    assert ProgramNetwork("./data/example_01.txt").group_count() == 2
