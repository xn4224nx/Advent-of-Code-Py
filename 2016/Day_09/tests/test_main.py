"""
Tests for the main script
"""

from main import read_data, find_markers, calc_len


def test_read_data_exp1():
    assert read_data("./data/example_01.txt") == "ADVENT"


def test_read_data_exp2():
    assert read_data("./data/example_02.txt") == "A(1x5)BC"


def test_read_data_exp3():
    assert read_data("./data/example_03.txt") == "(3x3)XYZ"


def test_read_data_exp4():
    assert read_data("./data/example_04.txt") == "A(2x2)BCD(2x2)EFG"


def test_read_data_exp5():
    assert read_data("./data/example_05.txt") == "(6x1)(1x3)A"


def test_read_data_exp6():
    assert read_data("./data/example_06.txt") == "X(8x2)(3x3)ABCY"


def test_read_data_exp7():
    assert read_data("./data/example_07.txt") == "(27x12)(20x12)(13x14)(7x10)(1x12)A"


def test_read_data_exp8():
    assert (
        read_data("./data/example_08.txt")
        == "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN"
    )


def test_find_markers_exp1():
    assert find_markers("ADVENT", False) == []


def test_find_markers_exp2():
    assert find_markers("A(1x5)BC", False) == [
        {
            "len": 1,
            "rep": 5,
            "start": 1,
            "end": 6,
            "copies": 1,
        }
    ]


def test_find_markers_exp3():
    assert find_markers("(3x3)XYZ", False) == [
        {
            "len": 3,
            "rep": 3,
            "start": 0,
            "end": 5,
            "copies": 1,
        }
    ]


def test_find_markers_exp4():
    assert find_markers("A(2x2)BCD(2x2)EFG", False) == [
        {
            "len": 2,
            "rep": 2,
            "start": 1,
            "end": 6,
            "copies": 1,
        },
        {
            "len": 2,
            "rep": 2,
            "start": 9,
            "end": 14,
            "copies": 1,
        },
    ]


def test_find_markers_exp5():
    assert find_markers("(6x1)(1x3)A", False) == [
        {
            "len": 6,
            "rep": 1,
            "start": 0,
            "end": 5,
            "copies": 1,
        }
    ]


def test_find_markers_exp6():
    assert find_markers("X(8x2)(3x3)ABCY", False) == [
        {
            "len": 8,
            "rep": 2,
            "start": 1,
            "end": 6,
            "copies": 1,
        }
    ]


def test_find_markers_exp7():
    assert find_markers("(27x12)(20x12)(13x14)(7x10)(1x12)A", False) == [
        {
            "len": 27,
            "rep": 12,
            "start": 0,
            "end": 7,
            "copies": 1,
        }
    ]


def test_find_markers_exp8():
    assert find_markers(
        "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", False
    ) == [
        {
            "len": 25,
            "rep": 3,
            "start": 0,
            "end": 6,
            "copies": 1,
        },
        {
            "len": 18,
            "rep": 9,
            "start": 46,
            "end": 51,
            "copies": 1,
        },
    ]


def test_find_markers_rec_exp1():
    assert find_markers("ADVENT", True) == []


def test_find_markers_rec_exp2():
    assert find_markers("A(1x5)BC", True) == [
        {
            "len": 1,
            "rep": 5,
            "start": 1,
            "end": 6,
            "copies": 1,
        }
    ]


def test_find_markers_rec_exp3():
    assert find_markers("(3x3)XYZ", True) == [
        {
            "len": 3,
            "rep": 3,
            "start": 0,
            "end": 5,
            "copies": 1,
        }
    ]


def test_find_markers_rec_exp4():
    assert find_markers("A(2x2)BCD(2x2)EFG", True) == [
        {
            "len": 2,
            "rep": 2,
            "start": 1,
            "end": 6,
            "copies": 1,
        },
        {
            "len": 2,
            "rep": 2,
            "start": 9,
            "end": 14,
            "copies": 1,
        },
    ]


def test_find_markers_rec_exp5():
    assert find_markers("(6x1)(1x3)A", True) == [
        {
            "len": 6,
            "rep": 1,
            "start": 0,
            "end": 5,
            "copies": 1,
        },
        {
            "len": 1,
            "rep": 3,
            "start": 5,
            "end": 10,
            "copies": 1,
        },
    ]


def test_find_markers_rec_exp6():
    assert find_markers("X(8x2)(3x3)ABCY", True) == [
        {
            "len": 8,
            "rep": 2,
            "start": 1,
            "end": 6,
            "copies": 1,
        },
        {
            "len": 3,
            "rep": 3,
            "start": 6,
            "end": 11,
            "copies": 2,
        },
    ]


def test_find_markers_rec_exp7():
    assert find_markers("(27x12)(20x12)(13x14)(7x10)(1x12)A", True) == [
        {
            "len": 27,
            "rep": 12,
            "start": 0,
            "end": 7,
            "copies": 1,
        },
        {
            "len": 20,
            "rep": 12,
            "start": 7,
            "end": 14,
            "copies": 1 * 12,
        },
        {
            "len": 13,
            "rep": 14,
            "start": 14,
            "end": 21,
            "copies": 1 * 12 * 12,
        },
        {
            "len": 7,
            "rep": 10,
            "start": 21,
            "end": 27,
            "copies": 1 * 12 * 12 * 14,
        },
        {
            "len": 1,
            "rep": 12,
            "start": 27,
            "end": 33,
            "copies": 1 * 12 * 12 * 14 * 10,
        },
    ]


def test_find_markers_rec_exp8():
    assert find_markers(
        "(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", True
    ) == [
        {
            "len": 25,
            "rep": 3,
            "start": 0,
            "end": 6,
            "copies": 1,
        },
        {
            "len": 3,
            "rep": 3,
            "start": 6,
            "end": 11,
            "copies": 1 * 3,
        },
        {
            "len": 2,
            "rep": 3,
            "start": 14,
            "end": 19,
            "copies": 1 * 3,
        },
        {
            "len": 5,
            "rep": 2,
            "start": 21,
            "end": 26,
            "copies": 1 * 3,
        },
        {
            "len": 18,
            "rep": 9,
            "start": 32,
            "end": 38,
            "copies": 1,
        },
        {
            "len": 3,
            "rep": 2,
            "start": 38,
            "end": 43,
            "copies": 1 * 9,
        },
        {
            "len": 5,
            "rep": 7,
            "start": 46,
            "end": 51,
            "copies": 1 * 9,
        },
    ]


def test_calc_len_exp1():
    assert calc_len("./data/example_01.txt", False) == 6


def test_calc_len_exp2():
    assert calc_len("./data/example_02.txt", False) == 7


def test_calc_len_exp3():
    assert calc_len("./data/example_03.txt", False) == 9


def test_calc_len_exp4():
    assert calc_len("./data/example_04.txt", False) == 11


def test_calc_len_exp5():
    assert calc_len("./data/example_05.txt", False) == 6


def test_calc_len_exp6():
    assert calc_len("./data/example_06.txt", False) == 18


def test_calc_len_exp7():
    assert calc_len("./data/example_03.txt", True) == 9


def test_calc_len_exp8():
    assert calc_len("./data/example_06.txt", True) == 20


def test_calc_len_exp9():
    assert calc_len("./data/example_07.txt", True) == 241920


def test_calc_len_exp10():
    assert calc_len("./data/example_08.txt", True) == 445
