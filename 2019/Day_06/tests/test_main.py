"""
Tests for the main script.
"""

from main import Orrery


def test_new_orrery_exp_0():
    test = Orrery("./data/example_0.txt")
    assert test.sub_orbits == {
        "COM": {"B"},
        "B": {"G", "C"},
        "C": {"D"},
        "D": {"I", "E"},
        "E": {"J", "F"},
        "F": {},
        "G": {"H"},
        "H": {},
        "I": {},
        "J": {"K"},
        "K": {"L"},
        "L": {},
    }
    assert test.links == {
        "COM": "B",
        "B": "C",
        "C": "D",
        "D": "E",
        "E": "F",
        "B": "G",
        "G": "H",
        "D": "I",
        "E": "J",
        "J": "K",
        "K": "L",
    }


def test_num_orbits_exp_0():
    assert Orrery("./data/example_0.txt").num_orbits() == 42
