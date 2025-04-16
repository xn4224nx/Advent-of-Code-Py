"""
Tests for the main script and the KnotHash class.
"""

from main import GeneratorDuel


def test_pair_iteration_exp01():
    test = GeneratorDuel(65, 8921)
    for _ in range(1):
        test.iterate()
    assert test.gen_a == 1092455
    assert test.gen_b == 430625591


def test_pair_iteration_exp02():
    test = GeneratorDuel(65, 8921)
    for _ in range(2):
        test.iterate()
    assert test.gen_a == 1181022009
    assert test.gen_b == 1233683848


def test_pair_iteration_exp03():
    test = GeneratorDuel(65, 8921)
    for _ in range(3):
        test.iterate()
    assert test.gen_a == 245556042
    assert test.gen_b == 1431495498


def test_pair_iteration_exp04():
    test = GeneratorDuel(65, 8921)
    for _ in range(4):
        test.iterate()
    assert test.gen_a == 1744312007
    assert test.gen_b == 137874439


def test_pair_iteration_exp05():
    test = GeneratorDuel(65, 8921)
    for _ in range(5):
        test.iterate()
    assert test.gen_a == 1352636452
    assert test.gen_b == 285222916


def test_pair_comp_exp01():
    assert GeneratorDuel(1092455, 430625591).compare_pair(1092455, 430625591) == False


def test_pair_comp_exp02():
    assert (
        GeneratorDuel(1181022009, 1233683848).compare_pair(1181022009, 1233683848)
        == False
    )


def test_pair_comp_exp03():
    assert (
        GeneratorDuel(245556042, 1431495498).compare_pair(245556042, 1431495498) == True
    )


def test_pair_comp_exp04():
    assert (
        GeneratorDuel(1744312007, 137874439).compare_pair(1744312007, 137874439)
        == False
    )


def test_pair_comp_exp05():
    assert (
        GeneratorDuel(1352636452, 285222916).compare_pair(1352636452, 285222916)
        == False
    )


def test_matching_pairs_exp01():
    assert GeneratorDuel(65, 8921).matching_pairs(5) == 1


def test_matching_pairs_exp02():
    assert GeneratorDuel(65, 8921).matching_pairs(40_000_000) == 588


def test_detatched_matching_pairs_exp01():
    assert GeneratorDuel(65, 8921).detatched_matching_pairs(5) == 0


def test_detatched_matching_pairs_exp02():
    assert GeneratorDuel(65, 8921).detatched_matching_pairs(1056) == 1


def test_detatched_matching_pairs_exp03():
    assert GeneratorDuel(65, 8921).detatched_matching_pairs(5_000_000) == 309
