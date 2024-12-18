from tkinter import *

class PrintAllStudents:
    def __init__(self, student):
        self.student_data = student
        
    def print_all_students(self):
        print("\n○●○●○●○●○● All Students' Information ○●○●○●○●○●\n")
        for student in self.student_data.allstudents:
            print(f"Name: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail: {student[3]}\nPhone Number: {student[4]}\n")
        print("\n○●○●○●○●○● Nothing Follows ○●○●○●○●○●\n")

    def show_list_ui(self, parent):
        self.container = parent
        Label(self.container, text="All Students' Information", font=("Courier New", 18), bg="white", fg="#121212", width=40).grid(row=0, column=0, columnspan=2, pady=10)
        data_frame = Frame(self.container, bg="#181818")
        data_frame.grid(row=1, column=0, sticky="nsew")
        scrollbar = Scrollbar(self.container, orient="vertical") #ああああ分かんねえよ何これ??
        scrollbar.grid(row=1, column=1, sticky="ns")
        canvas = Canvas(data_frame, bg="#181818", highlightthickness=0, yscrollcommand=scrollbar.set) #カンヴァスって何
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=canvas.yview)
        scrollable_frame = Frame(canvas, bg="#181818")
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        for i, student in enumerate(self.student_data.allstudents):
            name, age, student_id, email, phone = student
            Label(scrollable_frame, text=f"Name: {name}", font=("Courier New", 14), bg="#181818", fg="white", anchor="w", width=60).grid(row=i*5, column=0, sticky="w")
            Label(scrollable_frame, text=f"Age: {age}", font=("Courier New", 14), bg="#181818", fg="white", anchor="w", width=60).grid(row=i*5+1, column=0, sticky="w")
            Label(scrollable_frame, text=f"ID Number: {student_id}", font=("Courier New", 14), bg="#181818", fg="white", anchor="w", width=60).grid(row=i*5+2, column=0, sticky="w")
            Label(scrollable_frame, text=f"Email: {email}", font=("Courier New", 14), bg="#181818", fg="white", anchor="w", width=60).grid(row=i*5+3, column=0, sticky="w")
            Label(scrollable_frame, text=f"Phone: {phone}", font=("Courier New", 14), bg="#181818", fg="white", anchor="w", width=60).grid(row=i*5+4, column=0, sticky="w")
            Label(scrollable_frame, text="", font=("Courier New", 14), bg="#181818", fg="white").grid(row=i*5+5, column=0)
        scrollable_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))
