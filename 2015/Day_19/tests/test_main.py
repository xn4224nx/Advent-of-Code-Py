"""
Tests for functions in the main script.
"""

import main


def test_read_machine_data_exp1():
    instr, chem = main.read_machine_data("./data/example_01.txt")
    assert chem == "HOH"
    assert instr == [("H", "HO"), ("H", "OH"), ("O", "HH")]


def test_find_all_possible_chems_exp1():
    instr, chem = main.read_machine_data("./data/example_01.txt")
    assert main.find_all_possible_chems(instr, chem) == 4


def test_find_all_possible_chems_exp2():
    instr, _ = main.read_machine_data("./data/example_01.txt")
    assert main.find_all_possible_chems(instr, "HOHOHO") == 7


def test_find_one_instr_molec_exp1():
    pos_molcs = main.find_one_instr_molec(("H", "HO"), "HOH")
    assert len(pos_molcs) == 2
    assert set(pos_molcs) == set(["HOOH", "HOHO"])


def test_find_one_instr_molec_exp2():
    pos_molcs = main.find_one_instr_molec(("H", "OH"), "HOH")
    assert len(pos_molcs) == 2
    assert set(pos_molcs) == set(["HOOH", "OHOH"])


def test_find_one_instr_molec_exp3():
    pos_molcs = main.find_one_instr_molec(("O", "HH"), "HOH")
    assert len(pos_molcs) == 1
    assert set(pos_molcs) == set(["HHHH"])
