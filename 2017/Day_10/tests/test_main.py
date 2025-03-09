"""
Tests for the main script
"""

from main import KnotHash
from collections import deque


def test_data_ingestion_exp1():
    test = KnotHash(4, "./data/example_01.txt")
    assert test.rope == [0, 1, 2, 3, 4]
    assert test.lengths == [3, 4, 1, 5]
    assert test.pos == 0
    assert test.skip_size == 0


def test_data_ingestion_exp3():
    test = KnotHash(4, "./data/example_03.txt", True)
    assert test.lengths == [17, 31, 73, 47, 23]


def test_data_ingestion_exp4():
    test = KnotHash(4, "./data/example_04.txt", True)
    assert test.lengths == [65, 111, 67, 32, 50, 48, 49, 55, 17, 31, 73, 47, 23]


def test_data_ingestion_exp5():
    test = KnotHash(4, "./data/example_05.txt", True)
    assert test.lengths == [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]


def test_reverse_exp1():
    test = KnotHash(4, "./data/example_01.txt")
    test.reverse(3)

    assert test.rope == [2, 1, 0, 3, 4]
    assert test.pos == 3
    assert test.skip_size == 1


def test_reverse_exp2():
    test = KnotHash(4, "./data/example_01.txt")
    test.rope = [2, 1, 0, 3, 4]
    test.pos = 3
    test.skip_size = 1

    test.reverse(4)

    assert test.rope == [4, 3, 0, 1, 2]
    assert test.pos == 3
    assert test.skip_size == 2


def test_reverse_exp3():
    test = KnotHash(4, "./data/example_01.txt")
    test.rope = [4, 3, 0, 1, 2]
    test.pos = 3
    test.skip_size = 2

    test.reverse(1)

    assert test.rope == [4, 3, 0, 1, 2]
    assert test.pos == 1
    assert test.skip_size == 3


def test_reverse_exp4():
    test = KnotHash(4, "./data/example_01.txt")
    test.rope = [4, 3, 0, 1, 2]
    test.pos = 1
    test.skip_size = 3

    test.reverse(5)

    assert test.rope == [3, 4, 2, 1, 0]
    assert test.pos == 4
    assert test.skip_size == 4


def test_final_result_exp1():
    assert KnotHash(4, "./data/example_01.txt").final_result() == 12


def test_final_result_exp2():
    assert KnotHash(255, "./data/example_02.txt").final_result() == 4480


def test_calc_digest_exp3():
    assert (
        KnotHash(255, "./data/example_03.txt", True).calc_digest()
        == "a2582a3a0e66e6e86e3812dcb672a272"
    )


def test_calc_digest_exp4():
    assert (
        KnotHash(255, "./data/example_04.txt", True).calc_digest()
        == "33efeb34ea91902bb2f59c9920caa6cd"
    )


def test_calc_digest_exp5():
    assert (
        KnotHash(255, "./data/example_05.txt", True).calc_digest()
        == "3efbe78a8d82f29979031a4aa0b16a9d"
    )


def test_calc_digest_exp6():
    assert (
        KnotHash(255, "./data/example_06.txt", True).calc_digest()
        == "63960835bcdc130f0b66d7ff4f6a5a8e"
    )
