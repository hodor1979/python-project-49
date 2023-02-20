#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import progression


def main():
    description = 'What number is missing in the progression?'
    engine.main(progression.generate_round, description)


if __name__ == "__main__":
    main()
