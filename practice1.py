class Money:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.amount + other.amount)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.amount - other.amount)
        return NotImplemented

    def __mul__(self, factor):
        if isinstance(factor, (int, float)):
            return Money(self.amount * factor)
        return NotImplemented

    def __truediv__(self, divisor):
        if isinstance(divisor, (int, float)):
            return Money(self.amount / divisor)
        return NotImplemented

    def __str__(self):
        return f"${self.amount:.2f}"