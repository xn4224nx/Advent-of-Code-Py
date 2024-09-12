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
"""


class WizardBattle:
    """
    Simulate a wizard in a battle, casting spells and taking damage from an
    enemy.
    """

    def __init__(self, w_health, mana, b_health, damage):
        self.w_health = w_health
        self.b_health = b_health
        self.mana = mana
        self.damage = damage
        self.mana_used = 0

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
        assert self.mana >= 53
        self.new_turn()

        self.mana -= 53
        self.b_health -= 4

    def cast_drain(self):
        pass

    def cast_shield(self):
        pass

    def cast_poison(self):
        pass

    def cast_recharge(self):
        pass

    def cast_rnd_spell(self):
        pass

    def battle(self):
        pass


if __name__ == "__main__":
    pass
