import datetime

x = datetime.datetime.now()
y = datetime.datetime(1997,10,14)
print(x)
print(y)
print(y.strftime("%A%B%Y"))

from random import randint,choice
x = randint(1, 40)
print(x)
l = ['heads','tails']
print(choice(l))