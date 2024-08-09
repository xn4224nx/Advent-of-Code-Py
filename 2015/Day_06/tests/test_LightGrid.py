"""
Tests for the valid_mine() function.
"""

import main


def test_example_01():
    t_grid = main.LightGrid("./data/example_01.txt", False)
    t_grid.execute_commands()

    assert t_grid.count_on_lights() == 1_000_000


def test_example_02():
    t_grid = main.LightGrid("./data/example_02.txt", False)
    t_grid.execute_commands()

    assert t_grid.count_on_lights() == 1_000


def test_example_03():
    t_grid = main.LightGrid("./data/example_03.txt", False)
    t_grid.execute_commands()

    assert t_grid.count_on_lights() == 0


def test_example_04():
    t_grid = main.LightGrid("./data/example_04.txt", True)
    t_grid.execute_commands()

    assert t_grid.count_on_lights() == 1


def test_example_05():
    t_grid = main.LightGrid("./data/example_05.txt", True)
    t_grid.execute_commands()

    assert t_grid.count_on_lights() == 2000000
