def multiple(a):
    b = 0
    for i in range (a):
        if (a%3 and a%5)==0:
            b=i+b
    print("sum is",b)
a=int(input("enter a number"))
multiple(a)