"""
Tests for the valid_mine() function.
"""

import main


def test_initalisation():
    t_grid = main.LightGrid((1000, 1000), False)

    assert isinstance(t_grid, main.LightGrid)


def test_example_01():
    t_grid = main.LightGrid((1000, 1000), False)
    t_grid.execute_commands("./data/example_01.txt")

    assert t_grid.count_on_lights() == 1_000_000


def test_example_02():
    t_grid = main.LightGrid((1000, 1000), False)
    t_grid.execute_commands("./data/example_02.txt")

    assert t_grid.count_on_lights() == 1_000


def test_example_03():
    t_grid = main.LightGrid((1000, 1000), True)
    t_grid.execute_commands("./data/example_03.txt")

    assert t_grid.count_on_lights() == 999996
