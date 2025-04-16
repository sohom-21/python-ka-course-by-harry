# Write a program to calculate the factorial of a given number using for loop.
number = int(input('Enter a number to calculate the factorial of: '))
fact = 1
if number > 1:
    for i in range(1, number+1):
        fact = fact * i
else:
    fact = 1
print(f'The factorial of the number {number} is {fact}')
# it better version of this code

f  = lambda num: 1 if num <= 1 else num * f(num-1)
print(f'The factorial of the number {number} is {f(number)}')
