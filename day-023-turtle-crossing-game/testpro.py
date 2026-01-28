from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height= 600)

hehe = []

for i in range(3):
    turtle1 = Turtle()
    turtle1.goto(0,0)
    hehe.append(turtle1)

for turt in hehe:
    print(turt.xcor())



screen.exitonclick()