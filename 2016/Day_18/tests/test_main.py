"""
Tests for the main script
"""

from main import TrapRoom


def test_parse_data():
    assert TrapRoom("./data/example_01.txt").start_tiles == ["..^^."]
    assert TrapRoom("./data/example_02.txt").start_tiles == [".^^.^.^^^^"]


def test_row_generation_exp1():
    test = TrapRoom("./data/example_01.txt")
    test.gen_total_rows(3)
    assert test.tiles[0] == "..^^."
    assert test.tiles[1] == ".^^^^"
    assert test.tiles[2] == "^^..^"


def test_row_generation_exp2():
    test = TrapRoom("./data/example_02.txt")
    test.gen_total_rows(10)
    assert test.tiles == [
        ".^^.^.^^^^",
        "^^^...^..^",
        "^.^^.^.^^.",
        "..^^...^^^",
        ".^^^^.^^.^",
        "^^..^.^^..",
        "^^^^..^^^.",
        "^..^^^^.^^",
        ".^^^..^.^^",
        "^^.^^^..^^",
    ]


def test_count_safe_tiles():
    test = TrapRoom("./data/example_02.txt")
    test.gen_total_rows(10)
    assert test.count_safe_tiles() == 38
