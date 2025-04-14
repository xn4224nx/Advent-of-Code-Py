"""
Tests for the main script and the KnotHash class.
"""

from knothash import KnotHash
from main import DiskDefrag


def test_knothash_exp01():
    assert KnotHash("").calc_digest() == "a2582a3a0e66e6e86e3812dcb672a272"


def test_knothash_exp02():
    assert KnotHash("AoC 2017").calc_digest() == "33efeb34ea91902bb2f59c9920caa6cd"


def test_knothash_exp03():
    assert KnotHash("1,2,3").calc_digest() == "3efbe78a8d82f29979031a4aa0b16a9d"


def test_knothash_exp04():
    assert KnotHash("1,2,4").calc_digest() == "63960835bcdc130f0b66d7ff4f6a5a8e"


def test_knothash_exp05():
    assert (
        KnotHash("147,37,249,1,31,2,226,0,161,71,254,243,183,255,30,70").calc_digest()
        == "70b856a24d586194331398c7fcfa0aaf"
    )


def test_defrag_init_exp01():
    test = DiskDefrag("flqrgnkx")
    assert test.seed == "flqrgnkx"
    assert test.rows[0][:8] == [1, 1, 0, 1, 0, 1, 0, 0]
    assert test.rows[1][:8] == [0, 1, 0, 1, 0, 1, 0, 1]
    assert test.rows[2][:8] == [0, 0, 0, 0, 1, 0, 1, 0]
    assert test.rows[3][:8] == [1, 0, 1, 0, 1, 1, 0, 1]
    assert test.rows[4][:8] == [0, 1, 1, 0, 1, 0, 0, 0]
    assert test.rows[5][:8] == [1, 1, 0, 0, 1, 0, 0, 1]
    assert test.rows[6][:8] == [0, 1, 0, 0, 0, 1, 0, 0]
    assert test.rows[7][:8] == [1, 1, 0, 1, 0, 1, 1, 0]


def test_num_used_sqrs_exp01():
    assert DiskDefrag("flqrgnkx").num_used_sqrs() == 8108
