#!/usr/bin/env python3

import argparse
import sys

from dice import DicePool

import colorama


def parse_arguments():
    parser = argparse.ArgumentParser(description='Analyzes or rolls SW EotE dice pools.')
    parser.add_argument('-p',
                        '--pool',
                        type=str,
                        required=True,
                        help='A string containing the EotE dice pool, annotated using the first '
                             'letter of color of the die (except for black Setback dice, '
                             'which use "k".  Example: "yygbrppk".')

    parser.add_argument('-r',
                        '--roll',
                        action='store_true',
                        help='Roll the dice pool.')

    subparsers = parser.add_subparsers()
    analysis_parser = subparsers.add_parser('analyze', help='Analysis commands.')
    analysis_parser.add_argument('-t',
                                 '--triumph-cutoff',
                                 type=int,
                                 required=False,
                                 default=None,
                                 help='Return probability of at least this many triumph.')
    analysis_parser.add_argument('-s',
                                 '--success-cutoff',
                                 type=int,
                                 required=False,
                                 default=None,
                                 help='Return probability of at least this many success.')
    analysis_parser.add_argument('-a',
                                 '--advantage-cutoff',
                                 type=int,
                                 required=False,
                                 default=None,
                                 help='Return probability of at least this many advantage.')
    analysis_parser.add_argument('-d',
                                 '--despair-cutoff',
                                 type=int,
                                 required=False,
                                 default=None,
                                 help='Return probability of at least this many despair.')

    return parser.parse_args()


def main() -> None:
    colorama.init(autoreset=True, strip=False)
    args = parse_arguments()

    try:
        dice_pool = DicePool.from_string(args.pool)
        print('Dice Pool: {}'.format(dice_pool))

        if hasattr(args, 'triumph_cutoff'):
            print(dice_pool.mean())
            if (args.triumph_cutoff is not None or
               args.success_cutoff is not None or
               args.advantage_cutoff is not None or
               args.despair_cutoff is not None):
                probability_above = dice_pool.probability_above(
                    triumph_cutoff=args.triumph_cutoff,
                    success_cutoff=args.success_cutoff,
                    advantage_cutoff=args.advantage_cutoff,
                    despair_cutoff=args.despair_cutoff)
                if probability_above >= 0.5:
                    probability_color = colorama.Fore.GREEN
                else:
                    probability_color = colorama.Fore.RED

                print('{}Probability Above: {}{}%{}'.format(
                    colorama.Style.BRIGHT,
                    probability_color,
                    round(probability_above, 2) * 100,
                    colorama.Style.RESET_ALL))
                if args.triumph_cutoff is not None:
                    print('\tTriumph: {}'.format(args.triumph_cutoff))
                if args.success_cutoff is not None:
                    print('\tSuccess: {}'.format(args.success_cutoff))
                if args.advantage_cutoff is not None:
                    print('\tAdvantage: {}'.format(args.advantage_cutoff))
                if args.despair_cutoff is not None:
                    print('\tDespair: {}'.format(args.despair_cutoff))
        elif args.roll:
            symbols_ascii, cancelled_symbols_ascii = dice_pool.roll_ascii()
            print('Full Roll: {}'.format(symbols_ascii))
            print('Net Roll:  {}'.format(cancelled_symbols_ascii))
        else:
            print('No command specified, see --help.', file=sys.stderr)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
