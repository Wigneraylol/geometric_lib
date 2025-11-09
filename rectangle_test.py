import unittest
from rectangle import perimeter as P
from rectangle import area as S

class RectangleTestCase(unittest.TestCase):
    def test_int_per(self):
       res = P(10, 5)
       self.assertEqual(res, 30)

    def test_float_per(self):
       res = P(10.2, 5.5)
       self.assertEqual(res, 31.4)

    def test_zero_per(self):
       res = P(10, 0)
       self.assertEqual(res, 20)
       
    def test_square_per(self):
       res = P(10, 10)
       self.assertEqual(res, 40)
    
    def test_negative_per(self):
        with self.assertRaises(ValueError):
            P(-2,10)
        with self.assertRaises(ValueError):
            P(10,-2)

    def test_invalidtype_per(self):
        with self.assertRaises(TypeError):
            P(12, "2")
        with self.assertRaises(TypeError):
            P("3",12)

    def test_int_area(self):
        res = S(10,12)
        self.assertEqual(res,120)

    def test_float_area(self):
        res = S(10.2,12.5)
        self.assertAlmostEqual(res,127.5)

    def test_zero_area(self):
       res = S(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_area(self):
       res = S(10, 10)
       self.assertEqual(res, 100)
    
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            S(-2,10)
        with self.assertRaises(ValueError):
            S(10,-2)

    def test_invalidtype_area(self):
        with self.assertRaises(TypeError):
            S(12, "2")
        with self.assertRaises(TypeError):
            S("3",12)
