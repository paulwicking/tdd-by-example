

class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        amount = self.amount * multiplier
        return Dollar(amount)
