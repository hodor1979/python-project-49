from random import randint


def generate_round():
    opers = ['+', '-', '*']
    a = randint(4, 20)
    b = randint(4, 20)
    z = randint(0, 2)
    x = opers[z]
    question = '{} {} {} '.format(a, x, b)
    correct_answer = str(eval(question))
    return question, correct_answer
