from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    let = [random.choice(letters) for _ in range(random.randint(8, 10))]
    sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    num = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = let + sym + num

    random.shuffle(password_list)

    password = ''.join(password_list)

    password_input.delete(0, "end")
    password_input.insert(0, password)
    # 자동으로 비밀번호를 복사한다
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    w = website_input.get()
    e = email_input.get()
    p = password_input.get()

    if len(w) == 0 or len(e) == 0 or len(p) == 0:
        messagebox.showerror(title="Oops", message="Please fill in the information")
    else:    
        is_ok = messagebox.askokcancel(title=w, message=f"These are the details enterd: \nEmail: {e} \nPassword: {p} \nIs it ok to save?")


        # ok를 누르면 밑에 있는 코드가 작동한다
        # cancel을 누르면 아무것도 안 된다
        if is_ok == True:
            with open("data.txt", "a") as data_add:
                data_add.write(f"{w} | {e} | {p}\n")

            website_input.delete(0, "end")
            password_input.delete(0, "end")
    



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
lock.create_image(100, 100, image=lock_image)
lock.grid(row=0, column=1)

# --------- 사이트 이름---------
website = Label(text="Website:", pady=5)
website.grid(row=1, column=0)

website_input = Entry(width=40)
website_input.grid(row=1, column=1, columnspan=2)
# 실행이 되면 입력하는 곳을 클릭 없이 바로 쓸 수 있다
website_input.focus()


# ---------이메일 또는 유저 이름---------
email = Label(text="Email/Username:", pady=5)
email.grid(row=2, column=0)

email_input = Entry(width=40)
email_input.grid(row=2, column=1, columnspan=2)
# 값을 미리 넣어두는 
email_input.insert(0, "jejoonlee@naver.com")


# ---------비밀번호---------
password = Label(text="Password:", pady=5)
password.grid(row=3, column=0)

password_input = Entry(width=22)
password_input.grid(row=3, column=1)

generate_password = Button(text="Generate Password", width=17, command=password_generate)
generate_password.grid(row=3, column=2)


# ---------추가버튼---------
final = Button(text="Add", width=40, command=save_password)
final.grid(row=4, column=1, columnspan=2)


window.mainloop()
