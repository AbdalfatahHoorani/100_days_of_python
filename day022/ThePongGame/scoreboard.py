from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.isdown()
        self.left_score = 0
        self.right_score = 0

    def displayScore(self):
        self.clear()
        self.write(f"The Score is: {self.left_score} : {self.right_score}",
                   False, "center", ("Arial", 15, "normal"))

    def rightSideAdd(self):
        self.right_score += 1

    def leftSideAdd(self):
        self.left_score += 1

    def endGame(self):
        self.hideturtle()
        self.write(f"The Score is: {self.left_score} : {self.right_score}",
                   False, "center", ("Arial", 15, "normal"))