"""
Tests for the main script
"""

from main import find_final_elf, find_final_elf_half


def test_find_final_elf_exp1():
    assert find_final_elf(5) == 3


def test_find_final_elf_exp2():
    assert find_final_elf_half(5) == 2
