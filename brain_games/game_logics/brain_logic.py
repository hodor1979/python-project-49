import random
from random import randint
def even_logic(): # логика только для игры в чётные числа
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (question, correct_answer)


def calc_logic():
    opers = ['+', '-', '*']  # список арифметических операторов
    a = randint(4, 20)  # случайное число a
    b = randint(4, 20)  # случайное число b
    z = randint(0, 2)  # случайный порядковый номер для выбора оператора
    x = opers[z]  # случайный элемент из списка операторов
    question = '{} {} {} '.format(a, x, b) # формирую вопрос игры
    # print(question)
    # print(f'{a} {x} {b} = {eval(question)}')
    correct_answer = str(eval(question))
    return (question, correct_answer)

def progress_logic():
    prog = []  # будущий список для наполнения его элементами прогрессии
    inc = randint(2, 5)  # инкремент прогрессии
    item_pos = randint(0, 9)  # случайный номер элемента для изъятия из
    # прогрессии
    prog = [i * inc for i in range(1, 11)]  # наполнение прогрессии
    correct_answer = str(prog[item_pos])  # присвоение правильного ответа
    prog[item_pos] = '..'  # заменяю элемент точками в списке
    question = " ".join(map(str, prog)) # формирую "строковый" вариант вопроса
    return (question, correct_answer)
