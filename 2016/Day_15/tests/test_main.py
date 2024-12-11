"""
Tests for the main script
"""

from main import read_sculp_data, simulate_pass_through, find_first_drop_time


def test_read_sculp_data():
    assert read_sculp_data("./data/example_01.txt") == [
        (5, 4),
        (2, 1),
    ]

    assert read_sculp_data("./data/input.txt") == [
        (5, 2),
        (13, 7),
        (17, 10),
        (3, 2),
        (19, 9),
        (7, 0),
    ]


def test_simulate_pass_through():
    assert (
        simulate_pass_through(
            [
                (5, 4),
                (2, 1),
            ],
            0,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                (5, 4),
                (2, 1),
            ],
            1,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                (5, 4),
                (2, 1),
            ],
            2,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                (5, 4),
                (2, 1),
            ],
            3,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                (5, 4),
                (2, 1),
            ],
            4,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                (5, 4),
                (2, 1),
            ],
            5,
        )
        == True
    )


def test_find_first_drop_time():
    assert (
        find_first_drop_time(
            [
                (5, 4),
                (2, 1),
            ]
        )
        == 5
    )
