import unittest
from square import perimeter as P
from square import area as S

class SquareTestCase(unittest.TestCase):
    def test_int_per(self):
       res = P(10)
       self.assertEqual(res, 40)

    def test_float_per(self):
       res = P(10.2)
       self.assertAlmostEqual(res, 40.8)

    def test_zero_per(self):
       res = P(0)
       self.assertEqual(res, 0)
       
    def test_negative_per(self):
        with self.assertRaises(ValueError):
            P(-2)

    def test_invalidtype_per(self):
        with self.assertRaises(TypeError):
            P("2")

    def test_int_area(self):
        res = S(10)
        self.assertEqual(res, 100)

    def test_float_area(self):
        res = S(10.2)
        self.assertAlmostEqual(res, 104.04)

    def test_zero_area(self):
       res = S(0)
       self.assertEqual(res, 0)
       
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            S(-2)

    def test_invalidtype_area(self):
        with self.assertRaises(TypeError):
            S("2")