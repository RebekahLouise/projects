from tkinter import *

class SearchStudent:
    def __init__(self, student):
        self.student_data = student
        
    def search_student(self, keyword):
        for student_id in self.student_data.allstudents:
            if student_id[2] == keyword:
                return f"\nStudent Found!\n\n○●○●○●○●○● Student's Info ○●○●○●○●○●\n\nName: {student_id[0]}\nAge: {student_id[1]}\nID Number: {student_id[2]}\nEmail: {student_id[3]}\nPhone Number: {student_id[4]}\n\n○●○●○●○●○● Nothing Follows ○●○●○●○●○●\n"
        return "\nStudent not found...\n"
    
    def verify_login(self, list, idnum):
        for student_id in list:
            if student_id[2] == idnum:
                return f"{student_id[0]} {student_id[2]}"
        return False

    def show_info_ui(self, parent, user_id):
        self.container = parent
        for student in self.student_data.allstudents:
            if student[2] == user_id:
                info = f"Name: {student[0]}\nAge: {student[1]}\nID Number: {student[2]}\nEmail: {student[3]}\nPhone Number: {student[4]}"
                break
        else:
            info = "Student information not found."
        Label(self.container, text=info, font=("Courier New", 14), bg="#181818", fg="white", justify="left", anchor="w").grid(row=1, column=0, sticky="w", padx=10, pady=5)

    def show_search_ui(self, parent):
        self.container = parent
        Label(self.container, text="Enter Student ID:", font=("Courier New", 14), bg="#181818", fg="white").grid(row=1, column=0, sticky="w", padx=10, pady=5)
        entry = Entry(self.container, font=("Courier New", 14), width=20, bg="#333333", fg="white")
        entry.grid(row=1, column=1, sticky="w", padx=10, pady=5)
        label_info = Label(self.container, text="", font=("Courier New", 14), bg="#181818", fg="white", justify="left", anchor="w")
        label_info.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)
        def search():
            keyword = entry.get()
            info = self.search_student(keyword)
            label_info.config(text=info)
            entry.delete(0, "end")
        Button(self.container, text="Search", font=("Courier New", 14), bg="white", fg="#121212", command=search).grid(row=2, column=0, columnspan=2, pady=10)
