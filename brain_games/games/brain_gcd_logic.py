from random import randint


def gcd_logic():
    a = randint(1, 10)  # первое случайное число
    b = randint(1, 10)  # второе случайное число
    c = min(a, b)
    for i in range(c, 0, -1):
        if (a % i == 0 and b % i == 0):
            correct_answer = str(i)
            break
    question = f'{a}  {b}'
    return question, correct_answer
