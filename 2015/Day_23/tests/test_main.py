"""
Tests for functions in the main script.
"""

from main import Register


def test_read_instr_example_01():
    test = Register()
    test.read_instr("./data/example.01.txt")
    assert test.instr == [
        "inc a",
        "jio a, +2",
        "tpl a",
        "inc a",
    ]


def test_read_instr_input():
    test = Register()
    test.read_instr("./data/example.01.txt")
    assert test.instr == [
        "jio a, +18",
        "inc a",
        "tpl a",
        "inc a",
        "tpl a",
        "tpl a",
        "tpl a",
        "inc a",
        "tpl a",
        "inc a",
        "tpl a",
        "inc a",
        "inc a",
        "tpl a",
        "tpl a",
        "tpl a",
        "inc a",
        "jmp +22",
        "tpl a",
        "inc a",
        "tpl a",
        "inc a",
        "inc a",
        "tpl a",
        "inc a",
        "tpl a",
        "inc a",
        "inc a",
        "tpl a",
        "tpl a",
        "inc a",
        "inc a",
        "tpl a",
        "inc a",
        "inc a",
        "tpl a",
        "inc a",
        "inc a",
        "tpl a",
        "jio a, +8",
        "inc b",
        "jie a, +4",
        "tpl a",
        "inc a",
        "jmp +2",
        "hlf a",
        "jmp -7",
    ]


def test_halve_register_a():
    test = Register()
    test.a = 9
    test.execute_instr("hlf a")
    assert test.a == 4


def test_halve_register_b():
    test = Register()
    test.b = 1
    test.execute_instr("hlf b")
    assert test.b == 0


def test_triple_register_a():
    test = Register()
    test.a = 3
    test.execute_instr("tpl a")

    assert test.a == 9


def test_triple_register_b():
    test = Register()
    test.b = 4
    test.execute_instr("tpl b")
    assert test.b == 12


def test_incr_register_a():
    test = Register()
    test.execute_instr("inc a")
    test.execute_instr("inc a")
    test.execute_instr("inc a")
    assert test.a == 3


def test_incr_register_b():
    test = Register()
    test.execute_instr("inc b")
    test.execute_instr("inc b")
    test.execute_instr("inc b")
    test.execute_instr("inc b")
    assert test.b == 4


def test_pos_jump():
    test = Register()
    test.execute_instr("jmp +2")
    assert test.instr_idx == 2


def test_neg_jump():
    test = Register()
    test.instr_idx = 9
    test.execute_instr("jmp -5")
    assert test.instr_idx == 4


def test_even_jump_01():
    test = Register()
    test.a = 100
    test.execute_instr("jie a, +4")
    assert test.instr_idx == 4


def test_even_jump_02():
    test = Register()
    test.a = 101
    test.instr_idx = 1
    test.execute_instr("jie a, +4")
    assert test.instr_idx == 1


def test_odd_jump_01():
    test = Register()
    test.b = 7
    test.execute_instr("jio b, +20")
    assert test.instr_idx == 20


def test_odd_jump_02():
    test = Register()
    test.b = 2
    test.instr_idx = 10
    test.execute_instr("jio b, +20")
    assert test.instr_idx == 10


def test_a_register_example():
    test = Register()
    test.read_instr("./data/example_01.txt")
    test.run_all_instr()
    assert test.a == 2
