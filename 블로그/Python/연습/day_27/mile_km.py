from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=40, pady=20)

def calculate():
    num = int(mile.get())
    km["text"] = round(num * 1.6, 2)
    print(km["text"])

mile = Entry(width=10)
mile.grid(column=1, row=0)

mile_measure = Label(text="Miles")
mile_measure.config(padx=10, pady=10)
mile_measure.grid(column=2, row=0)

word = Label(text="is equal to")
word.config(padx=10, pady=10)
word.grid(column=0, row=1)

km = Label(text="")
km.config(padx=10, pady=10)
km.grid(column=1, row=1)

km_measure = Label(text="Km")
km_measure.config(padx=10, pady=10)
km_measure.grid(column=2, row=1)

button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()