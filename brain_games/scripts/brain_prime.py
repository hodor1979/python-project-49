#!/usr/bin/env python3

from brain_games import any_game_logic
from brain_games.games import prime


def main():
    intro = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    any_game_logic.main(prime.generate_round, intro)


if __name__ == "__main__":
    main()
