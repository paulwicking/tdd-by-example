from unittest import TestCase
from money_example import *


class TestDollar(TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        product = five.times(2)

        self.assertEqual(10, product)

        product = five.times(3)
        self.assertEqual(15, product)

    def test_equality(self):
        self.assertTrue(Dollar(5).equals(Dollar(5)))
        self.assertFalse(Dollar(5).equals(Dollar(6)))
