"""
Tests for the main script
"""

from main import FuelGrid


def test_grid_initialisation_exp0():
    test = FuelGrid(8, (300, 300))
    assert test.grid[3][5] == 4


def test_grid_initialisation_exp1():
    test = FuelGrid(57, (300, 300))
    assert test.grid[122][79] == -5


def test_grid_initialisation_exp2():
    test = FuelGrid(39, (300, 300))
    assert test.grid[217][196] == 0


def test_grid_initialisation_exp3():
    test = FuelGrid(71, (300, 300))
    assert test.grid[101][153] == 4


def test_grid_initialisation_exp4():
    test = FuelGrid(18, (300, 300))
    assert test.grid[33][45] == 4


def test_grid_initialisation_exp5():
    test = FuelGrid(42, (300, 300))
    assert test.grid[21][61] == 4


def test_coords_of_max_power_exp0():
    test = FuelGrid(18, (300, 300))
    assert test.coords_of_max_power((3, 3)) == (33, 45)


def test_coords_of_max_power_exp1():
    test = FuelGrid(42, (300, 300))
    assert test.coords_of_max_power((3, 3)) == (21, 61)
