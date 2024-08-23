"""
Tests for functions in the main script.
"""

import main


def test_exp_parse_1():
    rels, guests = main.parse_relationships("./data/example_01.txt")
    assert set(guests) == set(["David", "Alice", "Bob", "Carol"])


def test_exp_parse_2():
    rels, guests = main.parse_relationships("./data/example_01.txt")
    assert rels == {
        ("Alice", "Bob"): 54,
        ("Alice", "Carol"): -79,
        ("Alice", "David"): -2,
        ("Bob", "Alice"): 83,
        ("Bob", "Carol"): -7,
        ("Bob", "David"): -63,
        ("Carol", "Alice"): -62,
        ("Carol", "Bob"): 60,
        ("Carol", "David"): 55,
        ("David", "Alice"): 46,
        ("David", "Bob"): -7,
        ("David", "Carol"): 41,
    }


def test_max_happy():
    rels, guests = main.parse_relationships("./data/example_01.txt")
    assert main.find_max_happy(rels, guests) == 330
