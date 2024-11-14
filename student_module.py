# student_module.py

# Define the Student class here

class Student:                                                  # Define the Student class, containing student info.

    def __init__ (self, student_id, name, department):          # Defining initializer, using the self keyword and identifiers for each student (ID - name - department) and self for Student
        self.student_id = student_id                            
        self.name = name
        self.department = department

    def display_info (self):                                    # Defines displaying the Student information, as a string.
        return f"ID: {self.student_id}\nName: {self.name}\nDepartment: {self.department}" # Using \n to set new lines for the identifiers.

# Define the Course class here

class Course:                                                   # Defines Course class, containing course info (and the students in it).
    def __init__(self, course_name):                            # Initializing the Course class, and the course_name.
        self.course_name = course_name                          
        self.students = {}                                      # Creating a dictionary to store the students of the course in.

    def enroll_student(self, student):                          # Defining the enrolling function, checks if student_id is is there, and if not adds them to the course.
        if student.student_id in self.students: 
            print(f"Student with ID {student.student_id} is already enrolled.")
        else:
            self.students[student.student_id] = {               # Adding student and grade (None to avoid errors and wrong averages) to self (Course). 
                'student' : student,
                'grade' : None
            }
            print(f"{student.name} has been enrolled in {self.course_name}.")

    def add_grade (self, student_id, grade):                    # Defining the add grade function to add grade to the course/student.
        if student_id in self.students:
            self.students[student_id]['grade'] = grade          # Going into the Students dictionary to find the student_id, and then the grade related to it. 
            print(f"Grade {grade} has been added for student ID {student_id}.")
        else:
            print(f"No student found with ID {student_id}.")    # Student not found with student_id then it gives this error. 

    def list_students(self):                                    # Defining the listing student function, using the student_id as a key for items to loop through student info.
        for student_id, student_info in self.students.items():
            student = student_info['student']                   # Getting the students name for the print.
            grade = student_info['grade']                       # Getting the students grade for the print.
            print(student.display_info())                       # Displaying and printing the info.
            if grade == None:                                   # Grade is showed if defined, otherwise is not shown.
                print(f'Grade: No grade assigned')
            else:
                print(f'Grade: {grade}')                        