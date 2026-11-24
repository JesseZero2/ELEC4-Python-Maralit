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


# Function 2: Open and read a file
def open_file():
    filename = input("Enter file name: ")

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    else:
        print("\nFile Contents:")
        print(content)


# Function 3: Main menu
def main():
    while True:
        print("\n=== SAFE MENU PROGRAM ===")
        print("Prepared by: Jessie B. Maralit")
        print("1. Divide Numbers")
        print("2. Open File")
        print("3. Exit")

        choice = input("Choose (1-3): ")

        if choice == "1":
            divide_numbers()

        if choice == "2":
            open_file()

        if choice == "3":
            print("Thank you! Goodbye.")
            break

        if choice not in ("1", "2", "3"):
            print("Invalid menu choice. Try again.")


main()
