from random import randint


def prime_logic():  # логика только для игры в простые числа
    question = randint(1, 51)
    count = 0
    for i in range(1, question):
        if question % i == 0:
            count += 1
            break
    if count > 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return question, correct_answer
