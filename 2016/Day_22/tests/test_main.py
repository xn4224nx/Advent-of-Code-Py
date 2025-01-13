"""
Tests for the main script
"""

from main import NodeGrid


def test_data_parse():
    test = NodeGrid("./data/example_01.txt")

    assert test.nodes == [".", ".", "#", ".", "_", ".", "G", ".", "."]
    assert test.node_loc == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]


def test_find_viable_pairs():
    test = NodeGrid("./data/example_01.txt")
    assert len(test.viable_pairs(test.nodes)) == 7


def test_find_ajacent_pairs():
    test = NodeGrid("./data/example_01.txt")
    assert test.viable_pairs((".", ".", ".", ".", "_", ".", ".", ".", "."), True) == [
        (1, 4),
        (3, 4),
        (5, 4),
        (7, 4),
    ]

    assert test.viable_pairs(
        (
            "_",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
            ".",
        ),
        True,
    ) == [
        (1, 0),
        (3, 0),
    ]

    assert test.viable_pairs((".", ".", ".", ".", ".", "_", ".", ".", "."), True) == [
        (2, 5),
        (4, 5),
        (8, 5),
    ]


def test_moves_empty_to_data():
    assert NodeGrid("./data/example_01.txt").moves_empty_to_data() == 1
    assert NodeGrid("./data/example_02.txt").moves_empty_to_data() == 69


def test_minimum_data_moves():
    assert NodeGrid("./data/example_01.txt").data_extact_min_moves() == 7
    assert NodeGrid("./data/example_02.txt").data_extact_min_moves() == 225
