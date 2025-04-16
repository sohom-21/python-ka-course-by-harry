# 🤓 Tere liye Ek Challenge:
# Ek function banao divide_and_mod(a, b) jo:
# a ko b se divide kare (normal division)
# a ka b se modulus bhi nikaale (remainder)
# dono values return kare

# Then function ko call karo aur output print karo like:
# Quotient is: ...
# Remainder is: ...

def divide_and_mod(a,b):
    return a/b, a%b

a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

quotient, remainder = divide_and_mod(a,b)
print(f'Quotient is: {quotient}')
print(f'Remainder is: {remainder}')