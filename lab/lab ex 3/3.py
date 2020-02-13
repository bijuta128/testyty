def showNumbers(limit):
    for i in range(0,limit,1):
        a=i%2
        if a==0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
limit=int(input("Enter a number"))
showNumbers(limit)