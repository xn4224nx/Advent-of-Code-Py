"""
Tests for the Circuit class.
"""

import main


def test_example_01():

    test = main.Circuit("./data/example_01.txt")
    test.execute_instructions()

    assert test.wire_sig == {
        "d": 72,
        "e": 507,
        "f": 492,
        "g": 114,
        "h": 65412,
        "i": 65079,
        "x": 123,
        "y": 456,
    }
