"""
Tests for the main script
"""

from main import RailNetwork
from collections import deque


def test_rail_network_creation_exp0():
    test = RailNetwork("./data/example_0.txt")
    assert test.minecart_locs == [[0, 2], [3, 9]]
    assert test.nxt_minecart_direct == [0, 0]
    assert test.track == [
        ["/", "-", ">", "-", "\\", " ", " ", " ", " ", " ", " ", " ", " "],
        ["|", " ", " ", " ", "|", " ", " ", "/", "-", "-", "-", "-", "\\"],
        ["|", " ", "/", "-", "+", "-", "-", "+", "-", "\\", " ", " ", "|"],
        ["|", " ", "|", " ", "|", " ", " ", "|", " ", "v", " ", " ", "|"],
        ["\\", "-", "+", "-", "/", " ", " ", "\\", "-", "+", "-", "-", "/"],
        [" ", " ", "\\", "-", "-", "-", "-", "-", "-", "/", " ", " ", " "],
    ]


def test_str_output_exp0():
    assert str(RailNetwork("./data/example_0.txt")) == "\n".join(
        (
            "/->-\\        ",
            "|   |  /----\\",
            "| /-+--+-\\  |",
            "| | |  | v  |",
            "\\-+-/  \\-+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp00():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(1):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/-->\\        ",
            "|   |  /----\\",
            "| /-+--+-\\  |",
            "| | |  | |  |",
            "\\-+-/  \\->--/",
            "  \\------/   ",
        )
    )


def test_tick_exp01():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(2):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---v        ",
            "|   |  /----\\",
            "| /-+--+-\\  |",
            "| | |  | |  |",
            "\\-+-/  \\-+>-/",
            "  \\------/   ",
        )
    )


def test_tick_exp02():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(3):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   v  /----\\",
            "| /-+--+-\\  |",
            "| | |  | |  |",
            "\\-+-/  \\-+->/",
            "  \\------/   ",
        )
    )


def test_tick_exp03():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(4):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /----\\",
            "| /->--+-\\  |",
            "| | |  | |  |",
            "\\-+-/  \\-+--^",
            "  \\------/   ",
        )
    )


def test_tick_exp04():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(5):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /----\\",
            "| /-+>-+-\\  |",
            "| | |  | |  ^",
            "\\-+-/  \\-+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp05():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(6):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /----\\",
            "| /-+->+-\\  ^",
            "| | |  | |  |",
            "\\-+-/  \\-+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp06():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(7):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /----<",
            "| /-+-->-\\  |",
            "| | |  | |  |",
            "\\-+-/  \\-+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp07():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(8):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /---<\\",
            "| /-+--+>\\  |",
            "| | |  | |  |",
            "\\-+-/  \\-+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp08():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(9):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /--<-\\",
            "| /-+--+-v  |",
            "| | |  | |  |",
            "\\-+-/  \\-+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp09():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(10):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /-<--\\",
            "| /-+--+-\\  |",
            "| | |  | v  |",
            "\\-+-/  \\-+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp10():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(11):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /<---\\",
            "| /-+--+-\\  |",
            "| | |  | |  |",
            "\\-+-/  \\-<--/",
            "  \\------/   ",
        )
    )


def test_tick_exp11():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(12):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  v----\\",
            "| /-+--+-\\  |",
            "| | |  | |  |",
            "\\-+-/  \\<+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp12():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(13):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /----\\",
            "| /-+--v-\\  |",
            "| | |  | |  |",
            "\\-+-/  ^-+--/",
            "  \\------/   ",
        )
    )


def test_tick_exp13():
    test = RailNetwork("./data/example_0.txt")

    for _ in range(14):
        test.tick()

    assert str(test) == "\n".join(
        (
            "/---\\        ",
            "|   |  /----\\",
            "| /-+--+-\\  |",
            "| | |  X |  |",
            "\\-+-/  \\-+--/",
            "  \\------/   ",
        )
    )
