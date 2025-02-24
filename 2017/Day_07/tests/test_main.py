"""
Tests for the main script
"""

from main import ProgramTower


def test_read_data_exp1():
    test = ProgramTower("./data/example_01.txt")
    assert test.disks == {
        "pbga": {"above": [], weight: 66},
        "xhth": {"above": [], weight: 57},
        "ebii": {"above": [], weight: 61},
        "havc": {"above": [], weight: 66},
        "ktlj": {"above": [], weight: 57},
        "fwft": {"above": ["ktlj", "cntj", "xhth"], weight: 72},
        "qoyq": {"above": [], weight: 66},
        "padx": {"above": ["pbga", "havc", "qoyq"], weight: 45},
        "tknk": {"above": ["ugml", "padx", "fwft"], weight: 41},
        "jptl": {"above": [], weight: 61},
        "ugml": {"above": ["gyxo", "ebii", "jptl"], weight: 68},
        "gyxo": {"above": [], weight: 61},
        "cntj": {"above": [], weight: 57},
    }


def test_find_bottom_disk_exp1():
    assert ProgramTower("./data/example_01.txt").bottom_disk() == "tknk"
