"""
Tests for functions in the main script.
"""

import main

file_p = "./data/example_01.txt"


def test_read_example():
    ts = main.DeliveryNetwork(file_p)
    assert ts.data == {
        "Belfast": {"Dublin": 141, "London": 518},
        "Dublin": {"Belfast": 141, "London": 464},
        "London": {"Belfast": 518, "Dublin": 464},
    }


def test_min_path_len():
    ts = main.DeliveryNetwork(file_p)
    assert ts.bf_min_max_path()[0] == 605


def test_max_path_len():
    ts = main.DeliveryNetwork(file_p)
    assert ts.bf_min_max_path()[1] == 982
