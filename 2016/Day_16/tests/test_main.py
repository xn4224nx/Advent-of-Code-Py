"""
Tests for the main script
"""

from main import convert_2_bin, convert_2_str, dragon_fold, checksum, disk_fill_checksum


def test_convert_2_bin():
    assert convert_2_bin("1111") == 15
    assert convert_2_bin("1000") == 8
    assert convert_2_bin("100000001111101110101000111000001010") == 34623622666
    assert convert_2_bin("1001010001111001111100101111100") == 1245510012
    assert (
        convert_2_bin(
            ("11011101110111111110110111101" "1001001000011110000100110100001")
        )
        == 999234925155518881
    )


def test_convert_2_str():
    assert convert_2_str(42) == "101010"
    assert convert_2_str(4200) == "1000001101000"
    assert convert_2_str(94498345) == "101101000011110111000101001"
    assert convert_2_str(6634497165551) == (
        "1100000100010110110110110001100100011101111"
    )
    assert convert_2_str(77299398389454049842) == (
        "1000011000010111110" "1010000101001001000" "1001011001111100100" "1000110010"
    )


def test_dragon_fold():
    assert dragon_fold(convert_2_bin("1")) == convert_2_bin("100")
    assert dragon_fold(convert_2_bin("0")) == convert_2_bin("001")
    assert dragon_fold(convert_2_bin("11111")) == convert_2_bin("11111000000")
    assert dragon_fold(convert_2_bin("111100001010")) == convert_2_bin(
        "1111000010100101011110000"
    )


def test_checksum():
    assert checksum(convert_2_bin("110010110100")) == convert_2_bin("100")
    assert checksum(convert_2_bin("10000011110010000111")) == convert_2_bin("01100")


def test_disk_fill_checksum():
    assert disk_fill_checksum("10000", 20) == "01100"
