import unittest
from circle import perimeter as P
from circle import area as S

class CircleTestCase(unittest.TestCase):
    def test_int_per(self):
       res = P(10)
       self.assertAlmostEqual(res, 62.831853071)

    def test_float_per(self):
       res = P(10.2)
       self.assertAlmostEqual(res, 64.08849013)

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
        self.assertAlmostEqual(res,314.15926535)

    def test_float_area(self):
        res = S(10.2)
        self.assertAlmostEqual(res,326.851299679)

    def test_zero_area(self):
       res = S(0)
       self.assertEqual(res, 0)
       
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            S(-2)

    def test_invalidtype_area(self):
        with self.assertRaises(TypeError):
            S("2")