"""
Tests for the main script.
"""

from main import IntcodeProgram


def test_new_program_exp_0():
    test = IntcodeProgram("./data/example_0.txt")
    assert test.pntr == 0
    assert test.register == [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]


def test_step_exp_0():
    test = IntcodeProgram("./data/example_0.txt")
    test.step()
    assert test.pntr == 4
    assert test.register == [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_step_exp_1():
    test = IntcodeProgram("./data/example_0.txt")
    test.step()
    assert test.pntr == 8
    assert test.register == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_final_prog_exp_0():
    test = IntcodeProgram("./data/example_0.txt")
    assert test.final_prog_value() == 3500
    assert test.register == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]


def test_final_prog_exp_1():
    test = IntcodeProgram("./data/example_1.txt")
    assert test.final_prog_value() == 2
    assert test.register == [2, 0, 0, 0, 99]


def test_final_prog_exp_2():
    test = IntcodeProgram("./data/example_2.txt")
    assert test.final_prog_value() == 2
    assert test.register == [2, 3, 0, 6, 99]


def test_final_prog_exp_3():
    test = IntcodeProgram("./data/example_3.txt")
    assert test.final_prog_value() == 2
    assert test.register == [2, 4, 4, 5, 99, 9801]


def test_final_prog_exp_4():
    test = IntcodeProgram("./data/example_4.txt")
    assert test.final_prog_value() == 30
    assert test.register == [30, 1, 1, 4, 2, 5, 6, 0, 99]
