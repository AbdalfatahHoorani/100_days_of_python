import time
import turtle as t
import pandas
from numpy.ma.core import append

ALIGNMENT = "center"
FONT = ("Courier", 7, "normal")


def correctAnswer(answer, data_file):
    answer_turtle = t.Turtle()
    answer_turtle.hideturtle()
    answer_turtle.penup()
    x_coor = data_file[data_file.state == answer]["x"]
    y_coor = data_file[data_file.state == answer]["y"]
    answer_turtle.goto(x=int(x_coor), y=int(y_coor))
    answer_turtle.write(answer, align=ALIGNMENT, font=FONT)

def finishedGame(score):
    ending_title = t.Turtle()
    ending_title.hideturtle()
    ending_title.penup()
    ending_title.color("white")
    ending_title.goto(0, 0)
    ending_title.write(f"Great Job! You guessed all {score} states!", align="center", font=("Courier", 16, "bold"))



screen = t.Screen()
screen.bgcolor("black")
screen.title("U.S. Game")

image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)
# t.onscreenclick(get_mouse_click_coor)



data = pandas.read_csv("50_states.csv")

states_list = data["state"].to_list()

screen.tracer(0)



score = 0
game_on = True
already_answered = []
while game_on:
    state = screen.textinput(title=f"{score}/50 States Correct", prompt="Give a State.").title()

    if state is None:
        game_on = False
        break


    if state == "Exit":
            missed_states = [s for s in states_list if s not in already_answered ]
            with open("missed_states.csv", "w") as mising_states:
                pandas.DataFrame(missed_states).to_csv("missed_states.csv", index=False)
            game_on = False
    elif state in states_list and state != "" and state not in already_answered:
        already_answered.append(state)
        score += 1
        print(score)
        correctAnswer(str(state), data)
        time.sleep(0.1)
        screen.update()
        if score == 50:
            print("Well done you've answered everything.")
            game_on = False









t.mainloop()
