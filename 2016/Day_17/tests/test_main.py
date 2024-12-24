"""
Tests for the main script
"""

from main import Route


def test_hashing():
    test = Route("hijkl")
    assert test.hash_md5("") == "ced9"
    assert test.hash_md5("D") == "f2bc"
    assert test.hash_md5("DR") == "5745"
    assert test.hash_md5("DU") == "528e"


def test_path_2_coords():
    test = Route("hijkl")

    assert test.path_2_coords("") == test.start
    assert test.path_2_coords("DDD") == (0, 3)
    assert test.path_2_coords("RRR") == (3, 0)

    assert test.path_2_coords("DDRRRD") == (3, 3)
    assert test.path_2_coords("DDUDRLRRUDRD") == (3, 3)
    assert test.path_2_coords("DRURDRUDDLLDLUURRDULRLDUUDDDRR") == (3, 3)


def test_detect_next_steps():
    test = Route("hijkl")
    assert set(test.detect_next_steps("")) == {"U", "D", "L"}
    assert set(test.detect_next_steps("D")) == {"U", "L", "R"}
    assert set(test.detect_next_steps("DR")) == set()
    assert set(test.detect_next_steps("DU")) == {"R"}
    assert set(test.detect_next_steps("DUR")) == set()


def test_shortest_path():
    assert Route("ihgpwlah").find_shortest_path() == "DDRRRD"
    assert Route("kglvqrro").find_shortest_path() == "DDUDRLRRUDRD"
    assert Route("ulqzkmiv").find_shortest_path() == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"
