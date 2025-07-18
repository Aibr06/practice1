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
    
if __name__ == "__main__":
    m1 = Money(100)
    m2 = Money(50)

    print("m1:", m1)  # Output: m1: $100.00
    print("m2:", m2)  # Output: m2: $50.00

    m3 = m1 + m2
    print("m1 + m2:", m3)  # Output: $150.00

    m4 = m1 - m2
    print("m1 - m2:", m4)  # Output: $50.00

    m5 = m1 * 2
    print("m1 * 2:", m5)  # Output: $200.00

    m6 = m1 / 2
    print("m1 / 2:", m6)  # Output: $50.00