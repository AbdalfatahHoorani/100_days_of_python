import json
from tkinter import *
from tkinter import messagebox
import random
from xml.etree.ElementTree import indent

import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generatePassword():
    password_list = []

    letters_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    symbols_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    numbers_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list
    random.shuffle(password_list)

    password = ''.join(str(x) for x in password_list)
    pass_entry.insert(index=0, string=password)
    pyperclip.copy(password)

# ---------------------------- Search PASSWORD ------------------------------- #

def find_password():
    new_data = {"for creation": {
        "email": "email",
        "password": "password",
    }
    }

    try:
        with open("saved_passwords.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File is being created")
        with open("saved_passwords.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)

    else:
        website = web_entry.get().title()
        for websites in data:
            if websites == website:
                messagebox.showinfo("Notice", f"email: {data[website]["email"]} \n\n"
                                              f"password: {data[website]["password"]}")
            else:
                messagebox.showinfo(title="No Data Found", message=f"there is not information about {website}")

    finally:
        web_entry.delete(0, END)
        pass_entry.delete(0, END)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def savingPassword():
    website = web_entry.get().title()
    email = eu_entry.get()
    password = pass_entry.get()
    new_data = {website: {
        "email": email,
        "password": password,
                          }
    }



    if password == "" or website == "" or email == "":
        messagebox.showinfo(title="empty entry", message=f"You left one of the entries empty!")
    else:
        try:
            with open("saved_passwords.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("saved_passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
            print("Created a new file")

        else:
            data.update(new_data)
            with open("saved_passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window  = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


#image logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


#labels: WEBSITE, EMAIL/USERNAME, PASSWORD
website_label = Label(text="Website")
website_label.grid(row= 1, column= 0)

eu_label = Label(text="Email/Username")
eu_label.grid(row= 2, column= 0)

password_label = Label(text="Password")
password_label.grid(row= 3, column= 0)

#Entry: WEBSITE ENTRY, EU ENTRY, PASSWORD ENTRY


eu_entry = Entry(width= 42)
eu_entry.grid(row= 2, column= 1, columnspan= 2)
eu_entry.insert(0, "SomeEmail@Gmail.Com")


#frame the password's entry and button together
password_frame = Frame(window)
password_frame.grid(row=3, column=1, columnspan=2)

pass_entry = Entry(password_frame, width=18)
pass_entry.grid(row=0, column=0)

#buttons: ADD,GENERATE, Search
generate_button = Button(password_frame, text="Generate Password", width= 19, command=generatePassword)
generate_button.grid(row=0, column=1, padx=2)

add_button = Button(text= "Add",width= 36, command=savingPassword)
add_button.grid(row= 4, column= 1, columnspan= 2)


search_frame = Frame(window)
search_frame.grid(row=1, column=1, columnspan=2)

web_entry = Entry(search_frame, width=18)
web_entry.grid(row= 1, column= 1)
web_entry.focus()

search_button = Button(search_frame, text="Search", width= 19, command=find_password)
search_button.grid(column=2, row= 1, padx=2)





window.mainloop()
