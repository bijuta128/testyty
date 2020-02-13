import turtle
wn=turtle.Screen()
pen=turtle.Turtle()
for i in range (5):
    pen.circle(20*i)
    pen.up()
    pen.sety((20*i)*-1)
    pen.down()
turtle.done()