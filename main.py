import tkinter as tk

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
app = tk.Tk()
app.title("Password Manager")

# Canvas
canvas = tk.Canvas(width=200, height=200)
my_image = tk.PhotoImage(file="images/logo.png")
canvas.create_image(10, 10, image=my_image, anchor="nw")
# canvas.pack(padx=20, pady=20)
canvas.grid(column=0, row=0, padx=20, pady=20)

# UI logic above this line
app.mainloop()
