"""
Tests for the main script
"""

from main import BalanceBots


def test_read_instructions_data_1():
    test = BalanceBots("./data/example_01.txt")
    assert test.instrucs == [
        {"type": "send-val", "val": 5, "bot": 2},
        {
            "type": "bal-mov",
            "src-bot": 2,
            "low-dest": 1,
            "low-bot": True,
            "high-dest": 0,
            "high-bot": True,
        },
        {"type": "send-val", "val": 3, "bot": 1},
        {
            "type": "bal-mov",
            "src-bot": 1,
            "low-dest": 1,
            "low-bot": False,
            "high-dest": 0,
            "high-bot": True,
        },
        {
            "type": "bal-mov",
            "src-bot": 0,
            "low-dest": 2,
            "low-bot": False,
            "high-dest": 0,
            "high-bot": False,
        },
        {"type": "send-val", "val": 2, "bot": 2},
    ]


def test_read_instructions_data_2():
    test = BalanceBots("./data/example_02.txt")
    assert test.instrucs == [
        {"type": "send-val", "val": 99, "bot": 0},
        {"type": "send-val", "val": 8, "bot": 1},
        {"type": "send-val", "val": 3, "bot": 2},
        {"type": "send-val", "val": 44, "bot": 3},
        {"type": "send-val", "val": 7, "bot": 5},
        {"type": "send-val", "val": 1, "bot": 10},
        {"type": "send-val", "val": 6, "bot": 5},
        {"type": "send-val", "val": 2, "bot": 10},
    ]


def test_read_instructions_data_3():
    test = BalanceBots("./data/example_03.txt")
    assert test.instrucs == [
        {"type": "send-val", "val": 9, "bot": 0},
        {"type": "send-val", "val": 10, "bot": 1},
        {"type": "send-val", "val": 11, "bot": 3},
        {"type": "send-val", "val": 12, "bot": 3},
        {
            "type": "bal-mov",
            "src-bot": 3,
            "low-dest": 1,
            "low-bot": True,
            "high-dest": 0,
            "high-bot": True,
        },
        {
            "type": "bal-mov",
            "src-bot": 1,
            "low-dest": 1,
            "low-bot": False,
            "high-dest": 2,
            "high-bot": True,
        },
        {
            "type": "bal-mov",
            "src-bot": 0,
            "low-dest": 2,
            "low-bot": True,
            "high-dest": 0,
            "high-bot": False,
        },
    ]


def test_send_val_to_bot_1():
    test = BalanceBots("./data/example_02.txt")
    test.execute_all_insrucs()

    assert test.bots == [
        [99],
        [8],
        [3],
        [44],
        [],
        [7, 6],
        [],
        [],
        [],
        [],
        [],
        [1, 2],
    ]


def test_send_val_to_bot_2():
    test = BalanceBots("")
    test.bots = [[] for _ in range(11)]

    test.send_val_to_bot(99, 0)
    test.send_val_to_bot(8, 1)
    test.send_val_to_bot(3, 2)
    test.send_val_to_bot(44, 3)
    test.send_val_to_bot(7, 5)
    test.send_val_to_bot(1, 10)
    test.send_val_to_bot(6, 5)
    test.send_val_to_bot(2, 10)

    assert test.bots == [
        [99],
        [8],
        [3],
        [44],
        [],
        [7, 6],
        [],
        [],
        [],
        [],
        [],
        [1, 2],
    ]


def test_send_val_to_bot_3():
    test = BalanceBots("./data/example_03.txt")
    test.execute_all_insrucs()

    assert test.bots == [
        [],
        [],
        [
            11,
            9,
        ],
        [],
    ]

    assert test.outputs == [
        [
            12,
        ],
        [
            10,
        ],
    ]


def test_send_val_to_bot_4():
    test = BalanceBots("")
    test.send_val_to_bot(9, 0)
    test.send_val_to_bot(10, 1)
    test.send_val_to_bot(11, 2)
    test.send_val_to_bot(12, 3)
    test.balance_move(3, True, 1, True, 0)
    test.balance_move(1, False, 1, True, 2)
    test.balance_move(0, True, 2, False, 0)

    assert test.bots == [
        [],
        [],
        [
            11,
            9,
        ],
        [],
    ]

    assert test.outputs == [
        [
            12,
        ],
        [
            10,
        ],
    ]


def test_example_1():
    test = BalanceBots("./data/example_01.txt")
    test.execute_all_insrucs()

    assert test.bots == [
        [],
        [],
        [],
    ]

    assert test.outputs == [[5], [2], [3]]


def test_find_comp():
    test = BalanceBots("./data/example_01.txt")
    assert test.find_comp_bot(5, 2) == 2
    assert test.find_comp_bot(2, 5) == 2
