from unittest import TestCase
from money_example import *


class TestDollar(TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        actual = five.times(2)

        self.assertEqual(10, actual.amount)

        actual = five.times(3)
        self.assertEqual(15, actual.amount)
