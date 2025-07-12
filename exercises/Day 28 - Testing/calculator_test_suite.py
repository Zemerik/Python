"""
Exercise 1: Calculator Test Suite
Create a test suite for a calculator module that:
- Tests all arithmetic operations
- Covers edge cases (division by zero)
- Mocks file I/O operations
(Use unittest and unittest.mock.)
"""

import unittest
from unittest.mock import mock_open, patch

# Simulated calculator module
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError('division by zero')
        return a / b
    def save_result(self, result, filename):
        with open(filename, 'w') as f:
            f.write(str(result))

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)
    @patch('builtins.open', new_callable=mock_open)
    def test_save_result(self, mock_file):
        self.calc.save_result(42, 'result.txt')
        mock_file.assert_called_with('result.txt', 'w')
        mock_file().write.assert_called_once_with('42')

if __name__ == '__main__':
    unittest.main() 