"""
Tests for functions in the main script.
"""

from main import WizardBattle

def test_new_turn_1():
    test = WizardBattle(20, 100, 20, 3)

    test.poison = 4
    test.shield = 5
    test.recharge = 6

    test.new_turn()
    test.new_turn()
    test.new_turn()

    test.poison = 1
    test.shield = 2
    test.recharge = 3


def test_new_turn_2():
    test = WizardBattle(20, 100, 20, 3)

    test.poison = 3
    test.shield = 2
    test.recharge = 1

    test.new_turn()
    test.new_turn()

    test.poison = 0
    test.shield = 0
    test.recharge = 1

def test_new_turn_3():
    test = WizardBattle(20, 100, 20, 3)
    test.poison = 7
    test.shield = 0
    test.recharge = 1

    test.new_turn()
    test.new_turn()

    test.poison = 5
    test.shield = 0
    test.recharge = 0

def test_boss_attack_raw_1():
    test = WizardBattle(20, 100, 20, 3)
    test.boss_attacks()
    test.boss_attacks()
    test.boss_attacks()
    assert test.w_health == 11


def test_boss_attack_raw_2():
    test = WizardBattle(21, 100, 20, 4)
    test.boss_attacks()
    test.boss_attacks()
    assert test.w_health == 13


def test_boss_attack_raw_3():
    test = WizardBattle(35, 100, 20, 5)
    test.boss_attacks()
    assert test.w_health == 30


def test_boss_attack_while_shield_1():
    test = WizardBattle(100, 120, 20, 4)
    test.cast_shield()
    for _ in range(10):
        test.boss_attacks()

    assert test.w_health == 78
    assert test.mana == 7


def test_boss_attack_while_shield_2():
    test = WizardBattle(21, 113, 20, 7)
    test.cast_shield()
    test.boss_attacks()
    test.boss_attacks()
    assert test.w_health == 19
    assert test.mana == 0


def test_boss_attack_while_shield_3():
    test = WizardBattle(21, 120, 20, 8)
    test.cast_shield()
    test.boss_attacks()
    test.boss_attacks()
    assert test.w_health == 19
    assert test.mana == 7


def test_boss_attack_while_shield_4():
    test = WizardBattle(21, 120, 20, 10)
    test.cast_shield()
    test.boss_attacks()
    test.boss_attacks()
    assert test.w_health == 15
    assert test.mana == 7


def test_magic_missile_1():
    test = WizardBattle(21, 500, 20, 10)
    test.cast_missile()
    test.cast_missile()
    test.cast_missile()
    assert test.b_health == 8
    assert test.mana == 341


def test_magic_missile_2():
    test = WizardBattle(21, 53, 20, 10)
    test.cast_missile()
    assert test.b_health == 16
    assert test.mana == 0


def test_magic_missile_3():
    test = WizardBattle(21, 250, 20, 10)
    test.cast_missile()
    test.cast_missile()
    assert test.b_health == 8


def test_drain_1():
    test = WizardBattle(21, 250, 20, 10)
    test.cast_drain()

    assert test.b_health == 18
    assert test.w_health == 23
    assert test.mana == 177


def test_drain_2():
    test = WizardBattle(21, 250, 20, 10)
    test.cast_drain()
    test.cast_drain()

    assert test.b_health == 16
    assert test.w_health == 25
    assert test.mana == 104


def test_drain_3():
    test = WizardBattle(21, 250, 20, 10)
    test.cast_drain()
    test.cast_drain()
    test.cast_drain()

    assert test.b_health == 14
    assert test.w_health == 27
    assert test.mana == 31


def test_shield():
    test = WizardBattle(100, 1000, 100, 4)

    test.cast_shield()
    assert test.mana == 887

    test.boss_attacks()
    assert test.w_health == 99
    test.cast_missile()

    test.boss_attacks()
    assert test.w_health == 98
    test.cast_missile()

    test.boss_attacks()
    assert test.b_health == 97
    test.cast_missile()

    test.boss_attacks()
    assert test.w_health == 93


def test_recharge():
    test = WizardBattle(100, 1000, 100, 4)
    test.cast_recharge()
    assert test.mana == 771

    test.boss_attacks()
    assert test.mana == 872

    test.cast_missile()
    assert test.mana == 920

    test.boss_attacks()
    assert test.mana == 1021

    test.cast_missile()
    assert test.mana == 1069

    test.boss_attacks()
    assert test.mana == 1170

    test.cast_missile()
    assert test.mana == 1218

    test.boss_attacks()
    assert test.mana == 1218


def test_battle_1():
    test = WizardBattle(10, 250, 13, 8)
    test.cast_poison()

    assert test.b_health == 13
    assert test.w_health == 10
    assert test.mana == 77

    test.boss_attacks()

    assert test.b_health == 10
    assert test.w_health == 2
    assert test.mana == 77

    test.cast_missile()

    assert test.b_health == 3
    assert test.w_health == 2
    assert test.mana == 24


def test_battle_2():
    test = WizardBattle(10, 250, 14, 8)
    test.cast_recharge()

    assert test.w_health == 10
    assert test.mana == 21
    assert test.b_health == 14

    test.boss_attacks()

    assert test.w_health == 2
    assert test.mana == 122
    assert test.b_health == 14

    test.cast_shield()

    assert test.w_health == 2
    assert test.mana == 110
    assert test.b_health == 14

    test.boss_attacks()

    assert test.w_health == 1
    assert test.mana == 211
    assert test.b_health == 14

    test.cast_poison()

    assert test.w_health == 3
    assert test.mana == 239
    assert test.b_health == 12

    test.boss_attacks()

    assert test.w_health == 2
    assert test.mana == 340
    assert test.b_health == 12

    test.cast_drain()

    assert test.w_health == 2
    assert test.mana == 167
    assert test.b_health == 12

    test.boss_attacks()

    assert test.w_health == 1
    assert test.mana == 167
    assert test.b_health == 9

    test.cast_missile()

    assert test.w_health == 1
    assert test.mana == 114
    assert test.b_health == 2
