import unittest
from math_utils import add, subtract, divide

class TestMathUtils(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 3), 3.333, places=2)
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()