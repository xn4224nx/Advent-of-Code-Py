"""
Tests for the main script
"""

from main import HVAC


def test_class_initialisation():
    test = HVAC("./data/example_01.txt")
    assert test.nodes == {
        0: (1, 1),
        1: (3, 1),
        2: (9, 1),
        3: (9, 3),
        4: (1, 3),
    }
    assert test.free == {(x, 1) for x in range(1, 10)} | {
        (x, 3) for x in range(1, 10)
    } | {(1, 2), (9, 2)}


def test_next_steps():
    test = HVAC("./data/example_01.txt")
    assert test.next_steps((1, 1)) == {(2, 1), (1, 2)}
    assert test.next_steps((1, 2)) == {(1, 1), (1, 3)}
    assert test.next_steps((5, 3)) == {(4, 3), (6, 3)}


def test_fewest_steps_from_nodes():
    test = HVAC("./data/example_01.txt")
    assert test.fewest_steps_from_nodes(0, 4) == 2
    assert test.fewest_steps_from_nodes(4, 0) == 2
    assert test.fewest_steps_from_nodes(4, 1) == 4
    assert test.fewest_steps_from_nodes(1, 2) == 6
    assert test.fewest_steps_from_nodes(2, 1) == 6
    assert test.fewest_steps_from_nodes(2, 3) == 2
    assert test.fewest_steps_from_nodes(4, 3) == 8
    assert test.fewest_steps_from_nodes(2, 0) == 8
    assert test.fewest_steps_from_nodes(3, 0) == 10


def test_fewest_steps():
    assert HVAC("./data/example_01.txt").fewest_steps() == 14
