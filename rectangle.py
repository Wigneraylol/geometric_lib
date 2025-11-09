def area(a, b): 
    ''' Возвращает площадь прямоугольника с заданными сторонами.
        Параметры:
            a (int or float): длина первой стороны прямоугольника
            b (int or float): длина второй стороны прямоугольника
        
        Возвращаемое значение: 
            (int or float): площадь прямоугольника
            
        Пример вызова:
            rectangle_area = area(2.5 , 4) # rectangle_area = 10.0 '''
    if a < 0 or b < 0 :
        raise ValueError()
    if not(type(a) == float or type(a) == int) or not (type(b) == float or type(b) == int):
        raise TypeError()

    return a * b 

def perimeter(a, b): 
    ''' Возвращает периметр прямоугольника с заданными сторонами.
        Параметры:
            a (int or float): длина первой стороны прямоугольника
            b (int or float): длина второй стороны прямоугольника
        
        Возвращаемое значение: 
            (int or float): периметр прямоугольника
        
        Пример вызова:
            rectangle_perimeter = perimeter(2.5 , 4) # rectangle_perimeter = 13.0'''

    if a < 0 or b < 0 :
        raise ValueError()
    if not(type(a) == float or type(a) == int) or not (type(b) == float or type(b) == int):
        raise TypeError()

    return 2 * (a + b)
