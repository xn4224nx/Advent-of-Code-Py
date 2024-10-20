"""
Tests for the main script
"""

from main import SecurityScreen


def test_read_instructions():
    test_scrn = SecurityScreen((7, 3))
    test_scrn.read_instru("./data/example_01.txt")
    assert test_scrn.instructs == [
        "rect 3x2",
        "rotate column x=1 by 1",
        "rotate row y=0 by 4",
        "rotate column x=1 by 1",
    ]


def test_indvid_instructions():
    test_scrn = SecurityScreen((7, 3))
    assert test_scrn.show_screen() == (".......\n" ".......\n" ".......\n")

    test_scrn.turn_on_rect(3, 2)
    assert test_scrn.show_screen() == ("###....\n" "###....\n" ".......\n")

    test_scrn.rotate_col(1, 1)
    assert test_scrn.show_screen() == ("#.#....\n" "###....\n" ".#.....\n")

    test_scrn.rotate_row(0, 4)
    assert test_scrn.show_screen() == ("....#.#\n" "###....\n" ".#.....\n")

    test_scrn.rotate_col(1, 1)
    assert test_scrn.show_screen() == (".#..#.#\n" "#.#....\n" ".#.....\n")


def test_str_instrc_execution():
    test_scrn = SecurityScreen((7, 3))
    assert test_scrn.show_screen() == (".......\n" ".......\n" ".......\n")

    test_scrn.execute_instr("rect 3x2")
    assert test_scrn.show_screen() == ("###....\n" "###....\n" ".......\n")

    test_scrn.execute_instr("rotate column x=1 by 1")
    assert test_scrn.show_screen() == ("#.#....\n" "###....\n" ".#.....\n")

    test_scrn.execute_instr("rotate row y=0 by 4")
    assert test_scrn.show_screen() == ("....#.#\n" "###....\n" ".#.....\n")

    test_scrn.execute_instr("rotate column x=1 by 1")
    assert test_scrn.show_screen() == (".#..#.#\n" "#.#....\n" ".#.....\n")


def test_execute_all_instructions():
    test_scrn = SecurityScreen((7, 3))
    test_scrn.read_instru("./data/example_01.txt")
    test_scrn.execute_all_instr()
    assert test_scrn.show_screen() == (".#..#.#\n" "#.#....\n" ".#.....\n")


def test_count_all_on_pixels():
    test_scrn = SecurityScreen((7, 3))
    assert test_scrn.count_on_pixels() == 0

    test_scrn.execute_instr("rect 3x2")
    assert test_scrn.count_on_pixels() == 6

    test_scrn.execute_instr("rotate column x=1 by 1")
    assert test_scrn.count_on_pixels() == 6

    test_scrn.execute_instr("rotate row y=0 by 4")
    assert test_scrn.count_on_pixels() == 6

    test_scrn.execute_instr("rotate column x=1 by 1")
    assert test_scrn.count_on_pixels() == 6
