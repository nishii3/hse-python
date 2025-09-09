# Задание 10: Множества
# Реализуйте функции для работы с множествами


def create_set_from_list(lst):
    """
    Создает множество из списка, удаляя дубликаты
    """
    return set(lst)


def is_subset(set1, set2):
    """
    Проверяет, является ли set1 подмножеством set2
    """
    return set1.issubset(set2)


def union_sets(set1, set2):
    """
    Возвращает объединение двух множеств
    """
    return set1 | set2


def intersection_sets(set1, set2):
    """
    Возвращает пересечение двух множеств
    """
    return set1 & set2


def difference_sets(set1, set2):
    """
    Возвращает разность множеств (элементы, которые есть в set1, но отсутствуют в set2)
    """
    return set1 - set2


def symmetric_difference_sets(set1, set2):
    """
    Возвращает симметричную разность множеств
    (элементы, которые есть в одном из множеств, но не в обоих одновременно)
    """
    return union_sets(set1, set2) - intersection_sets(set1, set2)


def remove_duplicates_preserve_order(lst):
    """
    Удаляет дубликаты из списка, сохраняя порядок первого появления элементов
    Используйте множество для отслеживания уже встреченных элементов
    """
    ans = []
    n = set()
    for i in lst:
        if not i in n:
            ans.append(i)
            n.add(i)
    return ans
