# Задание 7: Списки и операции со списками
# Реализуйте функции для работы со списками


def create_list(start, end, step=1):
    """
    Создает список чисел от start до end (включительно) с шагом step
    """
    if step > 0:
        return [i for i in range(start, end + 1, step)]
    return [i for i in range(start, end - 1, step)]
        


def find_element_index(lst, element):
    """
    Находит индекс первого вхождения элемента в список
    Если элемент не найден, возвращает -1
    """
    if element in lst:
        return lst.index(element)
    return -1


def remove_duplicates(lst):
    """
    Удаляет дубликаты из списка, сохраняя порядок элементов
    """
    return list(dict.fromkeys(lst))


def merge_lists(list1, list2):
    """
    Объединяет два списка в один, удаляя дубликаты
    """
    return remove_duplicates(list1 + list2)


def list_intersection(list1, list2):
    """
    Возвращает список элементов, которые есть в обоих списках
    """
    return list(set(list1).intersection(set(list2)))


def list_difference(list1, list2):
    """
    Возвращает список элементов, которые есть в list1, но отсутствуют в list2
    """
    return list(set(list1) - set(list2))


def flatten_list(nested_list):
    """
    Преобразует вложенный список в плоский
    Например, [1, [2, 3], [4, [5, 6]]] -> [1, 2, 3, 4, 5, 6]
    """
    ans = []
    for i in nested_list:
        if isinstance(i, list):
            ans.extend(flatten_list(i))
        else:
            ans.append(i)
    return ans
