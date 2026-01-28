from turtle import Turtle

SCORE_NUM = -1

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.isdown()

    def displayScore(self):
        global SCORE_NUM
        SCORE_NUM += 1
        self.clear()
        self.write(f"The Score is: {SCORE_NUM}", False, "center", ("Arial", 15, "normal"))
