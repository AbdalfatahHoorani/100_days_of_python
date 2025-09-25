from tkinter import *

import pandas
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

def next_card():
    global current_card
    current_card = random.choice(records)

    canvas.itemconfig(card_image, image=front_image)  # make sure front is visible
    language_label.config(text="French", bg="white", fg="black")
    word_label.config(text=current_card['French'], bg="white", fg="black")

    # schedule the flip
    window.after(3000, flip_card)

def is_known():
    records.remove(current_card)
    next_card()
    data = pandas.DataFrame(records)
    data.to_csv("./data/words_to_learn.csv", index=False)



def flip_card():
    # change the image
    canvas.itemconfig(card_image, image=back_image)

    # change labels to English
    language_label.config(text="English", bg="#91C2AF", fg="white")
    word_label.config(text=current_card['English'], bg="#91C2AF", fg="white")



window = Tk()
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
window.after(3000, func=flip_card)

#Data from the CSV file

records = {}
try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    records = original_data.to_dict(orient="records")
else:
    records = data.to_dict(orient="records")

back_image = PhotoImage(file="./images/card_back.png")

#Canvas front and back
canvas = Canvas(width=800, height=526,highlightthickness=0, bg=BACKGROUND_COLOR)
front_image = PhotoImage(file="./images/card_front.png")
card_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)




#Labels
language_label = Label(text="French",font=("Ariel", 40, "italic"), bg="White")
language_label.place(x=330, y=100)

word_label = Label(text="Aboud",font=("Ariel", 40, "bold"), bg="White")
word_label.place(x=330, y=200)
current_card = {}









# right and wrong buttons
right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)






next_card()


window.mainloop()
