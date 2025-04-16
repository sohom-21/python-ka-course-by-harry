# 🧠 Mini Challenge: Number Check Function
# Task:
# Ek function banao check_number(n) jo:

# 1.Number n ko input lega (as parameter)
# 2.Check kare:
    # Agar number positive hai → return "Positive"
    # Agar number negative hai → return "Negative"
    # Agar number zero hai → return "Zero"

# Function ko call karo user se number lekar
# Print the result

# 🎯 Expected Output:
# Enter a number: -5
# The number is: Negative

# ya

# Enter a number: 0
# The number is: Zero

def check_number(n):
    if n > 0:
        return 'Positive 🔼'
    elif n < 0:
        return 'Negative 🔽'
    else:
        return 'Zero 🟰'

n = int(input('Enter a number to determine: '))
final_result = check_number(n)
print(f'The number you entered is: {final_result}')
