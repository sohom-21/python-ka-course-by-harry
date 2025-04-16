# Write a program to find whether a given number is prime or not.

verify_counter = 1
number_to_verify = int(input('Enter the number: '))
for i in range(2, number_to_verify+1):
    if number_to_verify%i == 0:
        verify_counter += 1
if verify_counter == 2:
    print(f'{number_to_verify} is a prime number since it is getting divided by one and its self')
else:
    print(f'{number_to_verify} is not a prime number')

# 🧠 optimized logic + code:
num = int(input("Enter the number: "))

if num < 2:
    print(f"{num} is not a prime number")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")

# So why use the root of the given_number ?
# Agar koi number num non-prime hai, toh uska koi factor hamesha √num ke aas paas ya usse pehle mil jaata hai.
# Example:
# Maan lo num = 36
# Toh iska ek factor pair hai:

# 6 × 6
# 4 × 9
# 3 × 12
# 2 × 18

# Ab dekho:
# Agar 36 ko divide karne wala factor 9 (jo √36 se bada) hai,
# Toh pair mein 4 bhi hoga (jo √36 se chhota hai)
# Iska matlab:
# Agar 36 kisi bade factor se divide hota hai, toh uska chhota pair wala factor already √36 se pehle hi aa chuka hota.