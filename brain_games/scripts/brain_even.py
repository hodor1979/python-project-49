#!/usr/bin/env python3

from brain_games import any_game_logic
from brain_games.games import even


def main():
    intro = 'Answer "yes" if the number is even, otherwise answer "no".'
    any_game_logic.main(even.generate_round, intro)


if __name__ == "__main__":
    main()
