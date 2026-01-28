import random
from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

RIGHT_PLAYER = (350, 0)
LEFT_PLAYER = (-350, 0)
MOVE_DISTANCE = 10

#initialize the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)

#in paddle class
paddle1 = Paddle(RIGHT_PLAYER)
paddle2 = Paddle(LEFT_PLAYER)

#in ball
ball = Ball()

scoreboard = Scoreboard()
scoreboard.displayScore()

screen.listen()
screen.onkeypress(paddle1.up,"Up")
screen.onkeypress(paddle1.down,"Down")
screen.onkeypress(paddle2.up,"w")
screen.onkeypress(paddle2.down,"s")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    ball.collisionWithWall(600 - 20)
    ball.collisionWithPaddle(paddle1.position())
    ball.collisionWithPaddle(paddle2.position())
    result = ball.collisionWithScoreWall(800)
    if result == "left side hit":
        scoreboard.rightSideAdd()
        scoreboard.displayScore()
    elif result == "right side hit":
        scoreboard.leftSideAdd()
        scoreboard.displayScore()

    if scoreboard.right_score == 3:
        print("right won")
        game_on = False
    elif scoreboard.left_score == 3:
        print("left won")
        game_on = False





screen.exitonclick()
