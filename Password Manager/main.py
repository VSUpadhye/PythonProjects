from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT = ("Arial", 10, "normal")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    web = website.get()
    email = user_entry.get()
    password = password_entry.get()

    if web == "" or email == "" or password == "":
        messagebox.showerror(title= "Oops!", message= "Please do not leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title= "Adding Password", message= "Are you sure?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{web} | {email} | {password}\n")
                website.delete(0, END)
                user_entry.delete(0, END)
                password_entry.delete(0, END)
                website.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx= 50, pady= 50)
window.title("Password Manager")

canvas = Canvas(height= 200, width= 200)
logo_img = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= logo_img)
canvas.grid(column= 1, row= 0)

# Labels
web_label = Label(text= "Website:", font= FONT)
web_label.grid(column= 0, row= 1)

user_label = Label(text= "Email/Username:", font= FONT)
user_label.grid(column= 0, row= 2)

password_label = Label(text= "Password:", font= FONT)
password_label.grid(column= 0, row= 3)

# Entries
website = Entry(width= 35)
website.grid(column= 1, row= 1, columnspan= 2)
website.focus()

user_entry = Entry(width=35)
user_entry.grid(column= 1, row= 2, columnspan= 2)
#insert method can be used to write something which should already show up when the program is run. Takes index and text

password_entry = Entry(width= 21)
password_entry.grid(column= 1, row= 3)

# Buttons
generate_button = Button(text= "Generate Password", command= generate_password)
generate_button.grid(column= 2, row= 3)

add_button = Button(text= "Add", width= 36, command= save_data)
add_button.grid(column= 1, row= 4, columnspan= 2)

window.mainloop()