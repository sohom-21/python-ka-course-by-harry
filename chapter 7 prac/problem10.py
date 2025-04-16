# 10. Write a program to print multiplication table of n using for loops in reversed order.

number = int(input('Enter a number: '))
for i in range (number,-1,-1):
    print(f'{number} x {i} is {number * i}')