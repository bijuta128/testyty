def factriol(a):
    if a==1:
        return 1
    else:
        return(a*factriol(a-1))
num=int(input("enter a number"))
fact=factriol(num)
print("the facriol is",fact)










