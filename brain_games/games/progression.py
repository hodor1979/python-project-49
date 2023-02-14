from random import randint


def generate_round():
    prog = []
    inc = randint(2, 5)
    item_pos = randint(0, 9)
    prog = [i * inc for i in range(1, 11)]
    correct_answer = str(prog[item_pos])
    prog[item_pos] = '..'
    question = " ".join(map(str, prog))
    return question, correct_answer
