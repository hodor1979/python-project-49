#!/usr/bin/env python3
import prompt
from random import randint    # числа для игры будут генерироваться случайно
import cli
# from scripts.brain_even import current_func
# current_func = ""
# def greet_user():
#     name = cli.welcome_user()


def even_logic(): # логика только для игры в чётные числа
    x = randint(1, 100)
    if x % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return x, correct_answer
# def calc():
#     ###
# current_func = ""
def main(): # логика, свойственная любой brain -игре
    name = cli.welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        x, correct_answer = even_logic() # current_func() # пытаюсь передать
        # из стартовых
        # скриптов функцию при помощи переменной current_func и не получается
        print('Question:', x)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            if i == 2:
                print(f'Congratulations, {name}!')
                continue
        else:
            print(f"'{user_answer}' is wrong answer /;(./ Correct answer was "
                  f"    {correct_answer}.")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    main()