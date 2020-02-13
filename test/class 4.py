print('write your choices?')
print('1 for addition')
print('2 for subtraction')
print('3 for multiplication')
print('4 for division')
def addition(x,y) :
 z=int(x+y)
 print(z)
def subtraction(a,b) :
    c=int(a-b)
    print(c)
def multiplication(e,f) :
    g=int(e*f)
    print(g)
def division(i,j) :
    k=int(j/i)
    print(k)
if (choice ==1):
    x = int(input('enter a number'))
    y = int(input('enter a number'))
    addition(x,y)
elif (choice == 2):
    a = int(input('enter a number'))
    b = int(input('enter a number'))
    subtraction(a,b)
elif (choice == 3):
    e = int(input('enter a number'))
    f = int(input('enter a number'))
    multiplication(e,f)
elif (choice == 4):
    i = int(input('enter a number'))
    j = int(input('enter a number'))
    division(i,j)
