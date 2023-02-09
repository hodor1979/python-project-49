#!/usr/bin/env python3

from brain_games import any_game_logic
from brain_games.games import brain_progression_logic


def main():
    intro = 'What number is missing in this progression?'
    any_game_logic.main(brain_progression_logic.progress_logic, intro)


if __name__ == "__main__":
    main()
