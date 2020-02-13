a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
if (a<b and a<c):
    print(a,"is the smallest")
elif(b<a and b<c):
    print(b,"is the smallest")
else:
    print(c,"is the smallest")