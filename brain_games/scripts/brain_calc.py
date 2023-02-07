#!/usr/bin/env python3
from brain_games import any_game_logic
from brain_games.game_logics import brain_calc_logic


def main():
    # brain_games.welcome_user()
    intro = 'What it rhe result of the expression?'
    any_game_logic.main(brain_calc_logic.calc_logic, intro)


if __name__ == "__main__":
    main()
