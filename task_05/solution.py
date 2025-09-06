# Задание 5: Циклы (for)
# Реализуйте функции с использованием цикла for


def sum_of_numbers(n):
    """
    Возвращает сумму чисел от 1 до n включительно
    """
    return n * (n + 1) // 2


def factorial(n):
    """
    Возвращает факториал числа n (произведение чисел от 1 до n)
    Для n <= 1 возвращает 1
    """
    if n <= 1:
        return 1
    k = 1
    for i in range(2, n + 1):
        k *= i
    return k


def count_vowels(s):
    """
    Возвращает количество гласных букв в строке s
    Гласные: 'a', 'e', 'i', 'o', 'u' (регистр не имеет значения)
    """
    let = ['a', 'e', 'i', 'o', 'u']
    s = s.lower()
    ans = 0
    for i in let:
        ans += s.count(i)
    return ans


def find_max(numbers):
    """
    Возвращает максимальное число из списка numbers
    Если список пуст, возвращает None
    """
    if not numbers:
        return None
    return max(numbers)


def filter_even_numbers(numbers):
    """
    Возвращает новый список, содержащий только четные числа из списка numbers
    """
    a = []
    for i in numbers:
        if abs(i) % 2 == 0:
            a.append(i)
    return a


def generate_multiplication_table(n):
    """
    Возвращает таблицу умножения размером n x n в виде списка списков
    Например, для n=3 результат должен быть:
    [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    """
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            a[i][j] = (i + 1) * (j + 1)
    return a
