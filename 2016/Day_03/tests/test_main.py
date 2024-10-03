"""
Tests for the main script
"""

from main import read_triangle_data, is_valid_triangle


def test_read_triangle_data_exp_1():
    assert read_triangle_data("./data/example_01.txt") == [
        (330, 143, 338),
        (769, 547, 83),
        (930, 625, 317),
        (669, 866, 147),
        (15, 881, 210),
    ]


def test_is_valid_triangle_exp_1():
    assert is_valid_triangle((5, 10, 25)) == False


def test_is_valid_triangle_exp_2():
    assert is_valid_triangle((330, 143, 338)) == True


def test_is_valid_triangle_exp_3():
    assert is_valid_triangle((769, 547, 83)) == False


def test_is_valid_triangle_exp_4():
    assert is_valid_triangle((930, 625, 317)) == True


def test_is_valid_triangle_exp_5():
    assert is_valid_triangle((669, 866, 147)) == False


def test_is_valid_triangle_exp_6():
    assert is_valid_triangle((15, 881, 210)) == False
