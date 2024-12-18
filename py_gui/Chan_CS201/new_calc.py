from tkinter import *
from functools import partial
win = Tk()
win.geometry("240x262+830+370")
win.config(bg='#121212')
res = Label(win, width=20, text="0", font=("Impact", 16), bg='#121212', fg='white', anchor="e")
res.grid(row=0, column=0, columnspan=4)
def compute(text):
    txt = res.cget("text")
    if txt == "Error": res.config(text=f"{text}")
    elif txt == "0" and text.isdigit(): res.config(text=f"{text}")
    else: res.config(text=f"{txt}{text}")
def equals():
    txt = res.cget("text")
    try: res.config(text=str(eval(txt)))
    except Exception: res.config(text="Error")
def clear(): res.config(text="0")
btn_text = ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "=", "/"]
row_num, col_num = 1, 0
for i in range(len(btn_text)):
    if btn_text[i] == "=": Button(win, text=btn_text[i], width=5, font=("Impact", 16), bg="red", fg='white', command=equals).grid(row=row_num+1, column=col_num)
    elif btn_text[i] == "C": Button(win, text=btn_text[i], width=5, font=("Impact", 16), bg="red", fg='white', command=clear).grid(row=row_num+1, column=col_num)
    else: Button(win, text=btn_text[i], width=5, font=("Impact", 16), bg="red", fg='white', command=partial(compute, btn_text[i])).grid(row=row_num+1, column=col_num)
    col_num += 1
    if col_num == 4:
        row_num += 1
        col_num = 0
win.title("Chan - Calculator")
win.mainloop()
