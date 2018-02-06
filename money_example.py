
class Money(object):
    def __init__(self, amount):
        self._amount = amount

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


class Dollar(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        amount = self._amount * multiplier
        return Dollar(amount)


class Franc(Money):
    def __init__(self, amount):
        super().__init__(amount)

    def times(self, multiplier):
        amount = self._amount * multiplier
        return Franc(amount)
