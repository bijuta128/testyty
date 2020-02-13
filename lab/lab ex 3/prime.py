def prime(a):
    count=0
    for i in range(1,a+1,1):
        p=a%i
        if(p==0):
            count=count+1
    if count==2:
        print("prime")
    else:
        print("composit")
a=int(input("enter a number"))
prime(a)