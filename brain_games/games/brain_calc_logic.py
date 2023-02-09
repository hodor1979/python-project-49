from random import randint


def calc_logic():
    opers = ['+', '-', '*']  # список арифметических операторов
    a = randint(4, 20)  # случайное число a
    b = randint(4, 20)  # случайное число b
    z = randint(0, 2)  # случайный порядковый номер для выбора оператора
    x = opers[z]  # случайный элемент из списка операторов
    question = '{} {} {} '.format(a, x, b)   # формирую вопрос игры
    correct_answer = str(eval(question))  # вычисляю из выражения
    #  его результат
    return question, correct_answer
