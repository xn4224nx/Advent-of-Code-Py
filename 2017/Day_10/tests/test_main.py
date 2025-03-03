"""
Tests for the main script
"""

from main import KnotHash


def test_data_ingestion():
    test = KnotHash(4, "./data/example_01.txt")
    assert test.rope == [0, 1, 2, 3, 4]
    assert test.skips == [3, 4, 1, 5]
    assert test.pos == 0
    assert test.skip_size == 0


def test_reverse_exp1():
    test = KnotHash(4, "./data/example_01.txt")
    test.reverse(0, 3)

    assert test.rope == [2, 1, 0, 3, 4]
    assert test.pos == 3
    assert test.skip_size == 1


def test_reverse_exp2():
    test = KnotHash(4, "./data/example_01.txt")
    test.rope = [2, 1, 0, 3, 4]
    test.pos = 3
    test.skip_size = 1

    test.reverse(3, 4)

    assert test.rope == [4, 3, 0, 1, 2]
    assert test.pos == 3
    assert test.skip_size == 2


def test_reverse_exp3():
    test = KnotHash(4, "./data/example_01.txt")
    test.rope = [4, 3, 0, 1, 2]
    test.pos = 3
    test.skip_size = 2

    test.reverse(3, 1)

    assert test.rope == [4, 3, 0, 1, 2]
    assert test.pos == 1
    assert test.skip_size == 3


def test_reverse_exp4():
    test = KnotHash(4, "./data/example_01.txt")
    test.rope = [4, 3, 0, 1, 2]
    test.pos = 1
    test.skip_size = 3

    test.reverse(1, 5)

    assert test.rope == [3, 4, 2, 1, 0]
    assert test.pos == 4
    assert test.skip_size == 4


def test_final_result():
    assert KnotHash(4, "./data/example_01.txt").final_result() == 12
