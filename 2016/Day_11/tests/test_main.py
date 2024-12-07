"""
Tests for the main script
"""

from main import RTGMover


def test_class_initialisation():
    test_build = RTGMover("./data/example_01.txt")

    assert test_build.data_file == "./data/example_01.txt"
    assert test_build.state == [0, 1, 2, 0, 0]
    assert test_build.max_floor == 3
    assert test_build.names == ["hydrogen", "lithium"]
    assert test_build.num_ele == 2


def test_valid_moves_0():
    test_build = RTGMover("")
    test_build.max_floor = 3
    test_build.num_ele = 2
    test_states = test_build.determine_valid_moves([0, 0, 0, 0, 0])

    true_states = [
        [1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1],
    ]

    for state in test_states:
        assert state in true_states

    for state in true_states:
        assert state in test_states


def test_valid_moves_1():
    test_build = RTGMover("")
    test_build.max_floor = 3
    test_build.num_ele = 2
    test_states = test_build.determine_valid_moves([1, 1, 1, 1, 1])

    true_states = [
        [2, 1, 1, 1, 2],
        [2, 1, 1, 2, 1],
        [2, 2, 1, 2, 1],
        [2, 1, 2, 1, 2],
        [2, 2, 2, 1, 1],
        [2, 1, 1, 2, 2],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 0, 1],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0],
    ]

    for state in test_states:
        assert state in true_states

    for state in true_states:
        assert state in test_states


def test_is_state_valid_0():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([0, 1, 2, 0, 0]) == True


def test_is_state_valid_1():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([1, 1, 2, 1, 0]) == True


def test_is_state_valid_2():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([2, 2, 2, 2, 0]) == True


def test_is_state_valid_3():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([1, 2, 2, 1, 0]) == True


def test_is_state_valid_4():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([0, 2, 2, 0, 0]) == True


def test_is_state_valid_5():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([0, 0, 0, 2, 2]) == True


def test_is_state_valid_6():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([2, 2, 2, 2, 2]) == True


def test_is_state_valid_7():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([3, 2, 2, 3, 3]) == True


def test_is_state_valid_8():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([2, 2, 2, 2, 3]) == True


def test_is_state_valid_9():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([3, 3, 3, 2, 3]) == True


def test_is_state_valid_10():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([2, 3, 3, 2, 2]) == True


def test_is_state_valid_11():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([3, 3, 3, 3, 3]) == True


def test_is_state_valid_12():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([0, 1, 0, 0, 1]) == False


def test_is_state_valid_13():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([0, 0, 3, 3, 0]) == False


def test_is_state_valid_13():
    test_build = RTGMover("")
    test_build.num_ele = 2
    assert test_build.is_state_valid([0, 1, 3, 3, 2]) == False


def test_solver():
    test_build = RTGMover("./data/example_01.txt")
    assert test_build.solve_bfs() == 11


def test_show_0():
    test_build = RTGMover("")
    test_build.state = [0, 1, 2, 0, 0]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  .  .  LG .  \n"
        "F2 .  HG .  .  .  \n"
        "F1 E  .  HM .  LM \n"
    )


def test_show_1():
    test_build = RTGMover("")
    test_build.state = [1, 1, 2, 1, 0]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  .  .  LG .  \n"
        "F2 E  HG HM .  .  \n"
        "F1 .  .  .  .  LM \n"
    )


def test_show_2():
    test_build = RTGMover("")
    test_build.state = [2, 2, 2, 2, 0]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 E  HG HM LG .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  LM \n"
    )


def test_show_3():
    test_build = RTGMover("")
    test_build.state = [1, 2, 2, 1, 0]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  HG .  LG .  \n"
        "F2 E  .  HM .  .  \n"
        "F1 .  .  .  .  LM \n"
    )


def test_show_4():
    test_build = RTGMover("")
    test_build.state = [0, 2, 2, 0, 0]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  HG .  LG .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 E  .  HM .  LM \n"
    )


def test_show_5():
    test_build = RTGMover("")
    test_build.state = [1, 2, 2, 1, 1]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 .  HG .  LG .  \n"
        "F2 E  .  HM .  LM \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_6():
    test_build = RTGMover("")
    test_build.state = [2, 2, 2, 2, 2]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  .  .  .  .  \n"
        "F3 E  HG HM LG LM \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_7():
    test_build = RTGMover("")
    test_build.state = [3, 2, 2, 3, 3]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 E  .  HM .  LM \n"
        "F3 .  HG .  LG .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_8():
    test_build = RTGMover("")
    test_build.state = [2, 2, 2, 2, 3]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  .  .  .  LM \n"
        "F3 E  HG HM LG .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_9():
    test_build = RTGMover("")
    test_build.state = [3, 3, 3, 2, 3]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 E  HG .  LG LM \n"
        "F3 .  .  HM .  .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_10():
    test_build = RTGMover("")
    test_build.state = [2, 3, 3, 2, 2]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 .  HG .  LG .  \n"
        "F3 E  .  HM .  LM \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )


def test_show_11():
    test_build = RTGMover("")
    test_build.state = [3, 3, 3, 3, 3]
    test_build.names = ["hydrogen", "lithium"]
    test_build.max_floor = 3
    test_build.num_ele = 2

    assert test_build.show() == (
        "F4 E  HG HM LG LM \n"
        "F3 .  .  .  .  .  \n"
        "F2 .  .  .  .  .  \n"
        "F1 .  .  .  .  .  \n"
    )
