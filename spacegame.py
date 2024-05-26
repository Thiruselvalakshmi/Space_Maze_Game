import turtle
rocket=turtle.Turtle()
space=turtle.Screen()
sman=turtle.Turtle()
space.bgpic("D:\MY DETAILS (THIRU)\LMES\game1\space.gif")
space.addshape("D:\MY DETAILS (THIRU)\LMES\game1\jet.gif")
space.addshape("D:\MY DETAILS (THIRU)\LMES\game1\Rjet.gif")
space.addshape("D:\MY DETAILS (THIRU)\LMES\game1\Ljet.gif")
space.addshape("D:\MY DETAILS (THIRU)\LMES\game1\Djet.gif")
rocket.shape("D:\MY DETAILS (THIRU)\LMES\game1\jet.gif")
space.addshape("D:\MY DETAILS (THIRU)\LMES\game1\spaceman.gif")
sman.shape("D:\MY DETAILS (THIRU)\LMES\game1\spaceman.gif")
sman.penup()
sman.goto(-103,255)
rocket.penup()
rocket.goto(180,-230)
rocket.speed(1500)

def up():
    rocket.shape("D:\MY DETAILS (THIRU)\LMES\game1\jet.gif")
    y=rocket.ycor()
    y+=10
    if y>=255:
        y=255
    rocket.sety(y)
    '''rocket.setheading(90)
    rocket.forward(10)
    rocket.setheading(0)'''

def down():
    rocket.shape("D:\MY DETAILS (THIRU)\LMES\game1\Djet.gif")
    y=rocket.ycor()
    y-=10
    if y<=-230:
        y=-230
    rocket.sety(y)
    '''rocket.setheading(270)
    rocket.forward(10)
    rocket.setheading(0)'''

def left():
    rocket.shape("D:\MY DETAILS (THIRU)\LMES\game1\Ljet.gif")
    x=rocket.xcor()
    x-=10
    if x<=-220:
        x=-220
    rocket.setx(x)
    '''rocket.setheading(180)
    rocket.forward(10)
    rocket.setheading(0)'''

def right():
    rocket.shape("D:\MY DETAILS (THIRU)\LMES\game1\Rjet.gif")
    x=rocket.xcor()
    x+=10
    if x>=250:
        x=250
    rocket.setx(x)
    #rocket.forward(10)


turtle.listen()
turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")

while True:
    space.update()
    if rocket.distance(sman)<10:
        space.bgpic("D:\MY DETAILS (THIRU)\LMES\game1\op.gif")

turtle.done()