# 1. Write a function to find maximum of three numbers in Python.

def maximum(a,b,c):
         if (a>b and a>c):
                  return a
         elif(b>c):
                  return b
         else:
                  return c

maximum = lambda a,b,c : a if(a>b and a > c) else b if(b>c) else c

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))
c = int(input('Enter a number: '))

print(f"The maximum between three numbers would be {maximum(a,b,c)}")
