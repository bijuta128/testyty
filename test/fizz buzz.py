def fizz_buzz(x):
    if x%3==0 and x%5==0:
        return "fizzbuzz"
    elif x%3==0:
        return "fizz"
    elif x%5==0:
        return"buzz"
    else:
        return
a=int(input("enter a number:"))
print (fizz_buzz(a))

