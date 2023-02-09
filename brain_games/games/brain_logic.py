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


def even_logic():   # логика только для игры в чётные числа
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer


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


def prime_logic():  # логика только для игры в чётные числа
    question = randint(1, 21)
    count = 0
    for i in range(1, question):
        if question % i == 0:
            count += 1
        else:
            continue
    if count > 1:
        correct_answer = 'no'
    else:
        correct_answer = 'yes'
    return question, correct_answer


def progress_logic():
    prog = []  # будущий список для наполнения его элементами прогрессии
    inc = randint(2, 5)  # инкремент прогрессии
    item_pos = randint(0, 9)  # случайный номер элемента для изъятия из
    # прогрессии
    prog = [i * inc for i in range(1, 11)]  # наполнение прогрессии
    correct_answer = str(prog[item_pos])  # присвоение правильного ответа
    prog[item_pos] = '..'  # заменяю элемент точками в списке
    question = " ".join(map(str, prog))  # формирую "строковый" вариант вопроса
    return question, correct_answer
