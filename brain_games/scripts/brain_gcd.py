#!/usr/bin/env python3

from brain_games import any_game_logic
from brain_games.games import gcd


def main():
    intro = 'Find the greatest common divisor of given numbers.'
    any_game_logic.main(gcd.generate_round, intro)


if __name__ == "__main__":
    main()
