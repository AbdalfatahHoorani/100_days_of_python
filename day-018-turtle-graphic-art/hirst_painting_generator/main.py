import colorgram
from turtle import Turtle, Screen
import random
# colors = colorgram.extract('hirst.jpg', 30)
#
# color_bank = []
# for l in range(len(colors)):
#     color = colors[l]
#     rgb = color.rgb
#     new_entry = (rgb[0],rgb[1],rgb[2])
#     color_bank.append(new_entry)
#
# print(color_bank)

color_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5),
              (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12),
              (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229),
              (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198),
              (65, 231, 239), (217, 88, 51)]

def timmyNextLine():
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)
    timmy.forward(510)
    timmy.right(180)

screen = Screen()
screen.colormode(255)

timmy = Turtle()
timmy.speed(1000)
timmy.pensize(20)
timmy.penup()
timmy.left(90)
timmy.forward(300)
timmy.left(90)
timmy.forward(500)
timmy.left(180)

for j in range(10):
    for l in range(10):
        timmy.pendown()
        timmy.pencolor(random.choice(color_list))
        timmy.forward(1)
        timmy.penup()
        timmy.forward(50)
    timmyNextLine()
timmy.color("white")


screen.exitonclick()
