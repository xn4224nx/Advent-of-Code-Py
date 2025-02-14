"""
Tests for the main script
"""

from main import InverseCaptcha
from collections import deque


def test_read_example_01():
    assert InverseCaptcha("./data/example_01.txt").ring == deque([1, 1, 2, 2])


def test_read_example_02():
    assert InverseCaptcha("./data/example_02.txt").ring == deque([1, 1, 1, 1])


def test_read_example_03():
    assert InverseCaptcha("./data/example_03.txt").ring == deque([1, 2, 3, 4])


def test_read_example_04():
    assert InverseCaptcha("./data/example_04.txt").ring == deque(
        [9, 1, 2, 1, 2, 1, 2, 9]
    )


def test_adj_sum_example_01():
    assert InverseCaptcha("./data/example_01.txt").adjacent_sum() == 3


def test_adj_sum_example_02():
    assert InverseCaptcha("./data/example_02.txt").adjacent_sum() == 4


def test_adj_sum_example_03():
    assert InverseCaptcha("./data/example_03.txt").adjacent_sum() == 0


def test_adj_sum_example_04():
    assert InverseCaptcha("./data/example_04.txt").adjacent_sum() == 9
