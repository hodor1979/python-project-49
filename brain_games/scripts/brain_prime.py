#!/usr/bin/env python3

from brain_games import any_game_logic
from brain_games.games import brain_prime_logic


def main():
    intro = "Answer 'yes' if given number is prime. Otherwise answer 'no'."
    any_game_logic.main(brain_prime_logic.prime_logic, intro)


if __name__ == "__main__":
    main()
