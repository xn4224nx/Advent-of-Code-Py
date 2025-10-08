"""
Tests for the main script.
"""

from main import AdvIntProgram
from random import randrange, randint


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


def test_diagnostics_exp00():
    val = randrange(10000)
    assert AdvIntProgram("./data/example_0.txt").diagnostics(val) == val


def test_diagnostics_exp01_position_equal_to():
    assert AdvIntProgram("./data/example_3.txt").diagnostics(8) == 1


def test_diagnostics_exp02_position_equal_to():
    assert AdvIntProgram("./data/example_3.txt").diagnostics(randint(-1000, 7)) == 0


def test_diagnostics_exp03_position_equal_to():
    assert AdvIntProgram("./data/example_3.txt").diagnostics(randint(9, 1000)) == 0


def test_diagnostics_exp04_position_less_than():
    assert AdvIntProgram("./data/example_4.txt").diagnostics(randint(8, 1000)) == 0


def test_diagnostics_exp05_position_less_than():
    assert AdvIntProgram("./data/example_4.txt").diagnostics(8) == 0


def test_diagnostics_exp06_position_less_than():
    assert AdvIntProgram("./data/example_4.txt").diagnostics(randint(-1000, 7)) == 1


def test_diagnostics_exp07_immediate_equal_to():
    assert AdvIntProgram("./data/example_5.txt").diagnostics(8) == 1


def test_diagnostics_exp08_immediate_equal_to():
    assert AdvIntProgram("./data/example_5.txt").diagnostics(randint(9, 1000)) == 0


def test_diagnostics_exp09_immediate_equal_to():
    assert AdvIntProgram("./data/example_5.txt").diagnostics(randint(-1000, 7)) == 0


def test_diagnostics_exp10_immediate_less_than():
    assert AdvIntProgram("./data/example_6.txt").diagnostics(randint(-1000, 7)) == 1


def test_diagnostics_exp11_immediate_less_than():
    assert AdvIntProgram("./data/example_6.txt").diagnostics(8) == 0


def test_diagnostics_exp12_immediate_less_than():
    assert AdvIntProgram("./data/example_6.txt").diagnostics(randint(8, 1000)) == 0


def test_diagnostics_exp13_jump_position():
    assert AdvIntProgram("./data/example_7.txt").diagnostics(0) == 0


def test_diagnostics_exp14_jump_position():
    assert AdvIntProgram("./data/example_7.txt").diagnostics(randint(-1000, -1)) == 1


def test_diagnostics_exp15_jump_position():
    assert AdvIntProgram("./data/example_7.txt").diagnostics(randint(1, 1000)) == 1


def test_diagnostics_exp16_jump_immediate():
    assert AdvIntProgram("./data/example_8.txt").diagnostics(0) == 0


def test_diagnostics_exp17_jump_immediate():
    assert AdvIntProgram("./data/example_8.txt").diagnostics(randint(-1000, -1)) == 1


def test_diagnostics_exp18_jump_immediate():
    assert AdvIntProgram("./data/example_8.txt").diagnostics(randint(1, 1000)) == 1


def test_diagnostics_exp19():
    assert AdvIntProgram("./data/example_9.txt").diagnostics(8) == 1000


def test_diagnostics_exp20():
    assert AdvIntProgram("./data/example_9.txt").diagnostics(randint(-1000, 7)) == 999


def test_diagnostics_exp21():
    assert AdvIntProgram("./data/example_9.txt").diagnostics(randint(9, 1000)) == 1001
