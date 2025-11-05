import pytest
from rectangle import area, perimeter

class TestRectangle:
    """Тесты для функций прямоугольника"""
    
    def test_perimeter_valid(self):
        """Тест периметра с валидными параметрами"""
        assert perimeter(5, 3) == 16
        assert perimeter(10, 2) == 24
        assert perimeter(7, 7) == 28  
    
    def test_area_valid(self):
        """Тест площади с валидными параметрами"""
        assert area(5, 3) == 15
        assert area(10, 2) == 20
        assert area(4, 4) == 16
    