from abc import ABCMeta, abstractmethod


class Money(object):
    __metaclass__ = ABCMeta

    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __repr__(self):
        return repr(
            str(self.__class__)
            + ': ' +
            str(self._amount)
            + ' ' +
            self.currency
        )

    def __str__(self):
        return str(self._amount + ' ' + self.currency)

    def __hash__(self):
        return hash((self.__class__, self._amount))

    def __eq__(self, other):
        return (
                self.currency == other.currency and
                self._amount == other._amount
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def equals(self, other):
        return self.__eq__(other)

    @staticmethod
    def dollar(amount, currency='USD'):
        return Money(amount, currency=currency)

    @staticmethod
    def franc(amount, currency='CHF'):
        return Money(amount, currency=currency)

    def times(self, multiplier):
        return Money(self._amount * multiplier, self.currency)

    @property
    def currency(self):
        return self._currency
