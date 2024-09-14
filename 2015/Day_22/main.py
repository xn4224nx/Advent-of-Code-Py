"""
--- Day 22: Wizard Simulator 20XX ---
Little Henry Case decides that defeating bosses with swords and stuff is boring.
Now he's playing the game with a wizard. Of course, he gets stuck on another
boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking
alternating turns. The player still goes first. Now, however, you don't get any
equipment; instead, you must choose one of your spells to cast. The first
character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack
normally. However, since you do magic damage, your opponent's armor is ignored,
and so the boss effectively has zero armor as well. As before, if armor (from a
spell, in this case) would reduce damage below 1, it becomes 1 instead - that
is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast. If you
cannot afford to cast any spell, you lose. Spells cost mana; you start with 500
mana, but have no maximum limit. You must have enough mana to cast a spell, and
its cost is immediately deducted when you cast it. Your spells are Magic
Missile, Drain, Shield, Poison, and Recharge.

    -   Magic Missile costs 53 mana. It instantly does 4 damage.

    -   Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit
        points.

    -   Shield costs 113 mana. It starts an effect that lasts for 6 turns. While
        it is active, your armor is increased by 7.

    -   Poison costs 173 mana. It starts an effect that lasts for 6 turns. At
        the start of each turn while it is active, it deals the boss 3 damage.

    -   Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At
        the start of each turn while it is active, it gives you 101 new mana.

Effects all work the same way. Effects apply at the start of both the player's
turns and the boss' turns. Effects are created with a timer (the number of turns
they last); at the start of each turn, after they apply any effect they have,
their timer is decreased by one. If this decreases the timer to zero, the effect
ends. You cannot cast a spell that would start an effect which is already
active. However, effects can be started on the same turn they end.

You start with 50 hit points and 500 mana points.

PART 1: What is the least amount of mana you can spend and still win the fight?
        (Do not include mana recharge effects as "spending" negative mana.)

On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1
hit point. If this brings you to or below 0 hit points, you lose.

PART 2: With the same starting stats for you and the boss, what is the least
        amount of mana you can spend and still win the fight?
"""

import random
import sys


class WizardBattle:
    """
    Simulate a wizard in a battle, casting spells and taking damage from an
    enemy.
    """

    def __init__(self, w_health: int, mana: int, b_health: int, damage: int):
        self.start_w_health = w_health
        self.start_b_health = b_health
        self.start_mana = mana
        self.damage = damage
        self.mana_used = 0

        # Temporary variables
        self.w_health = w_health
        self.b_health = b_health
        self.mana = mana

        # Record the duration of active effects
        self.poison = 0
        self.shield = 0
        self.recharge = 0

        self.spell_costs = {
            "missile": 53,
            "drain": 73,
            "shield": 113,
            "poison": 173,
            "recharge": 229,
        }

        self.cheapest_spell = min([x for x in self.spell_costs.values()])

    def reset_stats():
        """
        Re-initialise the stats of a wizard battle.
        """
        self.w_health = self.start_w_health
        self.b_health = self.start_b_health
        self.mana = self.start_mana

        # Record the duration of active effects
        self.poison = 0
        self.shield = 0
        self.recharge = 0


    def new_turn(self):
        """
        Change the state of the battle at the start of a new turn.
        """
        if self.recharge > 0:
            self.mana += 101
            self.recharge -= 1

        if self.poison > 0:
            self.b_health -= 3
            self.poison -= 1

        if self.shield > 0:
            self.shield -= 1

    def boss_attacks(self):
        """
        Simulate the boss attacking the wizard.
        """
        self.new_turn()

        if self.shield > 0:
            self.w_health -= max(self.damage - 7, 1)
        else:
            self.w_health -= self.damage

    def cast_missile(self):
        """
        Simulate the wizard casting the Magic Missile spell.
        """
        assert self.mana >= self.spell_costs["missile"]
        self.new_turn()

        self.mana -= self.spell_costs["missile"]
        self.mana_used += self.spell_costs["missile"]
        self.b_health -= 4

    def cast_drain(self):
        """
        Simulate the wizard casting the Drain spell.
        """
        assert self.mana >= self.spell_costs["drain"]
        self.new_turn()

        self.mana -= self.spell_costs["drain"]
        self.mana_used += self.spell_costs["drain"]
        self.b_health -= 2
        self.w_health += 2

    def cast_shield(self):
        """
        Simulate the wizard casting the Shield spell.
        """
        assert self.mana >= self.spell_costs["shield"]
        self.new_turn()
        self.shield = 6
        self.mana -= self.spell_costs["shield"]
        self.mana_used += self.spell_costs["shield"]

    def cast_poison(self):
        """
        Simulate the wizard casting the Poison spell.
        """
        assert self.mana >= self.spell_costs["poison"]
        self.new_turn()
        self.poison = 6
        self.mana -= self.spell_costs["poison"]
        self.mana_used += self.spell_costs["poison"]

    def cast_recharge(self):
        """
        Simulate the wizard casting the Recharge spell.
        """
        assert self.mana >= self.spell_costs["recharge"]
        self.new_turn()
        self.recharge = 5
        self.mana -= self.spell_costs["recharge"]
        self.mana_used += self.spell_costs["recharge"]

    def cast_rnd_spell(self):
        """
        Pick a random spell that can be cast with the ammount of mana the
        wizard has.
        """
        viable_spells = [x for x, y in self.spell_costs.items() if y <= self.mana]

        # Catch no viable spells, so nothing can be cast and the wizard has lost
        if not viable_spells:
            return

        rnd_spell = random.choice(viable_spells)

        if rnd_spell == "missile":
            self.cast_missile()

        elif rnd_spell == "drain":
            self.cast_drain()

        elif rnd_spell == "shield":
            self.cast_shield()

        elif rnd_spell == "poison":
            self.cast_poison()

        elif rnd_spell == "recharge":
            self.cast_recharge()

        else:
            raise Exception(f"Unknown spell {rnd_spell} encountered!")

    def battle(self, hard_mode: bool = False) -> bool:
        """
        Simulate a battle between a boss and a wizard. If it returns true then
        the boss has been defeated and the wizard has won.
        """
        while True:

            if hard_mode:
                self.w_health -= 1

            # The wizard loses if they have no health or can't cast a spell
            if self.w_health <= 0 or self.mana < self.cheapest_spell:
                return False
            elif self.b_health <= 0:
                return True

            self.cast_rnd_spell()

            if hard_mode:
                self.w_health -= 1

            # The boss looses if they run out of health
            if self.w_health <= 0:
                return False
            elif self.b_health <= 0:
                return True

            self.boss_attacks()


def find_lowest_mana_to_win(itr: int = 100_000, hard_mode: bool = False) -> int:
    """
    Simulate multiple battles and find the lowest amount of mana it takes to
    win.
    """
    min_mana = sys.maxsize

    for _ in range(itr):
        siml = WizardBattle(50, 500, 51, 9)

        if siml.battle(hard_mode) and siml.mana_used < min_mana:
            min_mana = siml.mana_used
            print(f"New min found: {min_mana}")


    return min_mana


if __name__ == "__main__":
    print(f"Part 1 = {find_lowest_mana_to_win()}")
    print(f"Part 2 = {find_lowest_mana_to_win(hard_mode = True)}")
