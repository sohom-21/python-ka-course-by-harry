# 2. Write a class "calculator" capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self,number):
        self.num = number

    x = lambda self: (self.num ** 2)
    y = lambda self: (self.num ** 3)
    z = lambda self: (self.num ** 0.5)


number = int(input('Enter a number to find its square, cube and square root: '))
square = Calculator(number)
print(f"the square of a number is {square.x()}")
print(f"the cube of a number is {square.y()}")
print(f"the square root of a number is {square.z():.2f}")


"""
class Calculator:
    def __init__(self, number):
        self.num = number

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def square_root(self):
        return self.num ** 0.5

number = int(input('Enter a number to find its square, cube and square root: '))
calc = Calculator(number)

print(f"The square of the number is {calc.square()}")
print(f"The cube of the number is {calc.cube()}")
print(f"The square root of the number is {calc.square_root()}")
"""