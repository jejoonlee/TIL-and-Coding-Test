from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# card_back = PhotoImage(file="images/card_back.png")

# ------------------ random words ---------------------
words = pandas.read_csv("data/french_words.csv")
print(words.keys)

# ----------------------- UI --------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front)
french = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
french_word = canvas.create_text(400, 283, text="word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0)
button_wrong.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
button_correct = Button(image=right, highlightthickness=0)
button_correct.grid(row=1, column=1)

window.mainloop()
