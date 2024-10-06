"""
Tests for the main script
"""

from main import (
    read_room_data,
    is_room_real,
    sum_real_room_sector_ids,
    room_checksum,
    decrypt_room_name,
)


def test_read_example_room_data():
    assert read_room_data("./data/example_01.txt") == [
        {"name": "aaaaa-bbb-z-y-x", "sec_id": 123, "check_sum": "abxyz"},
        {"name": "a-b-c-d-e-f-g-h", "sec_id": 987, "check_sum": "abcde"},
        {"name": "not-a-real-room", "sec_id": 404, "check_sum": "oarel"},
        {"name": "totally-real-room", "sec_id": 200, "check_sum": "decoy"},
    ]


def test_rm_checksum_1():
    assert room_checksum("aaaaa-bbb-z-y-x") == "abxyz"


def test_rm_checksum_2():
    assert room_checksum("a-b-c-d-e-f-g-h") == "abcde"


def test_rm_checksum_3():
    assert room_checksum("not-a-real-room") == "oarel"


def test_rm_checksum_4():
    assert room_checksum("totally-real-room") == "loart"


def test_is_room_real_1():
    assert (
        is_room_real({"name": "aaaaa-bbb-z-y-x", "sec_id": 123, "check_sum": "abxyz"})
        == True
    )


def test_is_room_real_2():
    assert (
        is_room_real({"name": "a-b-c-d-e-f-g-h", "sec_id": 987, "check_sum": "abcde"})
        == True
    )


def test_is_room_real_3():
    assert (
        is_room_real({"name": "not-a-real-room", "sec_id": 404, "check_sum": "oarel"})
        == True
    )


def test_is_room_real_4():
    assert (
        is_room_real({"name": "totally-real-room", "sec_id": 200, "check_sum": "decoy"})
        == False
    )


def test_sum_real_room_sector_ids_exp1():
    assert (
        sum_real_room_sector_ids(
            [
                {"name": "aaaaa-bbb-z-y-x", "sec_id": 123, "check_sum": "abxyz"},
                {"name": "a-b-c-d-e-f-g-h", "sec_id": 987, "check_sum": "abcde"},
                {"name": "not-a-real-room", "sec_id": 404, "check_sum": "oarel"},
                {"name": "totally-real-room", "sec_id": 200, "check_sum": "decoy"},
            ]
        )
        == 1514
    )


def test_decrypt_room_name():
    assert (
        decrypt_room_name({"name": "qzmt-zixmtkozy-ivhz", "sec_id": 343})
        == "very encrypted name"
    )
