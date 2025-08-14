from turtle import Screen, Turtle
import random

game_on = False

screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
start_position = -70

turtle_list = []
for l in range(6):
    turtle_racing = Turtle("turtle")
    turtle_racing.color(colors[l])
    turtle_racing.penup()
    turtle_racing.goto(-230, start_position)
    start_position += 30
    turtle_list.append(turtle_racing)

if user_bet:
    game_on = True

while game_on:
    for turtle in turtle_list:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() >= 220:
            print(turtle.pencolor())
            if user_bet == turtle.pencolor:
                print("YOU'VE WON!!!")
            else:
                print(f"you choose {user_bet} and {turtle.pencolor()} won :( loser!" )
            game_on = False

screen.exitonclick()
