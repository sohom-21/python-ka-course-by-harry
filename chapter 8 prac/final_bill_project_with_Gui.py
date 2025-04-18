"""
# 🧾✨ Project Upgrade: Bill Slip with Item Names & Summary
# 📦 What We’ll Add:
# make a gui for this project
# to get a grasp of what's going on what a look at challenge 9
"""

import csv
import datetime
import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import filedialog

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

    try:
        price_of_item = int(input("Enter the price of item: "))
        quantity_of_item = int(input('Enter the quantity: '))
    except ValueError:
        print("❌Please ENTER valid Numbers for the price and Quantity: ☠️ ")
        user_bought_item()

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
        print(f'✨ Total Bill: {user_total_bill:.2f}')
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
                    print(f'✨ Total Bill: ₹{float(row[3]):.2f}')
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
        exit()
    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        show_main_menu()

# if __name__ == "__main__":
#     show_main_menu()
# This code will be implemented later as it will play an important role in the future ** TODO

def add_new_item():
    add_window = tk.Toplevel(root)
    add_window.title("➕ Add Items")
    add_window.geometry("600x500")

    # --- Input Labels & Fields ---
    tk.Label(add_window, text="Item Name:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_name = tk.Entry(add_window)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Price:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_price = tk.Entry(add_window)
    entry_price.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(add_window, text="Quantity:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
    entry_qty = tk.Entry(add_window)
    entry_qty.grid(row=2, column=1, padx=10, pady=10)

    # --- Treeview for Item Table ---
    columns = ("name", "qty", "price", "final")
    tree = ttk.Treeview(add_window, columns=columns, show='headings')
    tree.heading("name", text="Item")
    tree.heading("qty", text="Qty")
    tree.heading("price", text="Price")
    tree.heading("final", text="Final Total")
    tree.grid(row=4, column=0, columnspan=3, padx=10, pady=20)

    # --- Label for Running Total ---
    total_label = tk.Label(add_window, text="✨ Total: ₹0.00", font=("Arial", 12, "bold"))
    total_label.grid(row=5, column=0, columnspan=2)

    # --- Button to Add to Bill ---
    def add_to_bill_gui():
        name = entry_name.get().strip().lower()
        try:
            price = int(entry_price.get())
            qty = int(entry_qty.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter numbers for Price and Quantity.")
            return

        final_price = calculate_bill(price, qty)
        user_cart(name, price, qty, final_price)
        global user_total_bill
        user_total_bill += final_price

        tree.insert("", "end", values=(name, qty, price, f"{final_price:.2f}"))
        total_label.config(text=f"✨ Total: ₹{user_total_bill:.2f}")

        # Clear inputs
        entry_name.delete(0, tk.END)
        entry_price.delete(0, tk.END)
        entry_qty.delete(0, tk.END)

    add_button = ttk.Button(add_window, text="➕ Add to Bill", command=add_to_bill_gui)
    add_button.grid(row=3, column=0, columnspan=2, pady=10)

def generate_final_bill():
    if not items:
        messagebox.showwarning("Empty", "No items to generate the bill.")
        return

    export_to_csv(items, user_total_bill)
    print_bill_to_txt(items, user_total_bill)
    messagebox.showinfo("Success", "✅ Final bill generated!\nCSV and TXT files saved.")

def import_bill_gui():
    file_path = filedialog.askopenfilename(
        title="Select Bill CSV File",
        filetypes=[("CSV Files", "*.csv")]
    )

    if not file_path:
        return  # User cancelled

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header

            bill_text = "📜 Imported Bill:\n"
            bill_text += "-" * 50 + "\n"
            bill_text += f'{"Item":<20}{"Qty":<8}{"Price":<10}{"Final Total"}\n'

            for row in reader:
                if not any(row):
                    continue
                if row[0].lower() == "total":
                    bill_text += "-" * 50 + "\n"
                    bill_text += f'✨ Total Bill: ₹{float(row[3]):.2f}\n'
                    break
                bill_text += f'{row[0]:<20}{row[1]:<8}{row[2]:<10}{row[3]}\n'

        # Show in a new window
        show_imported_bill_popup(bill_text)

    except FileNotFoundError:
        messagebox.showerror("Error", "❌ File not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

def show_imported_bill_popup(text):
    popup = tk.Toplevel(root)
    popup.title("📄 Imported Bill")
    popup.geometry("500x400")

    text_widget = tk.Text(popup, wrap='word', font=("Courier", 10))
    text_widget.insert('1.0', text)
    text_widget.config(state='disabled')  # Make it read-only
    text_widget.pack(fill='both', expand=True, padx=10, pady=10)

def exit_app():
    root.destroy()




def start_gui():
    # Step 1: Create the root window
    # Initialize main application window
    global root
    root = tk.Tk()  # Initializes your GUI window.
    root.title("🧾 Grocery Billing System")  # Sets the window title.
    root.geometry("600x500")  # Width x Height , Fixes the size of the window.

    # Step 2: Create the main frame
    # Create a main frame to hold everything
    main_frame = ttk.Frame(root, padding=10)  # ttk.Frame A clean modern container from ttk that holds the UI elements.
    main_frame.pack(fill='both', expand=True)  # pack() is layout manager that auto-places widgets in order.

    # Step 3: Welcome Label
    welcome_label = ttk.Label(main_frame, text="Welcome to Grocery Billing System!", font=("Arial", 16))
    welcome_label.pack(pady=20)

    # Step 4: Add Buttons for Menu
    btn_add = ttk.Button(main_frame, text="➕ Add New Items & Generate Bill", command=add_new_item)
    btn_add.pack(pady=10, ipadx=10, ipady=5)

    # Update this line to use import_bill_gui instead of import_previous_bill
    btn_import = ttk.Button(main_frame, text="📂 Import Previous Bill", command=import_bill_gui)
    btn_import.pack(pady=10, ipadx=10, ipady=5)

    btn_exit = ttk.Button(main_frame, text="❌ Exit", command=exit_app)
    btn_exit.pack(pady=10, ipadx=10, ipady=5)

    # Add the Generate Final Bill button here
    btn_generate = ttk.Button(main_frame, text="🧾 Generate Final Bill", command=generate_final_bill)
    btn_generate.pack(pady=10, ipadx=10, ipady=5)

    # Step 5: Start the GUI loop
    # Run the mainloop to display window
    root.mainloop()  # Keeps the window running


if __name__ == "__main__":
    mode = input("Choose mode (cli/gui): ").strip().lower()
    if mode == 'cli':
        show_main_menu()
    elif mode == 'gui':
        start_gui()
    else:
        print("❌ Invalid mode. Please choose either 'cli' or 'gui'.")
