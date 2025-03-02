"""
Tests for the main script
"""

from main import CPU


def test_data_ingestion_exp1():
    test = CPU("./data/example_01.txt")

    assert test.register == {
        "a": 0,
        "b": 0,
        "c": 0,
    }

    assert test.cmds == [
        ["b", 5, "a", ">", 1],
        ["a", 1, "b", "<", 5],
        ["c", 10, "a", ">=", 1],
        ["c", -20, "c", "==", 10],
    ]


def test_execute_com_exp1():
    test = CPU("./data/example_01.txt")
    test.execute_command(0)
    assert test.register == {
        "a": 0,
        "b": 0,
        "c": 0,
    }

    test.execute_command(1)
    assert test.register == {
        "a": 1,
        "b": 0,
        "c": 0,
    }

    test.execute_command(2)
    assert test.register == {
        "a": 1,
        "b": 0,
        "c": 10,
    }

    test.execute_command(3)
    assert test.register == {
        "a": 1,
        "b": 0,
        "c": -10,
    }


def test_final_largest_value_exp1():
    assert CPU("./data/example_01.txt").final_largest_value() == 1
