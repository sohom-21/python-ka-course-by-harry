"""
🔥 Problem 2: Even or Odd Checker

Task:
 - User se ek number input lo, aur print karo:
    "The number is even"
    ya "The number is odd"

👉 Hint: Even number ka matlab kya hota hai in terms of remainder (% operator)?
"""
#solution
number = int(input('Enter a number: '))
if number % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')


"""
⚡ Mini-Check (thoda dimaag ghumane wala):
Agar user negative number input kare, jaise -7, toh kya tumhara code sahi se "odd" print karega ya koi dikkat hogi?

#answer
    Negative number ke case me bhi modulus (%) operator properly kaam karta hai Python me.
 For example:
 -7 % 2 = 1 → iska matlab odd hai
 -8 % 2 = 0 → iska matlab even hai
 Isliye tumhara code even/odd check ke liye positive ya negative dono numbers pe sahi chalega ✅
"""