"""
Tests for the main script
"""

from main import SecuritySystem


def test_data_ingestion_exp1():
    assert SecuritySystem("./data/example_01.txt").all_passphrases == [
        "aa bb cc dd ee",
        "aa bb cc dd aa",
        "aa bb cc dd aaa",
    ]


def test_data_ingestion_exp2():
    assert SecuritySystem("./data/example_02.txt").all_passphrases == [
        "abcde fghij",
        "abcde xyz ecdab",
        "a ab abc abd abf abj",
        "iiii oiii ooii oooi oooo",
        "oiii ioii iioi iiio",
    ]


def test_dupe_valid_phrase_exp1():
    assert (
        SecuritySystem("./data/example_01.txt").valid_phrase("aa bb cc dd ee") == True
    )


def test_dupe_valid_phrase_exp2():
    assert (
        SecuritySystem("./data/example_01.txt").valid_phrase("aa bb cc dd aa") == False
    )


def test_dupe_valid_phrase_exp3():
    assert (
        SecuritySystem("./data/example_01.txt").valid_phrase("aa bb cc dd aaa") == True
    )


def test_dupe_valid_phrase_exp4():
    assert (
        SecuritySystem("./data/example_02.txt").valid_phrase("abcde fghij", True)
        == True
    )


def test_dupe_valid_phrase_exp5():
    assert (
        SecuritySystem("./data/example_02.txt").valid_phrase("abcde xyz ecdab", True)
        == False
    )


def test_dupe_valid_phrase_exp6():
    assert (
        SecuritySystem("./data/example_02.txt").valid_phrase(
            "a ab abc abd abf abj", True
        )
        == True
    )


def test_dupe_valid_phrase_exp7():
    assert (
        SecuritySystem("./data/example_02.txt").valid_phrase(
            "iiii oiii ooii oooi oooo", True
        )
        == True
    )


def test_dupe_valid_phrase_exp8():
    assert (
        SecuritySystem("./data/example_02.txt").valid_phrase(
            "oiii ioii iioi iiio", True
        )
        == False
    )


def test_count_valid_passphrases_exp1():
    assert SecuritySystem("./data/example_01.txt").count_valid_passphrases() == 2
