"""
Tests for the main script
"""

from main import CompressedData


def test_marker_detection():
    assert CompressedData("./data/example_01.txt").markers == []
    assert CompressedData("./data/example_02.txt").markers == [(1, 5, 1, 5)]
    assert CompressedData("./data/example_03.txt").markers == [(0, 4, 3, 3)]
    assert CompressedData("./data/example_04.txt").markers == [
        (1, 5, 2, 2),
        (9, 13, 2, 2),
    ]
    assert CompressedData("./data/example_05.txt").markers == [
        (0, 4, 6, 1),
        (5, 9, 1, 3),
    ]
    assert CompressedData("./data/example_06.txt").markers == [
        (1, 5, 8, 2),
        (6, 10, 3, 3),
    ]
    assert CompressedData("./data/example_07.txt").markers == [
        (0, 6, 27, 12),
        (7, 13, 20, 12),
        (14, 20, 13, 14),
        (21, 26, 7, 10),
        (27, 32, 1, 12),
    ]
    assert CompressedData("./data/example_08.txt").markers == [
        (0, 5, 25, 3),
        (6, 10, 3, 3),
        (14, 18, 2, 3),
        (21, 25, 5, 2),
        (32, 37, 18, 9),
        (38, 42, 3, 2),
        (46, 50, 5, 7),
    ]


def test_decompression():
    assert CompressedData("./data/example_01.txt").decomp_len(False) == 6
    assert CompressedData("./data/example_02.txt").decomp_len(False) == 7
    assert CompressedData("./data/example_03.txt").decomp_len(False) == 9
    assert CompressedData("./data/example_04.txt").decomp_len(False) == 11
    assert CompressedData("./data/example_05.txt").decomp_len(False) == 6
    assert CompressedData("./data/example_06.txt").decomp_len(False) == 18


def test_recursive_decompression():
    assert CompressedData("./data/example_01.txt").decomp_len(True) == 6
    assert CompressedData("./data/example_03.txt").decomp_len(True) == 9
    assert CompressedData("./data/example_06.txt").decomp_len(True) == 20
    assert CompressedData("./data/example_07.txt").decomp_len(True) == 241920
    assert CompressedData("./data/example_08.txt").decomp_len(True) == 445
