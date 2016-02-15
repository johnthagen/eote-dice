#! /usr/bin/env python3

"""eote-dice tests."""

import unittest

# from eote_dice import parse_arguments
from dice import (AbilityDice, BoostDice, ChallengeDice, DicePool, dice_from_color_char,
                  DifficultyDice, ProficiencyDice, SetbackDice, Side, Symbol)


class SideTestCase(unittest.TestCase):
    def test_count_symbol(self):
        side = Side(symbols=[Symbol.Triumph, Symbol.Triumph, Symbol.Despair])
        self.assertEqual(side.count_symbol(Symbol.Triumph), 2)
        self.assertEqual(side.count_symbol(Symbol.Despair), 1)
        self.assertEqual(side.count_symbol(Symbol.Success), 0)


class DiceFromColorTestCase(unittest.TestCase):
    def test_invalid_dice_char(self):
        with self.assertRaises(ValueError):
            dice_from_color_char('z')

    def test_valid_dice_char(self):
        self.assertIsInstance(dice_from_color_char('y'), ProficiencyDice)
        self.assertIsInstance(dice_from_color_char('b'), BoostDice)
        self.assertIsInstance(dice_from_color_char('g'), AbilityDice)
        self.assertIsInstance(dice_from_color_char('k'), SetbackDice)
        self.assertIsInstance(dice_from_color_char('p'), DifficultyDice)
        self.assertIsInstance(dice_from_color_char('r'), ChallengeDice)


class DiceTestCase(unittest.TestCase):
    def test_num_sides(self):
        self.assertEqual(ProficiencyDice().num_sides(), 12)
        self.assertEqual(BoostDice().num_sides(), 6)

    def test_boost_roll(self):
        symbols = BoostDice().roll()
        self.assertGreaterEqual(len(symbols), 0)
        self.assertLessEqual(len(symbols), 2)
        if len(symbols) > 0:
            self.assertIsNot(symbols[0], Symbol.Triumph)
            self.assertIsNot(symbols[0], Symbol.Despair)
            self.assertIsNot(symbols[0], Symbol.Failure)
            self.assertIsNot(symbols[0], Symbol.Threat)

    def test_difficulty_roll(self):
        symbols = DifficultyDice().roll()
        self.assertGreaterEqual(len(symbols), 0)
        self.assertLessEqual(len(symbols), 2)
        if len(symbols) > 0:
            self.assertIsNot(symbols[0], Symbol.Triumph)
            self.assertIsNot(symbols[0], Symbol.Despair)
            self.assertIsNot(symbols[0], Symbol.Success)
            self.assertIsNot(symbols[0], Symbol.Advantage)


class DicePoolTestCase(unittest.TestCase):
    def test_from_string(self):
        DicePool.from_string('yygbrppk')

    def test_invalid_from_string(self):
        with self.assertRaises(ValueError):
            DicePool.from_string('yyx')

if __name__ == '__main__':
    unittest.main()
