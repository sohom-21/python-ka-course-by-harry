# yahan function ko 3 numbers bhejne ke liye tayaar kiya hai (a, b, c)
def avg(a,b,c):
    average = (a+b+c)/3
    print('average is', average)

#function call karte waqt numbers de rahe hai as parameters
number1 = int(input('Enter a number: '))
number2 = int(input('Enter a number: '))
number3 = int(input('Enter a number: '))
avg(number1,number2, number3)