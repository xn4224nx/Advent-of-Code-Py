"""
Tests for the main script.
"""

from main import SpinLock
from collections import deque


def test_parse_data():
    test = SpinLock(3)
    assert test.buff == deque([0])
    assert test.step == 3
    assert test.idx == 1


def test_spin_exp01():
    test = SpinLock(3)
    test.spin()
    assert test.idx == 2
    assert test.buff == deque([0, 1])


def test_spin_exp02():
    test = SpinLock(3)
    test.idx = 2
    test.buff = deque([0, 1])
    test.spin()
    assert test.idx == 3
    assert test.buff == deque([1, 0, 2])


def test_spin_exp03():
    test = SpinLock(3)
    test.idx = 3
    test.buff = deque([1, 0, 2])
    test.spin()
    assert test.idx == 4
    assert test.buff == deque([1, 0, 2, 3])


def test_spin_exp04():
    test = SpinLock(3)
    test.idx = 4
    test.buff = deque([1, 0, 2, 3])
    test.spin()
    assert test.idx == 5
    assert test.buff == deque([3, 1, 0, 2, 4])


def test_spin_exp05():
    test = SpinLock(3)
    test.idx = 5
    test.buff = deque([3, 1, 0, 2, 4])
    test.spin()
    assert test.idx == 6
    assert test.buff == deque([2, 4, 3, 1, 0, 5])


def test_spin_exp06():
    test = SpinLock(3)
    test.idx = 6
    test.buff = deque([2, 4, 3, 1, 0, 5])
    test.spin()
    assert test.idx == 7
    assert test.buff == deque([1, 0, 5, 2, 4, 3, 6])


def test_spin_exp07():
    test = SpinLock(3)
    test.idx = 7
    test.buff = deque([1, 0, 5, 2, 4, 3, 6])
    test.spin()
    assert test.idx == 8
    assert test.buff == deque([2, 4, 3, 6, 1, 0, 5, 7])


def test_spin_exp08():
    test = SpinLock(3)
    test.idx = 8
    test.buff = deque([2, 4, 3, 6, 1, 0, 5, 7])
    test.spin()
    assert test.idx == 9
    assert test.buff == deque([6, 1, 0, 5, 7, 2, 4, 3, 8])


def test_spin_exp09():
    test = SpinLock(3)
    test.idx = 9
    test.buff = deque([6, 1, 0, 5, 7, 2, 4, 3, 8])
    test.spin()
    assert test.idx == 10
    assert test.buff == deque([5, 7, 2, 4, 3, 8, 6, 1, 0, 9])


def test_post_final_value_exp01():
    assert SpinLock(3).post_value(9, 9) == 5


def test_post_final_value_exp02():
    assert SpinLock(3).post_value(2017, 2017) == 638
