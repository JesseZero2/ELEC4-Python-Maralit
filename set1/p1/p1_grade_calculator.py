# Full Name: Jessie B. Maralit
# Section: IV-BSIT A
# Activity: P1 - Student Grade Calculator
# Date: November 18, 2026


# Passing average for students
PASSING_GRADE = 75


# Function 1: Accept and validate student grades
def enter_grades():
    while True:
        try:
            count = int(input("How many grades will you enter? "))

            if count <= 0:
                print("Please enter at least one grade.")
                continue

            break
        except ValueError:
            print("Invalid input. Enter a whole number.")

    grades = []

    for number in range(1, count + 1):
        while True:
            try:
                grade = float(input(f"Enter grade {number}: "))

                if not 0 <= grade <= 100:
                    print("Grade must be between 0 and 100.")
                    continue

                grades.append(grade)
                break

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


# Function 2: Calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 3: Get the highest grade
def get_highest_grade(grades):
    return max(grades)


# Function 4: Get the lowest grade
def get_lowest_grade(grades):
    return min(grades)


# Function 5: Determine pass or fail status
def get_status(grades):
    average = calculate_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"


# Temporary test for our five functions
if __name__ == "__main__":
    student_grades = enter_grades()

    print("\n--- STUDENT GRADE REPORT ---")
    print(f"Average: {calculate_average(student_grades):.2f}")
    print(f"Highest Grade: {get_highest_grade(student_grades)}")
    print(f"Lowest Grade: {get_lowest_grade(student_grades)}")
    print(f"Status: {get_status(student_grades)}")
