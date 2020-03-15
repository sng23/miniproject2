
from .Addition import fn_addition
from .Subtraction import fn_subtraction
from .Multiplication import fn_multiplication
from .Sqrt import fn_squareroot
from .Square import fn_square
from .Division import fn_division


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = fn_addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = fn_subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = fn_multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = fn_division(a, b)
        return self.result

    def square(self, a):
        self.result = fn_square(a)
        return self.result

    def squareroot(self, a):
        self.result = fn_squareroot(a)
        return self.result
