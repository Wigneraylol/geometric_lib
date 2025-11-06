import pytest
from circle import area, perimeter

class TestRectangle:
    """Тесты для функций круга"""
    
    def test_perimeter_valid(self):
        """Тест периметра с валидными параметрами"""
        assert perimeter(5) == 31.41592653589793
        assert perimeter(10) == 62.83185307179586
        assert perimeter(7) == 43.982297150257104  
    
    def test_area_valid(self):
        """Тест площади с валидными параметрами"""
        assert area(5) == 78.53981633974483
        assert area(10) == 314.1592653589793
        assert area(4) == 50.26548245743669