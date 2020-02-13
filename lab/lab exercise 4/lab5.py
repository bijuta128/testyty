def factorial(n):
    f=1
    for i in range(1,n+1,1):
        f=f*i
    print("Factorial",f)
n=int(input("Enter a number to compute factorial"))
factorial(n)