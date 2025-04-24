# Write a Python program to solve the Fibonacci Sequence using recursion

def fibonacci(num):
         if num == 0:
                  return 0
         if num == 1:
                  return 1
         if num > 1:
                  return (fibonacci(num-1)+fibonacci(num-2))

number = int(input("Enter a number: "))
print(fibonacci(number))