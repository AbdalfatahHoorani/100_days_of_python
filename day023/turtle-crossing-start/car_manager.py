import random
from turtle import Turtle
import time


COLORS = ["red", "orange", "Black", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NEW_SPEED = 5

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(900,900)
        self.garage = []
        self.count = 0



    def createCars(self):
        test = Turtle()
        test.shape("square")
        test.penup()
        test.shapesize(stretch_len=0.8, stretch_wid=0.5)
        test.color(random.choice(COLORS))
        test.goto(x=290, y=random.randint(-250, 250))
        self.garage.append(test)


    def move(self):
        for car in self.garage:
            car.backward(STARTING_MOVE_DISTANCE)


    def speedUp(self):
        self.clear()


