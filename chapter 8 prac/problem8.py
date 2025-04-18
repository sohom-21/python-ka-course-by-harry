# 8. Write a python function to print multiplication table of a given number.
def multiply_returner(num, times):
    for i in range(1,times+1):
        print(f'{num}x{i} is {num * i}')
    return 'done'

def over():
    num = int(input('Enter a number to find the multiple of: '))
    times = int(input('Enter the number of times it should print out the table till: '))
    result  = multiply_returner(num, times)
    print(result)

over()