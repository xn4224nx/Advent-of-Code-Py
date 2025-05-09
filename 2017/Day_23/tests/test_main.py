"""
Tests for the main script.
"""

from main import CPU


def test_count_on_pixels_exp04():
    test = CPU("./data/input.txt")
    assert test.cmd_idx == 0
    assert test.cmds == [
        ["set", "b", 57],
        ["set", "c", "b"],
        ["jnz", "a", 2],
        ["jnz", 1, 5],
        ["mul", "b", 100],
        ["sub", "b", -100000],
        ["set", "c", "b"],
        ["sub", "c", -17000],
        ["set", "f", 1],
        ["set", "d", 2],
        ["set", "e", 2],
        ["set", "g", "d"],
        ["mul", "g", "e"],
        ["sub", "g", "b"],
        ["jnz", "g", 2],
        ["set", "f", 0],
        ["sub", "e", -1],
        ["set", "g", "e"],
        ["sub", "g", "b"],
        ["jnz", "g", -8],
        ["sub", "d", -1],
        ["set", "g", "d"],
        ["sub", "g", "b"],
        ["jnz", "g", -13],
        ["jnz", "f", 2],
        ["sub", "h", -1],
        ["set", "g", "b"],
        ["sub", "g", "c"],
        ["jnz", "g", 2],
        ["jnz", 1, 3],
        ["sub", "b", -17],
        ["jnz", 1, -23],
    ]
    assert test.register == {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
    }


def test_set_exp01():
    test = CPU("./data/input.txt")
    test.cmds = [
        ["set", "b", 57],
    ]
    test.exe_command(0)
    assert test.register["b"] == 57


def test_set_exp02():
    test = CPU("./data/input.txt")
    test.register["c"] = -10
    test.cmds = [
        ["set", "a", "c"],
    ]
    test.exe_command(0)
    assert test.register["a"] == -10


def test_sub_exp01():
    test = CPU("./data/input.txt")
    test.cmds = [
        ["sub", "h", -1],
    ]
    test.exe_command(0)
    assert test.register["h"] == 1


def test_sub_exp02():
    test = CPU("./data/input.txt")
    test.cmds = [
        ["sub", "h", "b"],
    ]
    test.register["b"] = 1
    test.exe_command(0)
    assert test.register["h"] == -1


def test_mul_exp01():
    test = CPU("./data/input.txt")
    test.register["b"] = 7
    test.register["h"] = -3
    test.cmds = [
        ["mul", "h", "b"],
    ]
    test.exe_command(0)
    assert test.register["h"] == -21


def test_mul_exp02():
    test = CPU("./data/input.txt")
    test.register["b"] = 7
    test.cmds = [
        ["mul", "b", 10],
    ]
    test.exe_command(0)
    assert test.register["b"] == 70


def test_jnz_exp01():
    test = CPU("./data/input.txt")
    test.cmds = [
        ["jnz", "h", 8],
    ]
    test.exe_command(0)
    assert test.cmd_idx == 1


def test_jnz_exp02():
    test = CPU("./data/input.txt")
    test.cmds = [
        ["jnz", "h", "b"],
    ]
    test.exe_command(0)
    assert test.cmd_idx == 1


def test_jnz_exp03():
    test = CPU("./data/input.txt")
    test.register["h"] = 7
    test.cmds = [
        ["jnz", "h", 8],
    ]
    test.exe_command(0)
    assert test.cmd_idx == 8


def test_jnz_exp04():
    test = CPU("./data/input.txt")
    test.register["h"] = 7
    test.register["b"] = 7
    test.cmds = [
        ["jnz", "h", "b"],
    ]
    test.exe_command(0)
    assert test.cmd_idx == 7
