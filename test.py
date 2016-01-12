#! /usr/bin/env python3

"""eote-dice tests."""

import unittest

from dice import dice_from_color_char, ProficiencyDice, Side, Symbol


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


if __name__ == '__main__':
    unittest.main()
