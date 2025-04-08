# Write a program to input eight numbers from the user and display all the unique
# numbers (once).
unique_numbers = set(map(int, input("Enter 8 numbers separated by comma").split(',')))
print(f'all the unique numbers are {unique_numbers}')
