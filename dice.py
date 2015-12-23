#!/usr/bin/env python3

import enum
import itertools
from typing import Sequence

import colorama

_enum_value = itertools.count(1)


@enum.unique
class Symbol(enum.Enum):
    Blank = next(_enum_value)

    Triumph = next(_enum_value)
    Success = next(_enum_value)
    Advantage = next(_enum_value)

    Despair = next(_enum_value)
    Failure = next(_enum_value)
    Threat = next(_enum_value)


class Side:
    def __init__(self, symbols: Sequence[Symbol]):
        self.symbols = symbols


class Rating:
    def __init__(self, triumph, success, advantage, despair):
        self.triumph = triumph
        self.success = success
        self.advantage = advantage
        self.despair = despair

    def __str__(self):
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

        return ('{9}Rating:\n'
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


class Dice:
    def __init__(self, sides: Sequence[Side]):
        self._sides = sides

    def num_sides(self):
        return len(self._sides)

    def rating(self) -> Rating:
        num_triumph = 0
        net_success = 0
        net_advantage = 0
        num_despair = 0

        for side in self._sides:
            for symbol in side.symbols:
                if symbol is Symbol.Triumph:
                    num_triumph += 1
                if (symbol is Symbol.Success or
                   symbol is Symbol.Triumph):
                    net_success += 1
                elif symbol is Symbol.Advantage:
                    net_advantage += 1
                elif symbol is Symbol.Despair:
                    num_despair += 1
                elif (symbol is Symbol.Failure or
                      symbol is Symbol.Despair):
                    net_success -= 1
                elif symbol is Symbol.Threat:
                    net_advantage -= 1

        return Rating(num_triumph / self.num_sides(),
                      net_success / self.num_sides(),
                      net_advantage / self.num_sides(),
                      num_despair / self.num_sides())


class BoostDice(Dice):
    def __init__(self):
        super().__init__(sides=[
            Side(symbols=[Symbol.Blank]),
            Side(symbols=[Symbol.Blank]),
            Side(symbols=[Symbol.Advantage, Symbol.Advantage]),
            Side(symbols=[Symbol.Advantage]),
            Side(symbols=[Symbol.Success, Symbol.Advantage]),
            Side(symbols=[Symbol.Success])
            ])


class AbilityDice(Dice):
        def __init__(self):
            super().__init__(sides=[
                Side(symbols=[Symbol.Blank]),
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
            Side(symbols=[Symbol.Blank]),
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
            Side(symbols=[Symbol.Blank]),
            Side(symbols=[Symbol.Blank]),
            Side(symbols=[Symbol.Failure]),
            Side(symbols=[Symbol.Failure]),
            Side(symbols=[Symbol.Threat]),
            Side(symbols=[Symbol.Threat])
            ])


class DifficultyDice(Dice):
    def __init__(self):
        super().__init__(sides=[
            Side(symbols=[Symbol.Blank]),
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
            Side(symbols=[Symbol.Blank]),
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
    def names(cls):
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
    DiceColor.b: colorama.Fore.CYAN,
    DiceColor.g: colorama.Fore.GREEN,
    DiceColor.y: colorama.Fore.YELLOW,
    DiceColor.k: colorama.Fore.BLACK + colorama.Back.WHITE,
    DiceColor.p: colorama.Fore.MAGENTA,
    DiceColor.r: colorama.Fore.RED
}


class DicePool:
    def __init__(self, pool: Sequence[Dice]):
        self._pool = pool

    def rating(self):
        total_triumph = 0.0
        total_success = 0.0
        total_advantage = 0.0
        total_despair = 0.0

        for dice in self._pool:
            current_rating = dice.rating()  # type: Rating
            total_triumph += current_rating.triumph
            total_success += current_rating.success
            total_advantage += current_rating.advantage
            total_despair += current_rating.despair

        return Rating(total_triumph, total_success, total_advantage, total_despair)

    def __str__(self):
        s = ''
        for dice in self._pool:
            dice_color = DiceColor(type(dice))
            color_code = dice_color_to_ansi[dice_color]

            # Do not turn on bright style for black die as it makes it harder to read.
            brightness_code = colorama.Style.BRIGHT
            if dice_color is DiceColor.k:
                brightness_code = ''
            s += ('{}{}{}{}'.format(brightness_code, color_code, dice_color.name,
                                    colorama.Style.RESET_ALL))
        return s

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
    def from_string(cls, pool_string: str) -> 'DiceColor':
        dice_chars = []
        for char in pool_string:
            dice_chars.append(char)

        dice_chars.sort(key=cls._sort_dice_by_power)
        pool = []
        for dice_char in dice_chars:
            pool.append(dice_from_color_char(dice_char))

        return cls(pool)
