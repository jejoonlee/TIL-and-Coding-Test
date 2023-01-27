from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
my_timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)

    global REPS
    REPS = 0

    canvas.itemconfig(timer_text, text="00:00")
    timer_name.config(text="Timer", fg=GREEN)
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def starttimer():
    global REPS
    REPS += 1

    work_count = WORK_MIN * 60
    short_count = SHORT_BREAK_MIN * 60
    long_count = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        timer_name.config(text="Break", fg=RED)
        countdown(short_count)

    elif REPS % 2 == 0:
        timer_name.config(text="Break", fg=PINK)
        countdown(long_count)

    else:
        timer_name.config(text="Work", fg=GREEN)
        countdown(work_count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    global my_timer

    min = count // 60
    sec = "{:02d}".format(count % 60)
    # if sec < 10:
    #   sec = f"0{sec}"
    # 위와 같다

    canvas.itemconfig(timer_text, text=f"{min}:{sec}")
    if count > 0:
        # .after을 사용해서, 1초 마다 countdown 함수 실행하기
        my_timer = window.after(1000, countdown, count - 1)
    else:
        starttimer()
        mark = ""

        for _ in range(math.floor(REPS / 2)):
            mark += "✓"

        check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_name = Label(
    text="Timer", font=(FONT_NAME, 48, "bold"), background=YELLOW, fg=GREEN
)
timer_name.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white"
)
canvas.grid(column=1, row=1)

start_button = Button(
    text="Start", padx=10, pady=5, highlightthickness=0, command=starttimer
)
start_button.grid(column=0, row=2)


check = Label(font=(FONT_NAME, 20, "bold"), background=YELLOW, fg=GREEN)
check.grid(column=1, row=3)

reset_button = Button(
    text="Reset", padx=10, pady=5, highlightthickness=0, command=reset_timer
)
reset_button.grid(column=2, row=2)


window.mainloop()
