#!/usr/bin/env python3
from scripts import brain_games
import any_game_logic
from game_logics import brain_logic

def main():
    any_game_logic.main(brain_logic.even_logic)


if __name__ == "__main__":
    main()
