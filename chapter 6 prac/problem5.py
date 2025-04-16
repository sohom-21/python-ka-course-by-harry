# 5. Write a program which finds out whether a given name is present in a list or not.
name_list = ['harry', 'madan', 'kim seok-ryu', 'kim soo-hyun', 'sohom', 'alex', 'manas']

user_name = input("Enter your name: ").lower()

if user_name in name_list:
    print("Yay! Your name exists in the list!")
else:
    print("Your name doesn't exist, but we'll add it to the list.")
    name_list.append(user_name)
    print("Your name has been added.")

# Ask if user wants to try again
retry = input("Do you want to try again? (yes/no): ").lower()
if retry == "yes":
    user_name = input("Enter your name again and try: ").lower()
    if user_name in name_list:
        print(f"Your name is '{user_name}' and it exists in the system.")
    else:
        print("Hmm, something went wrong. We didn't find your name.")
else:
    print("Okay, goodbye!")