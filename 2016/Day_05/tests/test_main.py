"""
Tests for the main script
"""

from main import hash_door_index, find_password, find_positional_password


def test_hash_door_index_1():
    assert hash_door_index("abc", 3231929)[:5] == "00000"


def test_next_pass_char_1():
    assert hash_door_index("abc", 3231929)[5] == "1"


def test_hash_door_index_2():
    assert hash_door_index("abc", 5017308)[:5] == "00000"


def test_next_pass_char_2():
    assert hash_door_index("abc", 5017308)[5] == "8"


def test_hash_door_index_3():
    assert hash_door_index("abc", 5278568)[:5] == "00000"


def test_next_pass_char_3():
    assert hash_door_index("abc", 5278568)[5] == "f"


def test_find_password_1():
    assert find_password("abc") == "18f47a30"


def test_find_password_2():
    assert find_positional_password("abc") == "05ace8e3"
