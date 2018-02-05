

class Dollar(object):
    def __init__(self, amount):
        self._amount = amount

    def times(self, multiplier):
        amount = self._amount * multiplier
        return Dollar(amount)

    def equals(self, comparand):
        return self._amount == comparand._amount
