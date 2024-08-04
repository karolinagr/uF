import unittest
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        with self.assertRaises(ValueError):
            fibonacci(0)

    def test_fibonacci_first(self):
        actual = fibonacci(1)
        expected = 0
        self.assertEqual(expected, actual)

    def test_fibonacci_second(self):
        actual = fibonacci(2)
        expected = 1
        self.assertEqual(expected, actual)

    def test_fibonacci_fourth(self):
        actual = fibonacci(4)
        expected = 2
        self.assertEqual(expected, actual)

    def test_fibonacci_tenth(self):
        actual = fibonacci(10)
        expected = 34
        self.assertEqual(expected, actual)

    def test_fibonacci_seventeenth(self):
        actual = fibonacci(17)
        expected = 987
        self.assertEqual(expected, actual)
