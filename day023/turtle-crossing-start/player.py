from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.backward(MOVE_DISTANCE)

    def win_reset(self):
        self.goto(STARTING_POSITION)

    def collisionWithCar(self, car_list):
        for car in car_list:
            if self.distance(car) < 20:  # tweak 20 to your sizes
                return True
        return False

