from tkinter import *

window = Tk()
window.title("Aboud's First GUI Program")
window.minsize(width=500, height=500)

my_label = Label(text="Label")
my_label.pack()

my_label["text"] = "new text"
my_label.config(text="wew text")

def buttonClicked():
    my_label.config(text=input.get())

#button
button = Button(text="click me", command=buttonClicked)
button.pack()


#Entry
input = Entry()
input.pack()




window.mainloop()

# def add(*args):
#     total = 0
#     for n in args:
#         total  += n
#     print(total)
#
# add(1,1,1,1,1)




