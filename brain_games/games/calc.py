from random import randint


def generate_round():
    opers = ['+', '-', '*']
    a = randint(4, 20)
    b = randint(4, 20)
    z = randint(0, 2)
    x = opers[z]
    if x == '+':
        question = f'{a}' + '[b]'
        correct_answer = a + b
    if x == '-':
        question = f'{a}' - '[b]'
        correct_answer = a - b
    if x == '*':
        question = f'{a}' * '[b]'
        correct_answer = a * b
    return question, correct_answer
