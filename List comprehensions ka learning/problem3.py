
# 💡 Challenge 3: Even-Odd Tagging
# User se 5 numbers le aur ek list banao jisme "Even" ya "Odd" likha ho har number ke liye.
#
# Expected Output (input: 1,2,3,4,5)
# ['Odd', 'Even', 'Odd', 'Even', 'Odd']


Evenodd = ["even" if eval(x) % 2 ==0 else "odd" for x in (input('Enter numbers separated by commas').split(','))]
print(Evenodd)

# Challenge 3: Even-Odd Tagging
# Tera idea mast hai! Bas chhoti si cheezein:

# eval() avoid karo — ye risky hota hai (security reason).
# Safer option: int(x)
# Variable name Evenodd ko Python style me even_odd kar lo (optional, but clean).

even_odd = ["Even" if int(x) % 2 == 0 else "Odd" for x in input("Enter numbers separated by commas: ").split(',')]
print(even_odd)
