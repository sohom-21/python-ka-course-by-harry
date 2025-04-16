# 💥 Challenge 3: Skip the Vowels
# 👉 Given a string, print each character except vowels (a, e, i, o, u — ignore case).

# Example Input: "Programming"
# Expected Output: P r g r m m n g

# Chhoti tip: spaces daalne ke liye print(x, end=" ") use kar lena 😄

word = input("Enter your word: ").strip()
for char in word:
    if char.lower() not in {'a','e','i','o','u'}:
        print(char, end=' ')

# 🧠 Slightly improved version
vowels = {'a', 'e', 'i', 'o', 'u'}
word = input("Enter your word: ").strip()
for char in word:
    if char.lower() not in vowels:
        print(char, end=' ')
