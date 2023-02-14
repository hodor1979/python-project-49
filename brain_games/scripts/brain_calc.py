#!/usr/bin/env python3
from brain_games import any_game_logic
from brain_games.games import calc


def main():
    intro = 'What is the result of the expression?'
    any_game_logic.main(calc.generate_round, intro)


if __name__ == "__main__":
    main()
