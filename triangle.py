def area(a, h): 
    ''' Возвращает площадь треугольника с заданными стороной и высотой.
        Параметры:
            a (int or float): длина стороны треугольника
            h (int or float): длина высоты треугольника, проведенной к заданной стороне
        
        Возвращаемое значение: 
            (float): площадь треугольника 
            
        Пример вызова:
            triangle_area = area(5, 2) # triangle_area = 5.0'''
    if not(type(a) == float or type(a) == int) or not (type(h) == float or type(h) == int):
        raise TypeError()
        
    if a < 0:
        raise ValueError()
    
    return a * h / 2 

def perimeter(a, b, c): 
    ''' Возвращает периметр треугольника с заданными сторонами.
        Параметры:
            a (int or float): длина первой стороны треугольника
            b (int or float): длина второй стороны треугольника
            c (int or float): длина третьей стороны треугольника
        
        Возвращаемое значение: 
            (int or float): периметр треугольника
            
        Пример вызова:
            triangle_perimeter = perimeter(3, 4, 5) # triangle_perimeter = 12 '''\
    
    if not(type(a) == float or type(a) == int) or not (type(b) == float or type(b) == int) or not (type(c) == float or type(c) == int):
        raise TypeError()

    if a < 0 or b < 0 or c < 0:
        raise ValueError()

    elif (a + b <= c) or (a + c <= b) or (c + b <= a):
        raise ValueError() # Такого треугольника не существует

    return a + b + c 
