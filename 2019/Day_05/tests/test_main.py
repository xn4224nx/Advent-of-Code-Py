"""
Tests for the main script.
"""

from main import AdvIntProgram
from random import randrange


def test_new_inst_exp_0():
    test = AdvIntProgram("./data/example_0.txt")
    assert test.mem == [3, 0, 4, 0, 99]
    assert test.ptr == 0
    assert test.outputs == []


def test_new_inst_exp_1():
    test = AdvIntProgram("./data/example_1.txt")
    assert test.mem == [1002, 4, 3, 4, 33]
    assert test.ptr == 0
    assert test.outputs == []


def test_new_inst_exp_2():
    test = AdvIntProgram("./data/example_2.txt")
    assert test.mem == [1101, 100, -1, 4, 0]
    assert test.ptr == 0
    assert test.outputs == []


def test_multiply_step():
    test = AdvIntProgram("./data/example_1.txt")
    test.step()
    assert test.mem == [1002, 4, 3, 4, 99]


def test_add_step():
    test = AdvIntProgram("./data/example_2.txt")
    test.step()
    assert test.mem == [1101, 100, -1, 4, 99]


def test_print_step():
    test = AdvIntProgram("./data/example_0.txt")
    test.input_code = randrange(10000)

    test.step()
    assert test.mem == [test.input_code, 0, 4, 0, 99]

    test.step()
    assert test.outputs == [test.input_code]


def test_curr_params_exp0():
    test = AdvIntProgram("./data/example_0.txt")
    test.mem = [1002]
    assert test.curr_params() == (2, 0, 1, 0)


def test_curr_params_exp1():
    test = AdvIntProgram("./data/example_0.txt")
    test.mem = [4]
    assert test.curr_params() == (4, 0, 0, 0)


def test_curr_params_exp2():
    test = AdvIntProgram("./data/example_0.txt")
    test.mem = [3]
    assert test.curr_params() == (3, 0, 0, 0)


def test_curr_params_exp3():
    test = AdvIntProgram("./data/example_0.txt")
    test.mem = [1207]
    assert test.curr_params() == (7, 2, 1, 0)


def test_curr_params_exp4():
    test = AdvIntProgram("./data/example_0.txt")
    test.mem = [91207]
    assert test.curr_params() == (7, 2, 1, 9)


def test_curr_params_exp4():
    test = AdvIntProgram("./data/example_0.txt")
    test.mem = [9127]
    assert test.curr_params() == (27, 1, 9, 0)


def test_diagnostics_exp0():
    val = randrange(10000)
    assert AdvIntProgram("./data/example_0.txt").diagnostics(val) == val
