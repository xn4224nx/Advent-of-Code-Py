"""
Tests for the main script
"""

from main import SecuritySystem


def test_data_ingestion():
    assert SecuritySystem("./data/example_01.txt").all_passphrases == [
        "aa bb cc dd ee",
        "aa bb cc dd aa",
        "aa bb cc dd aaa",
    ]


def test_dupe_valid_phrase_exp1():
    assert (
        SecuritySystem("./data/example_01.txt").valid_phrase_dupe("aa bb cc dd ee")
        == True
    )


def test_dupe_valid_phrase_exp1():
    assert (
        SecuritySystem("./data/example_01.txt").valid_phrase_dupe("aa bb cc dd aa")
        == False
    )


def test_dupe_valid_phrase_exp1():
    assert (
        SecuritySystem("./data/example_01.txt").valid_phrase_dupe("aa bb cc dd aaa")
        == True
    )


def test_count_valid_passphrases_exp1():
    assert SecuritySystem("./data/example_01.txt").count_valid_passphrases() == 2
