Python 3.13.1 (main, Jan 16 2025, 13:50:41) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import json
... import os
...
... DATA_FILE = "grades.json"
...
...
... def load_data():
...     """Load student data from file."""
...     if os.path.exists(DATA_FILE):
...         with open(DATA_FILE, "r") as file:
...             return json.load(file)
...     return {}
...
...
... def save_data(data):
...     """Save student data to file."""
...     with open(DATA_FILE, "w") as file:
...         json.dump(data, file, indent=4)
...
...
... def add_student(data):
...     name = input("Enter student name: ")
...     if name not in data:
...         data[name] = []
...         print("Student added successfully.")
...     else:
...         print("Student already exists.")
...
...
... def add_grade(data):
...     name = input("Enter student name: ")
...     if name in data:
...         grade = float(input("Enter grade: "))
...         data[name].append(grade)
...         print("Grade added successfully.")
...     else:
...         print("Student not found.")
...
...
... def view_report(data):
...     if not data:
...         print("No students available.")
...         return
...
...     for student, grades in data.items():
...         if grades:
...             average = sum(grades) / len(grades)
...             print(f"\nStudent: {student}")
...             print(f"Grades: {grades}")
...             print(f"Average: {average:.2f}")
...             print(f"Highest: {max(grades)}")
...             print(f"Lowest: {min(grades)}")
...         else:
...             print(f"\nStudent: {student} has no grades.")
...
...
... def main():
...     data = load_data()
...
...     while True:
...         print("\n===== Student Grade Tracker =====")
...         print("1. Add Student")
...         print("2. Add Grade")
...         print("3. View Report")
...         print("4. Exit")
...
...         choice = input("Choose an option: ")
...
...         if choice == "1":
...             add_student(data)
...         elif choice == "2":
...             add_grade(data)
...         elif choice == "3":
...             view_report(data)
...         elif choice == "4":
...             save_data(data)
...             print("Data saved. Goodbye!")
...             break
...         else:
...             print("Invalid choice.")
...
...
... if __name__ == "__main__":
...     main()
...

===== Student Grade Tracker =====
1. Add Student
2. Add Grade
3. View Report
4. Exit
Choose an option: 2
Enter student name: Kiara Milner
Student not found.

===== Student Grade Tracker =====
1. Add Student
2. Add Grade
3. View Report
4. Exit
Choose an option: 1
Enter student name: Kiara Milner
Student added successfully.

===== Student Grade Tracker =====
1. Add Student
2. Add Grade
3. View Report
4. Exit
Choose an option: 2
Enter student name: Kiara Milner
Enter grade: 88
Grade added successfully.

===== Student Grade Tracker =====
1. Add Student
2. Add Grade
3. View Report
4. Exit
Choose an option: 4
Data saved. Goodbye!
>>>