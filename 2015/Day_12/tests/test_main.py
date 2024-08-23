"""
Tests for functions in the main script.
"""

import main
import json


def test_sum_exp_1():
    assert main.sum_all_nums("[1,2,3]") == 6


def test_sum_exp_2():
    assert main.sum_all_nums('{"a":2,"b":4}') == 6


def test_sum_exp_3():
    assert main.sum_all_nums("[[[3]]]") == 3


def test_sum_exp_4():
    assert main.sum_all_nums('{"a":{"b":4},"c":-1}') == 3


def test_sum_exp_5():
    assert main.sum_all_nums('{"a":[-1,1]}') == 0


def test_sum_exp_6():
    assert main.sum_all_nums('[-1,{"a":1}]') == 0


def test_sum_exp_7():
    assert main.sum_all_nums("[]") == 0


def test_sum_exp_8():
    assert main.sum_all_nums("{}") == 0


def test_sum_non_red_exp_1():
    assert main.non_red_sum(json.loads("[1,2,3]")) == 6


def test_sum_non_red_exp_2():
    assert main.non_red_sum(json.loads('[1,{"c":"red","b":2},3]')) == 4


def test_sum_non_red_exp_3():
    assert main.non_red_sum(json.loads('{"d":"red","e":[1,2,3,4],"f":5}')) == 0


def test_sum_non_red_exp_4():
    assert main.non_red_sum(json.loads('[1,"red",5]')) == 6
