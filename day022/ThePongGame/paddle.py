from turtle import Turtle

PADDLE_SIZE = 20
PLAYER_COLOR = "White"
MOVEMENT_SPEED = 20

class Paddle(Turtle):

    def __init__(self, player_coord):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(PLAYER_COLOR)
        self.goto(player_coord)


    # RIGHT PLAYER CONTROLS
    def up(self):
        self.goto(self.xcor(), self.ycor() + MOVEMENT_SPEED)
    def down(self):
        self.goto(self.xcor(), self.ycor() - MOVEMENT_SPEED)




