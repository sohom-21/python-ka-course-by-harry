# Write a recursive function to calculate the sum of first n natural numbers.

"""
🧠 solution:
to print the sum of first n natural numbers using a recursive function
"""

def find_sum(n):
    if n > 0:
        return n + find_sum(n-1)
    else:
        return 0

number_byuser = int(input('Enter a number that is none negative: '))
print(f'The sum of first {number_byuser} natural number is {find_sum(number_byuser)}')

"""
🧠 modified less line solution:
Now lets us a lambda function to make it even smaller
"""
natural_find = lambda n: n + natural_find(n-1) if (n > 0) else 0
print(f'The sum of first {number_byuser} natural number is {natural_find(number_byuser)}')
