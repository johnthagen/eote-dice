#!/usr/bin/env python3

import argparse

from dice import DicePool

import colorama


def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyzes or rolls SW EotE dice pools.')
    parser.add_argument('-p',
                        '--pool',
                        type=str,
                        required=True,
                        help='A string containing the EotE dice pool, annotated using the first '
                             'letter of color of the die (except for black Setback die, which use '
                             '"k".  Example: "yygbrppk".')

    command_group = parser.add_mutually_exclusive_group(required=True)
    command_group.add_argument('-a',
                               '--analyze',
                               action='store_true',
                               help='Statistically analyze the dice pool.')
    command_group.add_argument('-r',
                               '--roll',
                               action='store_true',
                               help='Roll the dice pool.')
    return parser.parse_args()


def main() -> None:
    colorama.init(autoreset=True, strip=False)
    args = parse_arguments()

    try:
        dice_pool = DicePool.from_string(args.pool)
        print('Dice Pool: {}'.format(dice_pool))

        if args.analyze:
            print(dice_pool.rating())
        elif args.roll:
            symbols_ascii, cancelled_symbols_ascii = dice_pool.roll_ascii()
            print('Full Roll: {}'.format(symbols_ascii))
            print('Net Roll:  {}'.format(cancelled_symbols_ascii))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
