# Write a program using functions to find greatest of three numbers.

def find_greatest(a,b,c):
    if (a > b) and (a > c):
        return a
    elif b > c:
        return b
    else:
        return c

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))
print(f"The greatest number among the 3 is {find_greatest(num1,num2,num3)}")

find = lambda a,b,c : a if(a>b and a>c) else b if(b>c) else c

print(f'the greatest among the numbers using lambda function {find(num1, num2, num3)}')
