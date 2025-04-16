# Write a program to find the sum of first n natural numbers using while loop.

number = int(input('Enter the number to find the sum of natural number: '))
i = 1
total_sum = 0
while(i <= number):
    total_sum = total_sum + i
    i += 1
print('sum is', total_sum)