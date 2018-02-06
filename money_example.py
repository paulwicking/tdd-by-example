

class Sum:
    def __init__(self, augend, addend):

        self.augend = augend
        self.addend = addend

    def reduce(self, to):
        amount = self.augend._amount + self.addend._amount
        return Money(amount, to)


class Money:
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
        return str(self._amount) + ' ' + str(self.currency)

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

    def plus(self, addend):
        return Sum(self, addend)

    @property
    def currency(self):
        return self._currency


class Bank:
    def reduce(self, source, to):
        return source.reduce(to)
