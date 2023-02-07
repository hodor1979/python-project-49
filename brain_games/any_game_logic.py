#!/usr/bin/env python3

import sys
import prompt
from brain_games import cli
from brain_games.scripts import brain_games


def main(current_func, introduction):     # логика, общая для любой brain
    # -игры
    brain_games.main()
    name = cli.welcome_user()
    print(introduction)
    for i in range(0, 3):
        [question, correct_answer] = current_func()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
                continue
        else:
            print(f"'{user_answer}' is wrong answer /;(./ Correct answer was "
                  f"{correct_answer}.")
            print(f"Let's try again, {name}!")
            break
    sys.exit()

# if __name__ == "__main__":
#     main()
