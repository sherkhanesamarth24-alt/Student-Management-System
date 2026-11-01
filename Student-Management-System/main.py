import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    if not DATA_FILE.exists():
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read student data. Starting with an empty list.")
        return []


def save_students(students):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4, ensure_ascii=False)


def find_student(students, roll_no):
    return next((student for student in students if student["roll_no"] == roll_no), None)


def add_student(students):
    try:
        roll_no = int(input("Roll number: "))
        if roll_no <= 0:
            print("Roll number must be positive.")
            return
        if find_student(students, roll_no):
            print("That roll number already exists.")
            return

        name = input("Student name: ").strip()
        course = input("Course: ").strip()
        try:
            marks = float(input("Marks (0-100): "))
        except ValueError:
            print("Marks must be a number.")
            return

        if not name or not course:
            print("Name and course cannot be empty.")
            return
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        students.append({
            "roll_no": roll_no,
            "name": name,
            "course": course,
            "marks": marks
        })
        save_students(students)
        print("Student added successfully.")
    except ValueError:
        print("Roll number must be a whole number.")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n" + "-" * 68)
    print(f"{'ROLL NO.':<12}{'NAME':<24}{'COURSE':<20}{'MARKS':>8}")
    print("-" * 68)
    for student in sorted(students, key=lambda item: item["roll_no"]):
        print(
            f"{student['roll_no']:<12}"
            f"{student['name'][:22]:<24}"
            f"{student['course'][:18]:<20}"
            f"{student['marks']:>8.1f}"
        )
    print("-" * 68)


def search_student(students):
    try:
        roll_no = int(input("Enter roll number to search: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    student = find_student(students, roll_no)
    if student:
        print("\nStudent found:")
        print(f"Roll number : {student['roll_no']}")
        print(f"Name        : {student['name']}")
        print(f"Course      : {student['course']}")
        print(f"Marks       : {student['marks']}")
    else:
        print("Student not found.")


def update_student(students):
    try:
        roll_no = int(input("Enter roll number to update: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    student = find_student(students, roll_no)
    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")
    name = input(f"Name [{student['name']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()
    marks_text = input(f"Marks [{student['marks']}]: ").strip()

    if name:
        student["name"] = name
    if course:
        student["course"] = course
    if marks_text:
        try:
            marks = float(marks_text)
            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100. Update cancelled.")
                return
            student["marks"] = marks
        except ValueError:
            print("Invalid marks. Update cancelled.")
            return

    save_students(students)
    print("Student updated successfully.")


def delete_student(students):
    try:
        roll_no = int(input("Enter roll number to delete: "))
    except ValueError:
        print("Please enter a valid roll number.")
        return

    student = find_student(students, roll_no)
    if not student:
        print("Student not found.")
        return

    confirm = input(f"Delete {student['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        students.remove(student)
        save_students(students)
        print("Student deleted successfully.")
    else:
        print("Delete cancelled.")


def show_summary(students):
    if not students:
        print("No records available for summary.")
        return

    average = sum(student["marks"] for student in students) / len(students)
    topper = max(students, key=lambda student: student["marks"])
    print(f"Total students : {len(students)}")
    print(f"Average marks  : {average:.2f}")
    print(f"Topper         : {topper['name']} ({topper['marks']:.1f})")


def main():
    students = load_students()

    while True:
        print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Show class summary")
        print("0. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_summary(students)
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Choose from 0 to 6.")


if __name__ == "__main__":
    main()
