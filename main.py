from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for letter in range(nr_letters)]
    password_symbols = [random.choice(symbols) for sym in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for num in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    if len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any fields empty!")

    else:
        is_okay = messagebox.askokcancel(title=website_entry.get(), message=f"These are the details entered: "
                                                                  f"\nEmail: {email_entry.get()}"
                                                                  f"\nPassword: {password_entry.get()}"
                                                                  f"\nIs it okay to save?")

        if is_okay:
            with open("data.txt", "a") as data:
                data.write(f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_entry = Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=51)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "tmtran926@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=33)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
