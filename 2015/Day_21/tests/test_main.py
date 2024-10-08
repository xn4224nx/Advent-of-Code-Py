"""
Tests for functions in the main script.
"""

from main import (
    read_store_data,
    iter_equipment,
    cost_store_purchases,
    determine_stats,
    boss_defeated,
)


def test_read_store_data_1():
    assert read_store_data("./data/shop.txt") == {
        "Weapons": {
            "Dagger": {"Cost": 8, "Damage": 4, "Armor": 0},
            "Shortsword": {"Cost": 10, "Damage": 5, "Armor": 0},
            "Warhammer": {"Cost": 25, "Damage": 6, "Armor": 0},
            "Longsword": {"Cost": 40, "Damage": 7, "Armor": 0},
            "Greataxe": {"Cost": 74, "Damage": 8, "Armor": 0},
        },
        "Armor": {
            "Leather": {"Cost": 13, "Damage": 0, "Armor": 1},
            "Chainmail": {"Cost": 31, "Damage": 0, "Armor": 2},
            "Splintmail": {"Cost": 53, "Damage": 0, "Armor": 3},
            "Bandedmail": {"Cost": 75, "Damage": 0, "Armor": 4},
            "Platemail": {"Cost": 102, "Damage": 0, "Armor": 5},
        },
        "Rings": {
            "Damage +1": {"Cost": 25, "Damage": 1, "Armor": 0},
            "Damage +2": {"Cost": 50, "Damage": 2, "Armor": 0},
            "Damage +3": {"Cost": 100, "Damage": 3, "Armor": 0},
            "Defense +1": {"Cost": 20, "Damage": 0, "Armor": 1},
            "Defense +2": {"Cost": 40, "Damage": 0, "Armor": 2},
            "Defense +3": {"Cost": 80, "Damage": 0, "Armor": 3},
        },
    }


def test_read_store_data_2():
    assert read_store_data("./data/small_shop.txt") == {
        "Weapons": {
            "Dagger": {"Cost": 8, "Damage": 4, "Armor": 0},
        },
        "Armor": {
            "Leather": {"Cost": 13, "Damage": 0, "Armor": 1},
            "Chainmail": {"Cost": 31, "Damage": 0, "Armor": 2},
        },
        "Rings": {
            "Damage +1": {"Cost": 25, "Damage": 1, "Armor": 0},
            "Defense +1": {"Cost": 20, "Damage": 0, "Armor": 1},
        },
    }


def test_iter_equipment():
    true_equip_combs = [
        {"Weapons": ["Dagger"], "Armor": [], "Rings": []},
        {"Weapons": ["Dagger"], "Armor": ["Leather"], "Rings": []},
        {"Weapons": ["Dagger"], "Armor": ["Chainmail"], "Rings": []},
        {"Weapons": ["Dagger"], "Armor": [], "Rings": ["Damage +1"]},
        {"Weapons": ["Dagger"], "Armor": ["Leather"], "Rings": ["Damage +1"]},
        {"Weapons": ["Dagger"], "Armor": ["Chainmail"], "Rings": ["Damage +1"]},
        {"Weapons": ["Dagger"], "Armor": [], "Rings": ["Defense +1"]},
        {"Weapons": ["Dagger"], "Armor": ["Leather"], "Rings": ["Defense +1"]},
        {"Weapons": ["Dagger"], "Armor": ["Chainmail"], "Rings": ["Defense +1"]},
        {"Weapons": ["Dagger"], "Armor": [], "Rings": ["Damage +1", "Defense +1"]},
        {
            "Weapons": ["Dagger"],
            "Armor": ["Leather"],
            "Rings": ["Damage +1", "Defense +1"],
        },
        {
            "Weapons": ["Dagger"],
            "Armor": ["Chainmail"],
            "Rings": ["Damage +1", "Defense +1"],
        },
    ]

    store = read_store_data("./data/small_shop.txt")
    test_combs = [x for x in iter_equipment(store)]

    # Ensure there are no extra combinations outside the true amount
    assert len(test_combs) == len(true_equip_combs)

    # for each true combination ensure that it gets created
    for true_comb in true_equip_combs:
        for comb in test_combs:
            if comb == true_comb:
                break

        # If no match has been found the test has failed
        else:
            raise Exception(f"Combination {true_comb} could not be found")


def test_cost_store_purchases_1():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store, {"Weapons": ["Dagger"], "Armor": ["Leather"], "Rings": []}
        )
        == 21
    )


def test_cost_store_purchases_2():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store,
            {"Weapons": ["Dagger"], "Armor": ["Leather"], "Rings": ["Defense +3"]},
        )
        == 101
    )


def test_cost_store_purchases_3():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store, {"Weapons": ["Longsword"], "Armor": [], "Rings": ["Defense +1"]}
        )
        == 60
    )


def test_cost_store_purchases_4():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store, {"Weapons": ["Greataxe"], "Armor": ["Chainmail"], "Rings": []}
        )
        == 105
    )


def test_cost_store_purchases_5():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store,
            {
                "Weapons": ["Longsword"],
                "Armor": ["Splintmail"],
                "Rings": ["Defense +3"],
            },
        )
        == 173
    )


def test_cost_store_purchases_6():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store,
            {"Weapons": ["Warhammer"], "Armor": ["Leather"], "Rings": ["Defense +2"]},
        )
        == 78
    )


def test_cost_store_purchases_7():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store,
            {"Weapons": ["Dagger"], "Armor": ["Chainmail"], "Rings": ["Damage +3"]},
        )
        == 139
    )


def test_cost_store_purchases_8():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store, {"Weapons": ["Greataxe"], "Armor": ["Bandedmail"], "Rings": []}
        )
        == 149
    )


def test_cost_store_purchases_9():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store,
            {"Weapons": ["Warhammer"], "Armor": ["Platemail"], "Rings": ["Damage +1"]},
        )
        == 152
    )


def test_cost_store_purchases_10():
    store = read_store_data("./data/shop.txt")
    assert (
        cost_store_purchases(
            store,
            {
                "Weapons": ["Shortsword"],
                "Armor": ["Splintmail"],
                "Rings": ["Damage +2"],
            },
        )
        == 113
    )


def test_determine_stats_1():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store, {"Weapons": ["Dagger"], "Armor": ["Leather"], "Rings": ["Defense +3"]}
    ) == {
        "Hit Points": 100,
        "Damage": 4,
        "Armor": 4,
    }


def test_determine_stats_2():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store, {"Weapons": ["Dagger"], "Armor": ["Leather"], "Rings": []}
    ) == {
        "Hit Points": 100,
        "Damage": 4,
        "Armor": 1,
    }


def test_determine_stats_3():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store, {"Weapons": ["Longsword"], "Armor": [], "Rings": ["Defense +1"]}
    ) == {
        "Hit Points": 100,
        "Damage": 7,
        "Armor": 1,
    }


def test_determine_stats_4():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store, {"Weapons": ["Greataxe"], "Armor": ["Chainmail"], "Rings": []}
    ) == {
        "Hit Points": 100,
        "Damage": 8,
        "Armor": 2,
    }


def test_determine_stats_5():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store,
        {"Weapons": ["Longsword"], "Armor": ["Splintmail"], "Rings": ["Defense +3"]},
    ) == {
        "Hit Points": 100,
        "Damage": 7,
        "Armor": 6,
    }


def test_determine_stats_6():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store, {"Weapons": ["Warhammer"], "Armor": ["Leather"], "Rings": ["Defense +2"]}
    ) == {
        "Hit Points": 100,
        "Damage": 6,
        "Armor": 3,
    }


def test_determine_stats_7():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store, {"Weapons": ["Dagger"], "Armor": ["Chainmail"], "Rings": ["Damage +3"]}
    ) == {
        "Hit Points": 100,
        "Damage": 7,
        "Armor": 2,
    }


def test_determine_stats_8():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store, {"Weapons": ["Greataxe"], "Armor": ["Bandedmail"], "Rings": []}
    ) == {
        "Hit Points": 100,
        "Damage": 8,
        "Armor": 4,
    }


def test_determine_stats_9():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store,
        {"Weapons": ["Warhammer"], "Armor": ["Platemail"], "Rings": ["Damage +1"]},
    ) == {
        "Hit Points": 100,
        "Damage": 7,
        "Armor": 5,
    }


def test_determine_stats_10():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store,
        {"Weapons": ["Shortsword"], "Armor": ["Splintmail"], "Rings": ["Damage +2"]},
    ) == {
        "Hit Points": 100,
        "Damage": 7,
        "Armor": 3,
    }


def test_determine_stats_11():
    store = read_store_data("./data/shop.txt")
    assert determine_stats(
        store, {"Weapons": ["Dagger"], "Armor": [], "Rings": []}
    ) == {
        "Hit Points": 100,
        "Damage": 4,
        "Armor": 0,
    }


def test_boss_defeated():
    assert boss_defeated(
        {"Hit Points": 12, "Damage": 7, "Armor": 2},
        {"Hit Points": 8, "Damage": 5, "Armor": 5},
    )
