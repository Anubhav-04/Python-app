import unittest
from app import *

class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.c = Calculate()

    def test_add(self):
        self.assertEqual(self.c.add(2, 3), 5)
        self.assertEqual(self.c.add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.c.subtract(5, 3), 2)
        self.assertEqual(self.c.subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(self.c.Multiply(2, 3), 6)
        self.assertEqual(self.c.Multiply(-1, 8), -8)
        self.assertEqual(self.c.Multiply(0, 9), 0)

    def test_division(self):
        self.assertEqual(self.c.Division(6, 2), 3)
        self.assertAlmostEqual(self.c.Division(5, 2), 2.5)
        # Test division by zero returns ZeroDivisionError type
        self.assertEqual(self.c.Division(4, 0), ZeroDivisionError)

if __name__ == '__main__':
    unittest.main()