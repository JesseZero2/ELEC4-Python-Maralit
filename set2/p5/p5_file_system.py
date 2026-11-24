
# Full Name: Jessie B. Maralit
# Section: IV-BSIT A
# Activity: P5 - Student Information File System
# Date: November 24, 2026

from pathlib import Path

# Store students.txt in the same folder as this program.
FILE_PATH = Path(__file__).parent / "students.txt"


# Load student records from the text file.
def load_students():
    students = []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    students.append(data)

    except FileNotFoundError:
        print("No existing student file. Starting with empty records.")

    return students


# Save student records to the text file.
def save_students(students):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        for student in students:
            file.write("|".join(student) + "\n")


# Add a new student record.
def add_student(students):
    student_id = input("Enter Student ID: ").strip()

    if student_id == "":
        print("Student ID cannot be empty.")
        return

    for student in students:
        if student[0] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Full Name: ").strip()
    course = input("Enter Course/Section: ").strip()

    if name == "" or course == "":
        print("Name and course/section cannot be empty.")
        return

    try:
        average = float(input("Enter General Average: "))

        if average < 0 or average > 100:
            print("Average must be between 0 and 100.")
            return

    except ValueError:
        print("Invalid average. Please enter a number.")
        return

    students.append([
        student_id,
        name,
        course,
        str(average)
    ])

    save_students(students)
    print("Student added and saved successfully.")


# Display all student records.
def display_students(students):
    if len(students) == 0:
        print("No student records available.")
        return

    print("\n=== STUDENT RECORDS ===")

    for student in students:
        print("Student ID:", student[0])
        print("Full Name:", student[1])
        print("Course/Section:", student[2])
        print("General Average:", student[3])
        print("------------------------")

    print("Total Students:", len(students))


# Display the main menu.
def main():
    students = load_students()

    while True:
        print("\n=== STUDENT INFORMATION FILE SYSTEM ===")
        print("Prepared by: Jessie B. Maralit")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Choose (1-3): ")

        if choice == "1":
            add_student(students)

        if choice == "2":
            display_students(students)

        if choice == "3":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3"):
            print("Invalid menu selection.")


main()