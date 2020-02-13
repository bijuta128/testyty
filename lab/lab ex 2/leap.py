def year(n):
    if (n%4 == 0 and n%100 != 0):
        return ("yes, the year",n,"is a leap year")
    else:
        return ("no, the year",n,"isn't a leap year")

n=int(input("enter a year"))
x=year(n)
print(x)