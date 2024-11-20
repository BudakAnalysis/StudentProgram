# Student Management Program

A Python-based application for managing student enrollment and grading in a course. This program is designed to facilitate easy enrollment, manage students' grades, and compute overall course averages. The software is organized into separate modules for efficient functionality and code clarity.

### Features

Student and Course Management:
* Enroll Students: Easily add students to the course with their unique ID, name, and department.
* View All Students: Display detailed information about all enrolled students, including whether grades have been assigned.
* Add Grades: Assign and update grades for each student in the course.
* Calculate Average Grade: Compute and display the average grade for the entire course.

### Modules Overview:

student_module.py: Defines the core classes:
* Student: Represents individual students with attributes like student_id, name, and department. Includes a method to display student details.
* Course: Manages a collection of students, provides methods to enroll students, assign grades, and list student information.

utility_module.py: Contains the calculate_average function to compute and display the average grade for the course.

main.py: Implements the main menu and user interface, allowing the user to interact with the program through options like enrolling students, viewing students, adding grades, and calculating averages.

### User-Friendly Interface:

Simple menu-driven interface to navigate through the different functionalities.
Clear prompts and feedback messages for a seamless user experience.

### How to Run
1. Ensure all files (student_module.py, utility_module.py, main.py) are in the same directory.
2. Run main.py to start the course management program.
3. Follow the on-screen menu options to manage the course efficiently.
