"""
Tests for the main script and the KnotHash class.
"""

from main import ProgramDance
from collections import deque


def test_parse_data():
    test = ProgramDance("abcde", "./data/example_01.txt")
    assert test.instructs == [
        {"name": "spin", "magnitude": 1},
        {"name": "exchange", "idx_a": 3, "idx_b": 4},
        {"name": "partner", "prog_a": "e", "prog_b": "b"},
    ]
    assert test.progs == deque("abcde")


def test_spin_exp01():
    test = ProgramDance("abcde", "./data/example_01.txt")
    test.spin(3)
    assert test.progs == deque("cdeab")


def test_spin_exp02():
    test = ProgramDance("abcde", "./data/example_01.txt")
    test.spin(1)
    assert test.progs == deque("eabcd")


def test_exchange_exp01():
    test = ProgramDance("eabcd", "./data/example_01.txt")
    test.exchange(3, 4)
    assert test.progs == deque("eabdc")


def test_partner_exp01():
    test = ProgramDance("eabdc", "./data/example_01.txt")
    test.partner("e", "b")
    assert test.progs == deque("baedc")


def test_execute_command_exp01():
    test = ProgramDance("abcde", "./data/example_01.txt")
    test.execute_command({"name": "spin", "magnitude": 1})
    assert test.progs == deque("eabcd")


def test_execute_command_exp01():
    test = ProgramDance("eabcd", "./data/example_01.txt")
    test.execute_command({"name": "exchange", "idx_a": 3, "idx_b": 4})
    assert test.progs == deque("eabdc")


def test_execute_command_exp01():
    test = ProgramDance("eabdc", "./data/example_01.txt")
    test.execute_command({"name": "partner", "prog_a": "e", "prog_b": "b"})
    assert test.progs == deque("baedc")


def test_run_all_commands_exp01():
    test = ProgramDance("abcde", "./data/example_01.txt")
    assert test.run_all_commands() == "baedc"
