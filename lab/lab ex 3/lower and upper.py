def u_l(a):
    count1=0
    count2=0
    for i in a:
        if (a.islower()):
            count1=count1+1
        elif (a.isupper()):
            count2=count2+1
    print(count1)
    print(count2)
a=str(input("enter a word"))
u_l(a)
