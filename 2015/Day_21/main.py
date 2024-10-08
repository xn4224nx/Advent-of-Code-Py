"""
--- Day 21: RPG Simulator 20XX ---

Little Henry Case got a new video game for Christmas. It's an RPG, and he's
stuck on a boss. He needs to know what equipment to buy at the shop. He hands
you the controller.

In this game, the player (you) and the enemy (the boss) take turns attacking.
The player always goes first. Each attack reduces the opponent's hit points by at
least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score
minus the defender's armor score. An attacker always does at least 1 damage. So,
if the attacker has a damage score of 8, and the defender has an armor score of
3, the defender loses 5 hit points. If the defender had an armor score of 300,
the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by
buying items in exchange for gold. You start with no items and have as much gold
as you need. Your total damage or armor is equal to the sum of those stats from
all of your items. You have 100 hit points.

You must buy exactly one weapon; no dual-wielding. Armor is optional, but you
can't use more than one. You can buy 0-2 rings (at most one for each hand). You
must use any items you buy. The shop only has one of each item, so you can't
buy, for example, two rings of Damage +3.

PART 1: You have 100 hit points. The boss's actual stats are in your puzzle
        input. What is the least amount of gold you can spend and still win the
        fight?

Turns out the shopkeeper is working with the boss, and can persuade you to buy
whatever items he wants. The other rules still apply, and he still only has one
of each item.

PART 2: What is the most amount of gold you can spend and still lose the fight?
"""

from itertools import combinations
import sys


def read_store_data(file_path: str) -> dict[str : dict[str:int]]:
    """
    Open the file detailing the store contents and parse it into a nested
    dictionary format.
    """
    store = {}

    with open(file_path, "r") as fp:
        for line in fp.readlines():

            # A new list of item types is starting
            if "Cost  Damage  Armor" in line:
                cata, _ = line.split(":")
                store[cata] = {}

            # Add a item to the store
            elif line != "\n":
                revline = line[::-1]
                cont = revline.split(None, 3)

                # Un-reverse the individual string parts
                store[cata][cont[3][::-1]] = {
                    "Cost": int(cont[2][::-1]),
                    "Damage": int(cont[1][::-1]),
                    "Armor": int(cont[0][::-1]),
                }

    return store


def iter_equipment(store: dict[str : dict[str:int]]) -> dict[str : list[str]]:
    """
    Generate the possible equipment configurations possible from the store.
    """

    # You must always buy a weapon
    for weapon in store["Weapons"].keys():

        # You can have one or no piece of armour
        for arm_num in [0, 1]:
            for arm_comb in combinations(store["Armor"].keys(), arm_num):

                # You can have 0 to 2 rings but no duplicates
                for ring_num in [0, 1, 2]:
                    for ring_comb in combinations(store["Rings"].keys(), ring_num):

                        yield {
                            "Weapons": [weapon],
                            "Armor": list(arm_comb),
                            "Rings": list(ring_comb),
                        }


def cost_store_purchases(
    store: dict[str : dict[str:int]], equip: dict[str : list[str]]
) -> int:
    """
    Determine the total cost of a certain set of equipment.
    """
    return sum([store[cata][x]["Cost"] for cata, prods in equip.items() for x in prods])


def determine_stats(
    store: dict[str : dict[str:int]], equip: list[str]
) -> dict[str:int]:
    """
    Calculate hit-points, damage, armour based on the equipment attached.
    """
    stats = {"Damage": 0, "Armor": 0}

    # Lookup and record the modifiers for each item of equipment
    for cata, prods in equip.items():
        for prd in prods:
            for sta in stats.keys():
                stats[sta] += store[cata][prd][sta]

    # Health is set value
    stats["Hit Points"] = 100

    return stats


def boss_defeated(boss_stats: dict[str:int], adve_stats: dict[str:int]) -> bool:
    """
    Does the adventurer defeat the boss?
    """
    boss_health = boss_stats["Hit Points"]
    adve_health = adve_stats["Hit Points"]

    while True:

        # The adventurer attacks
        boss_health -= max(adve_stats["Damage"] - boss_stats["Armor"], 1)

        if boss_health <= 0:
            return True

        # The boss attacks
        adve_health -= max(boss_stats["Damage"] - adve_stats["Armor"], 1)

        if adve_health <= 0:
            return False


def find_min_gold_to_win(
    boss_stats: dict[str:int], store: dict[str : dict[str:int]]
) -> int:
    """
    Determine every possible equipment combination and find the cheapest one
    that beats the boss.
    """
    min_cost = sys.maxsize

    for equip in iter_equipment(store):

        adve_stats = determine_stats(store, equip)
        equip_cost = cost_store_purchases(store, equip)

        if equip_cost < min_cost and boss_defeated(boss_stats, adve_stats):
            min_cost = equip_cost

    return min_cost


def find_max_gold_to_lose(
    boss_stats: dict[str:int], store: dict[str : dict[str:int]]
) -> int:
    """
    Determine every possible equipment combination and find the most expensive
    one that loses to the boss.
    """
    max_cost = 0

    for equip in iter_equipment(store):

        adve_stats = determine_stats(store, equip)
        equip_cost = cost_store_purchases(store, equip)

        if equip_cost > max_cost and not boss_defeated(boss_stats, adve_stats):
            max_cost = equip_cost

    return max_cost


if __name__ == "__main__":
    store_data = read_store_data("./data/shop.txt")
    boss_stats = {"Hit Points": 100, "Damage": 8, "Armor": 2}

    print(f"Part 1 = {find_min_gold_to_win(boss_stats, store_data)}")
    print(f"Part 2 = {find_max_gold_to_lose(boss_stats, store_data)}")
