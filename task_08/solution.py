# Задание 8: Функции
# Реализуйте различные функции согласно их описанию

import math

def greet(name):
    """
    Возвращает приветствие для имени
    Например, "Привет, Иван!"
    """
    return f"Привет, {name}!"


def absolute_value(number):
    """
    Возвращает абсолютное значение числа
    """
    return abs(number)


def calculate_area(shape, *args):
    """
    Вычисляет площадь фигуры

    Параметры:
    - shape: строка, тип фигуры ("circle", "rectangle", "triangle")
    - *args: аргументы для вычисления площади
        - для "circle": радиус
        - для "rectangle": длина и ширина
        - для "triangle": основание и высота

    Возвращает:
    - площадь фигуры или None, если тип фигуры неизвестен
    """
    if shape == "circle":
        return args[0] ** 2 * math.pi
    if shape == "rectangle":
        return args[0] * args[1]
    if shape == "triangle":
        return args[0] * args[1] / 2
    return


def apply_operation(operation, a, b):
    """
    Применяет операцию к двум числам

    Параметры:
    - operation: строка, операция ("add", "subtract", "multiply", "divide")
    - a, b: числа

    Возвращает:
    - результат операции или None, если операция неизвестна
    """
    if operation == "add":
        return a + b
    if operation == "subtract":
        return a - b
    if operation == "multiply":
        return a * b
    if operation == "divide" and b != 0:
        return a / b
    return


def create_multiplier(factor):
    """
    Создает и возвращает функцию, которая умножает свой аргумент на factor

    Пример использования:
    double = create_multiplier(2)
    result = double(5)  # result = 10
    """
    def A(x):
        return x * factor
    return A


def apply_to_each(func, items):
    """
    Применяет функцию func к каждому элементу списка items
    и возвращает список результатов

    Пример использования:
    result = apply_to_each(lambda x: x*2, [1, 2, 3])  # result = [2, 4, 6]
    """
    ans = []
    for i in items:
        ans.append(func(i))
    return ans
