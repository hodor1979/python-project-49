#!/usr/bin/env python3

from brain_games import engine
from brain_games.games import gcd


def main():
    description = 'Find the greatest common divisor of given numbers.'
    engine.main(gcd.generate_round, description)


if __name__ == "__main__":
    main()
