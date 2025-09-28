"""
Tests for the main script
"""

from main import CaveGarden
from collections import deque


def test_garden_creation_exp0():
    test = CaveGarden("./data/example_0.txt")

    assert test.plants == deque("#..#.#..##......###...###")
    assert test.orig_start == 0
    assert test.r_remove == []
    assert test.r_add == [
        list("...##"),
        list(".#..."),
        list(".#.#."),
        list(".#.##"),
        list("##.#."),
        list("##.##"),
    ]
    assert test.r_maintain == [
        list("..#.."),
        list(".##.."),
        list(".####"),
        list("#.#.#"),
        list("#.###"),
        list("###.."),
        list("###.#"),
        list("####."),
    ]


def test_growth_exp00():
    test = CaveGarden("./data/example_0.txt")
    test.grow()
    assert "#...#....#.....#..#..#..#" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#...#....#.....#..#..#..#".count("#")


def test_growth_exp01():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(2):
        test.grow()

    assert "##..##...##....#..#..#..##" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "##..##...##....#..#..#..##".count("#")


def test_growth_exp02():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(3):
        test.grow()

    assert "#.#...#..#.#....#..#..#...#" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#.#...#..#.#....#..#..#...#".count("#")


def test_growth_exp03():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(4):
        test.grow()

    assert "#.#..#...#.#...#..#..##..##" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#.#..#...#.#...#..#..##..##".count("#")


def test_growth_exp04():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(5):
        test.grow()

    assert "#...##...#.#..#..#...#...#" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#...##...#.#..#..#...#...#".count("#")


def test_growth_exp05():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(6):
        test.grow()

    assert "##.#.#....#...#..##..##..##" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "##.#.#....#...#..##..##..##".count("#")


def test_growth_exp06():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(7):
        test.grow()

    assert "#..###.#...##..#...#...#...#" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#..###.#...##..#...#...#...#".count("#")


def test_growth_exp07():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(8):
        test.grow()

    assert "#....##.#.#.#..##..##..##..##" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#....##.#.#.#..##..##..##..##".count("#")


def test_growth_exp08():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(9):
        test.grow()

    assert "##..#..#####....#...#...#...#" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "##..#..#####....#...#...#...#".count("#")


def test_growth_exp09():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(10):
        test.grow()

    assert "#.#..#...#.##....##..##..##..##" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#.#..#...#.##....##..##..##..##".count(
        "#"
    )


def test_growth_exp10():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(11):
        test.grow()

    assert "#...##...#.#...#.#...#...#...#" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#...##...#.#...#.#...#...#...#".count(
        "#"
    )


def test_growth_exp11():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(12):
        test.grow()

    assert "##.#.#....#.#...#.#..##..##..##" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "##.#.#....#.#...#.#..##..##..##".count(
        "#"
    )


def test_growth_exp12():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(13):
        test.grow()

    assert "#..###.#....#.#...#....#...#...#" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#..###.#....#.#...#....#...#...#".count(
        "#"
    )


def test_growth_exp13():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(14):
        test.grow()

    assert "#....##.#....#.#..##...##..##..##" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "#....##.#....#.#..##...##..##..##".count(
        "#"
    )


def test_growth_exp14():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(15):
        test.grow()

    assert "##..#..#.#....#....#..#.#...#...#" in "".join(test.plants)
    assert "".join(test.plants).count("#") == "##..#..#.#....#....#..#.#...#...#".count(
        "#"
    )


def test_growth_exp15():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(16):
        test.grow()

    assert "#.#..#...#.#...##...#...#.#..##..##" in "".join(test.plants)
    assert "".join(test.plants).count(
        "#"
    ) == "#.#..#...#.#...##...#...#.#..##..##".count("#")


def test_growth_exp16():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(17):
        test.grow()

    assert "#...##...#.#.#.#...##...#....#...#" in "".join(test.plants)
    assert "".join(test.plants).count(
        "#"
    ) == "#...##...#.#.#.#...##...#....#...#".count("#")


def test_growth_exp17():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(18):
        test.grow()

    assert "##.#.#....#####.#.#.#...##...##..##" in "".join(test.plants)
    assert "".join(test.plants).count(
        "#"
    ) == "##.#.#....#####.#.#.#...##...##..##".count("#")


def test_growth_exp18():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(19):
        test.grow()

    assert "#..###.#..#.#.#######.#.#.#..#.#...#" in "".join(test.plants)
    assert "".join(test.plants).count(
        "#"
    ) == "#..###.#..#.#.#######.#.#.#..#.#...#".count("#")


def test_growth_exp19():
    test = CaveGarden("./data/example_0.txt")
    for _ in range(20):
        test.grow()

    assert "#....##....#####...#######....#.#..##" in "".join(test.plants)
    assert "".join(test.plants).count(
        "#"
    ) == "#....##....#####...#######....#.#..##".count("#")


def test_total_plants_after_time():
    assert CaveGarden("./data/example_0.txt").total_plants_after_time(20) == 325
