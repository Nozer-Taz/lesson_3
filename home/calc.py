

class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __mul__(self, other):
        return Calculator(self.value * other.value)

    def __truediv__(self, other):
        if other.value == 0:
            raise ValueError("Деление на ноль невозможно!")
        return Calculator(self.value / other.value)

    def __str__(self):
        return f"Результат: {self.value}"

calc1 = Calculator(2)
calc2 = Calculator(5)

print(calc1 + calc2)
print(calc1 - calc2)
print(calc1 * calc2)
print(calc1 / calc2)