import json

students = []
FILE_NAME = "students.json"


# Save student records to JSON file
def save_students():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Load student records from JSON file
def load_students():
    global students

    try:
        with open(FILE_NAME, "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []


# Get valid marks from user
def get_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} marks: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Add a new student
def add_student():
    print("\n===== Add Student =====")

    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    # Check duplicate roll number
    for student in students:
        if student["roll_no"] == roll_no:
            print("A student with this roll number already exists.")
            return

    python_marks = get_marks("Python")
    html_marks = get_marks("HTML")
    css_marks = get_marks("CSS")

    total = python_marks + html_marks + css_marks
    percentage = total / 3

    if percentage >= 40:
        status = "Pass"
    else:
        status = "Fail"

    student = {
        "name": name,
        "roll_no": roll_no,
        "python": python_marks,
        "html": html_marks,
        "css": css_marks,
        "total": total,
        "percentage": percentage,
        "status": status
    }

    students.append(student)
    save_students()

    print("\nStudent added successfully!")
    print("------------------------")
    print("Name:", name)
    print("Roll Number:", roll_no)
    print("Total:", total)
    print("Percentage:", round(percentage, 2))
    print("Status:", status)


# View all students
def view_students():
    print("\n===== All Students =====")

    if len(students) == 0:
        print("No student records found.")
        return

    for student in students:
        print("\n------------------------")
        print("Name:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Python:", student["python"])
        print("HTML:", student["html"])
        print("CSS:", student["css"])
        print("Total:", student["total"])
        print("Percentage:", round(student["percentage"], 2))
        print("Status:", student["status"])


# Search student
def search_student():
    print("\n===== Search Student =====")

    roll_no = input("Enter roll number to search: ")

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print("------------------------")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Python:", student["python"])
            print("HTML:", student["html"])
            print("CSS:", student["css"])
            print("Total:", student["total"])
            print("Percentage:", round(student["percentage"], 2))
            print("Status:", student["status"])
            return

    print("Student not found.")


# Update student
def update_student():
    print("\n===== Update Student =====")

    roll_no = input("Enter roll number to update: ")

    for student in students:
        if student["roll_no"] == roll_no:

            print("\nStudent Found!")

            name = input("Enter new name: ")

            python_marks = get_marks("Python")
            html_marks = get_marks("HTML")
            css_marks = get_marks("CSS")

            total = python_marks + html_marks + css_marks
            percentage = total / 3

            if percentage >= 40:
                status = "Pass"
            else:
                status = "Fail"

            student["name"] = name
            student["python"] = python_marks
            student["html"] = html_marks
            student["css"] = css_marks
            student["total"] = total
            student["percentage"] = percentage
            student["status"] = status

            save_students()

            print("\nStudent details updated successfully!")
            return

    print("Student not found.")


# Delete student
def delete_student():
    print("\n===== Delete Student =====")

    roll_no = input("Enter roll number to delete: ")

    for student in students:
        if student["roll_no"] == roll_no:

            students.remove(student)
            save_students()

            print("Student deleted successfully.")
            return

    print("Student not found.")


# Load existing records when program starts
load_students()


# Main menu
while True:

    print("\n======================================")
    print("   STUDENT RESULT MANAGEMENT SYSTEM")
    print("======================================")

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Result Management System!")
        break

    else:
        print("Invalid choice. Please select 1-6.")