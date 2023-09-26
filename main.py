import tkinter as tk
from tkinter import messagebox
import random
from support_data import characters as c
import pyperclip
import json
from pathlib import Path

DEFAULT_USER = "xxx@gmail.com"  # add os and .env
path_storage = Path("storage/data.json")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    pw_letters = [random.choice(c.letters) for _ in range(random.randint(7, 10))]
    pw_capital = [random.choice(c.capital) for _ in range(random.randint(2, 4))]
    pw_numbers = [random.choice(c.numbers) for _ in range(random.randint(2, 5))]
    pw_symbols = [random.choice(c.symbols) for _ in range(random.randint(2, 4))]

    password_list = pw_letters + pw_capital + pw_numbers + pw_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    pyperclip.copy(password)
    entry_password.delete(0, tk.END)
    entry_password.insert(index=0, string=password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def dir_exist(file_path):
    dummy_data = {}
    if not file_path.parent.is_dir() or not file_path.is_file():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w") as file:
            json.dump(dummy_data, file, indent=4)


def store_pw():
    dir_exist(path_storage)
    website = entry_website.get()
    user = entry_user.get()
    pw = entry_password.get()

    if len(website) == 0 or len(pw) == 0:
        messagebox.showinfo(
            title="Error", message="Website and Password has to be filled"
        )
    else:
        data_dict = {
            website: {
                "user": user,
                "password": pw,
            },
        }
        #    save = messagebox.askokcancel(
        #        title=website,
        #        message=f"These are the details entered: \nEmail: {user}\nPassword: {pw}",
        #    )
        #    if save:

        with open(path_storage, "r") as file:
            data = json.load(file)
            data.update(data_dict)
        with open(path_storage, "w") as file:
            json.dump(data, file, indent=4)
            entry_website.delete(0, tk.END)
            entry_password.delete(0, tk.END)
            entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #
app = tk.Tk()
app.title("Password Manager")
app.config(padx=50, pady=50)

# Canvas
canvas = tk.Canvas(width=200, height=200)
my_image = tk.PhotoImage(file="images/logo.png")
canvas.create_image(100, 100, image=my_image)
canvas.grid(column=1, row=0)

# Labels x 3
label_website = tk.Label(text="Website:")
label_website.grid(column=0, row=1)

label_user = tk.Label(text="Email/Username:")
label_user.grid(column=0, row=2)

label_password = tk.Label(text="Password:")
label_password.grid(column=0, row=3)

# Input x 3
entry_website = tk.Entry(width=35)
entry_website.grid(column=1, row=1, columnspan=2, sticky="EW")
entry_website.focus()

entry_user = tk.Entry(width=35)
entry_user.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_user.insert(index=tk.END, string=DEFAULT_USER)

entry_password = tk.Entry(width=21)
entry_password.grid(column=1, row=3, sticky="EW")

# Button x 2
button_generate = tk.Button(text="Generate Password", command=generate_pw)
button_generate.grid(column=2, row=3, sticky="EW")

button_add = tk.Button(text="Add", width=36, command=store_pw)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")

# UI logic above this line
app.mainloop()
