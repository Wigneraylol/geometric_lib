import unittest
from triangle import perimeter as P
from triangle import area as S

class TriangleTestCase(unittest.TestCase):
    def test_int_per(self):
       res = P(12,5,13)
       self.assertEqual(res, 30)

    def test_float_per(self):
       res = P(10.2,21.5,20.1)
       self.assertAlmostEqual(res, 51.8)

    def test_right_per(self):
       res = P(3,3,3)
       self.assertAlmostEqual(res, 9)

    def test_impossible_per(self):
        with self.assertRaises(ValueError):
            P(1,20,100)
       
    def test_negative_per(self):
        with self.assertRaises(ValueError):
            P(-2,-1,-1.5)

    def test_invalidtype_per(self):
        with self.assertRaises(TypeError):
            P("2",2,2)

    def test_int_area(self):
        res = S(10,2)
        self.assertEqual(res, 10)

    def test_float_area(self):
        res = S(10.2,4)
        self.assertAlmostEqual(res, 20.4)

    def test_zero_area(self):
       res = S(5,0)
       self.assertEqual(res, 0)
       
    def test_negative_area(self):
        with self.assertRaises(ValueError):
            S(-2,2)

    def test_invalidtype_area(self):
        with self.assertRaises(TypeError):
            S("2",5)