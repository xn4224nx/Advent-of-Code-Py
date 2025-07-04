"""
Tests for the main script.
"""

from main import Duo


def test_parse_data():
    test = Duo("./data/example_01.txt")
    assert test.idx == [0, 0]
    assert test.cmds == [
        {"cmd": "set", "x": "a", "y": 1},
        {"cmd": "add", "x": "a", "y": 2},
        {"cmd": "mul", "x": "a", "y": "a"},
        {"cmd": "mod", "x": "a", "y": 5},
        {"cmd": "snd", "x": "a"},
        {"cmd": "set", "x": "a", "y": 0},
        {"cmd": "rcv", "x": "a"},
        {"cmd": "jgz", "x": "a", "y": -1},
        {"cmd": "set", "x": "a", "y": 1},
        {"cmd": "jgz", "x": "a", "y": -2},
    ]
    assert test.regs == [{"a": 0}, {"a": 0}]
    assert test.transit == [[], []]


def test_send_example_01():
    test = Duo("./data/example_01.txt")
    test.snd(4)
    assert test.transit[0] == [4]
    assert test.idx[0] == 1


def test_send_example_02():
    test = Duo("./data/example_01.txt")
    test.snd("a")
    assert test.transit[0] == [0]
    assert test.idx[0] == 1


def test_set_example_01():
    test = Duo("./data/example_01.txt")
    test.set_val("a", 4)
    assert test.regs[0] == {"a": 4}
    assert test.idx[0] == 1


def test_set_example_02():
    test = Duo("./data/example_01.txt")
    test.regs[0] == {"a": 4, "b": -1}
    test.set_val("b", 4)
    assert test.regs[0]["b"] == 4
    assert test.idx[0] == 1


def test_set_example_03():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 2, "b": 0}
    test.set_val("b", "a")
    assert test.regs[0]["b"] == 2
    assert test.idx[0] == 1


def test_add_example_01():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 2, "b": 3}
    test.add("a", "b")
    assert test.regs[0]["a"] == 5
    assert test.idx[0] == 1


def test_add_example_02():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 2, "b": 3}
    test.add("b", "a")
    assert test.regs[0]["b"] == 5
    assert test.idx[0] == 1


def test_add_example_03():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 2, "b": 3}
    test.add("b", 7)
    assert test.regs[0]["b"] == 10
    assert test.idx[0] == 1


def test_mul_example_01():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 2, "b": 3}
    test.mul("a", "b")
    assert test.regs[0] == {"a": 6, "b": 3}
    assert test.idx[0] == 1


def test_mul_example_02():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 2, "b": 3}
    test.mul("b", 7)
    assert test.regs[0] == {"a": 2, "b": 21}
    assert test.idx[0] == 1


def test_mod_example_01():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 200, "b": 35}
    test.mod("b", 7)
    assert test.regs[0] == {"a": 200, "b": 0}
    assert test.idx[0] == 1


def test_mod_example_02():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 200, "b": 35}
    test.mod("a", "b")
    assert test.regs[0] == {"a": 25, "b": 35}
    assert test.idx[0] == 1


def test_rcv_example_01():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35}
    test.transit[0] = [11]
    test.rcv("a")
    assert test.transit[1] == []
    assert test.idx[0] == 1


def test_rcv_example_02():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35}
    test.transit[0] = [112]
    test.rcv(0)
    assert test.transit[1] == []
    assert test.idx[0] == 1


def test_rcv_example_03():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35}
    test.transit[0] = [-7]
    test.rcv("b")
    assert test.transit[1] == [-7]
    assert test.idx[0] == 1


def test_rcv_example_04():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35}
    test.transit[0] = [172]
    test.rcv(3)
    assert test.transit[1] == [172]
    assert test.idx[0] == 1


def test_jgz_example_01():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35, "c": -1}
    test.jgz("a", 4)
    assert test.idx[0] == 1


def test_jgz_example_02():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35, "c": -1}
    test.jgz("b", 4)
    assert test.idx[0] == 4


def test_jgz_example_03():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35, "c": -1}
    test.jgz("c", 4)
    assert test.idx[0] == 1


def test_jgz_example_04():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35, "c": -1}
    test.jgz(0, 4)
    assert test.idx[0] == 1


def test_jgz_example_05():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35, "c": -1}
    test.jgz(12, 4)
    assert test.idx[0] == 4


def test_jgz_example_06():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 0, "b": 35, "c": -1}
    test.jgz(-3, 4)
    assert test.idx[0] == 1


def test_execute_cmd_exp01():
    test = Duo("./data/example_01.txt")
    test.execute_cmd({"cmd": "set", "x": "a", "y": 1})
    assert test.regs[0] == {"a": 1}


def test_execute_cmd_exp02():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 1}
    test.execute_cmd({"cmd": "add", "x": "a", "y": 2})
    assert test.regs[0] == {"a": 3}


def test_execute_cmd_exp03():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 3}
    test.execute_cmd({"cmd": "mul", "x": "a", "y": "a"})
    assert test.regs[0] == {"a": 9}


def test_execute_cmd_exp04():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 9}
    test.execute_cmd({"cmd": "mod", "x": "a", "y": 5})
    assert test.regs[0] == {"a": 4}


def test_execute_cmd_exp05():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 4}
    test.execute_cmd({"cmd": "snd", "x": "a"})
    assert test.regs[0] == {"a": 4}
    assert test.transit[0] == [4]


def test_execute_cmd_exp06():
    test = Duo("./data/example_01.txt")
    test.regs[0] = {"a": 4}
    test.execute_cmd(
        {"cmd": "jgz", "x": "a", "y": -2},
    )
    assert test.idx[0] == -2


def test_first_rcv_execution_exp01():
    assert Duo("./data/example_01.txt").first_rcv_execution() == 4


def count_sent_values_exp01():
    assert Duo("./data/example_02.txt", True).sent_values(0) == 3


def count_sent_values_exp02():
    assert Duo("./data/example_02.txt", True).sent_values(1) == 3
