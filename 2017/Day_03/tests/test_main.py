"""
Tests for the main script
"""

from main import SpiralMemory


def test_exit_moves_exp1():
    assert SpiralMemory(1).moves_to_exit() == 0


def test_exit_moves_exp2():
    assert SpiralMemory(12).moves_to_exit() == 3


def test_exit_moves_exp3():
    assert SpiralMemory(23).moves_to_exit() == 2


def test_exit_moves_exp4():
    assert SpiralMemory(1024).moves_to_exit() == 31
