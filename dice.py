#!/usr/bin/env python3

"""Statical distribution needed for analyzing EotE dice."""

import collections
import enum
import random
from typing import List, Sequence, Tuple

import colorama

from distribution import QuadDistribution


@enum.unique
class Symbol(enum.Enum):
    Triumph = 'T'
    Success = 's'
    Advantage = 'a'

    Despair = 'D'
    Failure = 'f'
    Threat = 'r'


symbol_to_ansi = {
    Symbol.Triumph: colorama.Fore.YELLOW,
    Symbol.Success: colorama.Fore.GREEN,
    Symbol.Advantage: colorama.Fore.CYAN,
    Symbol.Despair: colorama.Fore.RED,
    Symbol.Failure: colorama.Fore.MAGENTA,
    Symbol.Threat: colorama.Fore.BLACK + colorama.Back.WHITE,
}


class Side:
    def __init__(self, symbols: Sequence[Symbol]):
        self._symbols = symbols

    def count_symbol(self, symbol: Symbol) -> int:
        n = 0
        for current_symbol in self.symbols:
            if current_symbol is symbol:
                n += 1
        return n

    @property
    def symbols(self):
        return self._symbols


class Dice:
    def __init__(self, sides: Sequence[Side]):
        self._sides = sides

        mapping = collections.defaultdict(int)
        for side in sides:
            side_triumph = side.count_symbol(Symbol.Triumph)
            side_success = (side.count_symbol(Symbol.Success) +
                            side.count_symbol(Symbol.Triumph) +
                            (-1 * side.count_symbol(Symbol.Failure)) +
                            (-1 * side.count_symbol(Symbol.Despair)))
            side_advantage = (side.count_symbol(Symbol.Advantage) +
                              (-1 * side.count_symbol(Symbol.Threat)))
            side_despair = side.count_symbol(Symbol.Despair)

            mapping[(side_triumph, side_success, side_advantage, side_despair)] += 1

        self.distribution = QuadDistribution(mapping)

    def num_sides(self) -> int:
        return len(self._sides)

    def roll(self) -> Sequence[Symbol]:
        return random.choice(self._sides).symbols


class BoostDice(Dice):
    def __init__(self):
        super().__init__(sides=[
            Side(symbols=[]),
            Side(symbols=[]),
            Side(symbols=[Symbol.Advantage, Symbol.Advantage]),
            Side(symbols=[Symbol.Advantage]),
            Side(symbols=[Symbol.Success, Symbol.Advantage]),
            Side(symbols=[Symbol.Success])
        ])


class AbilityDice(Dice):
    def __init__(self):
        super().__init__(sides=[
            Side(symbols=[]),
            Side(symbols=[Symbol.Success]),
            Side(symbols=[Symbol.Success]),
            Side(symbols=[Symbol.Success, Symbol.Success]),
            Side(symbols=[Symbol.Advantage]),
            Side(symbols=[Symbol.Advantage]),
            Side(symbols=[Symbol.Success, Symbol.Advantage]),
            Side(symbols=[Symbol.Advantage, Symbol.Advantage]),
        ])


class ProficiencyDice(Dice):
    def __init__(self):
        super().__init__(sides=[
            Side(symbols=[]),
            Side(symbols=[Symbol.Success]),
            Side(symbols=[Symbol.Success]),
            Side(symbols=[Symbol.Success, Symbol.Success]),
            Side(symbols=[Symbol.Success, Symbol.Success]),
            Side(symbols=[Symbol.Advantage]),
            Side(symbols=[Symbol.Success, Symbol.Advantage]),
            Side(symbols=[Symbol.Success, Symbol.Advantage]),
            Side(symbols=[Symbol.Success, Symbol.Advantage]),
            Side(symbols=[Symbol.Advantage, Symbol.Advantage]),
            Side(symbols=[Symbol.Advantage, Symbol.Advantage]),
            Side(symbols=[Symbol.Triumph]),
        ])


class SetbackDice(Dice):
    def __init__(self):
        super().__init__(sides=[
            Side(symbols=[]),
            Side(symbols=[]),
            Side(symbols=[Symbol.Failure]),
            Side(symbols=[Symbol.Failure]),
            Side(symbols=[Symbol.Threat]),
            Side(symbols=[Symbol.Threat])
        ])


class DifficultyDice(Dice):
    def __init__(self):
        super().__init__(sides=[
            Side(symbols=[]),
            Side(symbols=[Symbol.Failure]),
            Side(symbols=[Symbol.Failure, Symbol.Failure]),
            Side(symbols=[Symbol.Threat]),
            Side(symbols=[Symbol.Threat]),
            Side(symbols=[Symbol.Threat]),
            Side(symbols=[Symbol.Threat, Symbol.Threat]),
            Side(symbols=[Symbol.Failure, Symbol.Threat])
        ])


class ChallengeDice(Dice):
    def __init__(self):
        super().__init__(sides=[
            Side(symbols=[]),
            Side(symbols=[Symbol.Failure]),
            Side(symbols=[Symbol.Failure]),
            Side(symbols=[Symbol.Failure, Symbol.Failure]),
            Side(symbols=[Symbol.Failure, Symbol.Failure]),
            Side(symbols=[Symbol.Threat]),
            Side(symbols=[Symbol.Threat]),
            Side(symbols=[Symbol.Failure, Symbol.Threat]),
            Side(symbols=[Symbol.Failure, Symbol.Threat]),
            Side(symbols=[Symbol.Threat, Symbol.Threat]),
            Side(symbols=[Symbol.Threat, Symbol.Threat]),
            Side(symbols=[Symbol.Despair])
        ])


@enum.unique
class DiceColor(enum.Enum):
    b = BoostDice
    g = AbilityDice
    y = ProficiencyDice
    k = SetbackDice
    p = DifficultyDice
    r = ChallengeDice

    @classmethod
    def names(cls) -> List[str]:
        names = []
        for dice_color in cls:
            names.append(dice_color.name)
        return names


def dice_from_color_char(color_char: str) -> Dice:
    try:
        dice_color = DiceColor[color_char]
    except KeyError:
        raise ValueError('Invalid dice color: {}.  Possible choices are: {}'.format(
            color_char,
            DiceColor.names()))
    return dice_color.value()


dice_color_to_ansi = {
    DiceColor.y: colorama.Fore.YELLOW,
    DiceColor.g: colorama.Fore.GREEN,
    DiceColor.b: colorama.Fore.CYAN,
    DiceColor.r: colorama.Fore.RED,
    DiceColor.p: colorama.Fore.MAGENTA,
    DiceColor.k: colorama.Fore.BLACK + colorama.Back.WHITE,
}


class DicePoolMean:
    def __init__(self, mean: Tuple[float, float, float, float]):
        self.triumph = mean[0]
        self.success = mean[1]
        self.advantage = mean[2]
        self.despair = mean[3]

    def __str__(self):  # pragma: no cover
        if self.triumph > 0.0:
            triumph_color = colorama.Fore.GREEN
        else:
            triumph_color = colorama.Fore.RESET

        if self.success > 0.0:
            success_color = colorama.Fore.GREEN
        elif self.success < 0.0:
            success_color = colorama.Fore.RED
        else:
            success_color = colorama.Fore.RESET

        if self.advantage > 0.0:
            advantage_color = colorama.Fore.GREEN
        elif self.advantage < 0.0:
            advantage_color = colorama.Fore.RED
        else:
            advantage_color = colorama.Fore.RESET

        if self.despair > 0.0:
            despair_color = colorama.Fore.RED
        else:
            despair_color = colorama.Fore.RESET

        return ('{9}Mean:\n'
                '\tTriumph: {5}{0}{4}\n'
                '\tSuccess: {6}{1}{4}\n'
                '\tAdvantage: {7}{2}{4}\n'
                '\tDespair: {8}{3}{4}'.format(
            round(self.triumph, 2),
            round(self.success, 2),
            round(self.advantage, 2),
            round(self.despair, 2),
            colorama.Fore.RESET,
            triumph_color,
            success_color,
            advantage_color,
            despair_color,
            colorama.Style.BRIGHT))


class DicePool:
    def __init__(self, pool: Sequence[Dice]):
        self._pool = pool

        self.distribution = QuadDistribution()
        for dice in self._pool:
            self.distribution = self.distribution.add(dice.distribution)

    def probability_above(self,
                          triumph_cutoff: int = None,
                          success_cutoff: int = None,
                          advantage_cutoff: int = None,
                          despair_cutoff: int = None) -> float:
        return self.distribution.probability_above(cutoff=(triumph_cutoff,
                                                           success_cutoff,
                                                           advantage_cutoff,
                                                           despair_cutoff))

    def mean(self) -> DicePoolMean:
        return DicePoolMean(self.distribution.mean())

    def roll(self) -> List[Symbol]:
        symbols = []
        for dice in self._pool:
            symbols.extend(dice.roll())
        return symbols

    def roll_ascii(self) -> Tuple[str, str]:
        symbols = self.roll()
        symbols.sort(key=self._sort_symbol_by_power)

        cancelled_symbols = self._cancel_symbols(symbols)
        cancelled_symbols.sort(key=self._sort_symbol_by_power)

        return self._symbols_to_ascii_(symbols), self._symbols_to_ascii_(cancelled_symbols)

    def __str__(self):
        s = ''
        for dice in self._pool:
            dice_color = DiceColor(type(dice))
            color_code = dice_color_to_ansi[dice_color]

            # Do not turn on bright style for black die as it makes it harder to read.
            brightness_code = colorama.Style.BRIGHT
            if dice_color is DiceColor.k:
                brightness_code = ''
            s += '{}{}{}{}'.format(brightness_code, color_code, dice_color.name,
                                   colorama.Style.RESET_ALL)
        return s

    @staticmethod
    def _symbols_to_ascii_(symbols: Sequence[Symbol]) -> str:
        s = ''
        for symbol in symbols:
            brightness_code = colorama.Style.BRIGHT
            if symbol is Symbol.Threat:
                brightness_code = ''
            s += '{}{}{}{}'.format(brightness_code, symbol_to_ansi[symbol], symbol.value,
                                   colorama.Style.RESET_ALL)
        return s

    @staticmethod
    def _cancel_symbols(symbols: Sequence[Symbol]) -> List[Symbol]:
        net_success = 0
        net_advantage = 0

        # Do not inspect Triumph or Despair, because they do not cancel out.
        net_symbols = []
        for symbol in symbols:
            if symbol is Symbol.Success:
                net_success += 1
            elif symbol is Symbol.Advantage:
                net_advantage += 1
            elif symbol is Symbol.Failure:
                net_success -= 1
            elif symbol is Symbol.Threat:
                net_advantage -= 1
            # Allow Triumph and Despair pass through unchanged.
            else:
                net_symbols.append(symbol)

        if net_success >= 0:
            success_symbol = Symbol.Success
        else:
            net_success *= -1
            success_symbol = Symbol.Failure

        if net_advantage >= 0:
            advantage_symbol = Symbol.Advantage
        else:
            net_advantage *= -1
            advantage_symbol = Symbol.Threat

        for i in range(0, net_success):
            net_symbols.append(success_symbol)

        for i in range(0, net_advantage):
            net_symbols.append(advantage_symbol)

        return net_symbols

    @staticmethod
    def _sort_symbol_by_power(symbol: Symbol) -> int:
        if symbol is Symbol.Triumph:
            return 1
        elif symbol is Symbol.Success:
            return 2
        elif symbol is Symbol.Advantage:
            return 3
        elif symbol is Symbol.Despair:
            return 4
        elif symbol is Symbol.Failure:
            return 5
        elif symbol is Symbol.Threat:
            return 6

    @staticmethod
    def _sort_dice_by_power(dice_char: str) -> int:
        try:
            dice_color = DiceColor[dice_char]
            if dice_color is DiceColor.y:
                return 1
            elif dice_color is DiceColor.g:
                return 2
            elif dice_color is DiceColor.b:
                return 3
            elif dice_color is DiceColor.r:
                return 4
            elif dice_color is DiceColor.p:
                return 5
            elif dice_color is DiceColor.k:
                return 6
        except KeyError:
            raise ValueError('Invalid dice character given: {}'.format(dice_char))

    @classmethod
    def from_string(cls, pool_string: str) -> 'DicePool':
        dice_chars = []
        for char in pool_string:
            dice_chars.append(char)

        dice_chars.sort(key=cls._sort_dice_by_power)
        pool = []
        for dice_char in dice_chars:
            pool.append(dice_from_color_char(dice_char))

        return cls(pool)
