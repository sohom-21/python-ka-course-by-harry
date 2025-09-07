"""
📝 Problem 4: String Word Check
Task:
 --User se ek string input lo aur check karo ki "Python" uske andar hai ya nahi.
    Agar hai → "Yes, it contains Python!"
    Nahi hai → "No, Python not found."
"""

#hint for this problem
# Tum in operator ya .find() method use kar sakte ho.

string  = input("Enter a string: ")
string = string.lower()
# solution 1
if "python" in string:
    print("Yes, it contains Python!")
else:
    print("No, Python not found.")

# solution 2
print(f"it contains Python at index: {string.find('python')} in this sentence")
