num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
odd = 0
even = 0
for x in num:
        if  x % 2:
    	     odd+=1
        else:
    	     even+=1
print("Number of even numbers is",even)
print("Number of odd numbers is",odd)