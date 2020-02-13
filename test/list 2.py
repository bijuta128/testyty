num=[5,4,3,2,1]
I=0
while i<5:
    j=0
    while j<4:
        if num(j)>num[j+1]:
            temp=num[j]
            num(j)=num[j+1
            num[j+1]=temp
    j=j+1
    i=i+1
print(num)
