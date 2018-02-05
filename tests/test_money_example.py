from unittest import TestCase
from money_example import *


class TestDollar(TestCase):
    def test_multiplication(self):
        five = Dollar(5)
        five.times(2)

        self.assertEqual(10, five.amount)
