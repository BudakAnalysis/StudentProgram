# main.py

# Import the Student and Course classes from student_module and the calculate_average function from utility_module
from student_module import Student, Course      # importing student_module classes
from utility_module import calculate_average    # importing the calculating average function

# Instantiate a Course

course = Course("Python Programming")   # creating / naming course

# Main Menu Functionality
def course_management_menu():
    while True:
        print("\nCourse Management Menu:")
        print("1. Enroll a Student")
        print("2. View All Students in Course")
        print("3. Add Grade for a Student")
        print("4. Calculate Average Grade")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            student_id = input("Enter ID: ")    # defining the input as student_id
            student_name = input("Enter name: ")    # defining the input as name
            student_department = input("Enter department: ")    # defining the input as department
            student = Student(student_id, student_name, student_department) # adding all the inputted info into a list
            course.enroll_student(student) # Calling enrolling student function from course Class to enroll student
        elif choice == '2':
            course.list_students()  # calling listing student function to list the students
        elif choice == '3':
            student_id = input("Enter ID: ")    # defining the input as student id
            grade = float(input("Enter grade: "))   # defining the input as grade
            course.add_grade(student_id, grade)     # calling adding grade function with the input as a list of student id and grade
        elif choice == '4':
            calculate_average(course)   # calling average grade calculating function
        elif choice == '0':
            print("Exiting the program.")   # exiting the programme with a break
            break
        else:
            print("Error!")     # error message if any other value was chosen

# Run the menu
course_management_menu()