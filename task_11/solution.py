# Задание 11: Кортежи
# Реализуйте функции для работы с кортежами


def create_point(x, y):
    """
    Создает кортеж, представляющий точку в двумерном пространстве
    """
    return (x, y)


def get_coordinates(point):
    """
    Возвращает координаты x и y из кортежа-точки
    """
    return point[0], point[1]


def calculate_distance(point1, point2):
    """
    Вычисляет евклидово расстояние между двумя точками
    """
    x1, y1 = get_coordinates(point1)
    x2, y2 = get_coordinates(point2)
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def create_rectangle(top_left, bottom_right):
    """
    Создает кортеж, представляющий прямоугольник
    по координатам верхнего левого и нижнего правого углов
    """
    return (top_left, bottom_right)


def calculate_area(rectangle):
    """
    Вычисляет площадь прямоугольника
    """
    x1, y1 = get_coordinates(rectangle[0])
    x2, y2 = get_coordinates(rectangle[1])
    return abs(x1 - x2) * abs(y1 - y2)


def is_point_inside(rectangle, point):
    """
    Проверяет, находится ли точка внутри прямоугольника
    """
    x1, y1 = get_coordinates(rectangle[0])
    x2, y2 = get_coordinates(rectangle[1])
    x1, x2 = set([x1, x2])
    y1, y2 = set([y1, y2])
    return (x1 <= point[0] <= x2) and (y1 <= point[1] <= y2)


def swap_coordinates(point):
    """
    Меняет местами координаты x и y в точке
    """
    return point[::-1]
