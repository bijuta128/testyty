def f_b(a):
    if (a%3==0 and a%5!=0):
        return 1
    elif (a%5==0 and a%3!=0):
        return 2
    elif (a%3 and a%5)==0:
        return 3
    else:
        return 4

a=int(input("enter any number"))
x=f_b(a)
if x==1:
    print("fizz")
elif (x==2):
    print("buzz")
elif (x==3):
    print("fizzbuzz")
else:
    print("error")