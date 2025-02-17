"""
Tests for the main script
"""

from main import SpiralMemory


def test_coord_of_step_exp01():
    assert SpiralMemory().coord_of_step(1) == (0, 0)


def test_coord_of_step_exp02():
    assert SpiralMemory().coord_of_step(2) == (1, 0)


def test_coord_of_step_exp03():
    assert SpiralMemory().coord_of_step(3) == (1, 1)


def test_coord_of_step_exp04():
    assert SpiralMemory().coord_of_step(4) == (0, 1)


def test_coord_of_step_exp05():
    assert SpiralMemory().coord_of_step(5) == (-1, 1)


def test_coord_of_step_exp06():
    assert SpiralMemory().coord_of_step(7) == (-1, -1)


def test_coord_of_step_exp07():
    assert SpiralMemory().coord_of_step(8) == (0, -1)


def test_coord_of_step_exp08():
    assert SpiralMemory().coord_of_step(9) == (1, -1)


def test_coord_of_step_exp09():
    assert SpiralMemory().coord_of_step(13) == (2, 2)


def test_coord_of_step_exp10():
    assert SpiralMemory().coord_of_step(10) == (2, -1)


def test_coord_of_step_exp11():
    assert SpiralMemory().coord_of_step(25) == (2, -2)


def test_coord_of_step_exp12():
    assert SpiralMemory().coord_of_step(14) == (1, 2)


def test_coord_of_step_exp13():
    assert SpiralMemory().coord_of_step(15) == (0, 2)


def test_coord_of_step_exp14():
    assert SpiralMemory().coord_of_step(20) == (-2, -1)


def test_coord_of_step_exp15():
    assert SpiralMemory().coord_of_step(22) == (-1, -2)


def test_coord_of_step_exp16():
    assert SpiralMemory().coord_of_step(24) == (1, -2)


def test_exit_moves_exp1():
    assert SpiralMemory().moves_to_exit(2) == 1


def test_exit_moves_exp2():
    assert SpiralMemory().moves_to_exit(12) == 3


def test_exit_moves_exp3():
    assert SpiralMemory().moves_to_exit(23) == 2


def test_exit_moves_exp4():
    assert SpiralMemory().moves_to_exit(1024) == 31


def test_exit_moves_exp5():
    assert SpiralMemory().moves_to_exit(1) == 0


def test_find_first_gt_max_val_exp1():
    assert SpiralMemory(800).find_first_gt_max_val() == 806


def test_find_first_gt_max_val_exp2():
    assert SpiralMemory(700).find_first_gt_max_val() == 747


def test_find_first_gt_max_val_exp3():
    assert SpiralMemory(300).find_first_gt_max_val() == 304


def test_find_first_gt_max_val_exp4():
    assert SpiralMemory(20).find_first_gt_max_val() == 23


def test_find_first_gt_max_val_exp5():
    assert SpiralMemory(55).find_first_gt_max_val() == 57


def test_find_first_gt_max_val_exp6():
    assert SpiralMemory(133).find_first_gt_max_val() == 142


def test_find_first_gt_max_val_exp6():
    assert SpiralMemory(5).find_first_gt_max_val() == 10
