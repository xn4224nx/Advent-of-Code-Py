"""
Tests for the main script
"""

from main import Jumps


def test_initial_state_exp1():
    test = Jumps("./data/example_01.txt")

    assert test.state == [0, 3, 0, 1, -3]
    assert test.curr_instr == 0


def test_execute_curr_jump_exp1():
    test = Jumps("./data/example_01.txt")
    test.execute_curr_jump()

    assert test.state == [1, 3, 0, 1, -3]
    assert test.curr_instr == 0


def test_execute_curr_jump_exp2():
    test = Jumps("./data/example_01.txt")
    test.state = [1, 3, 0, 1, -3]
    test.curr_instr = 0

    test.execute_curr_jump()

    assert test.state == [2, 3, 0, 1, -3]
    assert test.curr_instr == 1


def test_execute_curr_jump_exp3():
    test = Jumps("./data/example_01.txt")
    test.state = [2, 3, 0, 1, -3]
    test.curr_instr = 1

    test.execute_curr_jump()

    assert test.state == [2, 4, 0, 1, -3]
    assert test.curr_instr == 4


def test_execute_curr_jump_exp4():
    test = Jumps("./data/example_01.txt")
    test.state = [2, 3, 0, 1, -3]
    test.curr_instr = 4

    test.execute_curr_jump()

    assert test.state == [2, 4, 0, 1, -2]
    assert test.curr_instr == 1


def test_execute_curr_jump_exp5():
    test = Jumps("./data/example_01.txt")
    test.state = [2, 4, 0, 1, -2]
    test.curr_instr = 1

    test.execute_curr_jump()

    assert test.state == [2, 5, 0, 1, -2]
    assert test.curr_instr == 5


def test_steps_to_exit_exp1():
    assert Jumps("./data/example_01.txt").steps_to_exit() == 5
