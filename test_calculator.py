import unittest
import math
from calculator import *


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 9), 0)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)
        self.assertAlmostEqual(div(4, 9), 2.25)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(3, 9), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -4)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-9)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)


if __name__ == "__main__":
    unittest.main()