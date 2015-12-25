#!/usr/bin/env python3

import argparse

from dice import DicePool

import colorama


def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyzes EotE dice pools.')
    parser.add_argument('-p',
                        '--pool',
                        type=str,
                        required=True,
                        help='A string containing the EotE dice pool, annotated using the first '
                             'letter of color of the die (except for black Setback die, which use '
                             '"k".  Example: "yygbrppk".')
    return parser.parse_args()


def main() -> None:
    colorama.init(autoreset=True, strip=False)
    args = parse_arguments()

    try:
        dice_pool = DicePool.from_string(args.pool)

        print('Dice Pool: {}'.format(dice_pool))
        print(dice_pool.rating())
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
