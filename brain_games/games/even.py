from random import randint


def generate_round():
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
