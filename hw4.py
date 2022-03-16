import turtle

screen = turtle.Screen()
arrow = turtle.Turtle()
screen.bgcolor('black')
arrow.pencolor('red')

forwardDistance=0
directionRight=0

arrow.speed(0)
arrow.penup()
arrow.goto(0,200)
arrow.pendown()
for i in range(210):
    arrow.forward(forwardDistance)
    arrow.right(directionRight)
    forwardDistance+=3
    directionRight+=1

    arrow.hideturtle()
turtle.done()
