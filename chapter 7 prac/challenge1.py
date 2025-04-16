# 💥 Challenge 1: Even-Index Characters Printer
# 👉 Given a string, print only those characters which are at even indices (0, 2, 4, …)
#
# Example Input: "LoopMaster"
# Expected Output: L o M s e

string_takenUserInput = input("Enter the word: ")
for x in range(0, len(string_takenUserInput), 2):
    print(string_takenUserInput[x])

# optimized version
string_takenUserInput = input("Enter the word: ")
for i in range(0, len(string_takenUserInput), 2):
    print(string_takenUserInput[i], end=" ")