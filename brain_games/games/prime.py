from random import randint


def generate_round():
    question = randint(1, 99)
    return question, is_prime(question)


def is_prime(num):
    count = 0
    for i in range(1, num):
        if num % i == 0:
            count += 1
        if count > 1:
            break
    if count > 1:
        correct_answer = "no"
    else:
        correct_answer = "yes"
    return correct_answer
