import time
from turtle import Screen, Turtle, ontimer
import random
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
player = Player()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

car = CarManager()
car_generator = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if car_generator == 6:
        car.createCars()
        car_generator = 0
    car.move()
    car_generator += 1


    if player.collisionWithCar(car.garage):
        print("")

    if player.ycor() > 300:
        player.win_reset()


screen.exitonclick()
