# Write a python function which converts inches to cms.

def convert(inch):
    cm = inch * 2.54
    return cm

def convert_to_inch(cm):
    inch =  cm / 2.54
    inch = '%.2f'%inch
    return inch

def main():
    print("\n Enter 1 to convert inch to cm")
    print("\n Enter 2 to convert cm to inch")
    print("\n Enter 3 to exit program")
    choice = int(input("\nEnter your choice"))
    if choice == 1:
        num =int(input("Enter the number: "))
        print(f"{num} inches in cm is {convert(num)}")
    elif choice == 2:
        num = int(input("Enter the number: "))
        print(f'{num} cm in inches is {convert_to_inch(num)}')
    else:
        print("Thank for using the program goodBye !!!")
        exit()

main()