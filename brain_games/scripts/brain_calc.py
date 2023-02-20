#!/usr/bin/env python3
from brain_games import engine
from brain_games.games import calc


def main():
    description = 'What is the result of the expression?'
    engine.main(calc.generate_round, description)


if __name__ == "__main__":
    main()
