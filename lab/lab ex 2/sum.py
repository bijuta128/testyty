def sum(a,b,c):
    if(a==b or a==c or b==c):
        return("sorry, two numbers are same")
    else:
        x=a+b+c
        return(x)

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
y=sum(a,b,c)
print(y)
