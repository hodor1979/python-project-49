#!/usr/bin/env python3

from brain_games import any_game_logic
from brain_games.games import progression


def main():
    intro = 'What number is missing in the progression?'
    any_game_logic.main(progression.generate_round, intro)


if __name__ == "__main__":
    main()
