"""
Tests for functions in the main script.
"""

import main
import pytest


def test_container_data_ex():
    assert main.read_container_sizes("./data/example_01.txt") == [
        20,
        15,
        10,
        5,
        5,
    ]


def test_container_data_input():
    assert main.read_container_sizes("./data/input.txt") == [
        33,
        14,
        18,
        20,
        45,
        35,
        16,
        35,
        1,
        13,
        18,
        13,
        50,
        44,
        48,
        6,
        24,
        41,
        30,
        42,
    ]


def test_valid_cont_comb_1():
    assert (
        main.valid_cont_comb(
            25,
            [
                15,
                10,
            ],
        )
        == True
    )


def test_valid_cont_comb_2():
    assert (
        main.valid_cont_comb(
            25,
            [
                20,
                5,
            ],
        )
        == True
    )


def test_valid_cont_comb_3():
    assert (
        main.valid_cont_comb(
            25,
            [
                15,
                5,
                5,
            ],
        )
        == True
    )


def test_valid_cont_comb_4():
    assert (
        main.valid_cont_comb(
            25,
            [
                5,
                5,
            ],
        )
        == False
    )


def test_valid_cont_comb_5():
    assert (
        main.valid_cont_comb(
            25,
            [
                5,
                10,
            ],
        )
        == False
    )


def test_valid_cont_comb_5():
    assert (
        main.valid_cont_comb(
            25,
            [
                5,
                30,
            ],
        )
        == False
    )


def test_find_poss_combs():
    assert (
        main.find_poss_combs(25, main.read_container_sizes("./data/example_01.txt"))
        == 4
    )


def test_find_poss_combs_min_size():
    assert (
        main.find_poss_combs(
            25, main.read_container_sizes("./data/example_01.txt"), True
        )
        == 3
    )
