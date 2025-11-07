import math


def area(r):
    ''' Возвращает площадь круга с заданным радиусом.
        Параметры:
            r (int or float): радиус круга
        
        Возвращаемое значение: 
           (float): площадь круга
           
        Пример вызова: 
            circle_area = area(5) # circle_area = 78.53981633974483'''

    if r <= 0:
        raise ValueError()
    if not(type(r) == float or type(r) == int):
        raise TypeError()

    return math.pi * round(r * r, 10)


def perimeter(r):
    ''' Возвращает периметр круга с заданным радиусом.
        Параметры:
            r (int or float): радиус круга
        
        Возвращаемое значение: 
            (float): периметр круга
        
        Пример вызова: 
            circle_perimeter = perimeter(5) # circle_perimeter = 31.41592653589793'''

    if r <= 0:
        raise ValueError()
    if not(type(r) == float or type(r) == int):
        raise TypeError()

    return 2 * math.pi * r

