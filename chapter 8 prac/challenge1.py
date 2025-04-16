# Ek function banao jo 2 numbers le aur unka sum, difference, aur product print kare

# Example:
# calculate(10, 5)
# Output:
# Sum: 15
# Difference: 5
# Product: 50

def my_Sum(a,b):
    Total_sum = a + b
    Product = a * b
    Difference = a - b
    print(f'The sum is {Total_sum}')
    print(f'The product is {Product}')
    print(f'The Difference is {Difference}')

a = int(input('Enter a number for this program: '))
b = int(input('Enter a number for this program: '))
my_Sum(a,b)
