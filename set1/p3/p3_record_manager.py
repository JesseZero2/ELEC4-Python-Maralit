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


# 3. Search for a student
def search_student():
    keyword = input("Enter name to search: ").strip().lower()

    if keyword == "":
        print("Please enter a name.")
        return

    found = False

    for student in students:
        if keyword in student.lower():
            print("Found:", student)
            found = True

    if not found:
        print("No matching student found.")


# 4. Display all students
def display_students():
    if len(students) == 0:
        print("No students recorded.")
        return

    print("\n--- STUDENT LIST ---")

    sorted_students = sorted(students, key=str.lower)

    for i in range(len(sorted_students)):
        print(f"{i + 1}. {sorted_students[i]}")

    print("Total students:", len(students))



# 5. Main menu
def main():
    while True:
        print("\n=== STUDENT RECORD MANAGER ===")
        print("Prepared by: Jessie B. Maralit")
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Search Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose (1-5): ").strip()

        if choice == "1":
            add_student()

        if choice == "2":
            remove_student()

        if choice == "3":
            search_student()

        if choice == "4":
            display_students()

        if choice == "5":
            print("Thank you for using the program!")
            break

        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice. Please try again.")


# Start the program
main()


# List and Set Explanation:
# A list stores items in order and allows duplicate values.
# I used the students list to keep the original student names.
# A set stores unique values and helps check for duplicates.
# I used the student_names set with lowercase names to
# prevent students from being added more than once.