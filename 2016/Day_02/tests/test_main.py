"""
Tests for the main script
"""

from main import SecSystem


def test_read_data():
    test = SecSystem(None, None)
    test.read_bathrm_codes("./data/example_01")
    test.codes == "ULLRRDDDLURDLUUUUD"


def test_valid_moves():
    test = SecSystem([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], (1, 1))

    test.execute_instr("U")
    assert test.curr_loc == (0, 1)

    test.execute_instr("L")
    assert test.curr_loc == (0, 0)

    test.execute_instr("R")
    assert test.curr_loc == (0, 1)

    test.execute_instr("D")
    test.execute_instr("D")
    assert test.curr_loc == (2, 1)


def test_invalid_moves():
    test = SecSystem([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], (0, 0))

    test.execute_instr("U")
    assert test.curr_loc == (0, 0)

    test.execute_instr("L")
    test.execute_instr("L")
    assert test.curr_loc == (0, 0)

    test.execute_instr("D")
    test.execute_instr("D")
    test.execute_instr("D")
    test.execute_instr("D")
    test.execute_instr("D")
    assert test.curr_loc == (2, 0)

    test.execute_instr("R")
    test.execute_instr("R")
    test.execute_instr("R")
    assert test.curr_loc == (2, 2)


def test_find_buttons_pressed():
    test = SecSystem([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]], (1, 1))
    test.read_bathrm_codes("./data/example_01")
    assert test.find_buttons_pressed() == "1985"
