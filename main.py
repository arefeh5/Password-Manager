from tkinter import *
from tkinter import messagebox
import random
#import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
               'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
               'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
               'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_', '+', "?", '.']
    picked_letters = random.randint(8,10)
    picked_numbers = random.randint(2,4)
    picked_symbols = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(picked_letters)]
    password_numbers = [random.choice(numbers) for _ in range(picked_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(picked_symbols)]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_entry.insert(0, password)
 #   pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)== 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Oh no! You've left something blank, please try again")
    else:
        correct = messagebox.askokcancel(title=website, message=f"This is the information given: \n \nEmail: {email} "
                                                f"\nPassword: {password} \n \nIs this correct and okay to save?")
        if correct:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
username = Label(text="Email/Username:")
username.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

#Userinputs
website_entry = Entry(width=56)
website_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky='w')
website_entry.focus()
email_entry = Entry(width=56)
email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky='w')
password_entry = Entry(width=36)
password_entry.grid(row=3, column=1, columnspan=2, pady=5, sticky='w')

#Buttons
generate_password_button = Button(text="Generate Password", width=15, command=generate_password)
generate_password_button.grid(row=3, column=2, padx=0, sticky='e')
add_button = Button(text="Add", width=47, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=5, sticky='w')


window.mainloop()
