"""
Tests for the main script
"""

from main import CaveGarden


def test_garden_creation_exp0():
    test = CaveGarden("./data/example_0.txt")

    assert test.min_plant == 0
    assert test.max_plant == 24
    assert test.plants == {0, 3, 5, 8, 9, 16, 17, 18, 22, 23, 24}
    assert test.r_maintain == [
        [0],
        [-1, 0],
        [-1, 0, 1, 2],
        [-2, 0, 2],
        [-2, 0, 1, 2],
        [-2, -1, 0],
        [-2, -1, 0, 2],
        [-2, -1, 0, 1],
    ]
    assert test.r_remove == []
    assert test.r_add == [
        [1, 2],
        [-1],
        [-1, 1],
        [-1, 1, 2],
        [-2, -1, 1],
        [-2, -1, 1, 2],
    ]


def test_growth_exp0():
    test = CaveGarden("./data/example_0.txt")
    test.grow()

    assert test.min_plant == 0
    assert test.max_plant == 24
    assert test.plants == {0, 4, 9, 15, 18, 21, 24}


def test_growth_exp1():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(19):
        test.grow()

    assert test.min_plant == -2
    assert test.max_plant == 33
    assert test.plants == {
        -2,
        1,
        2,
        3,
        5,
        8,
        10,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        20,
        22,
        24,
        27,
        29,
        33,
    }


def test_total_plants_after_time():
    test = CaveGarden("./data/example_0.txt")
    total = test.total_plants_after_time(20)

    assert test.min_plant == -2
    assert test.max_plant == 34
    assert total == 325
