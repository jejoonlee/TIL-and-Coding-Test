from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label()
        self.score.config(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.question_slide = Canvas()
        self.question_slide.config(height=250, width=300, bg="white")
        self.question_text = self.question_slide.create_text(150, 125, fill=THEME_COLOR, text="Question", font=("Arial", 20, "italic"))
        self.question_slide.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=correct_image, highlightthickness=0)
        self.correct.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong_image, highlightthickness=0)
        self.wrong.grid(row=2, column=1)

        self.window.mainloop()