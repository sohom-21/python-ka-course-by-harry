"""
📝 Problem 3: Largest of Three Numbers
Task:
    User se 3 numbers input lo, aur print karo sabse bada number kaunsa hai.

👉 Hint:
    Tum if-elif-else ka use kar sakte ho
    Ya phir built-in function max() bhi try kar sakte ho
    Tum kaunsa approach try karna chahoge pehle — apna logic with if-else, ya shortcut with max()?
"""

# solution
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"Largest number is {num1}")
elif num2 >= num1 and num2 >= num3:
    print(f"Largest number is {num2}")
else:
    print(f"Largest number is {num3}")

# solution 2
print(f"Largest number is {max(num1, num2, num3)}")

#quiz
"""
Agar d = {"x": 12, "y": 40, "z": 5} ho toh
    max(d) kya dega?
    max(d.values()) kya dega?
"""
d = {"x": 12, "y": 40, "z": 5}
print(max(d))
print(max(d.values()))
print(max(d, key=d.get))

"""
but last wala kaam kese kar raha wo thora samjh te hai
🔎 Breakdown:

Normally, max(d) → compare karega keys ("x", "y", "z")
Lekin agar tum key=... parameter use karte ho, toh Python har element pe ek function apply karke uske result ko compare karta hai.
👉 Yaha humne likha key=d.get
    d.get("x") → 12
    d.get("y") → 40
    d.get("z") → 5
Ab max() in values ko compare karega (12, 40, 5)
Aur jiska value sabse bada hai (40), uska key ("y") return karega.

So max(d, key=d.get) → "y"

⚡ Ek line me socho:
 -"max dikh raha hai keys ko, lekin keys ka value compare kar raha hai."
"""