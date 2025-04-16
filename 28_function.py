# a = int(input('Enter a number: '))
# b = int(input('Enter a number: '))
# c = int(input('Enter a number: '))
#
# average = (a+b+c)/3
# print(average)

# Pehle hum user se 3 numbers le rahe the, unka average nikaal ke print karte the

# Lekin soch, agar yehi code baar-baar likhna pad jaaye alag-alag jagah — boring ho jaayega
# Isliye function banate hain — ek baar likho, naam de do, aur jab chahiye tab bula lo

# Function banaya hai 'avg' naam ka ya isko function definition bolte hai !!!!!
def avg():
    # User se 3 numbers le rahe hain
    a = int(input('Enter a number: '))
    b = int(input('Enter a number: '))
    c = int(input('Enter a number: '))

    # Average calculate kar rahe hain
    average = (a + b + c) / 3

    # Average print kar rahe hain
    print(average)


# Function ko call kar rahe hain — ab ye 3 number lega, average nikaalega aur print karega
avg() #this is called function call

# toh ab iska definition dekh lete hai thora
# a function is a group of statements performing a specific task.
# when a program gets bigger in size and its complexity grows,
# it gets difficult for a program to keep track on which piece of code is doing what