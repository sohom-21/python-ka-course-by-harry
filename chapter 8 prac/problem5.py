# Write a python function to print first n lines of the following pattern:
# ***
# **
# *    - for n = 3
def usingloops(n):
    for i in range(1, n+1):
        print('*' * (n-i))
    return 'done'

def usingrecursion(n):
    if n > 0:
        print()