#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import even


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    engine.main(even.generate_round, description)


if __name__ == "__main__":
    main()
