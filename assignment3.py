student_id=[]
student_first_name=[]
student_last_name=[]
student_gpa=[]

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


def main():
    text_file=input("Please enter the file name: ")
    open(text_file, 'r+')
    load_students()
    update_students()

def load_students():
