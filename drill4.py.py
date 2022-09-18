import turtle

count = 1
turtle.left(90)
while(count < 7):
    turtle.forward(500)
    turtle.penup(); turtle.goto(count*100,0)
    turtle.pendown()
    count = count + 1
    
turtle.penup()
turtle.home()
turtle.pendown()

count = 1

while(count < 7):
    turtle.forward(500)
    turtle.penup(); turtle.goto(0,count*100)
    turtle.pendown()
    count = count + 1
    
    

turtle.exitonclick()
