"""
Tests for functions in the main script.
"""

import main
import pytest
import numpy as np


def test_read_lights_ex_1():
    assert np.array_equal(
        main.read_lights("./data/example_01.txt"),
        np.array(
            [
                [0, 1, 0, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
                [1, 0, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 0],
                [1, 0, 1, 0, 0, 1],
                [1, 1, 1, 1, 0, 0],
            ],
            dtype="bool",
        ),
    )


def test_read_lights_ex_2():
    assert np.array_equal(
        main.read_lights("./data/example_02.txt"),
        np.array(
            [
                [0, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0, 1],
                [0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0],
                [1, 0, 1, 1, 0, 0],
            ],
            dtype="bool",
        ),
    )


def test_read_lights_ex_3():
    assert np.array_equal(
        main.read_lights("./data/example_03.txt"),
        np.array(
            [
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 1, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0],
            ],
            dtype="bool",
        ),
    )


def test_read_lights_ex_4():
    assert np.array_equal(
        main.read_lights("./data/example_04.txt"),
        np.array(
            [
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ],
            dtype="bool",
        ),
    )


def test_read_lights_ex_5():
    assert np.array_equal(
        main.read_lights("./data/example_05.txt"),
        np.array(
            [
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0],
            ],
            dtype="bool",
        ),
    )


def test_find_adj_coords_1():
    pos_coords = main.find_adj_coords((3, 3), (0, 0))
    assert len(pos_coords) == 3
    assert set(pos_coords) == set([(0, 1), (1, 0), (1, 1)])


def test_find_adj_coords_2():
    pos_coords = main.find_adj_coords((3, 3), (0, 1))
    assert len(pos_coords) == 5
    assert set(pos_coords) == set([(0, 0), (0, 2), (1, 0), (1, 1), (1, 2)])


def test_find_adj_coords_3():
    pos_coords = main.find_adj_coords((3, 3), (0, 2))
    assert len(pos_coords) == 3
    assert set(pos_coords) == set([(0, 1), (1, 1), (1, 2)])


def test_find_adj_coords_4():
    pos_coords = main.find_adj_coords((3, 3), (1, 0))
    assert len(pos_coords) == 5
    assert set(pos_coords) == set([(0, 0), (0, 1), (1, 1), (2, 0), (2, 1)])


def test_find_adj_coords_5():
    pos_coords = main.find_adj_coords((3, 3), (1, 1))
    assert len(pos_coords) == 8
    assert set(pos_coords) == set(
        [(0, 0), (0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1), (2, 2)]
    )


def test_find_adj_coords_6():
    pos_coords = main.find_adj_coords((3, 3), (1, 2))
    assert len(pos_coords) == 5
    assert set(pos_coords) == set([(0, 1), (0, 2), (1, 1), (2, 1), (2, 2)])


def test_find_adj_coords_7():
    pos_coords = main.find_adj_coords((3, 3), (2, 0))
    assert len(pos_coords) == 3
    assert set(pos_coords) == set([(1, 0), (1, 1), (2, 1)])


def test_find_adj_coords_8():
    pos_coords = main.find_adj_coords((3, 3), (2, 1))
    assert len(pos_coords) == 5
    assert set(pos_coords) == set([(1, 0), (1, 1), (1, 2), (2, 0), (2, 2)])


def test_find_adj_coords_9():
    pos_coords = main.find_adj_coords((3, 3), (2, 2))
    assert len(pos_coords) == 3
    assert set(pos_coords) == set([(1, 1), (1, 2), (2, 1)])


def test_new_light_value_1():
    assert (
        main.new_light_value(
            np.array(
                [
                    [1, 1, 0],
                    [1, 1, 0],
                    [0, 0, 0],
                ],
                dtype="bool",
            ),
            (1, 0),
        )
        == True
    )


def test_new_light_value_2():
    assert (
        main.new_light_value(
            np.array(
                [
                    [1, 0, 0],
                    [0, 1, 0],
                    [0, 1, 0],
                ],
                dtype="bool",
            ),
            (1, 0),
        )
        == True
    )


def test_new_light_value_3():
    assert (
        main.new_light_value(
            np.array(
                [
                    [1, 1, 0],
                    [0, 0, 1],
                    [0, 0, 0],
                ],
                dtype="bool",
            ),
            (0, 1),
        )
        == True
    )


def test_new_light_value_4():
    assert (
        main.new_light_value(
            np.array(
                [
                    [0, 0, 1],
                    [0, 1, 0],
                    [0, 1, 1],
                ],
                dtype="bool",
            ),
            (1, 2),
        )
        == False
    )


def test_new_light_value_5():
    assert (
        main.new_light_value(
            np.array(
                [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 0, 0],
                ],
                dtype="bool",
            ),
            (0, 0),
        )
        == False
    )


def test_new_light_value_6():
    assert (
        main.new_light_value(
            np.array(
                [
                    [0, 0, 0],
                    [0, 0, 1],
                    [0, 0, 1],
                ],
                dtype="bool",
            ),
            (2, 2),
        )
        == False
    )


def test_step_lights_multi():
    initial = main.read_lights("./data/example_01.txt")
    final = main.read_lights("./data/example_05.txt")
    assert np.array_equal(main.step_lights(initial, 4), final)


def test_step_lights_1():
    initial = main.read_lights("./data/example_01.txt")
    final = main.read_lights("./data/example_02.txt")
    assert np.array_equal(main.step_lights(initial, 1), final)


def test_step_lights_2():
    initial = main.read_lights("./data/example_02.txt")
    final = main.read_lights("./data/example_03.txt")
    assert np.array_equal(main.step_lights(initial, 1), final)


def test_step_lights_3():
    initial = main.read_lights("./data/example_03.txt")
    final = main.read_lights("./data/example_04.txt")
    assert np.array_equal(main.step_lights(initial, 1), final)


def test_step_lights_4():
    initial = main.read_lights("./data/example_04.txt")
    final = main.read_lights("./data/example_05.txt")
    assert np.array_equal(main.step_lights(initial, 1), final)


def test_step_lights_multi_cor():
    initial = main.read_lights("./data/example_06.txt")
    final = main.read_lights("./data/example_11.txt")
    assert np.array_equal(main.step_lights(initial, 5, True), final)


def test_step_lights_1_cor():
    initial = main.read_lights("./data/example_06.txt")
    final = main.read_lights("./data/example_07.txt")
    assert np.array_equal(main.step_lights(initial, 1, True), final)


def test_step_lights_2_cor():
    initial = main.read_lights("./data/example_07.txt")
    final = main.read_lights("./data/example_08.txt")
    assert np.array_equal(main.step_lights(initial, 1, True), final)


def test_step_lights_3_cor():
    initial = main.read_lights("./data/example_08.txt")
    final = main.read_lights("./data/example_09.txt")
    assert np.array_equal(main.step_lights(initial, 1, True), final)


def test_step_lights_4_cor():
    initial = main.read_lights("./data/example_09.txt")
    final = main.read_lights("./data/example_10.txt")
    assert np.array_equal(main.step_lights(initial, 1, True), final)


def test_step_lights_5_cor():
    initial = main.read_lights("./data/example_10.txt")
    final = main.read_lights("./data/example_11.txt")
    assert np.array_equal(main.step_lights(initial, 1, True), final)
