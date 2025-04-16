# Write a program to find whether a given username contains less than 10
# characters or not.
name_of_the_user = input("Enter your name: ").strip()
name_length = len(name_of_the_user)
if name_length < 10:
    print(f"your name {name_of_the_user} has less than 10 characters")
else:
    print(f"you name {name_of_the_user} has more than 10 characters in it")
print("\nprograms has ended")
