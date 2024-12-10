"""
Tests for the main script
"""

from main import read_sculp_data, simulate_pass_through, find_first_drop_time


def test_read_sculp_data():
    assert read_sculp_data("./data/example_01.txt") == [
        {"num_pos": 5, "curr_pos": 4},
        {"num_pos": 2, "curr_pos": 1},
    ]

    assert read_sculp_data("./data/example_01.txt") == [
        {"num_pos": 5, "curr_pos": 2},
        {"num_pos": 13, "curr_pos": 7},
        {"num_pos": 17, "curr_pos": 10},
        {"num_pos": 3, "curr_pos": 2},
        {"num_pos": 19, "curr_pos": 9},
        {"num_pos": 7, "curr_pos": 0},
    ]


def test_simulate_pass_through():
    assert (
        simulate_pass_through(
            [
                {"num_pos": 5, "curr_pos": 4},
                {"num_pos": 2, "curr_pos": 1},
            ],
            0,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                {"num_pos": 5, "curr_pos": 4},
                {"num_pos": 2, "curr_pos": 1},
            ],
            1,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                {"num_pos": 5, "curr_pos": 4},
                {"num_pos": 2, "curr_pos": 1},
            ],
            2,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                {"num_pos": 5, "curr_pos": 4},
                {"num_pos": 2, "curr_pos": 1},
            ],
            3,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                {"num_pos": 5, "curr_pos": 4},
                {"num_pos": 2, "curr_pos": 1},
            ],
            4,
        )
        == False
    )

    assert (
        simulate_pass_through(
            [
                {"num_pos": 5, "curr_pos": 4},
                {"num_pos": 2, "curr_pos": 1},
            ],
            5,
        )
        == True
    )


def test_find_first_drop_time():
    assert (
        find_first_drop_time(
            [
                {"num_pos": 5, "curr_pos": 4},
                {"num_pos": 2, "curr_pos": 1},
            ]
        )
        == 5
    )
