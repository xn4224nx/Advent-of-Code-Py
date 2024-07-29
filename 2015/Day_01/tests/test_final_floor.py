"""
Tests for the final floor function.
"""

from main import final_floor


def test_example_01():
    assert final_floor("./data/example_01.txt") == 0


def test_example_02():
    assert final_floor("./data/example_02.txt") == 0


def test_example_03():
    assert final_floor("./data/example_03.txt") == 3


def test_example_04():
    assert final_floor("./data/example_04.txt") == 3


def test_example_05():
    assert final_floor("./data/example_05.txt") == 3


def test_example_06():
    assert final_floor("./data/example_06.txt") == -1


def test_example_07():
    assert final_floor("./data/example_07.txt") == -1


def test_example_08():
    assert final_floor("./data/example_08.txt") == -3


def test_example_09():
    assert final_floor("./data/example_09.txt") == -3


def test_example_10():
    assert final_floor("./data/example_10.txt", True) == 1


def test_example_11():
    assert final_floor("./data/example_11.txt", True) == 5
