# Write a python function to print first n lines of the following pattern:
# ***
# **
# *    - for n = 3
def usingloops(n):
    for i in range(0, n):
        print('*' * (n-i))
    return 'done'

def usingrecursion(n):
    if n > 0:
        print('*' * n)
        usingrecursion(n-1)
    else:
        return  # Changed from exit() to return

# Choose either recursion or loops to call, not both (unless you want to see both solutions)
# usingrecursion(3)
# usingloops(3)

def main():
    print("\n Enter 1 to see the pattern printed using loops")
    print("\n Enter 2 to see the pattern printed using recursion")
    print("\n Enter 3 to exit")
    choice = int(input("\n Enter your choice: "))
    if choice == 1:
        n = int(input("\n Enter the number of lines: "))
        usingloops(n)
    elif choice == 2:
        n = int(input("\n Enter the number of lines: "))
        usingrecursion(n)
    elif choice == 3:
        exit()
    return 0

main()