"""
Tests for the main script.
"""

from main import BridgeFinder


def test_new_finder():
    test = BridgeFinder("./data/example_01.txt")
    assert test.comps == [
        (0, 2),
        (2, 2),
        (2, 3),
        (3, 4),
        (3, 5),
        (0, 1),
        (10, 1),
        (9, 10),
        7,
    ]


def test_bridge_strength_exp01():
    assert (
        BridgeFinder("./data/example_01.txt").is_component_comb_valid((5, 6, 7)) == 31
    )


def test_bridge_strength_exp02():
    assert BridgeFinder("./data/example_01.txt").is_component_comb_valid((0)) == 2


def test_bridge_strength_exp02():
    assert (
        BridgeFinder("./data/example_01.txt").is_component_comb_valid((0, 1, 2, 4))
        == 19
    )


def test_is_component_comb_valid_exp01():
    assert BridgeFinder("./data/example_01.txt").is_component_comb_valid((0)) == True


def test_is_component_comb_valid_exp02():
    assert BridgeFinder("./data/example_01.txt").is_component_comb_valid((5)) == True


def test_is_component_comb_valid_exp03():
    assert BridgeFinder("./data/example_01.txt").is_component_comb_valid((1)) == False


def test_is_component_comb_valid_exp04():
    assert (
        BridgeFinder("./data/example_01.txt").is_component_comb_valid((0, 6)) == False
    )


def test_is_component_comb_valid_exp05():
    assert (
        BridgeFinder("./data/example_01.txt").is_component_comb_valid((0, 1, 2, 4))
        == True
    )


def test_is_component_comb_valid_exp06():
    assert (
        BridgeFinder("./data/example_01.txt").is_component_comb_valid((5, 6, 7)) == True
    )


def test_find_strongest_bridge_exp01():
    assert BridgeFinder("./data/example_01.txt").find_strongest_bridge() == 31
