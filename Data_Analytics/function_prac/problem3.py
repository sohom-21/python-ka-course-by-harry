# 3. Write a Python function that takes a number as a parameter and check if the number is prime or not.

from math import sqrt
def prime_check(number):
         if(number<=1):
                  return False
         for i in range(2,int(sqrt(number)+1)):
                  if((number % i) == 0):
                           return False
         else:
                  return True
         

number = int(input("Enter the number: "))
if prime_check(number):
         print(f"The number {number} is prime number")
else:
         print("The number is not prime")