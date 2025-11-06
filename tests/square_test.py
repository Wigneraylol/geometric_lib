import pytest
from square import area, perimeter

class TestRectangle:
    """Тесты для функций квадрата"""
    
    def test_perimeter_valid(self):
        """Тест периметра с валидными параметрами"""
        assert perimeter(5) == 20
        assert perimeter(10) == 40
        assert perimeter(7) == 28
    
    def test_area_valid(self):
        """Тест площади с валидными параметрами"""
        assert area(5) == 25
        assert area(10) == 100
        assert area(4) == 16