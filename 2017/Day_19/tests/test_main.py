"""
Tests for the main script.
"""

from main import Network


def test_parse_data_exp01():
    test = Network("./data/example_01.txt")
    assert test.plan == {
        (5, 0): "|",
        (5, 1): "|",
        (5, 2): "A",
        (5, 3): "|",
        (5, 4): "|",
        (5, 5): "+",
        (6, 5): "B",
        (7, 5): "-",
        (8, 5): "+",
        (8, 4): "|",
        (8, 3): "-",
        (8, 2): "|",
        (8, 1): "+",
        (9, 1): "-",
        (10, 1): "-",
        (11, 1): "+",
        (11, 2): "C",
        (11, 3): "|",
        (11, 4): "|",
        (11, 5): "+",
        (12, 5): "-",
        (13, 5): "-",
        (14, 5): "+",
        (14, 4): "D",
        (14, 3): "+",
        (13, 3): "-",
        (12, 3): "-",
        (10, 3): "E",
        (9, 3): "-",
        (8, 3): "-",
        (7, 3): "-",
        (6, 3): "-",
        (4, 3): "-",
        (3, 3): "-",
        (2, 3): "-",
        (1, 3): "F",
    }
    assert test.loc == (5, 0)
    assert test.direct == 1j


def test_step_exp01():
    test = Network("./data/example_01.txt")
    test.loc = (5, 0)
    test.direct = 1j
    test.step()
    assert test.loc == (5, 1)
    assert test.direct == 1j


def test_step_exp02():
    test = Network("./data/example_01.txt")
    test.loc = (5, 1)
    test.direct = 1j
    test.step()
    assert test.loc == (5, 2)
    assert test.direct == 1j


def test_step_exp03():
    test = Network("./data/example_01.txt")
    test.loc = (5, 2)
    test.direct = 1j
    test.step()
    assert test.loc == (5, 3)
    assert test.direct == 1j


def test_step_exp04():
    test = Network("./data/example_01.txt")
    test.loc = (5, 3)
    test.direct = 1j
    test.step()
    assert test.loc == (5, 4)
    assert test.direct == 1j


def test_step_exp05():
    test = Network("./data/example_01.txt")
    test.loc = (5, 4)
    test.direct = 1j
    test.step()
    assert test.loc == (5, 5)
    assert test.direct == 1


def test_step_exp06():
    test = Network("./data/example_01.txt")
    test.loc = (5, 5)
    test.direct = 1
    test.step()
    assert test.loc == (6, 5)
    assert test.direct == 1


def test_step_exp07():
    test = Network("./data/example_01.txt")
    test.loc = (6, 5)
    test.direct = 1
    test.step()
    assert test.loc == (7, 5)
    assert test.direct == 1


def test_step_exp08():
    test = Network("./data/example_01.txt")
    test.loc = (7, 5)
    test.direct = 1
    test.step()
    assert test.loc == (8, 5)
    assert test.direct == -1j


def test_step_exp09():
    test = Network("./data/example_01.txt")
    test.loc = (8, 5)
    test.direct = -1j
    test.step()
    assert test.loc == (8, 4)
    assert test.direct == -1j


def test_step_exp10():
    test = Network("./data/example_01.txt")
    test.loc = (8, 4)
    test.direct = -1j
    test.step()
    assert test.loc == (8, 3)
    assert test.direct == -1j


def test_step_exp11():
    test = Network("./data/example_01.txt")
    test.loc = (8, 3)
    test.direct = -1j
    test.step()
    assert test.loc == (8, 2)
    assert test.direct == -1j


def test_step_exp12():
    test = Network("./data/example_01.txt")
    test.loc = (8, 2)
    test.direct = -1j
    test.step()
    assert test.loc == (8, 1)
    assert test.direct == 1


def test_path_letters_exp01():
    assert Network("./data/example_01.txt").path_letters() == "ABCDEF"
