#!/usr/bin/env python3

# from brain_games import any_game_logic
import any_game_logic
from game_logics import brain_logic

def main():
    intro = 'Find the greatest common divisor of given numbers.'
    any_game_logic.main(brain_logic.gcd_logic, intro)


if __name__ == "__main__":
    main()
