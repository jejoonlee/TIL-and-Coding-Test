from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # quiz는 QuizBrain에서 질문을 가지고 온 속성
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label()
        self.score.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.question_slide = Canvas()
        self.question_slide.config(height=250, width=300, bg="white")
        self.question_text = self.question_slide.create_text(150, 125, width=280, fill=THEME_COLOR, text="Question", font=("Arial", 20, "italic"))
        self.question_slide.grid(row=1, column=0, columnspan=2, pady=50)

        correct_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=correct_image, highlightthickness=0, command=self.correct_button)
        self.correct.grid(row=2, column=0)

        wrong_image = PhotoImage(file="images/false.png")
        self.wrong = Button(image=wrong_image, highlightthickness=0, command=self.wrong_button)
        self.wrong.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.question_slide.config(bg="white")
        
        if self.quiz.still_has_questions():
            # QuizBrain에 있는 next_question() 메서드 가지고 오기
            q_text = self.quiz.next_question()
            self.question_slide.itemconfig(self.question_text, text=q_text)
        else:
            self.question_slide.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.correct.config(state="disabled")
            self.wrong.config(state="disabled")

    def correct_button(self):
        # 해당 버튼을 누르면 True값을 check_answer 메서드에 입력된다
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def wrong_button(self):
        # 해당 버튼을 누르면 False값을 check_answer 메서드에 입력된다
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        
        if is_right:
            self.question_slide.config(bg="green")
        else:
            self.question_slide.config(bg="red")

        self.score.config(text=f"Score: {self.quiz.score}")

        self.window.after(1000, self.get_next_question)