from turtle import Screen, Turtle
import  time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_over = Turtle()

game_over.hideturtle()
game_over.color("White")


scoreboard.displayScore()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")





game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        print("EAT")
        food.foodEaten()
        snake.addSegment()
        scoreboard.displayScore()

    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        print("you hit the wall")
        game_over.write("Game over! you've hit a wall :(", False, "center", ("Arial", 10, "normal"))
        game_on = False

    for segments in snake.segments[1:]:
        if snake.head.distance(segments) < 10:
            game_over.write("Game over! you've ATE your tail silly :(", False, "center", ("Arial", 10, "normal"))
            game_on = False


screen.exitonclick()
