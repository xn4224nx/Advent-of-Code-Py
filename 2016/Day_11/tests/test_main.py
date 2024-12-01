"""
Tests for the main script
"""

from main import RTGMover


def test_class_initialisation():
    test_build = RTGMover("./data/example_01.txt")

    assert test_build.data_file == "./data/example_01.txt"
    assert test_build.state == {"E": 0, "HG": 1, "HM": 0, "LG": 2, "LM": 0}
    assert test_build.max_floor == 3


def test_valid_moves_0():
    test_build = RTGMover("")
    test_build.max_floor = 3
    test_build.state = {"E": 0, "HG": 0, "HM": 0, "LG": 0, "LM": 0}

    assert set(test_build.determine_valid_moves()) == set(
        [
            {"E": 1, "HG": 0, "HM": 1, "LG": 0, "LM": 0},
            {"E": 1, "HG": 0, "HM": 0, "LG": 0, "LM": 1},
            {"E": 1, "HG": 0, "HM": 1, "LG": 0, "LM": 1},
            {"E": 1, "HG": 1, "HM": 0, "LG": 1, "LM": 0},
            {"E": 1, "HG": 1, "HM": 1, "LG": 0, "LM": 0},
            {"E": 1, "HG": 0, "HM": 0, "LG": 1, "LM": 1},
        ]
    )


def test_valid_moves_1():
    test_build = RTGMover("")
    test_build.max_floor = 3
    test_build.state = {"E": 1, "HG": 1, "HM": 1, "LG": 1, "LM": 1}

    assert set(test_build.determine_valid_moves()) == set(
        [
            {"E": 2, "HG": 1, "HM": 2, "LG": 1, "LM": 1},
            {"E": 2, "HG": 1, "HM": 1, "LG": 1, "LM": 2},
            {"E": 2, "HG": 1, "HM": 2, "LG": 1, "LM": 2},
            {"E": 2, "HG": 2, "HM": 1, "LG": 2, "LM": 1},
            {"E": 2, "HG": 2, "HM": 2, "LG": 1, "LM": 1},
            {"E": 2, "HG": 1, "HM": 1, "LG": 2, "LM": 2},
            {"E": 0, "HG": 1, "HM": 0, "LG": 1, "LM": 1},
            {"E": 0, "HG": 1, "HM": 1, "LG": 1, "LM": 0},
            {"E": 0, "HG": 1, "HM": 0, "LG": 1, "LM": 0},
            {"E": 0, "HG": 0, "HM": 1, "LG": 0, "LM": 1},
            {"E": 0, "HG": 0, "HM": 0, "LG": 1, "LM": 1},
            {"E": 0, "HG": 1, "HM": 1, "LG": 0, "LM": 0},
        ]
    )


def test_is_state_valid_0():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 0, "HG": 1, "HM": 0, "LG": 2, "LM": 0}) == True
    )


def test_is_state_valid_1():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 1, "HG": 1, "HM": 1, "LG": 2, "LM": 0}) == True
    )


def test_is_state_valid_2():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 2, "HG": 2, "HM": 2, "LG": 2, "LM": 0}) == True
    )


def test_is_state_valid_3():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 1, "HG": 2, "HM": 1, "LG": 2, "LM": 0}) == True
    )


def test_is_state_valid_4():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 0, "HG": 2, "HM": 0, "LG": 2, "LM": 0}) == True
    )


def test_is_state_valid_5():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 0, "HG": 2, "HM": 0, "LG": 2, "LM": 0}) == True
    )


def test_is_state_valid_6():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 2, "HG": 2, "HM": 2, "LG": 2, "LM": 2}) == True
    )


def test_is_state_valid_7():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 3, "HG": 2, "HM": 3, "LG": 2, "LM": 3}) == True
    )


def test_is_state_valid_8():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 2, "HG": 2, "HM": 2, "LG": 2, "LM": 3}) == True
    )


def test_is_state_valid_9():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 3, "HG": 3, "HM": 2, "LG": 3, "LM": 3}) == True
    )


def test_is_state_valid_10():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 2, "HG": 3, "HM": 2, "LG": 3, "LM": 2}) == True
    )


def test_is_state_valid_11():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 3, "HG": 3, "HM": 3, "LG": 3, "LM": 3}) == True
    )


def test_is_state_valid_12():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 0, "HG": 1, "HM": 0, "LG": 0, "LM": 1}) == False
    )


def test_is_state_valid_13():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 0, "HG": 0, "HM": 3, "LG": 3, "LM": 0}) == False
    )


def test_is_state_valid_13():
    test_build = RTGMover("")
    assert (
        test_build.is_state_valid({"E": 0, "HG": 1, "HM": 3, "LG": 3, "LM": 2}) == False
    )


def test_solver():
    test_build = RTGMover("./data/example_01.txt")
    assert test_build.solve() == 11


def test_show_0():
    test_build = RTGMover("")
    test_build.state = {"E": 0, "HG": 1, "HM": 0, "LG": 2, "LM": 0}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  .  .  LG .  \n"
        "F2 .  HG .  .  .  \n"
        "F1 E  .  HM .  LM \n"
    )


def test_show_1():
    test_build = RTGMover("")
    test_build.state = {"E": 1, "HG": 1, "HM": 1, "LG": 2, "LM": 0}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  .  .  LG .  \n"
        "F2 E  HG HM .  .  \n"
        "F1 .  .  .  .  LM \n"
    )


def test_show_2():
    test_build = RTGMover("")
    test_build.state = {"E": 2, "HG": 2, "HM": 2, "LG": 2, "LM": 0}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 E  HG HM LG .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  LM \n"
    )


def test_show_3():
    test_build = RTGMover("")
    test_build.state = {"E": 1, "HG": 2, "HM": 1, "LG": 2, "LM": 0}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  HG .  LG .  \n"
        "F2 E  .  HM .  .  \n"
        "F1 .  .  .  .  LM \n"
    )


def test_show_4():
    test_build = RTGMover("")
    test_build.state = {"E": 0, "HG": 2, "HM": 0, "LG": 2, "LM": 0}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  HG .  LG .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 E  .  HM .  LM \n"
    )


def test_show_5():
    test_build = RTGMover("")
    test_build.state = {"E": 1, "HG": 2, "HM": 1, "LG": 2, "LM": 1}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  HG .  LG .  \n"
        "F2 E  .  HM .  LM \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_6():
    test_build = RTGMover("")
    test_build.state = {"E": 2, "HG": 2, "HM": 2, "LG": 2, "LM": 2}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 E  HG HM LG LM \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_7():
    test_build = RTGMover("")
    test_build.state = {"E": 3, "HG": 2, "HM": 3, "LG": 2, "LM": 3}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 E  .  HM .  LM \n"
        "F3 .  HG .  LG .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_8():
    test_build = RTGMover("")
    test_build.state = {"E": 2, "HG": 2, "HM": 2, "LG": 2, "LM": 3}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  .  .  .  LM \n"
        "F3 E  HG HM LG .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_9():
    test_build = RTGMover("")
    test_build.state = {"E": 3, "HG": 3, "HM": 2, "LG": 3, "LM": 3}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 E  HG .  LG LM \n"
        "F3 .  .  HM .  .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_10():
    test_build = RTGMover("")
    test_build.state = {"E": 2, "HG": 3, "HM": 2, "LG": 3, "LM": 2}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 .  HG .  LG .  \n"
        "F3 E  .  HM .  LM \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_11():
    test_build = RTGMover("")
    test_build.state = {"E": 3, "HG": 3, "HM": 3, "LG": 3, "LM": 3}
    test_build.max_floor = 3

    assert test_build.show() == (
        "F4 E  HG HM LG LM \n"
        "F3 .  .  .  .  .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )
