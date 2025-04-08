# 🎯 Challenge:
# User se 3 input lo — A, B, aur C ke coins

# Fir print karo:

# "Chest A has the most coins!"
# OR
# "Chest B has the most coins!"
# OR
# "Chest C has the most coins!"
# But condition ye hai:

# ✨ Use nested ternary operators!
# Bonus point: agar do chests me equal maximum coins hain, toh print karo "It's a tie!"

# it's a challenge given by gpt bhai

# my answer

chest1, chest2, chest3 = list(map(int, input("Enter the coins contained in each chest separated by a semi colon: ").split(",")))

final_Chest_result = chest1 if ((chest1 > chest2) and (chest1 > chest3)) else \
    chest2 if((chest2 > chest3) and (chest2 > chest1)) else chest3 if ((chest3 > chest1) and (chest3 > chest2)) else "It's a tie"

print(f"final result is {final_Chest_result}")


# gpt ka more powerful answer
chest1, chest2, chest3 = map(int, input("Enter the coins in Chest A, B, C separated by commas: ").split(','))

result = "Chest A has the most coins!" if (chest1 > chest2 and chest1 > chest3) else \
         "Chest B has the most coins!" if (chest2 > chest1 and chest2 > chest3) else \
         "Chest C has the most coins!" if (chest3 > chest1 and chest3 > chest2) else \
         "It's a tie!"

print(result)

#Bonus Tip: Readability ko improve karne ke liye tu () brackets use kar sakta hai:
# result = (
#     "Chest A has the most coins!" if (chest1 > chest2 and chest1 > chest3)
#     else "Chest B has the most coins!" if (chest2 > chest1 and chest2 > chest3)
#     else "Chest C has the most coins!" if (chest3 > chest1 and chest3 > chest2)
#     else "It's a tie!"
# )

# Now the super optimized code by chatgpt
chest1, chest2, chest3 = map(int, input("Enter the coins in Chest A, B, C separated by commas: ").split(','))

maximum = max(chest1, chest2, chest3)

# Count how many times max value occurs
count = [chest1, chest2, chest3].count(maximum)

result = (
    "It's a tie!" if count > 1 else
    "Chest A has the most coins!" if maximum == chest1 else
    "Chest B has the most coins!" if maximum == chest2 else
    "Chest C has the most coins!"
)

print(result)