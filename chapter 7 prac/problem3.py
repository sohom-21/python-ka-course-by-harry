# Write a program to print multiplication table of a given number using while loop

multiple_of = int(input('Enter a number to the print the multiple of: '))
times = int(input('Enter the times till the number is to be printed: '))

i = 1
while i <= times:
    print(f'{multiple_of} X {i} is {multiple_of*i}')
    i = i+1
