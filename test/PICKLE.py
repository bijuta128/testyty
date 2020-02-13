a=int(input("enter a number:"))
b=int(input("enter a number:"))
try:
    print(b/a)
except ZeroDivisionError:
    print("cannot divide by zero biju")
print('over')