from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)

my_label = Label(text="This is new text", font=("Arial", 24, "bold"))
my_label.pack()

# button
def click_button():
    words = entry.get()
    my_label["text"] = words
    print("I got clicked")


button = Button(text="Click Me", command=click_button)
button.pack()

# Entry (input)
entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
print(entry.get())
entry.pack()

# textbox
text = Text(width=20, height=5)
text.focus()
text.insert(END, "Example of multi-line text entry")
print(text.get("1.0", END))
text.pack()

# spinbox
def spinbox_use():
    print(spin.get())

spin = Spinbox(from_=0, to=10, width=5, command=spinbox_use)
spin.pack()

# scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton
def checkbox_used():
    print(checked_state.get())

# IntVar : 1 또는 0
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state,command=checkbox_used)
checked_state.get()
checkbutton.pack()

# Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radio1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio1.pack()
radio2.pack()

# Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Watermelon"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
