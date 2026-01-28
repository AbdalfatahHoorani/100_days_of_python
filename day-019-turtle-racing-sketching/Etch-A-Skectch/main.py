import turtle
from operator import truediv
from turtle import Turtle, Screen

#W
def forward():
    timmy.forward(10)
    pass
#S
def backwards():
    timmy.backward(10)
    pass

#D
def clockwise():
    timmy.left(10)
    pass
#A
def counterClockwise():
    timmy.right(10)


#C
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

timmy = Turtle()
timmy.speed("fastest")

screen = Screen()

screen.listen()
screen.onkey(backwards, "s")
screen.onkey(forward, "w")
screen.onkey(clockwise, "d")
screen.onkey(counterClockwise, "a")
screen.onkey(clear,"c")





screen.exitonclick()
