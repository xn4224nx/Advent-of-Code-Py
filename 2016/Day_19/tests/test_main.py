"""
Tests for the main script
"""

from main import find_final_elf


def test_find_final_elf_exp1():
    assert find_final_elf(5) == 3
