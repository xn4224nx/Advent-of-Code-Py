"""
Tests for the main script
"""

from main import FuelGrid


def test_grid_initialisation_exp0():
    assert FuelGrid(8, 300).grid[3][5] == 4


def test_grid_initialisation_exp1():
    assert FuelGrid(57, 300).grid[122][79] == -5


def test_grid_initialisation_exp2():
    assert FuelGrid(39, 300).grid[217][196] == 0


def test_grid_initialisation_exp3():
    assert FuelGrid(71, 300).grid[101][153] == 4


def test_grid_initialisation_exp4():
    assert FuelGrid(18, 300).grid[33][45] == 4


def test_grid_initialisation_exp5():
    assert FuelGrid(42, 300).grid[21][61] == 4


def test_coords_of_max_power_exp0():
    assert FuelGrid(18, 300).coords_of_max_power(3) == ((33, 45), 29)


def test_coords_of_max_power_exp1():
    assert FuelGrid(42, 300).coords_of_max_power(3) == ((21, 61), 30)


def test_max_power_search_var_window_exp0():
    assert FuelGrid(18, 300).max_power_search_var_window() == ((90, 269), 16)


def test_max_power_search_var_window_exp1():
    assert FuelGrid(42, 300).max_power_search_var_window() == ((232, 251), 12)
