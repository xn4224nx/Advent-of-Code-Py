"""
Tests for the main script
"""

from main import (
    reverse_number,
    invert_number,
    dragon_fold,
    checksum,
    disk_fill_checksum,
)


def test_reverse_number():
    assert reverse_number("100") == "001"
    assert reverse_number("100101") == "101001"
    assert reverse_number("111110") == "011111"
    assert reverse_number("10101") == "10101"
    assert reverse_number("10010100") == "00101001"


def test_invert_number():
    assert invert_number("100") == "011"
    assert invert_number("100101") == "011010"
    assert invert_number("111110") == "000001"
    assert invert_number("10101") == "01010"
    assert invert_number("10010100") == "01101011"


def test_dragon_fold():
    assert dragon_fold("1") == "100"
    assert dragon_fold("0") == "001"
    assert dragon_fold("11111") == "11111000000"
    assert dragon_fold("111100001010") == "1111000010100101011110000"


def test_checksum():
    assert checksum("110010110100") == "100"
    assert checksum("10000011110010000111") == "01100"


def test_disk_fill_checksum():
    assert disk_fill_checksum("10000", 20) == "01100"
