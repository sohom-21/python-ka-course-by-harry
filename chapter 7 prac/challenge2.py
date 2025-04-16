# 💥 Challenge 2: Reverse Tuple Elements
# 👉 Given a tuple of integers, print them in reverse order using a loop.
#
# Example Input: (10, 20, 30, 40, 50)
# Expected Output: 50 40 30 20 10

given_numbersTO_tuple = tuple(map(int, input("Enter the numbers separated by a comma").split(',')))
length_of_tuple = len(given_numbersTO_tuple)-1
for i in range(length_of_tuple, -1,-1):
    print(given_numbersTO_tuple[i])

# 🧠 Optimized version:
given_numbersTO_tuple = tuple(map(int, input("Enter the numbers separated by a comma: ").split(',')))
for value in reversed(given_numbersTO_tuple):
    print(value, end=' ')
