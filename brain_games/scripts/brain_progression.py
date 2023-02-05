#!/usr/bin/env python3

import any_game_logic
from game_logics import brain_logic

def main():
    intro = 'What number is missing in this progression?'
    any_game_logic.main(brain_logic.progress_logic, intro)


if __name__ == "__main__":
    main()