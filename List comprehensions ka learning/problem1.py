
# Challenge 1: Square of Even Numbers
# User se ek comma-separated number input le (jaise "1,2,3,4,5,6")
# Aur output me sirf even numbers ke square print kar.

# Expected Output (if input is 1,2,3,4):
# [4, 16]



numbers  = list(map(int,input('Enter the numbers by separated using commas').split(',')))
square = [x**2 for x in numbers if x%2 == 0 ]
print(square)