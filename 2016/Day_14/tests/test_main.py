"""
Tests for the main script
"""

from main import KeyGenerator


def test_hash_generator():
    test = KeyGenerator("abc")

    test.index = 18
    assert "cc38887a5" in test.salted_hash()

    test.index = 39
    assert "eee" in test.salted_hash()

    test.index = 816
    assert "eeeee" in test.salted_hash()

    test.index = 92
    assert "999" in test.salted_hash()

    test.index = 200
    assert "99999" in test.salted_hash()


def test_key_scanner():
    test = KeyGenerator("abc")
    assert test.scan_for_keys(64) == 22728


def test_key_finder():
    test = KeyGenerator("abc")
    _ = test.scan_for_keys(64)

    assert 18 not in test.key_idxs
    assert 39 in test.key_idxs
    assert 92 in test.key_idxs
    assert 22728 in test.key_idxs
