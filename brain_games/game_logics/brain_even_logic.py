from random import randint


def even_logic():   # логика только для игры в чётные числа
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
