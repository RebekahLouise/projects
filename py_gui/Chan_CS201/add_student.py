from tkinter import *
from functools import partial
import tkinter.messagebox

class AddStudent: 
    def __init__(self, student):
        self.student_data = student
        
    def add_student(self, name, age, idnum, email, phone):
        self.set_name(name)
        self.set_age(age)
        self.set_id(idnum)
        self.set_email(email)
        self.set_phone(phone)
        student_info = [name, age, idnum, email, phone]
        self.student_data.allstudents.append(student_info)
        print(f"Added student {student_info[0]} to the record.")
        self.write_to_file(f"{name}, {age}, {idnum}, {email}, {phone}")
    
    def write_to_file(self, data_to_write):
        with open("student_data.txt", "a+") as file:
            for x in data_to_write:
                file.write(f"{x}")
            file.write("\n")
            file.close()
        print("\nStudent Data added to the database\n")
        
    def show_reg_ui(self, reg_frame):
        self.lblErrors = Label(reg_frame, text="", bg="#181818", font=("Courier New", 14), fg="red")
        self.lblErrors.grid(row=1, column=0, columnspan=4, pady=5)
        self.reg_txt = ["Name:", "Age:", "Student ID:", "Email Address:", "Phone Number"]
        self.reg_entry = []
        for i in range(len(self.reg_txt)):
            label = Label(reg_frame, text=self.reg_txt[i], font=("Courier New", 14), bg="#181818", fg="white", anchor="w")
            label.grid(row=i+2, column=0, padx=10, pady=5, sticky="w")
            entry = Entry(reg_frame, bg="#333333", width=20, font=("Courier New", 14), border=0, relief="solid")
            entry.grid(row=i+2, column=1, columnspan=3, pady=5, sticky="ew")
            self.reg_entry.append(entry)
        reg_btn = Button(reg_frame, width=30, border=0, text="Register", font=("Courier New", 16), bg="white", fg="#121212", command=self.check_entries)
        reg_btn.grid(row=len(self.reg_txt)+2, column=0, columnspan=4, pady=20, padx=10)

    def check_entries(self):
        errors = []
        for i in range(len(self.reg_entry)):
            if not self.reg_entry[i].get():
                errors.append(f"- Please enter {self.reg_txt[i]}\n")
        if not errors:
            name = self.reg_entry[0].get()
            age = self.reg_entry[1].get()
            idnum = self.reg_entry[2].get()
            email = self.reg_entry[3].get()
            phone = self.reg_entry[4].get()
            self.add_student(name, age, idnum, email, phone)
            tkinter.messagebox.showinfo("Register Success", "Added student to the list")
            for entry in self.reg_entry:
                entry.delete(0, "end")
        else:
            self.lblErrors.config(text=f"The following error(s) occured:\n{' '.join(errors)}\nPlease try again.")

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value):
        self._age = value

    def get_id(self):
        return self._student_id

    def set_id(self, value):
        self._student_id = value

    def get_email(self):
        return self._email

    def set_email(self, value):
        self._email = value

    def get_phone(self):
        return self._phone

    def set_phone(self, value):
        self._phone = value

