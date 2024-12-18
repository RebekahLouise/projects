from student import *
from search_student import *
from add_student import *
from print_all_students import *
from main_menu import *
from tkinter import *
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def check_id():
    global attempts
    login_check = entry_txt.get()
    user = ss.verify_login(stu.allstudents, login_check)
    if user:
        mm.main_menu(user)
        attempts = 0
        win.destroy()
    else:
        attempts += 1
        if attempts > 3:
            lbl_msg.config(text="Too many failed attempts. Exiting.")
            win.after(2000, win.destroy)
        else:
            lbl_msg.config(text=f"Invalid ID. {3 - attempts} attempts remaining.")    
            
def exit_program():
    win.destroy()
    
stu = StudentInfo()
add = AddStudent(stu)
ss = SearchStudent(stu)
prstu = PrintAllStudents(stu)
mm = MainMenu(add, ss, prstu)
stu.read_file()
attempts = 0
win = Tk()
win.title("Chan - Student InfoSys")
win.geometry(f"800x500+{int((win.winfo_screenwidth()-800)/2)}+{int((win.winfo_screenheight()-500)/2)}")
win.config(bg='#121212')
btns = []; container = []
btn_txt = ["MyInfo", "Search", "Register", "View All", "Logout"]

def login_confirm():
    global attempts
    login_check = entry_txt.get()
    user = ss.verify_login(stu.allstudents, login_check)
    if user:
        user_name, user_id = user.split()
        mm.main_menu(user)
        attempts = 0
        login_frame.pack_forget()
        main_frame.pack(fill="both", expand=True)
        ss.show_info_ui(container[0], user_id)
    else:
        attempts += 1
        if attempts > 3:
            lbl_msg.config(text="Too many failed attempts. Exiting.")
            win.after(2000, win.destroy)
        else:
            lbl_msg.config(text=f"Invalid ID.\n{3 - attempts} attempts remaining.\n")

def logout_confirm():
    main_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)
    entry_txt.delete(0, END)
    lbl_msg.config(text="")

def open_frame(frame_open, close):
    for i in range(len(close)):
        if close[i].winfo_ismapped():
            close[i].pack_forget()
    frame_open.pack(side="right", fill="x")

#login
login_frame = Frame(win, bg='#121212')
login_frame.pack(fill="both", expand=True)
login_form = Frame(login_frame, bg='#333333')
login_form.place(relx=0.5, rely=0.5, anchor="center")
Label(login_form, text="Login - Student InfoSys", font=("Courier New", 20), bg='#333333', fg='white', padx=20, pady=20).pack(pady=20)
Label(login_form, text="Enter Student ID", font=("Courier New", 16), bg='#333333', fg='white').pack(pady=10)
entry_txt = Entry(login_form, width=16, font=("Courier New", 16), bg='#121212', fg='white')
entry_txt.pack(pady=10)
lbl_msg = Label(login_form, text="", font=("Courier New", 16), bg='#333333', fg='red')
lbl_msg.pack(pady=10)
login_btn = Button(login_form, text="Login", width=5, font=("Courier New", 16), bg="white", fg='#121212', command=login_confirm)
login_btn.pack()
exit_btn = Button(login_form, text="Exit", width=5, font=("Courier New", 16), bg="white", fg='#121212', command=exit_program)
exit_btn.pack(pady=30)

#main
main_frame = Frame(win, bg="#121212")
menu_contain = Frame(main_frame, border=0, bg="#1f1f1f")
menu_contain.pack(side="left", fill="y")
content_frame = Frame(main_frame, border=0, bg="#121212")
content_frame.pack(side="right", fill="both", expand=True)

#all
for i in range(len(btn_txt)-1):
    container.append(Frame(content_frame, bg="#181818"))
    Label(container[i], text=btn_txt[i], font=("Courier New", 18), bg="white", fg="#121212", width=40).grid(row=0, column=0, columnspan=5)

func = [partial(open_frame, container[0], [container[1], container[2], container[3]]),
        partial(open_frame, container[1], [container[0], container[2], container[3]]),
        partial(open_frame, container[2], [container[1], container[0], container[3]]),
        partial(open_frame, container[3], [container[1], container[2], container[0]]),
        logout_confirm]

menu_title = Label(menu_contain, text="Main Menu", font=("Courier New", 20, "bold"), bg="#1f1f1f", fg="white", pady=10)
menu_title.grid(row=0, column=0, sticky="n", pady=10)

for i in range(len(btn_txt)):
    btns.append(Button(menu_contain, border=0, fg="white", bg="#333333", width=20, text=btn_txt[i], font=("Courier New", 18)))
    btns[i].grid(row=i+1, column=0)
    btns[i].config(command=func[i])

#reg
ss.show_search_ui(container[1])
add.show_reg_ui(container[2])
prstu.show_list_ui(container[3])

win.mainloop()
