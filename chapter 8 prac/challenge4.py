# 🛒 Mini Project: Simple Billing System
# 🔧 Task:
# Ek function banao calculate_bill(price, quantity) jo:
# 1.Total price nikaalega = price * quantity
# 2.Agar quantity 10 se zyada hai, toh 10% discount dega
# 3.Final amount return karega after discount (agar applicable ho)

#🧾 Requirements:
# Function ko call karo with user input for price and quantity
# Final bill print karo nicely

def calculate_bill(price, quantity):
    total_price = price * quantity
    if quantity > 10:
        discount = total_price * 0.10
        return (total_price - discount)
    else:
        return (total_price)

price_of_item = int(input('Enter the price of item: '))
quantity_of_the_item = int(input('Enter quantity: '))
bill = calculate_bill(price_of_item, quantity_of_the_item)
print(f'Total bill after discount: ₹{bill}')