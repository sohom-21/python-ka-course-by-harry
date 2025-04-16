# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression
x = lambda a : a + 10
print(x(5))

x = lambda a,b : a * b
print(x(5,6))

x = lambda a,b,c : a+b+c
print(x(2,7,8))