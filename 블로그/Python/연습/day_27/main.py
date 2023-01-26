from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

my_label = Label(text="This is new text", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)

# button
def click_button():
    words = entry.get()
    my_label["text"] = words
    print("I got clicked")


button = Button(text="Click Me", command=click_button)
button.grid(column=1, row=1)

button2 = Button(text="New Button", command=click_button)
button2.grid(column=2, row=0)

# Entry (input)
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
print(entry.get())
entry.grid(column=3, row=2)

window.mainloop()