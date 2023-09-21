import tkinter as tk
from tkinter import messagebox

DEFAULT_USER = "xxx@gmail.com"  # add os and .env
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
path_storage = "storage/data.txt"


def store_pw():
    website = entry_website.get()
    user = entry_user.get()
    pw = entry_password.get()

    save = messagebox.askokcancel(
        title=website,
        message=f"These are the details entered: \nEmail: {user}\nPassword: {pw}",
    )
    if save:
        data = f"email: {website} | user: {user} | pw: {pw}\n"

        with open(path_storage, "a") as file:
            file.write(data)
        entry_website.delete(0, tk.END)
        entry_password.delete(0, tk.END)
        entry_website.focus()
    else:
        pass


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
button_generate = tk.Button(text="Generate Password")
button_generate.grid(column=2, row=3, sticky="EW")

button_add = tk.Button(text="Add", width=36, command=store_pw)
button_add.grid(column=1, row=4, columnspan=2, sticky="EW")


# UI logic above this line
app.mainloop()
