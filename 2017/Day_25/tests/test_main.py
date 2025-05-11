"""
Tests for the main script.
"""

from main import TuringMachine


def test_new_machine_exp01():
    test = TuringMachine("./data/example_01.txt")
    assert test.state == "A"
    assert test.rules == {
        ("A", 0): [1, "R", "B"],
        ("A", 1): [0, "L", "B"],
        ("B", 0): [1, "L", "A"],
        ("B", 1): [1, "R", "A"],
    }
    assert test.tape == set()
    assert test.cursor == 0
    assert test.diag_steps == 6


def test_step_exp01():
    test = TuringMachine("./data/example_01.txt")
    test.step()
    assert test.state == "B"
    assert test.cursor == 1
    assert test.tape == {0}


def test_step_exp02():
    test = TuringMachine("./data/example_01.txt")
    test.state = "B"
    test.cursor = 1
    test.tape = {0}

    test.step()

    assert test.state == "A"
    assert test.cursor == 0
    assert test.tape == {0, 1}


def test_step_exp03():
    test = TuringMachine("./data/example_01.txt")
    test.state = "A"
    test.cursor = 0
    test.tape = {0, 1}

    test.step()

    assert test.state == "B"
    assert test.cursor == -1
    assert test.tape == {1}


def test_step_exp04():
    test = TuringMachine("./data/example_01.txt")
    test.state = "B"
    test.cursor = -1
    test.tape = {1}

    test.step()

    assert test.state == "A"
    assert test.cursor == -2
    assert test.tape == {1, -1}


def test_step_exp05():
    test = TuringMachine("./data/example_01.txt")
    test.state = "A"
    test.cursor = -2
    test.tape = {1, -1}

    test.step()

    assert test.state == "B"
    assert test.cursor == -1
    assert test.tape == {1, -1, -2}


def test_step_exp06():
    test = TuringMachine("./data/example_01.txt")
    test.state = "B"
    test.cursor = -1
    test.tape = {1, -1, -2}

    test.step()

    assert test.state == "A"
    assert test.cursor == 0
    assert test.tape == {1, -1, -2}


def test_diagnostic_checksum_exp01():
    assert TuringMachine("./data/example_01.txt").diagnostic_checksum() == 3
