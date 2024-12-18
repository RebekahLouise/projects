class StudentInfo:
    def __init__(self):
        self.allstudents = []
        
    def __str__(self):
        return f"Name: {self.allstudents[0]}\nAge: {self.allstudents[1]}\nID Number: {self.allstudents[2]}\nEmail: {self.allstudents[3]}\nPhone Number: {self.allstudents[4]}\n"

    def read_file(self, filename="student_data.txt"):
        try:
            with open("student_data.txt", "r") as file:
                lines = file.readlines()
                for line in lines[0:]:
                    self.allstudents.append(line.split(', '))
        except FileNotFoundError:
            print("\nNo existing student data found\n")    
