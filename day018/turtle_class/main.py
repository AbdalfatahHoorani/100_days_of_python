from turtle import Turtle, Screen, colormode
from random import randint

def squareByTurtle():
    for l in range(4):
        timmy.forward(100)
        timmy.right(90)


def dashedLines():
    for l in range(5):
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()

def polygons():
    length = 100
    num_sides = 3
    full_circle = 360

    while num_sides < 9:
        for _ in range(num_sides):
            timmy.forward(length)
            timmy.right(full_circle/num_sides)

        num_sides += 1
        randomLineColorGenerator()

def randomLineColorGenerator():
    rand1 = randint(1, 255)
    rand2 = randint(1, 255)
    rand3 = randint(0, 255)
    timmy.pencolor(rand1, rand2, rand3)

def randomWalk(walk_num):

    i = 0
    while i < walk_num:
        randomLineColorGenerator()
        random_choice = randint(1, 4)
        walk_length = 25

        #forward
        if random_choice == 1:
            timmy.forward(walk_length)
        #backwards
        elif random_choice == 2:
            timmy.right(180)
            timmy.forward(walk_length)
        #left
        elif random_choice == 3:
            timmy.left(90)
            timmy.forward(walk_length)
        #right
        elif random_choice == 3:
            timmy.right(90)
            timmy.forward(walk_length)
        i += 1
def drawACircle(times):
    for i in range(int(360/times)):
        randomLineColorGenerator()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + times )

screen = Screen()
colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.pensize(2)
timmy.speed("fastest")

drawACircle(20)

screen.exitonclick()
