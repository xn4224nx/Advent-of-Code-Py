"""
Tests for the main script
"""

from main import SignalGenerator, Comm


def test_class_initialisation():
    test = SignalGenerator("./data/example_01.txt")
    assert test.commands == [
        (Comm.CPY, 41, "a"),
        (Comm.INC, "a"),
        (Comm.INC, "a"),
        (Comm.DEC, "a"),
        (Comm.JNZ, "a", 2),
        (Comm.DEC, "a"),
        (Comm.OUT, "a"),
    ]
    assert test.register == {
        "a": 1,
        "b": 0,
        "c": 0,
        "d": 0,
    }
    assert test.command_idx == 0
    assert test.outputs == []
    assert test.start_a == 1


def test_cpy():
    test = SignalGenerator("./data/example_01.txt")
    test.parse_instruc((Comm.CPY, 6, "a"))
    test.parse_instruc((Comm.CPY, "a", "b"))
    test.parse_instruc((Comm.CPY, -7, "d"))
    assert test.register == {
        "a": 6,
        "b": 6,
        "c": 0,
        "d": -7,
    }
    assert test.command_idx == 3


def test_inc():
    test = SignalGenerator("./data/example_01.txt")
    test.parse_instruc((Comm.INC, "a"))
    test.parse_instruc((Comm.INC, "b"))
    test.parse_instruc((Comm.INC, "c"))
    assert test.register == {
        "a": 1,
        "b": 1,
        "c": 1,
        "d": 0,
    }
    assert test.command_idx == 3


def test_dec():
    test = SignalGenerator("./data/example_01.txt")
    test.parse_instruc((Comm.DEC, "a"))
    test.parse_instruc((Comm.DEC, "b"))
    test.parse_instruc((Comm.DEC, "c"))
    assert test.register == {
        "a": -1,
        "b": -1,
        "c": -1,
        "d": 0,
    }
    assert test.command_idx == 3


def test_jnz():
    test = SignalGenerator("./data/example_01.txt")
    test.register = {
        "a": 0,
        "b": 10,
        "c": -1,
        "d": 9,
    }

    test.parse_instruc((Comm.JNZ, "a", 4))
    assert test.command_idx == 1

    test.parse_instruc((Comm.JNZ, 4, "b"))
    assert test.command_idx == 11

    test.parse_instruc((Comm.JNZ, "c", "3"))
    assert test.command_idx == 14


def test_out():
    test = SignalGenerator("./data/example_01.txt")
    test.register = {
        "a": 20,
        "b": 10,
        "c": -1,
        "d": 9,
    }
    test.parse_instruc((Comm.OUT, "c"))
    test.parse_instruc((Comm.OUT, "a"))
    test.parse_instruc((Comm.OUT, "d"))
    test.parse_instruc((Comm.OUT, "b"))
    assert test.outputs == [-1, 20, 9, 10]
