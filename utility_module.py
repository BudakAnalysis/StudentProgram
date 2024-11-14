# utility_module.py

# Define the calculate_average function here

def calculate_average (course):                 # defining function 
    total_grade = 0.0                           # defining starting values for total grade and total
    total = 0
    for grades in course.students.values():     # creating a loop that accesses student values from the course Class
        grade = grades['grade']                 # grade 
        if grades is not None:                  # if the grade exists it increases the total count
            total += 1
            total_grade += grade                # adds the grade to the total grade
    average_grade = total_grade / total         # average grade calculation is made outside the loop
    if total_grade > 0.0:                       # grade is printed 
        print(f"The average grade for {course.course_name} is: {average_grade}")       # printing the average grade if the total grade is not zero
    else: 
        print(f"The average grade for {course.course_name} is: {total_grade}")         # if total grades is equal to zero it means there are no grades available