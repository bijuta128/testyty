def greatest(a,b,c):
    if (a>b and a>c):
        return (a, "is greatest")
    elif (b>a and b>c):
        return (b, "is greatest")
    else:
        return (c, "is greatest")

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
x=(greatest(a,b,c))
print (x)