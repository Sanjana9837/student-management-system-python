import os

FILE_NAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{roll},{name},{marks}\n")

    print("Student added successfully")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found")
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll} | Name: {name} | Marks: {marks}")

def search_student():
    roll_search = input("Enter roll number to search: ")

    with open(FILE_NAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == roll_search:
                print(f"Found: {name} with marks {marks}")
                return

    print("Student not found")

def main():
    while True:
        print("\n1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice")

main()
