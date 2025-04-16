# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program
# to detect these spam.
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
user_message = input("Enter the message you want to check: ")
if ((p1 in user_message) or (p2 in user_message) or (p3 in user_message) or (p4 in user_message)):
    print("This message is a spam message")
else:
    print("This message is not a spam message")
print("\n program ends here")
