#Write a Python program to convert temperatures to and from celsius to fahrenheit
#C = (5/9) * (F - 32)
Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))

Celsius = (Fahrenheit - 32) * 5.0/9.0

print("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C")