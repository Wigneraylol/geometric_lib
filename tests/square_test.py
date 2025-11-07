import pytest
from square import area, perimeter

class TestSquare:
    """Тесты для функций квадрата"""
    
    def test_perimeter_valid(self):
        """Тест периметра с валидными параметрами"""
        assert perimeter(5.25) == 21
        assert perimeter(10) == 40
    
    def test_area_valid(self):
        """Тест площади с валидными параметрами"""
        assert area(5) == 25
        assert area(0.4) == 0.16

    def test_perimeter_negative(self):
        """Тест периметра с неположительным параметром"""
        with pytest.raises(ValueError):
            perimeter(0)
        with pytest.raises(ValueError):
            perimeter(-2)

    def test_perimeter_negative(self):
        """Тест площади с неположительным параметром"""
        with pytest.raises(ValueError):
            area(0)
        with pytest.raises(ValueError):
            area(-2)

    def test_perimeter_invalidtype(self):
        """Тест периметра с нечисловым параметром"""
        with pytest.raises(TypeError):
            perimeter("2")
        with pytest.raises(TypeError):
            perimeter("Лабы")

    def test_area_invalidtype(self):
        """Тест площади с нечисловым параметром"""
        with pytest.raises(TypeError):
            area("2")
        with pytest.raises(TypeError):
            area("ИТМО")