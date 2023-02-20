#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import prime


def main():
    description = 'Answer "yes" if given number is prime. Otherwise answer ' \
                  '"no".'
    engine.main(prime.generate_round, description)


if __name__ == "__main__":
    main()
