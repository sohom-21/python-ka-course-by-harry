import random

computer = random.choice([-1,0,1])
you_choice = input("Enter you choice (s/w/g): ")
youDict = {"s":1,"w":-1,"g":0}
reverseDict = {1:"snake",-1:"water",0:"gun"}
you = youDict[you_choice]

print(f"you chose {reverseDict[you]} \nComputer chose {reverseDict[computer]}")

if computer == you:
    print("Its a draw!")
else:
    if(computer - you) == -1 or (computer - you) == 2:
        print("you lose!")
    else:
        print("you win!")

"""if (computer == -1) and (you == 1): (computer - you) = -2 
     print("you win!")
    elif (computer == -1) and (you == 0):  (computer - you) =-1
        print("you lose")
    elif (computer == 1) and (you == -1): (computer - you) = 2
        print("you lose")
    elif (computer == 1) and (you == 0):  (computer - you) =1
        print("you win")
    elif (computer == 0) and (you == -1):  (computer - you) =1
        print("you win")
    elif (computer == 0) and (you == 1):  (computer - you) =-1
        print("you lose")
    else:
        print("Something went wrong")
        # we are calculating (computer - you) to find a pattern and make the code smaller 
"""
