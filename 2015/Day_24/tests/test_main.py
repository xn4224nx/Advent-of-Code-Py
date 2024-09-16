"""
Tests for functions in the main script.
"""

from main import (
    read_box_sizes,
    calc_group_qe,
    calc_group_weight,
    check_all_weights_same,
    check_first_group_fewest,
    find_lowest_qe,
)


def test_calc_group_qe_01():
    assert calc_group_qe([11, 9]) == 99


def test_calc_group_qe_02():
    assert calc_group_qe([10, 9, 1]) == 90


def test_calc_group_qe_03():
    assert calc_group_qe([10, 8, 2]) == 160


def test_calc_group_qe_04():
    assert calc_group_qe([10, 7, 3]) == 210


def test_calc_group_qe_05():
    assert calc_group_qe([10, 5, 4, 1]) == 200


def test_calc_group_weight_01():
    assert calc_group_weight([46, 49, 5]) == 100


def test_calc_group_weight_02():
    assert calc_group_weight([1, 2, 3, 4, 5]) == 15


def test_calc_group_weight_03():
    assert calc_group_weight([32, 79, 67]) == 178


def test_calc_group_weight_04():
    assert calc_group_weight([89, 5, 7, 2]) == 103


def test_calc_group_weight_05():
    assert calc_group_weight([1, 1]) == 2


def test_check_all_weights_same_01():
    assert check_all_weights_same([[7, 9, 12], [12, 15], [28]]) == False


def test_check_all_weights_same_02():
    assert check_all_weights_same([[8, 2, 1], [3, 7, 1], [10, 1]]) == True


def test_check_all_weights_same_03():
    assert check_all_weights_same([[77, 33], [98, 1, 1], [99, 2]]) == False


def test_check_all_weights_same_04():
    assert check_all_weights_same([[79, 7, 4], [85, 5], [10, 25, 55]]) == True


def test_check_all_weights_same_05():
    assert check_all_weights_same([[7], [1, 6], [5, 2, 1]]) == False


def test_check_first_group_fewest_01():
    assert check_first_group_fewest([[1], [345, 89, 90], [159, 98, 79]]) == True


def test_check_first_group_fewest_02():
    assert check_first_group_fewest([[89, 19], [78], [63, 87, 46]]) == False


def test_check_first_group_fewest_03():
    assert check_first_group_fewest([[5], [9], [10]]) == True


def test_check_first_group_fewest_04():
    assert check_first_group_fewest([[89, 79, 56], [56, 12, 4], [64]]) == False


def test_check_first_group_fewest_05():
    assert (
        check_first_group_fewest([[67, 54, 1], [23, 18, 10, 77], [4, 59, 91]]) == True
    )


def test_find_lowest_qe():
    assert find_lowest_qe(read_box_sizes("./data/example_01.txt"), 3) == 99


def test_read_box_sizes_example_01():
    assert read_box_sizes("./data/example_01.txt") == [
        1,
        2,
        3,
        4,
        5,
        7,
        8,
        9,
        10,
        11,
    ]


def test_read_box_sizes_input():
    assert read_box_sizes("./data/input.txt") == [
        1,
        2,
        3,
        7,
        11,
        13,
        17,
        19,
        23,
        31,
        37,
        41,
        43,
        47,
        53,
        59,
        61,
        67,
        71,
        73,
        79,
        83,
        89,
        97,
        101,
        103,
        107,
        109,
        113,
    ]
