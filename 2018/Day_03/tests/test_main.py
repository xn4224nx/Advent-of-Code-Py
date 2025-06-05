"""
Tests for the main script
"""

from main import FabricSlicer


def test_read_exp01():
    assert FabricSlicer("./data/example_0.txt").coverage == {
        (3, 1): {2},
        (4, 1): {2},
        (5, 1): {2},
        (6, 1): {2},
        (3, 2): {2},
        (4, 2): {2},
        (5, 2): {2},
        (6, 2): {2},
        (1, 3): {1},
        (2, 3): {1},
        (3, 3): {1, 2},
        (4, 3): {1, 2},
        (5, 3): {2},
        (6, 3): {2},
        (1, 4): {1},
        (2, 4): {1},
        (3, 4): {1, 2},
        (4, 4): {1, 2},
        (5, 4): {2},
        (6, 4): {2},
        (1, 5): {1},
        (2, 5): {1},
        (3, 5): {1},
        (4, 5): {1},
        (5, 5): {3},
        (6, 5): {3},
        (1, 6): {1},
        (2, 6): {1},
        (3, 6): {1},
        (4, 6): {1},
        (5, 6): {3},
        (6, 6): {3},
    }


def test_calc_overlapping_exp01():
    assert FabricSlicer("./data/example_0.txt").calc_overlapping_area() == 4
