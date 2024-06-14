"""
--- Day 22: Wizard Simulator 20XX ---

You must choose one of your spells to cast. The first character at or below 0
hit points loses.

As before, if armor (from a spell, in this case) would reduce damage below 1,
it becomes 1 instead - that is, the boss' attacks always deal at least 1
damage.

On each of your turns, you must select one of your spells to cast. If you
cannot afford to cast any spell, you lose. Spells cost mana; you start with
500 mana, but have no maximum limit. You must have enough mana to cast a spell,
and its cost is immediately deducted when you cast it. Your spells are Magic
Missile, Drain, Shield, Poison, and Recharge.

Effects all work the same way. Effects apply at the start of both the player's
turns and the boss' turns. Effects are created with a timer (the number of
turns they last); at the start of each turn, after they apply any effect they
have, their timer is decreased by one. If this decreases the timer to zero, the
effect ends. You cannot cast a spell that would start an effect which is
already active. However, effects can be started on the same turn they end.
"""

import random


class WizardBattle:

    def __init__(self, turn_damage=False):
        # Stats for the battle
        self.boss_hit_points = 55
        self.player_hit_points = 50
        self.player_armour = 0
        self.starting_mana = 500
        self.boss_damage = 8
        self.spent_mana = 0
        self.current_mana = self.starting_mana
        self.turn_damage = turn_damage
        self.known_spells = {
            "Magic Missile": {"cost": 53, "damage": 4},
            "Drain": {"cost": 73, "damage": 2, "heal": 2},
            "Shield": {"cost": 113, "armour": 7, "turns": 6},
            "Poison": {"cost": 173, "damage_over_time": 3, "turns": 6},
            "Recharge": {"cost": 229, "turns": 5, "mana": 101},
        }
        self.active_spells = {}

    def execute_active_spells(self):
        """Implement the effects of all the active spells"""
        for spell in list(self.active_spells):

            # Decrement the turn counter
            self.active_spells[spell] -= 1

            # Activate effects
            if "armour" in self.known_spells[spell]:
                self.player_armour = self.known_spells[spell]["armour"]

            if "damage_over_time" in self.known_spells[spell]:
                self.boss_hit_points -= self.known_spells[
                    spell]["damage_over_time"]

            if "mana" in self.known_spells[spell]:
                self.current_mana += self.known_spells[spell]["mana"]

            # Remove active spells that have run there course
            if self.active_spells[spell] <= 0:
                del self.active_spells[spell]

        # Remove the effect of continuous spells
        if not [x for x in self.active_spells
                if "armour" in self.known_spells[x]]:
            self.player_armour = 0

    def wizard_cast(self, cast_spell):
        """The wizard casts a spell"""
        if "turns" in self.known_spells[cast_spell]:
            self.active_spells[cast_spell] \
                = self.known_spells[cast_spell]["turns"]
        else:
            if "damage" in self.known_spells[cast_spell]:
                self.boss_hit_points \
                    -= self.known_spells[cast_spell]["damage"]

            if "heal" in self.known_spells[cast_spell]:
                self.player_hit_points \
                    += self.known_spells[cast_spell]["heal"]

        # Modify the mana records
        self.spent_mana += self.known_spells[cast_spell]["cost"]
        self.current_mana -= self.known_spells[cast_spell]["cost"]

    def boss_attack(self):
        """Simulate the boss attacking the wizard."""
        self.player_hit_points -= max(
            [1, self.boss_damage - self.player_armour])

    def battle(self) -> tuple:
        """Simulate a wizard battling a boss and using random spells"""

        while True:

            # Damage at the start of the turn
            if self.turn_damage:
                self.player_hit_points -= 1

                # Check if the player is dead
                if self.player_hit_points <= 0:
                    return False, self.spent_mana

            # Execute the active spells
            self.execute_active_spells()

            # Check if the boss is dead
            if self.boss_hit_points <= 0:
                return True, self.spent_mana

            # Find out what spells the wizard could cast
            viable_spell = []
            for spell in self.known_spells:
                if self.known_spells[spell]["cost"] <= self.current_mana:
                    if spell not in self.active_spells:
                        viable_spell.append(spell)

            # If the wizard can't cast a spell he looses
            if not viable_spell:
                return False, self.spent_mana

            # Pick a spell for the wizard to cast
            cast_spell = random.choice(viable_spell)
            self.wizard_cast(cast_spell)

            # Execute the active spells
            self.execute_active_spells()

            # Check if the boss is dead
            if self.boss_hit_points <= 0:
                return True, self.spent_mana

            # The boss attacks
            self.boss_attack()

            # Check if the player is dead
            if self.player_hit_points <= 0:
                return False, self.spent_mana


results = []
results1 = []

for i in range(100000):

    inst = WizardBattle()
    battle_res = inst.battle()

    if battle_res[0]:
        results.append(battle_res[1])

    inst = WizardBattle(True)
    battle_res = inst.battle()

    if battle_res[0]:
        results1.append(battle_res[1])

# Part 1
print(min(results))

# Part 2
print(min(results1))




