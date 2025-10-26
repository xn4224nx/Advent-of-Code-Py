"""
Tests for the main script.
"""

from main import Amplifier


def test_run_phase_setting_exp_0():
    assert Amplifier("./data/example_0.txt").run_phase_setting([4, 3, 2, 1, 0]) == 43210


def test_run_phase_setting_exp_1():
    assert Amplifier("./data/example_1.txt").run_phase_setting([0, 1, 2, 3, 4]) == 54321


def test_run_phase_setting_exp_2():
    assert Amplifier("./data/example_2.txt").run_phase_setting([1, 0, 4, 3, 2]) == 65210


def test_max_amp_comb_exp_0():
    assert Amplifier("./data/example_0.txt").max_amp_comb() == [4, 3, 2, 1, 0]


def test_max_amp_comb_exp_1():
    assert Amplifier("./data/example_1.txt").max_amp_comb() == [0, 1, 2, 3, 4]


def test_max_amp_comb_exp_2():
    assert Amplifier("./data/example_2.txt").max_amp_comb() == [1, 0, 4, 3, 2]


def test_max_thruster_signal_exp_0():
    assert Amplifier("./data/example_0.txt").max_thruster_signal() == 43210


def test_max_thruster_signal_exp_1():
    assert Amplifier("./data/example_1.txt").max_thruster_signal() == 54321


def test_max_thruster_signal_exp_2():
    assert Amplifier("./data/example_2.txt").max_thruster_signal() == 65210
