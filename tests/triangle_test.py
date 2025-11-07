import pytest
from triangle import area, perimeter

class TestTriangle:
    """Тесты для функций треугольника"""
    
    def test_perimeter_valid(self):
        """Тест периметра с валидными параметрами"""
        assert perimeter(5, 3.5, 4) == 12.5
        assert perimeter(10.1, 2 , 11) == 23.1
        assert perimeter(25,25,36.7) == 86.7
    
    def test_area_valid(self):
        """Тест площади с валидными параметрами"""
        assert area(5, 3.2) == 8
        assert area(10.1, 2) == 10.1

    def test_perimeter_negative(self):
        """ Тест периметра с неположительными параметрами """
        with pytest.raises(ValueError, match = "values"):
            perimeter(1, -1 , 1)
        with pytest.raises(ValueError, match = "values"):
            perimeter(0, 2 , 3)
        with pytest.raises(ValueError, match = "values"):
            perimeter(5, 3 , -100)

    def test_area_negative(self):
        """ Тест площади с неположительными параметрами """
        with pytest.raises(ValueError, match = "values"):
            perimeter(1, -1 , 1)
        with pytest.raises(ValueError, match = "values"):
            perimeter(0, 2 , 3)
        with pytest.raises(ValueError, match = "values"):
            perimeter(5, 3 , -100)

    def test_perimeter_nosuchtriangle(self):
        """ Тест периметра с параметрами, задающими стороны несуществующего треугольника """
        with pytest.raises(ValueError, match = "no such triangle"):
            perimeter(1, 2, 3)
        with pytest.raises(ValueError, match = "no such triangle"):
            perimeter(100, 100, 201)

    def test_perimeter_invalidtype(self):
        """ Тест периметра с нечисловыми параметрами """
        with pytest.raises(TypeError):
            perimeter("a", 2, 3)
        with pytest.raises(TypeError):
            perimeter(1, "b", 3)
        with pytest.raises(TypeError):
            perimeter(1, 2, "c")

    def test_area_invalidtype(self):
        """ Тест площади с нечисловыми параметрами """
        with pytest.raises(TypeError):
            perimeter("Скоро", 100, 200)
        with pytest.raises(TypeError):
            perimeter(123123, "закончу", 25)
        with pytest.raises(TypeError):
            perimeter(0.2, 0.1, "лабу.")