import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
breadth=45
length=30
for i in range (5):
    pen.forward((length)*(breadth))
    pen.up()
    pen.left(90)
    pen.down()
turtle.done()
