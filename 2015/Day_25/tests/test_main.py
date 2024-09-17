"""
Tests for functions in the main script.
"""

from main import (
    next_num,
    place_in_order,
    find_val_at_coord,
)


def test_next_num_01():
    assert next_num(20151125) == 31916031


def test_next_num_02():
    assert next_num(31916031) == 18749137


def test_next_num_03():
    assert next_num(18749137) == 16080970


def test_next_num_04():
    assert next_num(16080970) == 21629792


def test_next_num_05():
    assert next_num(21629792) == 17289845


def test_place_in_order_01():
    assert place_in_order(6, 1) == 15


def test_place_in_order_02():
    assert place_in_order(1, 6) == 20


def test_place_in_order_03():
    assert place_in_order(3, 4) == 18


def test_place_in_order_04():
    assert place_in_order(5, 2) == 16


def test_place_in_order_05():
    assert place_in_order(2, 5) == 19


def test_find_val_at_coord_01():
    assert find_val_at_coord(20151125, 6, 6) == 27995004


def test_find_val_at_coord_02():
    assert find_val_at_coord(20151125, 6, 1) == 33071741


def test_find_val_at_coord_03():
    assert find_val_at_coord(20151125, 3, 4) == 7981243


def test_find_val_at_coord_04():
    assert find_val_at_coord(20151125, 5, 2) == 17552253


def test_find_val_at_coord_05():
    assert find_val_at_coord(20151125, 1, 6) == 33511524
