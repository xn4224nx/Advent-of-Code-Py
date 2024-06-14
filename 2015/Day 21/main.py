"""
--- Day 21: RPG Simulator 20XX ---

In this game, the player (you) and the enemy (the boss) take turns attacking.
The player always goes first. Each attack reduces the opponent's hit points by
at least 1. The first character at or below 0 hit points loses.

Damage dealt by an attacker each turn is equal to the attacker's damage score
minus the defender's armor score. An attacker always does at least 1 damage.
So, if the attacker has a damage score of 8, and the defender has an armor
score of 3, the defender loses 5 hit points. If the defender had an armor score
of 300, the defender would still lose 1 hit point.

Your damage score and armor score both start at zero. They can be increased by
buying items in exchange for gold. You start with no items and have as much
gold as you need. Your total damage or armor is equal to the sum of those stats
from all of your items. You have 100 hit points.

You must buy exactly one weapon; no dual-wielding. Armor is optional, but you
can't use more than one. You can buy 0-2 rings (at most one for each hand). You
must use any items you buy. The shop only has one of each item, so you can't
buy, for example, two rings of Damage +3.
"""

from itertools import combinations


def parse_data() -> tuple:
    """Parse the programs data"""

    boss_data = {
        "Hit Points": 103,
        "Damage": 9,
        "Armor": 2,
    }

    weapon_data = {
        "Dagger": {"cost": 8, "damage": 4, "armour": 0},
        "Shortsword": {"cost": 10, "damage": 5, "armour": 0},
        "Warhammer": {"cost": 25, "damage": 6, "armour": 0},
        "Longsword": {"cost": 40, "damage": 7, "armour": 0},
        "Greataxe": {"cost": 74, "damage": 8, "armour": 0},
    }

    armor_data = {
        "None": {"cost": 0, "damage": 0, "armour": 0},
        "Leather": {"cost": 13, "damage": 0, "armour": 1},
        "Chainmail": {"cost": 31, "damage": 0, "armour": 2},
        "Splintmail": {"cost": 53, "damage": 0, "armour": 3},
        "Bandedmail": {"cost": 75, "damage": 0, "armour": 4},
        "Platemail": {"cost": 102, "damage": 0, "armour": 5},
    }

    ring_data = {
        "None1": {"cost": 0, "damage": 0, "armour": 0},
        "None2": {"cost": 0, "damage": 0, "armour": 0},
        "Damage +1": {"cost": 25, "damage": 1, "armour": 0},
        "Damage +2": {"cost": 50, "damage": 2, "armour": 0},
        "Damage +3": {"cost": 100, "damage": 3, "armour": 0},
        "Defense +1": {"cost": 20, "damage": 0, "armour": 1},
        "Defense +2": {"cost": 40, "damage": 0, "armour": 2},
        "Defense +3": {"cost": 80, "damage": 0, "armour": 3},
    }

    return boss_data, weapon_data, armor_data, ring_data


def equipment_combs(weapon_data, armor_data, ring_data) -> tuple:
    """Generator for all equipment combinations."""

    for ring_i in combinations(ring_data, 2):
        for armour_i in combinations(armor_data, 1):
            for weapon_i in combinations(weapon_data, 1):

                yield ring_i, armour_i, weapon_i


def player_stats(equip_comb, weapon_data, armor_data, ring_data) -> tuple:
    """Calculate the player stats & cost based on the equipment they have."""

    i_cost = 0
    i_damage = 0
    i_armour = 0

    # Ring Effects
    for ring in equip_comb[0]:
        i_cost += ring_data[ring]["cost"]
        i_damage += ring_data[ring]["damage"]
        i_armour += ring_data[ring]["armour"]

    # Armour Effects
    i_cost += armor_data[equip_comb[1][0]]["cost"]
    i_damage += armor_data[equip_comb[1][0]]["damage"]
    i_armour += armor_data[equip_comb[1][0]]["armour"]

    # Weapon Effects
    i_cost += weapon_data[equip_comb[2][0]]["cost"]
    i_damage += weapon_data[equip_comb[2][0]]["damage"]
    i_armour += weapon_data[equip_comb[2][0]]["armour"]

    return i_cost, i_damage, i_armour


def battle_result(player, boss) -> bool:
    """Calculate the battle result between the player and the boss."""

    boss_hitpoints = boss["Hit Points"]
    player_hitpoints = 100

    # Simulate the battle
    while boss_hitpoints > 0 and player_hitpoints > 0:

        # Player hits the Boss
        boss_hitpoints -= max([1, player[1] - boss["Armor"]])

        if boss_hitpoints <= 0:
            return True

        # Boss hits the Player
        player_hitpoints -= max([1, boss["Damage"] - player[2]])

        if player_hitpoints <= 0:
            return False
    else:
        raise Exception("Battle error.")


# Parse the data
boss_info, weapon_info,  armor_info, ring_info = parse_data()

wins = []
losses = []

# Map all the possible item choices
for i in equipment_combs(weapon_info,  armor_info, ring_info):

    # What are the player stats
    player_ = player_stats(i, weapon_info, armor_info, ring_info)

    # If the player wins save the gold needed
    if battle_result(player_, boss_info):
        wins.append(player_[0])
    else:
        losses.append(player_[0])

# Part 1
print(min(wins))

# Part 2
print(max(losses))



