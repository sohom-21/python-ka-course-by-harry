# 🧾✨ Project Upgrade: Bill Slip with Item Names & Summary
# 📦 What We’ll Add:
# User will also enter item name
# Har item ka:
    # Name
    # Price
    # Quantity
    # Final price after discount & GST
    # yeh sab ek list me store hoga

# Sab items end mein ek clean bill slip format me print honge ✅

# 🧠 Sample Output:
# Enter item name: Milk
# Enter price: 50
# Enter quantity: 12
# Item total after discount + GST: ₹636.0

# Add another item? yes

# Enter item name: Bread
# Enter price: 30
# Enter quantity: 5
# Item total after GST: ₹177.0

# Add another item? no

# 🧾 Final Bill:
# ----------------------------------------
# Item        Qty   Price   Final Total
# Milk        12    50      ₹636.0
# Bread       5     30      ₹177.0
# ----------------------------------------
# Total Bill: ₹813.0

grocery_list = dict()
items = list()
def calculate_bill(price, quantity):
    total_price = price * quantity
    if quantity > 10:
        discounted_price = total_price - (total_price * 0.10)
        gst_price_upon_discounted = discounted_price + (discounted_price * 0.18)
        return gst_price_upon_discounted

    gst_price = total_price + (total_price*0.18)
    return gst_price

user_total_bill = 0
def UserCart(name, price, quantity, final_price):
    grocery_list.update({'name': name})
    grocery_list.update({'price': price})
    grocery_list.update({'quantity': quantity})
    grocery_list.update({'final total': final_price})
    items.append(grocery_list.copy())
    grocery_list.clear()

def user_bought_item():
    name_of_item = input('Enter item name: ').lower().strip()
    price_of_item = int(input("Enter the price of item: "))
    quantity_of_item = int(input('Enter the quantity: '))
    bill_of_the_item = calculate_bill(price_of_item,quantity_of_item)
    if quantity_of_item > 10:
        print(f'Item total after discount + GST: ₹{bill_of_the_item}')
    else:
        print(f'Item total of after Gst: ₹{bill_of_the_item}')

    UserCart(name_of_item, price_of_item, quantity_of_item, bill_of_the_item)
    global user_total_bill
    user_total_bill = user_total_bill + bill_of_the_item
    print('Do you want to add another item? (yes/no): ')
    decision = input().lower()

    if (decision == 'no'):
        print('🧾 Final Bill:')
        print('---------------------------------------')
        print(f'{"Item":<12}{"Qty":<8}{"Price":<10}{"Final Total"}')
        for i in items:
             print(f'{i.get('name'):<12}{i.get('quantity'):<8}{i.get('price'):<10}{i.get('final total')}')
        print('---------------------------------------')
        print(f'✨ Total Bill: {user_total_bill}')
        exit()
    else:
        user_bought_item()

user_bought_item()