import os

student_id=[]
student_first_name=[]
student_last_name=[]
student_gpa=[]
# Function Name: print_menu
# Description: This function lists out the items in the menu.
# Parameters: None
# Returns: selection - users menu choice
def print_menu():
    print("Welcome to the Student Registration Program")
    print("Menu options:")
    print("1. List all registered students")
    print("2. Add a new student") 
    print("3. Edit student")
    print("4. Delete student")
    print("5. Find a student")
    print("6. Calculate student average")
    print("7. Exit")
print_menu()
selection= {1:" List all registered students", 2:"Add a new student", 3:"Edit student", 4:"Delete student",
            5: " Find a student", 6: "Calculate student average", 7: "Exit" }
int(input("Your selection: "))
# Function Name: format_student
# Description: This function displays student information
# Parameters: student_information
# Returns: student_id, student_name, student_gpa
def format_student(student_information):
    student_id = []
    student_name = []
    gpa = []
    return f"{student_id},{student_name},{gpa}"
format_student()
# Function Name: display_std_header
# Description: This function displays student header
# Parameters: None
# Returns:  Student ID, Student Name, GPA
def display_std_header():
    print("Student ID, Student Name, GPA")
    return print
display_std_header()


def printLineOfChars(char, repeats):
    line = str(char) * repeats
    print(line)

def display_student(id):
    students_list_file = open('students.txt', 'r')
    for line in students_list_file:
        student_list = line.rstrip().split(',')
        student_id = student_list[0]
        student_name = student_list[1]
        student_gpa = float(student_list[2])
    # need to determine how to point at the exact student using just the ID as input
    # display_std_header()
    print("{:<20} {:<20} {:<10.0f}" .format(id, student_name, student_gpa))
    printLineOfChars('=', 75)
    students_list_file.close()

def list_students():
    students_list_file = open('students.txt', 'r')
    #If received list is empty, print “Students list has no students” error message.
    # display_std_header()
    for line in students_list_file:
        student_list = line.rstrip().split(',')
        student_id = student_list[0]
        student_name = student_list[1]
        student_gpa = float(student_list[2])
        print("{:<20} {:<20} {:<10.0f}" .format(student_id, student_name, student_gpa))
    printLineOfChars('=', 75)

def add_students():
    students_list_file = open('students.txt', 'a')
    print ("Adding a student...")
    new_student_id = input("Please enter the student ID: ")
    # Need to write an error for 'Student already exists with the given ID'.
    new_student_name = input("Please enter the student's name: ")
    new_student_gpa = (input("Please enter the student's GPA: "))
    students_list_file.write('\n' + new_student_id + ',' + new_student_name + ',' + new_student_gpa)
    print(f"Student {new_student_name} added successfully.")
    students_list_file.close()

def edit_student():
    edit_student_id = int(input("Enter student ID to edit: "))
    if edit_student_id == student_id:
        print(student_id, student_name, student_gpa)
        edit_name = input("Enter student name: ")
        edit_gpa = float(input("Enter student GPA: "))
        student_name = edit_name
        student_gpa = edit_gpa
        update_students()
        print("Student information updated successfully.")
    else:
        #Placeholder
        print("Please enter a valid student ID.")

def delete_student():
    delete_student_id = int(input("Enter student ID to delete: "))
    if delete_student_id == student_id:
        print("Deleting a student...")
        del()
        update_students()
        print("Student information updated successfully.")
    else:
        print("Please enter a valid student ID.")


# 10 need edit to be fit for parameters as guided
def calculate_average(file_name):
    with open(file_name, "r") as file:
        total_GPA = 0
        number_of_students = 0
        for line in file:
            student_items = line.strip().split(',')
            # print(student_list)
            individual_GPA = float(student_items[2])
            total_GPA += individual_GPA
            number_of_students += 1
            return round(total_GPA/number_of_students , 2)

# 11
def load_students(file_name):
    students_dic = {}
    with open(file_name, "r") as file:
        for line in file:
            items = line.strip().split(',')
            student_id = items[0]
            student_info = {
                "Student Name":items[1],
                "Student GPA":items[2]
            }
            students_dic[student_id] = student_info
        return students_dic

# 12  not sure if it's right
def update_students(file_name, students_dic):
    with open(file_name,"w") as file:
        for sdudent_id, student_info in students_dic.items():
            line = f"{sdudent_id},{student_info["Student Name"]},{student_info["Student GPA"]}\n"
            file.write(line)


def main():
    file_name = input("Please enter the file name: ")
    file_exisit = os.path.exists(file_name)
    while file_exisit != True:
        print("Error: File name doesn't exsist!")
        file_name = input("Please enter the file name: ")
        file_exisit = os.path.exists(file_name)
    print("Student information has been loaded successfully from the file.")
    # load and turn into a list
    open(file_name, 'r+')
    load_students()
    update_students()

main()

   

