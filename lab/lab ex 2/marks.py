a=int(input("enter the marks of 1st subject"))
b=int(input("enter the marks of 2nd subject"))
c=int(input("enter the marks of 3rd subject"))
d=int(input("enter the marks of 4th subject"))
x=a+b+c+d
per=(x/400)*100
print("your percentage is",x,"%")
if per>=70:
    print("you got Distinction")
elif(per>=60):
    print("you got first division")
elif(per>=40):
    print("you got second division")
elif(per<40):
    print("you failed")
