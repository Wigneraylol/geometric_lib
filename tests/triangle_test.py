import pytest
from triangle import area, perimeter

class TestRectangle:
    """Тесты для функций треугольника"""
    
    def test_perimeter_valid(self):
        """Тест периметра с валидными параметрами"""
        assert perimeter(5, 3, 4) == 12
        assert perimeter(10, 2 , 11) == 23
        assert perimeter(7, 7 ,7) == 21
    
    def test_area_valid(self):
        """Тест площади с валидными параметрами"""
        assert area(5, 3) == 7.5
        assert area(10, 2) == 10
        assert area(4, 4) == 8