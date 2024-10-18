"""
Tests for the main script
"""

import numpy as np
from main import read_signal_data, find_vert_msg


def test_read_signal_data():
    assert (
        read_signal_data("./data/example_01.txt").all()
        == np.array(
            [
                ["e", "e", "d", "a", "d", "n"],
                ["d", "r", "v", "t", "e", "e"],
                ["e", "a", "n", "d", "s", "r"],
                ["r", "a", "a", "v", "r", "d"],
                ["a", "t", "e", "v", "r", "s"],
                ["t", "s", "r", "n", "e", "v"],
                ["s", "d", "t", "t", "s", "a"],
                ["r", "a", "s", "r", "t", "v"],
                ["n", "s", "s", "d", "t", "s"],
                ["n", "t", "n", "a", "d", "a"],
                ["s", "v", "e", "t", "v", "e"],
                ["t", "e", "s", "n", "v", "t"],
                ["v", "n", "t", "s", "n", "d"],
                ["v", "r", "d", "e", "a", "r"],
                ["d", "v", "r", "s", "e", "n"],
                ["e", "n", "a", "r", "a", "r"],
            ],
            dtype="<U1",
        ).all()
    )


def test_find_vert_msg_exp1():
    assert find_vert_msg(read_signal_data("./data/example_01.txt")) == "easter"


def test_find_vert_msg_exp2():
    assert find_vert_msg(read_signal_data("./data/example_01.txt"), True) == "advent"
