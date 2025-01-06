"""
Tests for the main script
"""

from main import Scambler
from collections import deque


def test_class_initialisation():
    test = Scambler("./data/example_01.txt", "abcde")
    assert test.seed == deque(["a", "b", "c", "d", "e"])
    assert test.instructs == [
        "swap position 4 with position 0",
        "swap letter d with letter b",
        "reverse positions 0 through 4",
        "rotate left 1 step",
        "move position 1 to position 4",
        "move position 3 to position 0",
        "rotate based on position of letter b",
        "rotate based on position of letter d",
    ]


def test_swap_by_letters():
    test = Scambler("./data/example_01.txt", "ebcda")
    test.swap_by_letters("d", "b")
    assert test.seed == deque(["e", "d", "c", "b", "a"])


def test_swap_by_index():
    test = Scambler("./data/example_01.txt", "abcde")
    test.swap_by_index(4, 0)
    assert test.seed == deque(["e", "b", "c", "d", "a"])


def test_rotate_left():
    test = Scambler("./data/example_01.txt", "abcde")
    test.rotate_left(1)
    assert test.seed == deque(["b", "c", "d", "e", "a"])


def test_rotate_right():
    test = Scambler("./data/example_01.txt", "abcde")
    test.rotate_right(1)
    assert test.seed == deque(["e", "a", "b", "c", "d"])


def test_rotate_by_letter_pos():
    test = Scambler("./data/example_01.txt", "abdec")
    test.rotate_by_letter_pos("b")
    assert test.seed == deque(["e", "c", "a", "b", "d"])
    test.rotate_by_letter_pos("d")
    assert test.seed == deque(["d", "e", "c", "a", "b"])


def test_reverse_positions():
    test = Scambler("./data/example_01.txt", "edcba")
    test.reverse_positions(0, 4)
    assert test.seed == deque(["a", "b", "c", "d", "e"])


def test_move_positions():
    test = Scambler("./data/example_01.txt", "bcdea")
    test.move_positions(1, 4)
    assert test.seed == deque(["b", "d", "e", "a", "c"])
    test.move_positions(3, 0)
    assert test.seed == deque(["a", "b", "d", "e", "c"])


def test_execute_insruct():
    test = Scambler("./data/example_01.txt", "abcde")

    test.execute_insruct("swap position 4 with position 0")
    assert test.seed == deque(["e", "b", "c", "d", "a"])

    test.execute_insruct("swap letter d with letter b")
    assert test.seed == deque(["e", "d", "c", "b", "a"])

    test.execute_insruct("reverse positions 0 through 4")
    assert test.seed == deque(["a", "b", "c", "d", "e"])

    test.execute_insruct("rotate left 1 step")
    assert test.seed == deque(["b", "c", "d", "e", "a"])

    test.execute_insruct("move position 1 to position 4")
    assert test.seed == deque(["b", "d", "e", "a", "c"])

    test.execute_insruct("move position 3 to position 0")
    assert test.seed == deque(["a", "b", "d", "e", "c"])

    test.execute_insruct("rotate based on position of letter b")
    assert test.seed == deque(["e", "c", "a", "b", "d"])

    test.execute_insruct("rotate based on position of letter d")
    assert test.seed == deque(["d", "e", "c", "a", "b"])


def test_execute_all_commands():
    assert Scambler("./data/example_01.txt", "abcde").execute_all_commands() == "decab"
