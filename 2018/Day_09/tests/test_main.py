"""
Tests for the main script
"""

from main import MarbleGame


def test_high_score_exp01():
    assert MarbleGame(players=10, last_marble_worth=1618).high_score() == 8317


def test_high_score_exp02():
    assert MarbleGame(players=13, last_marble_worth=7999).high_score() == 146373


def test_high_score_exp03():
    assert MarbleGame(players=17, last_marble_worth=1104).high_score() == 2764


def test_high_score_exp04():
    assert MarbleGame(players=21, last_marble_worth=6111).high_score() == 54718


def test_high_score_exp05():
    assert MarbleGame(players=30, last_marble_worth=5807).high_score() == 37305
