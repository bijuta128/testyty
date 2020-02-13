def palin():
    b=0
    c=0
    a=int(input("enter a number"))
    x=a
    for i in range(a):
            c=a%10
            b=b*10 + c
            if (b==x):
                print("the number is palindrome")
            else:
                print("the number is not palindrome")
palin()