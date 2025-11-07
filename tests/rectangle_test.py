import pytest
from rectangle import area, perimeter

class TestRectangle:
    """Тесты для функций прямоугольника"""
    
    def test_perimeter_valid(self):
        """Тест периметра с валидными параметрами"""
        assert perimeter(5, 3.6) == 17.2
        assert perimeter(2.3, 10) == 24.6
    
    def test_area_valid(self):
        """Тест площади с валидными параметрами"""
        assert area(5, 5.5) == 27.5
        assert area(1.2, 1) == 1.2

    def test_perimeter_negative(self):
        """Тест периметра с неположительными параметрами"""
        with pytest.raises(ValueError):
            perimeter(2, 0)
        with pytest.raises(ValueError):
            perimeter(-2 , 2)

    def test_perimeter_negative(self):
        """Тест площади с неположительными параметрами"""
        with pytest.raises(ValueError):
            area(2, 0)
        with pytest.raises(ValueError):
            area(-2 , 2)

    def test_perimeter_invalidtype(self):
        """Тест периметра с нечисловыми параметрами"""
        with pytest.raises(TypeError):
            perimeter(2, "2")
        with pytest.raises(TypeError):
            perimeter("ИСРПО" , 2)

    def test_area_invalidtype(self):
        """Тест площади с нечисловыми параметрами"""
        with pytest.raises(TypeError):
            area(2, "2")
        with pytest.raises(TypeError):
            area("Юнит тесты" , 2)
