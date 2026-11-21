
# Full Name: Jessie B. Maralit
# Section: IV-BSIT A
# Activity: P3 - Student Record Manager
# Date: November 22, 2026

students = []
student_names = set()


# 1. Add a student
def add_student():
    name = input("Enter student name: ").strip()

    if name == "":
        print("Student name cannot be empty.")
        return

    if name.lower() in student_names:
        print("Student already exists.")
    else:
        students.append(name)
        student_names.add(name.lower())
        print("Student added successfully!")


# 2. Remove a student
def remove_student():
    name = input("Enter student name to remove: ").strip()

    if name.lower() not in student_names:
        print("Student not found.")
        return

    for student in students:
        if student.lower() == name.lower():
            students.remove(student)
            student_names.remove(name.lower())
            print("Student removed successfully!")
            break
