print('write your choices?')
print('1 for addition')
print('2 for subtraction')
print('3 for multiplication')
print('4 for division')
choice=int(input('which'))
def addition() :
 x=int(input('enter a number'))
 y=int(input('enter a number'))
 z=(x+y)
 print(z)
def subtraction() :
    a=int(input('enter a number'))
    b=int(input('enter a number'))
    c=(a-b)
    print(c)
def multiplication() :
    e=int(input('enter a number'))
    f=int(input('enter a number'))
    g=(e*f)
    print(g)
def division() :
    i=int(input('enter a number'))
    j=int(input('enter a number'))
    k=(j/i)
    print(k)
if (choice ==1):
    addition()
elif (choice == 2):
    subtraction()
elif (choice == 3):
    multiplication()
elif (choice == 4):
    division()









