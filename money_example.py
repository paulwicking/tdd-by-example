

class Dollar(object):
    def __init__(self, amount):
        self.__amount = amount

    def __repr__(self):
        return repr(self.__amount)

    def __eq__(self, other):
        return self.__amount == other

    def times(self, multiplier):
        amount = self.__amount * multiplier
        return Dollar(amount)

    def equals(self, comparand):
        return self.__eq__(comparand)
