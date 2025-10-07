"""
Tests for the main script.
"""

from main import AdvIntProgram


def test_new_inst_exp_0():
    test = AdvIntProgram("./data/example_0.txt")
    assert test.mem == [3, 0, 4, 0, 99]
    assert test.ptr == 0


def test_new_inst_exp_1():
    test = AdvIntProgram("./data/example_1.txt")
    assert test.mem == [1002, 4, 3, 4, 33]
    assert test.ptr == 0


def test_new_inst_exp_2():
    test = AdvIntProgram("./data/example_2.txt")
    assert test.mem == [1101, 100, -1, 4, 0]
    assert test.ptr == 0


def test_multiply_step():
    test = AdvIntProgram("./data/example_1.txt")
    test.step()
    assert test.mem == [1002, 4, 3, 4, 99]


def test_add_step():
    test = AdvIntProgram("./data/example_2.txt")
    test.step()
    assert test.mem == [1101, 100, -1, 4, 99]
