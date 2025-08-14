from turtle import Turtle
import random, math

HITBOX = 25
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fast")
        self.ball_speed = 200  # pixels per frame


        angle = random.uniform(0, 360)
        self.dx = self.ball_speed * math.cos(math.radians(angle))
        self.dy = self.ball_speed * math.sin(math.radians(angle))
        self.dx_reset = self.dx

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def collisionWithWall(self, height_of_screen):
        height_positive = height_of_screen/2
        height_negative = height_positive * -1
        if self.ycor() >= height_positive or self.ycor() <= height_negative:
            self.dy *= -1

    def collisionWithPaddle(self, paddle_coord):
        if (paddle_coord[0] - HITBOX <= self.xcor() <= paddle_coord[0] + HITBOX and
                paddle_coord [1] - HITBOX <= self.ycor() <= paddle_coord[1] + HITBOX):
            self.dx *= -1


    def collisionWithScoreWall(self, width_of_screen):
        right_side = (width_of_screen - 10 ) / 2
        left_side =  right_side * - 1
        if self.xcor() < left_side:
            self.goto(0,0)
            self.dx *= -1
            self.dx *= 0.9
            return "left side hit"
        if self.xcor() > right_side:
            self.goto(0,0)
            self.dx *= -1
            self.dx *= 0.9
            return "right side hit"
        return False




