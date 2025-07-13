"""
Tests for the main script
"""

from main import SleighSteps


def test_new_sleighsteps_exp01():
    test = SleighSteps("./data/example_0.txt")
    assert test.depends == {
        0: {2},
        1: {0},
        2: set(),
        3: {0},
        4: {1, 3, 5},
        5: {2},
    }


def test_correct_order_exp01():
    assert SleighSteps("./data/example_0.txt").correct_order() == "CABDFE"


def test_threaded_correct_order_exp01():
    assert SleighSteps("./data/example_0.txt").threaded_order_time(2, 0) == 15
