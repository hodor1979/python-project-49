#!/usr/bin/env python3

from brain_games import any_game_logic
from brain_games.game_logics import brain_gcd_logic


def main():
    intro = 'Find the greatest common divisor of given numbers.'
    any_game_logic.main(brain_gcd_logic.gcd_logic, intro)


if __name__ == "__main__":
    main()
