#!/usr/bin/env python3

import any_game_logic

from game_logics import brain_logic

def main():
    intro = 'Answer "yes" if the number is even, otherwise answer "no".'
    any_game_logic.main(brain_logic.even_logic, intro)


if __name__ == "__main__":
    main()
