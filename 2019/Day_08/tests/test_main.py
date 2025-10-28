"""
Tests for the main script.
"""

from main import DSNImage


def test_new_img_exp0():
    test = DSNImage("./data/example_0.txt", (3, 2))
    assert test.dims == (3, 2)
    assert test.pixels == [[1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 1, 2]]


def test_new_img_exp1():
    test = DSNImage("./data/example_1.txt", (2, 2))
    assert test.dims == (2, 2)
    assert test.pixels == [[0, 2, 2, 2], [1, 1, 2, 2], [2, 2, 1, 2], [0, 0, 0, 0]]


def test_checksum_exp0():
    assert DSNImage("./data/example_0.txt", (3, 2)).checksum() == 1


def test_render_exp0():
    assert str(DSNImage("./data/example_1.txt", (2, 2))) == " █\n█ \n"
