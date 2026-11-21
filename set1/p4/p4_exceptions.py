# Full Name: Jessie B. Maralit
# Section: IV-BSIT A
# Activity: P4 - Safe Menu Program
# Date: November 22, 2026


# Function 1: Divide two numbers
def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Result:", result)

    finally:
        print("Division operation finished.")


# Temporary test
divide_numbers()
