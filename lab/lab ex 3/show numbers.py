def limit(a):
    for i in range(a):
        a=i%2
        if a==0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
a=int(input("Enter a number"))
limit(a)