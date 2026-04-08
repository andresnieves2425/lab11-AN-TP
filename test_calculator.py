import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(0, 9), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertAlmostEqual(calculator.divide(4, 9), 2.25)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -4)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(25), 5)
        self.assertAlmostEqual(calculator.square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            calculator.square_root(-9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()