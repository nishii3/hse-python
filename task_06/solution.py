# Задание 6: Циклы (while)
# Реализуйте функции с использованием цикла while


def sum_of_digits(number):
    """
    Возвращает сумму цифр числа
    Например, для 123 результат должен быть 1 + 2 + 3 = 6
    """
    ans = 0
    while number > 0:
        ans += number % 10
        number //= 10
    return ans


def count_digits(number):
    """
    Возвращает количество цифр в числе
    Например, для 123 результат должен быть 3
    """
    ans = 0
    if number == 0:
        return 1
    while number > 0:
        ans += 1
        number //= 10
    return ans


def reverse_number(number):
    """
    Возвращает число, записанное в обратном порядке
    Например, для 123 результат должен быть 321
    """
    ans = 0
    while number > 0:
        ans *= 10
        ans += number % 10
        number //= 10
    return ans 


def is_prime(number):
    """
    Проверяет, является ли число простым
    Простое число - это число больше 1, которое делится только на 1 и на само себя
    """
    i = 2
    if number <= 1:
        return False
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    return True


def gcd(a, b):
    """
    Находит наибольший общий делитель (НОД) двух чисел
    Используйте алгоритм Евклида
    """
    while b != 0:
        k = b
        b = a % b
        a = k
    return a

def binary_search(sorted_list, target):
    """
    Реализует бинарный поиск элемента в отсортированном списке
    Возвращает индекс элемента, если он найден, иначе -1
    """
    if not sorted_list:
        return -1
    l = 0
    r = len(sorted_list)
    while r - l > 1:
        m = (l + r) // 2
        if sorted_list[m] > target:
            r = m
        else:
            l = m
    return l if sorted_list[l] == target else -1
    