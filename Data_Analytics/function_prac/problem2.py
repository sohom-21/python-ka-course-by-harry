# 2. Write a Python function to create and print a list where the values are square of numbers between 1 and 30.

def demo_test(): 
         value_list = list()
         for i in range(1,31):
                  value_list.append(i**2)
         # value_list = [i**2 for i in range(1,31)] other way of writing the operation above
         print(f"The list of values that are square values of 1 to 30 are {value_list}")
         

demo_test()