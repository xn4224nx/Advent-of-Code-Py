"""
Tests for the main script
"""

from main import Tree


def test_new_tree_exp01():
    test = Tree("./data/example_0.txt")
    assert test.raw_info == [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]


def test_node_metadata_sum_exp01():
    assert Tree("./data/example_0.txt").statistics()[0] == 138


def test_root_node_value_exp01():
    assert Tree("./data/example_0.txt").statistics()[1] == 66
