"""
Tests for the main script
"""

from main import TrapRoom


def test_parse_data():
    assert TrapRoom("./data/example_01.txt").tiles == ["..^^."]
    assert TrapRoom("./data/example_02.txt").tiles == [".^^.^.^^^^"]


def test_row_generation_exp1():
    test = TrapRoom("./data/example_01.txt")

    test.gen_next_row(1)
    assert test.tiles[-1] == ".^^^^"

    test.gen_next_row(1)
    assert test.tiles[-1] == "^^..^"


def test_row_generation_exp2():
    test = TrapRoom("./data/example_02.txt")
    test.gen_next_row(9)
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
    assert test.count_safe_tiles() == 38
