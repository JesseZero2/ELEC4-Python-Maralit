
# Full Name: Jessie B. Maralit
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 18, 2026

PASSING_GRADE = 75


# 1. Enter and validate grades
def enter_grades():
    while True:
        try:
            count = int(input("How many grades? "))

            if count > 0:
                break

            print("Please enter at least one grade.")

        except ValueError:
            print("Please enter a whole number.")

    grades = []

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Grade must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    return grades


# 2. Calculate average
def average(grades):
    return sum(grades) / len(grades)


# 3. Find highest grade
def highest(grades):
    return max(grades)


# 4. Find lowest grade
def lowest(grades):
    return min(grades)


# 5. Determine pass or fail
def status(grades):
    if average(grades) >= PASSING_GRADE:
        return "PASSED"

    return "FAILED"


# 6. Main program and menu
def main():
    grades = []

    while True:
        print("\n=== STUDENT GRADE CALCULATOR ===")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose (1-3): ").strip()

        # Enter grades
        if choice == "1":
            grades = enter_grades()
            print("Grades saved successfully!")

        # View results
        if choice == "2":
            if len(grades) == 0:
                print("Please enter grades first.")
            else:
                print("\n--- STUDENT GRADE RESULTS ---")
                print("Average:", round(average(grades), 2))
                print("Highest:", highest(grades))
                print("Lowest:", lowest(grades))
                print("Status:", status(grades))
                print("Prepared by: Jessie B. Maralit")

        # Exit program
        if choice == "3":
            print("Thank you for using the program!")
            break

        # Invalid menu selection
        if choice not in ("1", "2", "3"):
            print("Invalid choice. Please try again.")


# Start the program
main()


# Variable Scope Explanation:
# PASSING_GRADE is a global variable because it is
# defined outside all functions.
# The grades variable in main() is local because it
# is created inside the function.
# The enter_grades() function has local variables
# such as count and grade.
# Global variables can be accessed by other functions,
# while local variables belong to their own functions.