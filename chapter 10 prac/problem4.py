# 4. Add a static method in problem 2, to greet the user with hello.

class Calculator:
    def __init__(self, number):
        self.num = number

    def square(self):
        return self.num ** 2

    def cube(self):
        return self.num ** 3

    def square_root(self):
        return self.num ** 0.5

    @staticmethod
    def hello():
        print("hello there!")

number = int(input('Enter a number to find its square, cube and square root: '))
calc = Calculator(number)
calc.hello()
print(f"The square of the number is {calc.square()}")
print(f"The cube of the number is {calc.cube()}")
print(f"The square root of the number is {calc.square_root()}")