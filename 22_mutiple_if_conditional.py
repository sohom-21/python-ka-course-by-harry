a=int(input("Enter your age: "))

if (a%2 == 0):
    print("a is even")
#end of if statement no 1
if (a > 18):
    print("Aap vote de sakte ho")
    print("please vote properly as your vote matters")
elif (a < 0):
    print("you are entering an invalid age")
elif (a == 0):
    print("Madarchod tu toh abhi paida hi hua hai tera kesa vote ???")
else:
    print(f"Tum 18 ke nahi hue ho better luck again next {18 - a} years me")
#end of if statement no 2
print("\nEnd of program")

#there can be multiple no of if statements in a program as if statements are independent
#also there can be any number of elif statements in a program
#but the elif and else statement can be written in a program independently as they depend on if
#last else is only execute when the if and the elif before it fails
