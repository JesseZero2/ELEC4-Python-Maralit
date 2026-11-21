
# Full Name: Jessie B. Maralit
# Section: IV-BSIT A
# Activity: P2 - Custom Module
# Date: November 21, 2026

import student_utils
from student_utils import highest, lowest
from datetime import datetime


def main():
    grades = []

    while True:
        try:
            count = int(input("How many grades? "))
            if count > 0:
                break
            print("Enter at least one grade.")
        except ValueError:
            print("Please enter a whole number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Grade must be from 0 to 100.")
            except ValueError:
                print("Please enter a valid number.")

    print("\n=== STUDENT GRADE REPORT ===")
    print("Average:", round(student_utils.average(grades), 2))
    print("Status:", student_utils.status(grades))
    print("Highest:", highest(grades))
    print("Lowest:", lowest(grades))
    print("Date:", datetime.now().strftime("%Y-%m-%d %H:%M"))
    print("Prepared by: Jessie B. Maralit")


if __name__ == "__main__":
    main()