from tkinter import *

def conversionCalculation():
    get_entry = float(input.get())
    calculation = round(get_entry * 1.6009)
    output_label.config(text=f"is equal to      {calculation}        KM")


window = Tk()
window.title("Mile to Kilometer converter")
window.config(width=250, height=100,padx=30,pady=10)
window.minsize(width=110, height=30)

#Entry KM
input = Entry()
input.config(width=12)
input.place(x=70,y=10)

#First label
label = Label(text="Miles")
label.place(x=110,y=10)

#Second label
output_label = Label(text=f"is equal to              KM")
output_label.place(x=10,y=30)

#Entry button
button = Button(text="Calculate", command=conversionCalculation)
button.place(x=65,y=50)




window.mainloop()
