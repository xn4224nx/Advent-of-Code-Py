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


def test_detect_next_steps():
    test = Route("hijkl")
    assert set(test.detect_next_steps("")) == {"D"}
    assert set(test.detect_next_steps("D")) == {"U", "R"}
    assert set(test.detect_next_steps("DR")) == set()
    assert set(test.detect_next_steps("DU")) == {"R"}
    assert set(test.detect_next_steps("DUR")) == set()


def test_shortest_path():
    assert Route("ihgpwlah").find_shortest_path() == "DDRRRD"
    assert Route("kglvqrro").find_shortest_path() == "DDUDRLRRUDRD"
    assert Route("ulqzkmiv").find_shortest_path() == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"
