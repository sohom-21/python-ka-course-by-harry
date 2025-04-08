# 1. Write a program to find the greatest of four numbers entered by the user.
# num1 = int(input('please enter a number1: '))
# num2 = int(input('please enter a number2: '))
# num3 = int(input('please enter a number3: '))
# num4 = int(input('please enter a number4: '))
# Could have done this way but i wanted to write an oneliner for this

num1, num2, num3, num4 = list(map(int, input('Enter 4 numbers and separated each of them using a comma').split(',')))
print(num1,num2,num3,num4)

if ((num1 > num2) and (num1 > num3) and (num1 > num4)):
    print(f'{num1} is the greatest in all 4 number')
elif ((num2 > num3) and (num2 > num4)):
    print(f'{num2} is the greatest in all 4 number')
elif (num3 > num4):
    print(f'{num3} is the greatest in all 4 number')
else:
    print(f"{num4} is the greatest in all the numbers")

print('program has ended')


# let's write a ternary equivalent of this program in python
#remember in python the syntax of ternary is very different than that of C/java/javascript
#jo ki ye wala hai (condition ? value 1 jo condi true pe hoga : ya value 2 jo condi false pe hoga)
#python ka syntax kutch esa hai
#value_if_true if condition else value_if_false

greatest = num1 if ((num1 > num2) and (num1 > num3) and (num1 > num4)) else \
    num2 if ((num2 > num1) and (num2 > num3) and (num2 > num4)) else \
    num3 if (num3 > num4) else num4

print(f"{greatest} is the greatest number among the 4 numbers")
