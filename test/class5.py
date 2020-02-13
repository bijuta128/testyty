print('write your choices?')
print('1 for addition')
print('2 for subtraction')
print('3 for multiplication')
print('4 for division')
def addition(x,y) :
 z=int(x+y)
 return z
def subtraction(a,b) :
    c=int(a-b)
    return c
def multiplication(e,f) :
    g=int(e*f)
    return g
def division(i,j) :
    k=int(j/i)
    return k
if (choice ==1):
    x = int(input('enter a number'))
    y = int(input('enter a number'))
    m=addition(x,y)
    print(m)

elif (choice == 2):
    a = int(input('enter a number'))
    b = int(input('enter a number'))
   n=subtraction(a,b)
   print(n)
elif (choice == 3):
    e = int(input('enter a number'))
    f = int(input('enter a number'))
    o=multiplication(e,f)
   print(o)
elif (choice == 4):
    i = int(input('enter a number'))
    j = int(input('enter a number'))
    p=division(i,j)
    print(p)