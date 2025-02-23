"""
Tests for the main script
"""

from main import MemoryBank


def test_read_data():
    assert MemoryBank("./data/example_01.txt").state == [0, 2, 7, 0]


def test_max_bank_exp01():
    test = MemoryBank("./data/example_01.txt")
    test.state = [0, 2, 7, 0]
    assert test.max_bank() == 2


def test_max_bank_exp02():
    test = MemoryBank("./data/example_01.txt")
    test.state = [2, 4, 1, 2]
    assert test.max_bank() == 1


def test_max_bank_exp03():
    test = MemoryBank("./data/example_01.txt")
    test.state = [3, 1, 2, 3]
    assert test.max_bank() == 0


def test_max_bank_exp04():
    test = MemoryBank("./data/example_01.txt")
    test.state = [0, 2, 3, 4]
    assert test.max_bank() == 3


def test_max_bank_exp06():
    test = MemoryBank("./data/example_01.txt")
    test.state = [0, 2, 3, 4]
    assert test.max_bank() == 3


def test_max_bank_exp05():
    test = MemoryBank("./data/example_01.txt")
    test.state = [1, 3, 4, 1]
    assert test.max_bank() == 2


def test_max_bank_exp06():
    test = MemoryBank("./data/example_01.txt")
    test.state = [0, 2, 4, 4]
    assert test.max_bank() == 2


def test_redistribute_exp01():
    test = MemoryBank("./data/example_01.txt")
    test.state = [0, 2, 7, 0]
    test.redistribute()
    assert test.state == [2, 4, 1, 2]


def test_redistribute_exp02():
    test = MemoryBank("./data/example_01.txt")
    test.state = [2, 4, 1, 2]
    test.redistribute()
    assert test.state == [3, 1, 2, 3]


def test_redistribute_exp03():
    test = MemoryBank("./data/example_01.txt")
    test.state = [3, 1, 2, 3]
    test.redistribute()
    assert test.state == [0, 2, 3, 4]


def test_redistribute_exp04():
    test = MemoryBank("./data/example_01.txt")
    test.state = [0, 2, 3, 4]
    test.redistribute()
    assert test.state == [1, 3, 4, 1]


def test_redistribute_exp05():
    test = MemoryBank("./data/example_01.txt")
    test.state = [1, 3, 4, 1]
    test.redistribute()
    assert test.state == [2, 4, 1, 2]


def test_steps_until_loop():
    assert MemoryBank("./data/example_01.txt").steps_until_loop() == (5, 4)
