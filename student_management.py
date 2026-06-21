"""
Student Management System (simple CLI)

Features:
- Add a student (Name, ID, Marks)
- View all students
- Update student marks
- Delete a student
- Calculate average marks
- Store data in JSON (students.json)
- Sort students by marks

Run:
    python student_management.py

Keep it simple to explain in interviews.
"""
import json
import os
import statistics

DATA_FILE = "students.json"

def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_data(students):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(students, f, indent=2)

def find_student(students, sid):
    for s in students:
        if s.get("id") == sid:
            return s
    return None

def add_student(students):
    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    sid = input("ID: ").strip()
    if not sid:
        print("ID cannot be empty.")
        return
    if find_student(students, sid):
        print("A student with this ID already exists.")
        return
    try:
        marks = float(input("Marks: ").strip())
    except ValueError:
        print("Invalid marks. Use a number.")
        return
    students.append({"name": name, "id": sid, "marks": marks})
    save_data(students)
    print("Student added.")

def view_students(students):
    if not students:
        print("No students found.")
        return
    print("{:<20} {:<10} {:>6}".format("Name", "ID", "Marks"))
    print("-" * 40)
    for s in students:
        print("{:<20} {:<10} {:>6.2f}".format(s.get("name",""), s.get("id",""), float(s.get("marks",0))))

def update_marks(students):
    sid = input("Enter student ID to update: ").strip()
    student = find_student(students, sid)
    if not student:
        print("Student not found.")
        return
    try:
        marks = float(input(f"New marks for {student['name']}: ").strip())
    except ValueError:
        print("Invalid marks. Use a number.")
        return
    student["marks"] = marks
    save_data(students)
    print("Marks updated.")

def delete_student(students):
    sid = input("Enter student ID to delete: ").strip()
    student = find_student(students, sid)
    if not student:
        print("Student not found.")
        return
    students.remove(student)
    save_data(students)
    print("Student deleted.")

def calculate_average(students):
    if not students:
        print("No students to calculate average.")
        return
    marks = [float(s.get("marks",0)) for s in students]
    avg = statistics.mean(marks)
    print(f"Average marks: {avg:.2f}")

def sort_students(students):
    if not students:
        print("No students to sort.")
        return
    students.sort(key=lambda s: float(s.get("marks",0)), reverse=True)
    save_data(students)
    print("Students sorted by marks (descending).")

def menu():
    students = load_data()
    actions = {
        "1": ("Add student", add_student),
        "2": ("View all students", view_students),
        "3": ("Update student marks", update_marks),
        "4": ("Delete a student", delete_student),
        "5": ("Calculate average marks", calculate_average),
        "6": ("Sort students by marks", sort_students),
        "7": ("Exit", None),
    }

    while True:
        print("\n<+--- Student Management ---+>")
        for k, v in actions.items():
            print(f"{k}. {v[0]}")
        choice = input("Choose an option: ").strip()
        if choice == "7":
            print("Goodbye.")
            break
        action = actions.get(choice)
        if not action:
            print("Invalid option. Try again.")
            continue
        func = action[1]
        if func:
            func(students)

if __name__ == "__main__":
    menu()
