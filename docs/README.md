# Geometric_lib

## Описание 
Проект **geometric_lib** представляет из себя 4 модуля (*circle.py, rectangle.py, square.py, triangle.py*) на языке **Python**, содержащих функции для вычисления площади и периметра основных плоских геометрических фигур (*круг, прямоугольник, квадрат и треугольник*)

## Используемые формулы для вычисления площадей:
- Круг: **S = πR²**
- Прямоугольник: **S = ab**
- Квадрат: **S = a²**
- Треугольник: **S = ah / 2**

##  Используемые формулы для вычисления периметров:
- Круг: **P = 2πR**
- Прямоугольник: **P = 2a + 2b**
- Квадрат: **P = 4a**
- Треугольник: **P = a + b + c**

# Модули и функции
## Модуль circle.py

### 1. `area(r)`

**Описание:**
Возвращает площадь круга с заданным радиусом.

**Параметры:**
*   `r` (`int` or `float`) : радиус круга

**Возвращаемое значение:**
*   (`float`) : площадь круга

**Пример вызова:**

```python
import circle
result = circle.area(5)
print(result) # 78.53981633974483
```

### 2. `perimeter(r)`

**Описание:**
Возвращает периметр круга с заданным радиусом.

**Параметры:**
*   `r` (`int` or `float`) : радиус круга

**Возвращаемое значение:**
*   (`float`) : периметр круга

**Пример вызова:**

```python
import circle
result = circle.perimeter(5)
print(result) # 31.41592653589793
```

## Модуль rectangle.py

### 1. `area(a, b)`

**Описание:**
Возвращает площадь прямоугольника с заданными сторонами.

**Параметры:**
*   `a` (`int` or `float`): длина первой стороны прямоугольника
*   `b` (`int` or `float`): длина второй стороны прямоугольника

**Возвращаемое значение:**
*   (`int` or `float`): площадь прямоугольника

**Пример вызова:**

```python
import rectangle
result = rectangle.area(2.5, 4)
print(result) # 10.0
```

### 2. `perimeter(a, b)`

**Описание:**
Возвращает периметр прямоугольника с заданными сторонами.

**Параметры:**
*   `a` (`int` or `float`): длина первой стороны прямоугольника
*   `b` (`int` or `float`): длина второй стороны прямоугольника

**Возвращаемое значение:**
*   (`int` or `float`): периметр прямоугольника

**Пример вызова:**

```python
import rectangle
result = rectangle.perimeter(2.5, 4)
print(result) # 13.0
```
## Модуль square.py

### 1. `area(a)`

**Описание:**
Возвращает площадь квадрата с заданной стороной.

**Параметры:**
*   `a` (`int` or `float`): длина стороны квадрата

**Возвращаемое значение:**
*   (`int` or `float`): площадь квадрата

**Пример вызова:**

```python
import square
result = square.area(4)
print(result) # 16
```

### 2. `perimeter(a)`

**Описание:**
Возвращает периметр квадрата с заданной стороной.

**Параметры:**
*   `a` (`int` or `float`): длина стороны квадрата

**Возвращаемое значение:**
*   (`int` or `float`): периметр квадрата

**Пример вызова:**

```python
import square
result = square.perimeter(5.25)
print(result) # 21.0
```
## Модуль triangle.py

### 1. `area(a, h)`

**Описание:**
Возвращает площадь треугольника с заданными стороной и высотой.

**Параметры:**
*   `a` (`int` or `float`): длина стороны треугольника
*   `h` (`int` or `float`): длина высоты треугольника, проведенной к заданной стороне

**Возвращаемое значение:**
*   (`int` or `float`): площадь треугольника

**Пример вызова:**

```python
import triangle
result = triangle.area(5, 2)
print(result) # 5.0
```

### 2. `perimeter(a, b, c)`

**Описание:**
Возвращает периметр треугольника с заданными сторонами.

**Параметры:**
*   `a` (`int` or `float`): длина первой стороны треугольника
*   `b` (`int` or `float`): длина второй стороны треугольника
*   `c` (`int` or `float`): длина третьей стороны треугольника

**Возвращаемое значение:**
*   (`int` or `float`): периметр треугольника

**Пример вызова:**

```python
import triangle
result = triangle.perimeter(3, 4, 5)
print(result) # 12
```
# Тесты

## Unit tests

### circle.py

- Правильный ответ при входных int/float (area и perimeter)
- ValueError при входных < 0 (area и perimeter)
- TypeError при входных !(int or float) (area и perimeter)

### rectangle.py

- Правильный ответ при входных int/float (area и perimeter)
- ValueError при входных < 0 (area и perimeter)
- TypeError при входных !(int or float) (area и perimeter)

### square.py

- Правильный ответ при входных int/float (area и perimeter)
- ValueError при входных < 0 (area и perimeter)
- TypeError при входных !(int or float) (area и perimeter)

### triangle.py

- Правильный ответ при входных int/float (area и perimeter)
- ValueError при входных < 0 (area и perimeter)
- ValueError при входных данных, при которых треугольник не существует (perimeter)
- TypeError при входных !(int or float) (area и perimeter)




# История коммитов

## Commit 3 
- Hash: **844c31868f8c90100884d22e19851f748e9beb56**
- Author: **Wigner** <wigneraylol@gmail.com>
- Date: Sun Nov 9 14:56:08 2025 +0300
- **Added unit test for all modules**

## Commit 2 
- Hash: **ba695bd9b11cfd220a3b4ef221c0b629d37f2347**
- Author: **Wigner** <wigneraylol@gmail.com>
- Date:   Sun Oct 12 12:46:58 2025 +0300
- **"Added new file triangle.py and fixed mistake in rectangle.py"**

## Commit 1 
- Hash: **f5f4e0e8088029f8d648b677c552f9989858c81b**
- Author: **Wigner** <wigneraylol@gmail.com>
- Date:   Sun Oct 12 12:44:49 2025 +0300
- **"Added new file rectangle.py"**


