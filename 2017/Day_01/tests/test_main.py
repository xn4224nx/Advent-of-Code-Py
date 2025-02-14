"""
Tests for the main script
"""

from main import InverseCaptcha
from collections import deque


def test_read_example_01():
    assert InverseCaptcha("./data/example_01.txt").ring == [1, 1, 2, 2]


def test_read_example_02():
    assert InverseCaptcha("./data/example_02.txt").ring == [1, 1, 1, 1]


def test_read_example_03():
    assert InverseCaptcha("./data/example_03.txt").ring == [1, 2, 3, 4]


def test_read_example_04():
    assert InverseCaptcha("./data/example_04.txt").ring == [9, 1, 2, 1, 2, 1, 2, 9]


def test_comp_sum_example_01():
    assert InverseCaptcha("./data/example_01.txt").comparison_sum() == 3


def test_comp_sum_example_02():
    assert InverseCaptcha("./data/example_02.txt").comparison_sum() == 4


def test_comp_sum_example_03():
    assert InverseCaptcha("./data/example_03.txt").comparison_sum() == 0


def test_comp_sum_example_04():
    assert InverseCaptcha("./data/example_04.txt").comparison_sum() == 9


def test_comp_sum_example_05():
    assert InverseCaptcha("./data/example_05.txt").comparison_sum(False) == 6


def test_comp_sum_example_06():
    assert InverseCaptcha("./data/example_06.txt").comparison_sum(False) == 0


def test_comp_sum_example_07():
    assert InverseCaptcha("./data/example_07.txt").comparison_sum(False) == 4


def test_comp_sum_example_08():
    assert InverseCaptcha("./data/example_08.txt").comparison_sum(False) == 12


def test_comp_sum_example_09():
    assert InverseCaptcha("./data/example_09.txt").comparison_sum(False) == 4
