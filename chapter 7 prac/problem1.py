# 1. Write a program to print multiplication table of a given number using for loop.

number_given = int((input('Enter the number you want to see the multiplication table of: ').strip()))
iterate_to = int(input("Enter a number to which the tables should be printed to: ").strip())
for i in range(1, iterate_to+1):
    print(f'{number_given} X {i} is {number_given*i}')
else:
    print(f'printed multiples of {number_given} till times {iterate_to}')