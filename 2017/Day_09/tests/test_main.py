"""
Tests for the main script
"""

from main import CharStream


def test_read_file_exp1():
    assert CharStream("./data/example_01.txt").stream == "{}"


def test_read_file_exp2():
    assert CharStream("./data/example_02.txt").stream == "{{{}}}"


def test_read_file_exp3():
    assert CharStream("./data/example_03.txt").stream == "{{},{}}"


def test_read_file_exp4():
    assert CharStream("./data/example_04.txt").stream == "{{{},{},{{}}}}"


def test_read_file_exp5():
    assert CharStream("./data/example_05.txt").stream == "{<a>,<a>,<a>,<a>}"


def test_read_file_exp6():
    assert CharStream("./data/example_06.txt").stream == "{{<ab>},{<ab>},{<ab>},{<ab>}}"


def test_read_file_exp7():
    assert CharStream("./data/example_07.txt").stream == "{{<!!>},{<!!>},{<!!>},{<!!>}}"


def test_read_file_exp8():
    assert CharStream("./data/example_08.txt").stream == "{{<a!>},{<a!>},{<a!>},{<ab>}}"


def test_score_exp1():
    assert CharStream("./data/example_01.txt").score()[0] == 1


def test_score_exp2():
    assert CharStream("./data/example_02.txt").score()[0] == 6


def test_score_exp3():
    assert CharStream("./data/example_03.txt").score()[0] == 5


def test_score_exp4():
    assert CharStream("./data/example_04.txt").score()[0] == 16


def test_score_exp5():
    assert CharStream("./data/example_05.txt").score()[0] == 1


def test_score_exp6():
    assert CharStream("./data/example_06.txt").score()[0] == 9


def test_score_exp7():
    assert CharStream("./data/example_07.txt").score()[0] == 9


def test_score_exp8():
    assert CharStream("./data/example_08.txt").score()[0] == 3


def test_count_garbage_exp1():
    assert CharStream("<>").score()[1] == 0


def test_count_garbage_exp2():
    assert CharStream("<random characters>").score()[1] == 17


def test_count_garbage_exp3():
    assert CharStream("<<<<>").score()[1] == 3


def test_count_garbage_exp4():
    assert CharStream("<{!>}>").score()[1] == 2


def test_count_garbage_exp5():
    assert CharStream("<!!>").score()[1] == 0


def test_count_garbage_exp6():
    assert CharStream("<!!!>>").score()[1] == 0


def test_count_garbage_exp7():
    assert CharStream('<{o"i!a,<{i<a>').score()[1] == 10
