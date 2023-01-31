from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words_list = {}

# ------------------ random words ---------------------

try:
    words = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original = pandas.read_csv("data/french_words.csv")
    words_list = original.to_dict(orient="records")
else:
    words_list = words.to_dict(orient='records')

def next_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)

    current_card = random.choice(words_list)

    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card['French'], fill="black")
    canvas.itemconfig(card_background, image=card_front)

    flip_timer = window.after(3000, func=flip_card)
    
#---------- 3 seconds later, show english card ----------

def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['English'], fill="white")
    canvas.itemconfig(card_background, image=card_back)

#--------- 초록색 체크를 누르면, 리스트에서 없앤다 ---------

def is_known():
    words_list.remove(current_card)
    new_data = pandas.DataFrame.from_dict(words_list)
    new_data.to_csv("words_to_learn.csv", index=False)

    next_card()
    
# ----------------------- UI --------------------------
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 283, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
button_correct = Button(image=right, highlightthickness=0, command=is_known)
button_correct.grid(row=1, column=1)

next_card()

window.mainloop()
