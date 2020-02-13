a=int(input("enter a number"))
def boy(a):
    s=a
    sum=0
    while (a>0):
        d=(a%10)
        sum=sum+d
        a=a//10
    return (sum)
ans=boy(a)
print(ans)



