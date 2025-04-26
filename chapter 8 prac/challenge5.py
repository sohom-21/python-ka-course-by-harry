# 🛒💻 Project: Smart Billing with GST & Multiple Items
# 🔧 Requirements:
# Har item ke liye:
    # User se price aur quantity lo
    # Total calculate karo
    # Agar quantity > 10 hai → 10% discount
    # Fir uspe 18% GST lagao
    # Final bill return karo (after discount + GST)

# Har item ke baad puchho: "Do you want to add another item? (yes/no): "
    # Jab user no bole, tab program total bill print kare
# to get a grasp of what's going on what a look at challenge 4

final_bill = 0
def calculate_bill(price, quantity):
    total_price = price * quantity
    if (quantity > 10):
        Discount = total_price - (total_price * 0.10)
        gstPrice_withDiscount = Discount + (Discount*0.18)
        return gstPrice_withDiscount
    else:
        gstPrice_withoutDiscount = total_price + (total_price*0.18)
        return gstPrice_withoutDiscount

decide = True
while (decide):
    price_of_item = int(input('Enter the price of item: '))
    quantity_of_item = int(input('Enter Quantity: '))
    bill_of_the_item = calculate_bill(price_of_item, quantity_of_item)
    if quantity_of_item > 10:
        print(f'Item total after discount + GST: ₹{bill_of_the_item}')
    else:
        print(f'Item total of after Gst: ₹{bill_of_the_item}')

    final_bill = final_bill + bill_of_the_item
    print('Do you want to add another item? (yes/no): ')
    decision = input().lower()
    if decision == 'no':
        decide = False

print(f'Your total bill is: ₹{final_bill}')