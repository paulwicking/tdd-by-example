from abc import ABCMeta, abstractmethod


class Money(object):
    __metaclass__ = ABCMeta

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __repr__(self):
        return repr(self._amount)

    def __hash__(self):
        return hash((self.__class__, self._amount))

    def __eq__(self, other):
        return (
                self.__class__ == other.__class__ and
                self._amount == other._amount
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def equals(self, other):
        return self.__eq__(other)

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    @abstractmethod
    def times(self, multiplier):
        pass

    @property
    def currency(self):
        return self._currency


class Dollar(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount, currency):
        super().__init__(amount, currency)

    def times(self, multiplier):
        return Money.franc(self._amount * multiplier)
