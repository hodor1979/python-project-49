#!/usr/bin/env python3

from brain_games import any_game_logic
from brain_games.game_logics import brain_even_logic


def main():
    intro = 'Answer "yes" if the number is even, otherwise answer "no".'
    any_game_logic.main(brain_even_logic.even_logic, intro)


if __name__ == "__main__":
    main()
