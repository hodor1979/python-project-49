from random import randint


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
