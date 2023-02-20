from random import randint


def generate_round():
    first_rand = randint(1, 10)
    second_rand = randint(1, 10)
    question = f'{first_rand} {second_rand}'

    return question, gcd(first_rand, second_rand)


def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if (a % i == 0 and b % i == 0):
            correct_answer = str(i)
            break
    return correct_answer
