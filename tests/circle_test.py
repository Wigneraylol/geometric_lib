import pytest
from math import pi
from circle import area, perimeter

class TestCircle:
    """Тесты для функций круга"""
    
    def test_perimeter_valid(self):
        """Тест периметра с валидными параметрами"""
        assert perimeter(5.2) == 10.4 * pi
        assert perimeter(2**31) == 2**32 * pi
    
    def test_area_valid(self):
        """Тест площади с валидными параметрами"""
        assert area(1.2) == 1.44 * pi
        assert area(1) == pi

    def test_perimeter_negative(self):
        """ Тест периметра с неположительными параметрами """
        with pytest.raises(ValueError):
            perimeter(0)
        with pytest.raises(ValueError):
            perimeter(-5)

    def test_area_negative(self):
        """ Тест площади с неположительными параметрами """
        with pytest.raises(ValueError):
            area(0)
        with pytest.raises(ValueError):
            area(-5)

    def test_perimeter_invalidtype(self):
        """ Тест периметра с нечисловыми значениями """
        with pytest.raises(TypeError):
            perimeter(True)
        with pytest.raises(TypeError):
            perimeter("Hello")

    def test_area_invalidtype(self):
        """ Тест площади с нечисловыми значениями """
        with pytest.raises(TypeError):
            area(True)
        with pytest.raises(TypeError):
            area("Hello")