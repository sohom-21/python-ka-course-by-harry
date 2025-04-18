# 🧾✨ Project Upgrade: Bill Slip with Item Names & Summary
# 📦 What We’ll Add:
# Phase 2: CSV Import Feature (Repeat Orders / Old Data)
# to get a grasp of what's going on what a look at challenge 8

# Example:
# User gives a CSV file like this:
# Items,Quantity,Price
# milk,2,50
# bread,12,30

# Then we calculate the bill again using same calculate_bill() function for each line.
# ✨ Very realistic — think retail shops reloading frequent orders.

import csv
import datetime

def export_to_csv(items,total):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"final_bill_{timestamp}.csv"
    with open(filename, mode='w', newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Items", "Quantity","Price", "final Total"])
        for item in items:
            writer.writerow([
                item["name"],
                item["quantity"],
                item["price"],
                f'{item["final total"]:.2f}'
            ])
        writer.writerow([])
        writer.writerow(["","","Total", f'{total:.2f}'])
        print(f"🧾 Bill exported successfully to {filename}")

def print_bill_to_txt(items, total):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"final_bill_{timestamp}.txt"
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write("🧾 Final Bill\n")
        file.write("----------------------------------------------\n")
        file.write(f'{"Item":<20}{"Qty":<8}{"price":<10}{"final total"}\n')
        for item in items:
            file.write(f'{item["name"]:<20}{item["quantity"]:<8}{item["price"]:<10}{item["final total"]:.2f}\n')
        file.write("----------------------------------------------\n")
        file.write(f'✨ Total Bill: ₹{total:.2f}\n\n')
    print(f"🖨️ Bill printed successfully to {filename}")

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
def user_cart(name, price, quantity, final_price):
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

    user_cart(name_of_item, price_of_item, quantity_of_item, bill_of_the_item)
    global user_total_bill
    user_total_bill = user_total_bill + bill_of_the_item
    print('Do you want to add another item? (yes/no): ')
    decision = input().lower()

    if decision == 'no':
        print('🧾 Final Bill:')
        print('---------------------------------------')
        print(f'{"Item":<20}{"Qty":<8}{"Price":<10}{"Final Total"}')
        for i in items:
             print(f'{i.get('name'):<20}{i.get('quantity'):<8}{i.get('price'):<10}{i.get('final total'):.2f}')
        print('---------------------------------------')
        print(f'✨ Total Bill: {user_total_bill}')
        export_to_csv(items,user_total_bill)
        print_bill_to_txt(items,user_total_bill)
        exit()
    else:
        user_bought_item()

def import_previous_bill():
    filename = input("Enter the full name of the bill CSV file to import (e.g., final_bill_2025-04-16_15-30-55.csv): ").strip()
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)

            print('\n 📜 Imported Bill:')
            print('-------------------------------------------------')
            print(f'{"Item":<20}{"Qty":<8}{"price":<10}{"Final Total"}')

            for row in reader:
                if not any(row):
                    continue
                if row[0].lower() == "total":
                    print('-------------------------------------------------')
                    print(f'✨ Total Bill: ₹{row[3]}')
                    break
                print(f'{row[0]:<20}{row[1]:<8}{row[2]:<10}{row[3]}')
    except FileNotFoundError:
        print("❌ File not found! Please check the filename and try again.")
        import_previous_bill()

def show_main_menu():
    print("\n ======= Welcome to the Grocery Billing System ======")
    print("1. Add New Items and Generate Bill")
    print("2. Import previous bill (from exported csv)")
    print("3. Exit")
    choice = input("Enter your choice (1/2/3): ").strip()
    if choice == '1':
        user_bought_item()
    elif choice == '2':
        import_previous_bill()
    elif choice == '3':
        print("Thank you for using the system. GoodBye!!!!")
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        show_main_menu()

show_main_menu()