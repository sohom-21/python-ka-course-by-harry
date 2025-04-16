# Write a python program using function to convert Celsius to Fahrenheit.
def celsius_toFahrenheit(temp):
    f = (temp * 9/5) + 32
    return f

Temp = int(input("Enter the temperature"))
print(f' The temperature {Temp} ℃ in fahrenheit is {celsius_toFahrenheit(Temp)}')