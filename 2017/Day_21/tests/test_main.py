"""
Tests for the main script.
"""

from main import FractalArt
import numpy as np


def test_new_artwork():
    test = FractalArt("./data/example_01.txt")
    assert np.all(
        test.pixels
        == np.array(
            [[False, True, False], [False, False, True], [True, True, True]], dtype=bool
        )
    )

    assert np.all(
        test.rules[0][0] == np.array([[False, False], [False, True]], dtype=bool)
    )
    assert np.all(
        test.rules[0][1]
        == np.array(
            [
                [True, True, False],
                [True, False, False],
                [False, False, False],
            ],
            dtype=bool,
        )
    )

    assert np.all(
        test.rules[1][0]
        == np.array(
            [[False, True, False], [False, False, True], [True, True, True]], dtype=bool
        )
    )
    assert np.all(
        test.rules[1][1]
        == np.array(
            [
                [True, False, False, True],
                [False, False, False, False],
                [False, False, False, False],
                [True, False, False, True],
            ],
            dtype=bool,
        )
    )


def test_split_exp01():
    test = FractalArt("./data/example_01.txt")
    test.div_n_split(3)
    assert np.all(
        test.pixels
        == np.array(
            [
                [True, False, False, True],
                [False, False, False, False],
                [False, False, False, False],
                [True, False, False, True],
            ],
            dtype=bool,
        )
    )


def test_split_exp02():
    test = FractalArt("./data/example_01.txt")
    test.pixels = np.array(
        [
            [True, False, False, True],
            [False, False, False, False],
            [False, False, False, False],
            [True, False, False, True],
        ],
        dtype=bool,
    )
    test.div_n_split(2)
    assert np.all(
        test.pixels
        == np.array(
            [
                [
                    True,
                    True,
                    False,
                    True,
                    True,
                    False,
                ],
                [
                    True,
                    False,
                    False,
                    True,
                    False,
                    False,
                ],
                [
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ],
                [
                    True,
                    True,
                    False,
                    True,
                    True,
                    False,
                ],
                [
                    True,
                    False,
                    False,
                    True,
                    False,
                    False,
                ],
                [
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ],
            ],
            dtype=bool,
        )
    )


def test_multi_split_exp01():
    test = FractalArt("./data/example_01.txt")
    test.splits(2)
    assert np.all(
        test.pixels
        == np.array(
            [
                [
                    True,
                    True,
                    False,
                    True,
                    True,
                    False,
                ],
                [
                    True,
                    False,
                    False,
                    True,
                    False,
                    False,
                ],
                [
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ],
                [
                    True,
                    True,
                    False,
                    True,
                    True,
                    False,
                ],
                [
                    True,
                    False,
                    False,
                    True,
                    False,
                    False,
                ],
                [
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ],
            ],
            dtype=bool,
        )
    )


def test_count_on_pixels_exp01():
    test = FractalArt("./data/example_01.txt")
    test.count_on_pixels() == 5


def test_count_on_pixels_exp02():
    test = FractalArt("./data/example_01.txt")
    test.pixels = np.array(
        [
            [True, False, False, True],
            [False, False, False, False],
            [False, False, False, False],
            [True, False, False, True],
        ],
        dtype=bool,
    )
    test.count_on_pixels() == 4


def test_count_on_pixels_exp03():
    test = FractalArt("./data/example_01.txt")
    test.pixels = np.array(
        [
            [
                True,
                True,
                False,
                True,
                True,
                False,
            ],
            [
                True,
                False,
                False,
                True,
                False,
                False,
            ],
            [
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            [
                True,
                True,
                False,
                True,
                True,
                False,
            ],
            [
                True,
                False,
                False,
                True,
                False,
                False,
            ],
            [
                False,
                False,
                False,
                False,
                False,
                False,
            ],
        ],
        dtype=bool,
    )
    test.count_on_pixels() == 12


def test_count_on_pixels_exp04():
    test = FractalArt("./data/example_01.txt")
    test.splits(2)
    assert test.count_on_pixels() == 12


def test_str_art_exp01():
    assert str(FractalArt("./data/example_01.txt")) == (".#.\n" "..#\n" "###\n")


def test_str_art_exp02():
    test = FractalArt("./data/example_01.txt")
    test.pixels = np.array(
        [
            [True, False, False, True],
            [False, False, False, False],
            [False, False, False, False],
            [True, False, False, True],
        ],
        dtype=bool,
    )
    assert str(test) == ("#..#\n" "....\n" "....\n" "#..#\n")


def test_str_art_exp03():
    test = FractalArt("./data/example_01.txt")
    test.pixels = np.array(
        [
            [
                True,
                True,
                False,
                True,
                True,
                False,
            ],
            [
                True,
                False,
                False,
                True,
                False,
                False,
            ],
            [
                False,
                False,
                False,
                False,
                False,
                False,
            ],
            [
                True,
                True,
                False,
                True,
                True,
                False,
            ],
            [
                True,
                False,
                False,
                True,
                False,
                False,
            ],
            [
                False,
                False,
                False,
                False,
                False,
                False,
            ],
        ],
        dtype=bool,
    )
    assert str(test) == (
        "##.##.\n" "#..#..\n" "......\n" "##.##.\n" "#..#..\n" "......\n"
    )
