from tkinter import *
win = Tk()
win.geometry("540x300+700+350")
win.config(bg='#121212')
def add():
    z = str(int(txt1.get()) + int(txt2.get()))
    lbl3.config(text="Sum: "), lbl4.config(text=z)
def subtract():
    z = str(int(txt1.get()) - int(txt2.get()))
    lbl3.config(text="Difference: "), lbl4.config(text=z)
def multiply():
    z = str(int(txt1.get()) * int(txt2.get()))
    lbl3.config(text="Product: "), lbl4.config(text=z)
def divide():
    z = str(int(txt1.get()) / int(txt2.get()))
    lbl3.config(text="Quotient: "), lbl4.config(text=z)
def floor():
    z = str(int(txt1.get()) // int(txt2.get()))
    lbl3.config(text="Quotient (Floor): "), lbl4.config(text=z)
def exponent():
    z = str(int(txt1.get()) ** int(txt2.get()))
    lbl3.config(text="Power: "), lbl4.config(text=z)
def modulo():
    z = str(int(txt1.get()) % int(txt2.get()))
    lbl3.config(text="Remainder: "), lbl4.config(text=z)
lblTitle = Label(win, text=" Python Calculator ", font=("Impact", 18), bg='dimgrey', fg='white')
lblTitle.place(x=180, y=20)
lbl1, lbl2, lbl3, lbl4 = Label(win, text="First Number", font=("Impact", 16), bg='#121212', fg='white'), Label(win, text="Second Number", font=("Impact", 16), bg='#121212', fg='white'), Label(win, text=" Result: ", font=("Impact", 16), bg='#121212', fg='white'), Label(win, text="", font=("Impact", 16), bg='#121212', fg='lightcoral')
lbl1.place(x=30, y=80), lbl2.place(x=30, y=130), lbl3.place(x=30, y=180), lbl4.place(x=230, y=180)
txt1, txt2 = Entry(win, width=25, font=("Impact", 16), bg='#333333', fg='white'), Entry(win, width=25, font=("Impact", 16), bg='#333333', fg='white')
txt1.place(x=230, y=80), txt2.place(x=230, y=130)
buttons = [("+", add), ("-", subtract), ("x", multiply), ("÷", divide), ("//", floor), ("^", exponent), ("%", modulo)]
for i, (text, command) in enumerate(buttons):
    Button(win, width=5, height=1, text=text, font=("Impact", 16), command=command, bg="red", fg='white').place(x=30 + i * 70, y=240)
win.title("Chan - Calculator")
win.mainloop()
