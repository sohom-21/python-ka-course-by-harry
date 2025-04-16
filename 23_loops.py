# loops are pieces of code that help us to iterate or repeat a task multiple number of time
# therefore saving us the effort of write the same of piece of code again and again

# Type of loops in python
# primarily there are two types of loops in python
# -----> while loops
# ------> for loops

# while loop syntax
# while condition:
#          loop body

# here is an example of while loop in python
i = 0
while i < 50:
    print(f'Hey this is while loop in python{i}')
    i += 1

# see how much of the task is reduced
# for the same piece of code if had to be manually would need write 50 print statements

# For loop syntax
for i in range (1,51):
    print(f'hey this is a for loop{i}')