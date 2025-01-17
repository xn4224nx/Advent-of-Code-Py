"""
Tests for the main script
"""

from main import Computer


def test_computer_initialisation():
    test = Computer("./data/example_01.txt", 0)
    assert test.register == {"a": 0, "b": 0, "c": 0, "d": 0}
    assert test.insruc == [
        "cpy 2 a",
        "tgl a",
        "tgl a",
        "tgl a",
        "cpy 1 a",
        "dec a",
        "dec a",
    ]
    assert test.inverted == [False, False, False, False, False, False, False]
    assert test.curr_cmd == 0


def test_extract_var():
    test = Computer("./data/example_01.txt", 1)
    assert test.register == {"a": 1, "b": -3, "c": 5, "d": 6}
    assert test.extract_var("-7") == -7
    assert test.extract_var("a") == 1
    assert test.extract_var("b") == -3
    assert test.extract_var("90") == 90
    assert test.extract_var("9") == 9


def test_cpy_cmd():
    test = Computer("./data/example_01.txt", 0)
    test.cpy("4", "a")
    test.cpy("a", "b")
    test.cpy("-9", "c")
    assert test.register == {"a": 4, "b": 4, "c": -9, "d": 0}
    assert test.curr_cmd == 3

    test.cpy("4", "a", True)
    test.cpy("a", "b", True)
    test.cpy("c", "-9", False)
    assert test.register == {"a": 4, "b": 4, "c": -9, "d": 0}
    assert test.curr_cmd == 8


def test_inc_cmd():
    test = Computer("./data/example_01.txt", 0)
    test.inc("a")
    test.inc("a")
    test.inc("b")
    test.inc("c")
    test.inc("d")
    assert test.register == {"a": 2, "b": 1, "c": 1, "d": 1}
    assert test.curr_cmd == 5

    test.inc("a", True)
    test.inc("d", True)
    test.inc("b", True)
    test.inc("b", True)
    test.inc("d", True)
    assert test.register == {"a": 1, "b": -1, "c": 1, "d": -1}
    assert test.curr_cmd == 10


def test_dec_cmd():
    test = Computer("./data/example_01.txt", 4)
    test.dec("a")
    test.dec("a")
    test.dec("d")
    assert test.register == {"a": 2, "b": 0, "c": 0, "d": -1}
    assert test.curr_cmd == 3

    test.dec("b", True)
    test.dec("c", True)
    test.dec("d", True)
    test.dec("d", True)
    assert test.register == {"a": 2, "b": 1, "c": 1, "d": 1}
    assert test.curr_cmd == 7


def test_jnz_cmd():
    test = Computer("./data/example_01.txt", 0)
    test.register = {"a": -2, "b": 10, "c": 0, "d": 7}

    test.jnz("-1", "3")
    assert test.curr_cmd == 3

    test.jnz("c", "3")
    assert test.curr_cmd == 4

    test.jnz("0", "3")
    assert test.curr_cmd == 5

    test.jnz("14", "3")
    assert test.curr_cmd == 8


def test_tgl_cmd():
    test = Computer("./data/example_01.txt", 0)
    test.register["d"] = 4

    test.tgl("0")
    assert test.insr_invert[0] == True

    test.tgl("d")
    assert test.insr_invert[5] == True

    test.tgl("-1")
    assert test.insr_invert[1] == True

    test.tgl("1000")
    assert test.insr_invert == [True, True, False, False, False, False, False]
    assert test.curr_cmd == 4

    test.tgl("1", True)
    test.tgl("b", True)
    test.tgl("c", True)
    test.register = {"a": 0, "b": 1, "c": 1, "d": 0}
    assert test.curr_cmd == 8


def test_parse_instruc():
    test = Computer("./data/example_01.txt", 0)
    test.insruc = [
        "cpy 41 a",
        "cpy a c",
        "cpy -89 d",
        "inc b",
        "dec b",
        "jnz a 2",
        "dec d",
        "dec d",
        "dec d",
        "dec d",
        "inc c",
        "tgl a",
    ]

    test.parse_instruc(0)
    assert test.curr_cmd == 1
    assert test.test.register["a"] == 41

    test.parse_instruc(3)
    assert test.curr_cmd == 2
    assert test.test.register["b"] == 1

    test.parse_instruc(4)
    assert test.curr_cmd == 3
    assert test.test.register["b"] == 0

    test.parse_instruc(5)
    assert test.curr_cmd == 5

    test.parse_instruc(11)
    assert test.insr_invert[0] == True
    assert test.curr_cmd == 6


def test_final_register_val():
    assert Computer("./data/example_01.txt", 0).final_register_val("a") == 3
