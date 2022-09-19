import turtle

def turtle_move_Up():
    turtle.setheading(90)
    turtle.stamp()
    turtle.forward(50)

def turtle_move_Down():
    turtle.setheading(270)
    turtle.stamp()
    turtle.forward(50)

def turtle_move_Left():
    turtle.setheading(180)
    turtle.stamp()
    turtle.forward(50)

def turtle_move_Right():
    turtle.setheading(0)
    turtle.stamp()
    turtle.forward(50)

def escape():
    turtle.reset()


turtle.shape("turtle")
turtle.onkey(escape,'Escape')
turtle.onkey(turtle_move_Up,'Up')
turtle.onkey(turtle_move_Down,'Down')
turtle.onkey(turtle_move_Left,'Left')
turtle.onkey(turtle_move_Right,'Right')

turtle.listen()
