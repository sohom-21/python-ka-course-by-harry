# if-elif-else: ladder

# ✅Note:

#Python mein indentation (space ya tab) bahut important hota hai.
# **:** lagana mat bhoolna if, else, ya elif ke baad.

a=int(input("Enter your age: "))
if a > 18:
    print("Aap vote de sakte ho")
    print("please vote properly as your vote matters")
elif a < 0:
    print("you are entering an invalid age")
elif a == 0:
    print("Madarchod tu toh abhi paida hi hua hai tera kesa vote ???")

else:
    print(f"Tum 18 ke nahi hue ho better luck again next {18 - a} years me")

print("\nEnd of program")

# Bhai bas itna samajh le: if → "agar" else → "warna" elif → "nahi to agar"