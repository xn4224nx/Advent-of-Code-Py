"""
Tests for the main script
"""

from main import (
    read_ip_addresses,
    str_has_abba,
    supports_tls,
    count_valid_ip,
    find_bab_grps,
    supports_ssl,
    count_valid_ssl,
)


def test_read_ip_addresses_exp1():
    assert read_ip_addresses("./data/example_01.txt") == [
        {"brack_txt": ["mnop"], "out_brack_txt": ["abba", "qrst"]},
        {"brack_txt": ["bddb"], "out_brack_txt": ["abcd", "xyyx"]},
        {"brack_txt": ["qwer"], "out_brack_txt": ["aaaa", "tyui"]},
        {"brack_txt": ["asdfgh"], "out_brack_txt": ["ioxxoj", "zxcvbn"]},
    ]


def test_read_ip_addresses_exp2():
    assert read_ip_addresses("./data/example_02.txt") == [
        {"brack_txt": ["bab"], "out_brack_txt": ["aba", "xyz"]},
        {"brack_txt": ["xyx"], "out_brack_txt": ["xyx", "xyx"]},
        {"brack_txt": ["kek"], "out_brack_txt": ["aaa", "eke"]},
        {"brack_txt": ["bzb"], "out_brack_txt": ["zazbz", "cdb"]},
    ]


def test_str_has_abba_exp1():
    assert str_has_abba("abba") == True


def test_str_has_abba_exp2():
    assert str_has_abba("mnop") == False


def test_str_has_abba_exp3():
    assert str_has_abba("qrst") == False


def test_str_has_abba_exp4():
    assert str_has_abba("abcd") == False


def test_str_has_abba_exp5():
    assert str_has_abba("bddb") == True


def test_str_has_abba_exp6():
    assert str_has_abba("xyyx") == True


def test_str_has_abba_exp7():
    assert str_has_abba("aaaa") == False


def test_str_has_abba_exp8():
    assert str_has_abba("qwer") == False


def test_str_has_abba_exp9():
    assert str_has_abba("tyui") == False


def test_str_has_abba_exp10():
    assert str_has_abba("ioxxoj") == True


def test_str_has_abba_exp11():
    assert str_has_abba("asdfgh") == False


def test_str_has_abba_exp12():
    assert str_has_abba("zxcvbn") == False


def test_supports_tls_exp1():
    assert (
        supports_tls({"brack_txt": ["mnop"], "out_brack_txt": ["abba", "qrst"]}) == True
    )


def test_supports_tls_exp2():
    assert (
        supports_tls({"brack_txt": ["bddb"], "out_brack_txt": ["abcd", "xyyx"]})
        == False
    )


def test_supports_tls_exp3():
    assert (
        supports_tls({"brack_txt": ["qwer"], "out_brack_txt": ["aaaa", "tyui"]})
        == False
    )


def test_supports_tls_exp4():
    assert (
        supports_tls({"brack_txt": ["asdfgh"], "out_brack_txt": ["ioxxoj", "zxcvbn"]})
        == True
    )


def test_count_valid_ip_exp1():
    assert (
        count_valid_ip(
            [
                {"brack_txt": ["mnop"], "out_brack_txt": ["abba", "qrst"]},
                {"brack_txt": ["bddb"], "out_brack_txt": ["abcd", "xyyx"]},
                {"brack_txt": ["qwer"], "out_brack_txt": ["aaaa", "tyui"]},
                {"brack_txt": ["asdfgh"], "out_brack_txt": ["ioxxoj", "zxcvbn"]},
            ]
        )
        == 2
    )


def test_find_bab_grps_exp1():
    assert find_bab_grps("aba") == ["aba"]


def test_find_bab_grps_exp2():
    assert find_bab_grps("aba", True) == ["bab"]


def test_find_bab_grps_exp3():
    assert find_bab_grps("zazbz", False) == ["zaz", "zbz"]


def test_find_bab_grps_exp4():
    assert find_bab_grps("zazbz", True) == ["aza", "bzb"]


def test_suppports_ssl_exp1():
    supports_ssl({"brack_txt": ["bab"], "out_brack_txt": ["aba", "xyz"]}) == True


def test_suppports_ssl_exp2():
    supports_ssl({"brack_txt": ["xyx"], "out_brack_txt": ["xyx", "xyx"]}) == False


def test_suppports_ssl_exp3():
    supports_ssl({"brack_txt": ["kek"], "out_brack_txt": ["aaa", "eke"]}) == True


def test_suppports_ssl_exp4():
    supports_ssl({"brack_txt": ["bzb"], "out_brack_txt": ["zazbz", "cdb"]}) == True


def test_count_valid_ssl_exp1():
    assert (
        count_valid_ssl(
            [
                {"brack_txt": ["bab"], "out_brack_txt": ["aba", "xyz"]},
                {"brack_txt": ["xyx"], "out_brack_txt": ["xyx", "xyx"]},
                {"brack_txt": ["kek"], "out_brack_txt": ["aaa", "eke"]},
                {"brack_txt": ["bzb"], "out_brack_txt": ["zazbz", "cdb"]},
            ]
        )
        == 3
    )
