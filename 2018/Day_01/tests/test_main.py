"""
Tests for the main script
"""

from main import FreqDist


def test_read_exp01():
    assert FreqDist("./data/example_01.txt").changes == [1, -2, 3, 1]


def test_read_exp02():
    assert FreqDist("./data/example_02.txt").changes == [1, 1, 1]


def test_read_exp03():
    assert FreqDist("./data/example_03.txt").changes == [
        1,
        1,
        -2,
    ]


def test_read_exp04():
    assert FreqDist("./data/example_04.txt").changes == [-1, -2, -3]


def test_final_freq_exp01():
    assert FreqDist("./data/example_01.txt").final_freq() == 3


def test_final_freq_exp02():
    assert FreqDist("./data/example_02.txt").final_freq() == 3


def test_final_freq_exp03():
    assert FreqDist("./data/example_03.txt").final_freq() == 0


def test_final_freq_exp04():
    assert FreqDist("./data/example_04.txt").final_freq() == -6


def test_repeated_freq_exp05():
    assert FreqDist("./data/example_05.txt").repeated_freq() == 0


def test_repeated_freq_exp06():
    assert FreqDist("./data/example_06.txt").repeated_freq() == 10


def test_repeated_freq_exp07():
    assert FreqDist("./data/example_07.txt").repeated_freq() == 5


def test_repeated_freq_exp08():
    assert FreqDist("./data/example_08.txt").repeated_freq() == 14
