student_id=[]
student_first_name=[]
student_last_name=[]
student_gpa=[]

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
