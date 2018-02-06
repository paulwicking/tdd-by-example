from unittest import TestCase
from money_example import *


class TestMoney(TestCase):
    def test_multiplication(self):
        five = Money.dollar(5)
        self.assertEqual(Money.dollar(10), five.times(2))
        self.assertEqual(Money.dollar(15), five.times(3))

    def test_equality(self):
        self.assertTrue(Money.dollar(5).equals(Money.dollar(5)))
        self.assertFalse(Money.dollar(5).equals(Money.dollar(6)))
        self.assertFalse(Money.franc(5).equals(Money.dollar(5)))

    def test_currency(self):
        self.assertEqual("USD", Money.dollar(1).currency)
        self.assertEqual("CHF", Money.franc(1).currency)

    def test_simple_addition(self):
        five = Money(5, 'USD')
        test_sum = five.plus(five)
        bank = Bank()
        reduced = bank.reduce(test_sum, 'USD')
        self.assertEqual(Money.dollar(10), reduced)

    def test_reduce_sum(self):
        test_sum = Sum(Money.dollar(3), Money.dollar(4))
        bank = Bank()
        result = bank.reduce(test_sum, 'USD')

        self.assertEqual(Money.dollar(7), result)
