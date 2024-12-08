"""
Tests for the main script
"""

from main import Computer


def test_computer_initialisation():
    test = Computer("./data/example_01.txt")
    assert test.register == {"a": 0, "b": 0, "c": 0, "d": 0}
    assert test.curr_instruc == 0
    assert test.datafile == "./data/example_01.txt"
    assert test.instruc == ["cpy 41 a", "inc a", "inc a", "dec a", "jnz a 2", "dec a"]


def test_copy_command():
    test = Computer("./data/example_01.txt")

    test.copy(42, "a")
    assert test.register["a"] == 42

    test.copy("a", "b")
    assert test.register["b"] == 42

    test.execute_command("cpy -79 c")
    assert test.register["c"] == -79

    test.execute_command("cpy c d")
    assert test.register["d"] == -79


def test_increase_command():
    test = Computer("./data/example_01.txt")

    test.incr("a")
    test.incr("a")
    test.incr("a")
    assert test.register["a"] == 3

    test.execute_command("inc d")
    test.execute_command("inc d")
    test.execute_command("inc a")
    assert test.register["a"] == 4
    assert test.register["d"] == 2


def test_decrease_command():
    test = Computer("./data/example_01.txt")

    test.decr("a")
    test.decr("b")
    test.decr("c")
    test.decr("d")
    assert test.register == {"a": -1, "b": -1, "c": -1, "d": -1}

    test.execute_command("dec d")
    test.execute_command("dec d")
    assert test.register["d"] == -3


def test_jump_command():
    test = Computer("./data/example_01.txt")
    test.curr_instruc = 5

    test.zero_jump("a", 3)
    assert test.curr_instruc == 5

    test.execute_command("jnz b 3")
    assert test.curr_instruc == 5

    test.register["d"] = 1
    test.zero_jump("d", -3)
    assert test.curr_instruc == 2

    test.execute_command("jnz d 30")
    assert test.curr_instruc == 32


def test_example_01():
    test = Computer("./data/example_01.txt")
    test.exe_all_commands()
    assert test.register == {"a": 42, "b": 0, "c": 0, "d": 0}
