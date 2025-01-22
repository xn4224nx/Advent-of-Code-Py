"""
Tests for the main script
"""

from main import SignalGenerator, Comm


def test_class_initialisation():
    test = SignalGenerator("./data/example_01.txt")
    assert test.commands == [
        (Comm.CPY, 41, 1000),
        (Comm.INC, 1000),
        (Comm.INC, 1000),
        (Comm.DEC, 1000),
        (Comm.JNZ, 1000, 2),
        (Comm.DEC, 1000),
        (Comm.OUT, 1000),
    ]
    assert test.register == [0, 0, 0, 0]
    assert test.command_idx == 0
    assert test.outputs == []


def test_cpy():
    test = SignalGenerator("./data/example_01.txt")
    test.parse_instruc((Comm.CPY, 6, 1000))
    test.parse_instruc((Comm.CPY, 1000, 1001))
    test.parse_instruc((Comm.CPY, -7, 1003))
    assert test.register == [6, 6, 0, -7]
    assert test.command_idx == 3


def test_inc():
    test = SignalGenerator("./data/example_01.txt")
    test.parse_instruc((Comm.INC, 1000))
    test.parse_instruc((Comm.INC, 1001))
    test.parse_instruc((Comm.INC, 1002))
    assert test.register == [1, 1, 1, 0]
    assert test.command_idx == 3


def test_dec():
    test = SignalGenerator("./data/example_01.txt")
    test.parse_instruc((Comm.DEC, 1000))
    test.parse_instruc((Comm.DEC, 1001))
    test.parse_instruc((Comm.DEC, 1002))
    assert test.register == [-1, -1, -1, 0]
    assert test.command_idx == 3


def test_jnz():
    test = SignalGenerator("./data/example_01.txt")
    test.register = [0, 10, -1, 9]

    test.parse_instruc((Comm.JNZ, 1000, 4))
    assert test.command_idx == 1

    test.parse_instruc((Comm.JNZ, 4, 1001))
    assert test.command_idx == 11

    test.parse_instruc((Comm.JNZ, 1002, 3))
    assert test.command_idx == 14


def test_out():
    test = SignalGenerator("./data/example_01.txt")
    test.register = [20, 10, -1, 9]
    test.parse_instruc((Comm.OUT, 1002))
    test.parse_instruc((Comm.OUT, 1000))
    test.parse_instruc((Comm.OUT, 1003))
    test.parse_instruc((Comm.OUT, 1001))
    assert test.outputs == [-1, 20, 9, 10]
