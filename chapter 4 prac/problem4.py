
#Write a program to sum a list with 4 numbers.
numbers = tuple(map(int, input('Enter 4 numbers separated by commas: ').split(',')))
print(sum(numbers))

# Accha iska karne ke ek aur method
# - accept karunga 4 numbers
# -aur usko ke tuple me le lunga
# -aur fir sum function se total find karlunga extremely easy way me

number  =  tuple(int(x) for x in input("Enter 4 numbers separated by a comma").split(','))
print(sum(number))

# just wrote all the functions that were to be performed in a single liner
number2  =  sum(tuple(int(x) for x in input("Enter 4 numbers separated by a comma").split(',')))
print(number2)
